#update the value to 1998 of ESTAB if the existing value is 0 using update cursor

import arcpy
import os

gdb_path = r"D:\Sem 3\Prog_3\working_with_cursors_2\Practical_5_6_ProProject\05_06_Working_with_Cursors.gdb"
fc_name = "MajorAttractions"

fc_path = os.path.join(gdb_path, fc_name)

fields_list = ["NAME", "ESTAB"]

years_dict = {}

#HOTEL COMPLEX-DE ANZA COVE
with arcpy.da.UpdateCursor(fc_path, fields_list) as u_cursor:
    for row in u_cursor:
        years_dict[row[0]] = row[1]
        if row[1] ==0:
           row[1] = 1998

        u_cursor.updateRow(row)

print(years_dict)

print("process completed")
