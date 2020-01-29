import maya.cmsd as cmds

#a)Near/Far Clippling plane distance
cmds.viewClipPlane("renderCam",query=True,autoClipPlane=True)
