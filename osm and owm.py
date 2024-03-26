from pyowm.utils.geo import Point
from pyowm.commons.tile import Tile
from pyowm import OWM
from pyowm.tiles.enums import MapLayerEnum
from PIL import Image
import requests
from io import BytesIO
geopoint = Point(0.203, 47.996)
x_tile, y_tile = Tile.tile_coords_for_point(geopoint, 7)
print(x_tile, y_tile)

owm = OWM('')

# Choose the map layer you want tiles for (eg. temeperature
layer_temp = MapLayerEnum.TEMPERATURE
layer_precipitation = MapLayerEnum.PRECIPITATION
layer_temp = MapLayerEnum.TEMPERATURE

# Obtain an instance to a tile manager object
tm = owm.tile_manager(layer_name)
tile = tm.get_tile(512, 355, 7)


tile.persist('hi.png')

polygon = tile.bounding_polygon()
geopoints = polygon.points
geocoordinates = [(p.lon, p.lat) for p in geopoints]  # this gives you tuples with lon/lat

#top center https://a.tile.openstreetmap.org/8/128/88.png
#top right https://a.tile.openstreetmap.org/8/129/88.png
#top left https://a.tile.openstreetmap.org/8/127/88.png
#bottom center https://a.tile.openstreetmap.org/8/128/89.png
#bottom right https://a.tile.openstreetmap.org/8/129/89.png
#bottom left https://a.tile.openstreetmap.org/8/127/89.png