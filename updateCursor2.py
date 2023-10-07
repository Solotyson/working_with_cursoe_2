#update the value of HISTORIC field to 'YES' is ESTAB is greater than 1998 and less than 1980 or else update to 'NO"

import arcpy
import os

gdb_path = r"D:\Sem 3\Prog_3\working_with_cursoe_2\Practical_5_6_ProProject\05_06_Working_with_Cursors.gdb"
fc_name = "MajorAttractions"

fc_path = os.path.join(gdb_path, fc_name)

fields_list = ["NAME", "ESTAB", "HISTORIC"]

with arcpy.da.UpdateCursor(fc_path, fields_list) as u_cursor:
    for row in u_cursor:
        establishment_year = row[1]

        if establishment_year > 1960 and establishment_year < 1980:
            row[2] = "YES"
        else:
            row[2] = "NO"

        u_cursor.updateRow(row)

print("Process Completed")