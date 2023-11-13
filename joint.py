from maya import cmds as mc
cls = mc.cluster()
jnt = mc.joint()
prnt = mc.Unparent(jnt)
pnt = mc.parentConstraint(cls,jnt, mo=0)
dele = mc.delete(pnt,cls)
