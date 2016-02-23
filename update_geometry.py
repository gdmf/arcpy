import os
import arcpy

workspace = r"<A workspace>"
featureclass = r"<Feature class name>"

path = os.path.join(workspace, featureclass)

lat_field = "<field name for latitude>"
lon_field = "<field name for longitude>"

with arcpy.da.UpdateCursor(path, ["SHAPE@XY", lat_field, lon_field]) as cursor:
	for geom, lat, lon in cursor:
		new_row = [[lon, lat], lat, lon]
		cursor.updateRow(new_row)

