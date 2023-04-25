#Tool to create the daily schedule CSV table used for building the daily assignments email
import arcpy
import os
import pandas as pd
import shutil
#inputs
emailTable = arcpy.GetParameterAsText(0)
outputFolder = arcpy.GetParameterAsText(1)
arcpy.env.overwriteOutput = True
#exports to .txt file
arcpy.ExportXYv_stats(emailTable, ["INSP_ADDR", "LATERAL_NUM", "SEGMENT", "PC_Lateral_SEG", "G2_UTA_Type", "INSPECTION_STATUS", "Inspection_Type", "Assignment_Notes", "Project_Source", "Assigned_To", "Field_Order"], "SEMI-COLON", "Assignment_Email.txt", "ADD_FIELD_NAMES")
# reading given txt file and creating dataframe
df = pd.read_csv("Assignment_Email.txt", delimiter = ';')
  
# storing this dataframe in a csv file
df.to_csv("Assignment_Email.csv", 
                  index = None)
# sort the csv by assigned_to and field_order
sorted_df = df.sort_values(by=['Assigned_To','Field_Order'])
sorted_df.to_csv('Assignment_Email_Sorted.csv', index=False)
# copy Assignment Email Sort.csv to output location
shutil.copy2('Assignment_Email_Sorted.csv', outputFolder)
# delete unsorted assignment csv file
os.remove('Assignment_Email.csv')
# delete Assignment_Email.txt file
arcpy.Delete_management("Assignment_Email.txt")
