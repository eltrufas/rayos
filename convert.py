import dask.dataframe as dd
import numpy as np

df = dd.read_parquet('NLDN.parquet')

def wgs84_to_web_mercator(df, lon="lon", lat="lat"):
      k = 6378137
      df["lon"] = df[lon] * (k * np.pi/180.0)
      df["lat"] = np.log(np.tan((90 + df[lat]) * np.pi/360.0)) * k
      return df
df = wgs84_to_web_mercator(df)
df.to_parquet('NLDN2.parquet')
