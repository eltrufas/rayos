import dask.dataframe as dd
import pandas as pd
import holoviews as hv
import geoviews as gv
import geoviews.feature as gf
from holoviews.operation.datashader import datashade
import panel as pn

gv.extension('bokeh')
df = dd.read_parquet('NLDN.parquet')
df.persist()
df = df[['lat', 'lon', 'mult']]

def strikes_in_range(date_range):
    start, end = date_range
    subset = df[start:end]
    return gv.Points(dict(x=subset['lon'], y=subset['lat']))


start_hour = df.index.min().compute()
end_hour = df.index.max().compute()
time_slider = pn.widgets.DateRangeSlider(name='Hora', value=(start_hour, end_hour), start=start_hour, end=end_hour)

points = strikes_in_range((start_hour, end_hour))

timeline = pn.bind(strikes_in_range, date_range=time_slider)

plot = gv.tile_sources.Wikipedia * datashade(hv.DynamicMap(timeline))
layout = pn.Row(time_slider) + pn.Row(plot.opts(height=650,responsive=True))

pn.panel(layout).servable(title="Rayos")
