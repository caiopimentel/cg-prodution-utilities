import pymel.core as pm

#Change the exportDirectory string to the desire destination directory. Don't forget to add a / at the end.
exportDirectory = "path/assets/00_ProductionModels/00_Environment_Assets/01/"

selected = pm.selected()

for obj in selected:
    pm.select(obj)
    print ('_Exporting: ' + obj)
    fileName = exportDirectory + obj.split( ":" )[-1] + ".ass"
    pm.arnoldExportAss( f=fileName, s=1, mask=6399, lightLinks=0, shadowLinks=0, exportAllShadingGroups=1, boundingBox=1, cam="perspShape")