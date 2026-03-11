"""
Reproject CA_COUNTIES.json from EPSG:3857 → EPSG:4326
======================================================
This makes the county boundaries match the parcel data projection.

USAGE:
  Place this script in the same folder as CA_COUNTIES.json
  python reproject_counties.py

  Output: CA_COUNTIES_4326.json
"""

import geopandas as gpd
import sys
from pathlib import Path

INPUT  = "CA_COUNTIES.json"
OUTPUT = "CA_COUNTIES_4326.json"

print(f"Reading {INPUT} ...")
gdf = gpd.read_file(INPUT)
print(f"✓ {len(gdf)} features | CRS: {gdf.crs}")
print(f"  Properties: {[c for c in gdf.columns if c != 'geometry']}")

# Show a sample NAME
if 'NAME' in gdf.columns:
    print(f"  Sample NAME values: {gdf['NAME'].head(5).tolist()}")

print(f"\nReprojecting to EPSG:4326 ...")
gdf = gdf.to_crs("EPSG:4326")
print(f"✓ Now CRS: {gdf.crs}")

print(f"Exporting to {OUTPUT} ...")
gdf.to_file(OUTPUT, driver="GeoJSON")

size_mb = Path(OUTPUT).stat().st_size / (1024 * 1024)
print(f"\n✓ Done! → {OUTPUT} ({size_mb:.1f} MB)")
print(f"\nReplace data/CA_COUNTIES.json in your repo with this file.")
