import arcpy
import os

mxd_to_copy = r"<Path to MXD>"

mxds_to_change = [
	r"<Path to MXD>",
	r"<Path to MXD>",
]

mxd = arcpy.mapping.MapDocument(mxd_to_copy)

df = arcpy.mapping.ListDataFrames(mxd)[0]

targetExtent = df.extent

for mxd_to_change in mxds_to_change:
	mxd = arcpy.mapping.MapDocument(mxd_to_change)
	df = arcpy.mapping.ListDataFrames(mxd)[0]
	df.extent = targetExtent
	dir, base = os.path.split(mxd_to_change)
	new_base = os.path.splitext(base)[0] + "_new_extent.mxd"
	new_path = os.path.join(dir, new_base)
	print new_path
	mxd.saveACopy(new_path)
	del mxd

