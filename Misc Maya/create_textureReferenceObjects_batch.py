import pymel.core as pm
import maya.mel as mel

_isDefault = True
refFrame = "" # if blank the reference frame will be the first of the timeline

objects = pm.ls(("*snow_geo", "*bark_geo"), type='transform', r=True) if (_isDefault) else pm.selected(type='transform')
mel.eval('playButtonStart()') if (refFrame == "") else pm.setCurrentTime(refFrame)
test = map(lambda obj : (obj + '_reference'), objects)

for obj in objects:
    pm.select(obj)
    mel.eval('CreateTextureReferenceObject()')
    
pm.group(test, n = 'Pref_textRefObj_grp')