import pymel.core as pm

#Set newPath before running the script
texturesPath = "/sourceimages/"

changePaths = False


fileNodes = pm.ls(tex = True)

for texNode in fileNodes:
    if pm.attributeQuery( 'fileTextureName', n=texNode, ex=True ):
        print( pm.getAttr(texNode + '.fileTextureName') )

if changePaths:
    for texNode in fileNodes:
        if pm.attributeQuery( 'fileTextureName', n=texNode, ex=True ):
            #print(texNode)
            
            absolutePath = texNode.getAttr('fileTextureName')
            newPath = texturesPath + absolutePath.split('/')[-1]
            
            texNode.setAttr('fileTextureName', newPath)