import arcpy

first_fc = r"<path to feature class>"
second_fc = r"<path to feature class>"

first_desc = arcpy.Describe(first_fc)
first_fields = [field.name for field in first_desc.fields]
print first_fields

second_desc = arcpy.Describe(second_fc)
second_fields = [field.name for field in second_desc.fields]
print second_fields

first_set = set(first_fields)
second_set = set(second_fields)
print first_set.symmetric_difference(second_set)

print len(first_fields)
print len(second_fields)
