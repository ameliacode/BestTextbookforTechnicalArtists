import maya.cmds as cmds
from math import *

psphere = cmds.sphere(r=5)
pcube = cmds.polyCube()
pcone = cmds.polyCone()
closestToSurface = cmds.createNode("closestPointOnSurface")
cmds.connectAttr(closestToSurface+'.position', pcube[0]+'.translate')
cmds.connectAttr(pcone[0]+'.translate', closestToSurface+'.inPosition')
cmds.connectAttr(psphere[0]+'.worldSpace[0]',closestToSurface+'.inputSurface')
