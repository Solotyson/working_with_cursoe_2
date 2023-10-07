
import arcpy
import os

gdb_path = r"D:\Sem 3\Prog_3\working_with_cursoe_2\Practical_5_6_ProProject\05_06_Working_with_Cursors.gdb"
fc_name = "MajorAttractions"

fc_path = os.path.join(gdb_path, fc_name)

fields_list = ["NAME", "ESTAB", "ADDR"]

record = ("NEWATTRACTION", 2023, "STREET123")

i_cursor = arcpy.da.InsertCursor(fc_path, fields_list)

i_cursor.insertRow(record)

print("Process Completed")