from bokeh.layouts import layout
from bokeh.plotting import figure, show, ColumnDataSource, output_file, show, curdoc
from bokeh.models import Div, RangeSlider, Spinner, DateRangeSlider, CustomJS, CustomJSFilter, CDSView, BooleanFilter
import holoviews as hv
from holoviews import opts
import pandas as pd
from bokeh.tile_providers import CARTODBPOSITRON, get_provider
import numpy as np

output_file('tile.html')

tile_provider = get_provider(CARTODBPOSITRON)

def wgs84_to_web_mercator(df, lon="lon", lat="lat"):
      k = 6378137
      df["x"] = df[lon] * (k * np.pi/180.0)
      df["y"] = np.log(np.tan((90 + df[lat]) * np.pi/360.0)) * k

      return df


df = pd.read_parquet('NLDN.parquet')
df = df.head(500)

start_time = df.index.min()
end_time = df.index.max()

date_range_slider = DateRangeSlider(title="Date Range: ", start=start_time, end=end_time, value=(start_time, end_time), step=1, format='%d %b %Y %H:%M:%S')

wgs84_to_web_mercator(df)
print(df.head())
source = ColumnDataSource(df)

p = figure(x_range=(-2000000, 6000000), y_range=(-1000000, 7000000),
           x_axis_type="mercator", y_axis_type="mercator")
p.add_tile(tile_provider)

date_filter = BooleanFilter(booleans=[True for _ in df])

view = CDSView(source=source, filters=[date_filter])
p.dot(x='x', y='y', view=view)

lyt = layout([
    [date_range_slider],
    [p],
])

show(lyt)
