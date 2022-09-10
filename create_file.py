# from netCDF4 import Dataset
# from cftime import date2num

# df = pd.read_parquet('NLDN.parquet')
# df = df.head(500)

# rootgrp = Dataset('rayos.nc', 'w', format='NETCDF4')
# grpdims = {}
# grpvars = {}
# dims = ('lat', 'lon', 'time')
# for k in dims:
#     dim = rootgrp.createDimension(k)
#     grpvars[k] = dim

# lat = rootgrp.createVariable('lat', 'f4', ('lat',))
# lat.units = 'degrees north'

# lon = rootgrp.createVariable('lon', 'f4', ('lon',))
# lon.units = 'degrees east'

# times = rootgrp.createVariable('time', 'i4', ('time',))
# times.units = 'hours since 0001-01-01 00:00:00.0'
# times.calendar = 'gregorian'

# mult = rootgrp.createVariable('mult', 'i4', dims)

# print(df.head())

# datetimes = df.index.to_list()

# lat[:] = df['lat']
# lon[:] = df['lon']
# times[:] = date2num(datetimes, units=times.units, calendar=times.calendar)
# print(mult)
# mult[:] = df['mult']

# print(times)

# rootgrp.close()

import pandas as pd
import xarray as xr

df = pd.read_parquet('NLDN.parquet')

ds = xr.Dataset.from_dataframe(df, sparse=True)

print(ds)

import holoviews as hv
import geoviews as gv
import geoviews.feature as gf

kdims = ['datetime', 'lat', 'lon']
vdims = ['mult']

xr_dataset = gv.Dataset(ds, kdims=kdims, vdims=vdims)
print(repr(xr_dataset))

xr_dataset.to(gv.Points, ['lat', 'lon'])
