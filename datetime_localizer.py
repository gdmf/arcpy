import datetime
import arcpy

fc = r"<path to feature class>"

UTC_time_field = "DateTimeUTC"
local_time_field = "DateTime_Local"
# time delta from UTC in hours
timedelta_hours = -4

with arcpy.da.UpdateCursor(fc, [UTC_time_field, local_time_field]) as cursor:
    for row in cursor:
        row[1] = row[0] + datetime.timedelta(hours=timedelta_hours)
            cursor.updateRow(row)
