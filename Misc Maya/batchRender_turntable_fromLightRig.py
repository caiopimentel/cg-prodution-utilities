import pymel.core as pm
import maya.mel as mel
#import time


if len(pm.selected()) == 0:
    pm.warning('No LGT group selected')

else:
    selectedLight = str(pm.selected())
    selectedLight = selectedLight.split('\'')[1].split(':')[1] if len(selectedLight.split(":")) > 1 else selectedLight.split('\'')[1]
    #print (selectedLight)

    if 'LGT' in selectedLight:
        pm.setAttr("defaultRenderGlobals.renderVersion", selectedLight)
        currentVerion = pm.getAttr("defaultRenderGlobals.renderVersion")
        pm.inViewMessage( amg='version: ' + currentVerion, pos='topCenter', bkc=0x002836f4, fontSize=20, dragKill=True)
        #time.sleep(10)
        print('Kicking render')
        mel.eval("BatchRender")
    else:
        pm.warning('No LGT group selected')
