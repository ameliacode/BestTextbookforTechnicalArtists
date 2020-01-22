import maya.cmds as cmds
from math import *

#focal length
f1 = cmds.getAttr('cameraShape1.focalLength')
#horizontal film aperture, unit:inch
#for it has to be inch, else the screen will not fit in and exceed

hfa = cmds.getAttr('cameraShape1.horizontalFilmAperture')
fov = 2*atan(hfa/2*f1*0.0393700787)

#print(f1)

#horizontal aperture size
scalex = 2*50*tan(fov*0.5)
cmds.setAttr('nurbsPlane1.scaleX',scalex)

vfa = cmds.getAttr('cameraShape1.verticalFilmAperture')

scalez = scalex*vfa/hfa
cmds.setAttr('nurbsPlane1.scaleZ',scaleZ)
