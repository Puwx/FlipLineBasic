#Replace LINEFC with the name fo the feature class that you want to edit.
#This will change the geometry of the feature class you input so don't put something you don't want to edit.

with arcpy.da.UpdateCursor("LINEFC","SHAPE@") as curs:
    for row in curs:
        geom = row[0]
        for part in geom:
            outLine = arcpy.Polyline(arcpy.Array([crds for crds in part[::-1]]))
        row[0] = outLine
        curs.updateRow(row)
        
def reverseLine(original_polyline):
    for part in geom:
        outLine = arcpy.Polyline(arcpy.Array([crds for crds in part[::-1]))
    return outLine
    
#Usage of the function above is shown below:

with arcpy.da.UpdateCursor("MY_POLYLINE","SHAPE@") as curs:
    for row in curs:
        row[0] = reverseLine(row[0]
        curs.updateRow(row)
