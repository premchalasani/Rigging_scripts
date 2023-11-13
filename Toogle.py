
import maya.cmds as cmds

def tglJnts():
    av = cmds.getPanel(wf = 1)
    v = cmds.modelEditor(av, q = 1, j = 1)
    cmds.modelEditor(av, e = 1, j = not v)
def tglCrvs():
    av = cmds.getPanel(wf = 1)
    v = cmds.modelEditor(av, q = 1, nc = 1)
    cmds.modelEditor(av, e = 1, nc = not v)
def tglPolys():
    av = cmds.getPanel(wf = 1)
    v = cmds.modelEditor(av, q = 1, pm = 1)
    cmds.modelEditor(av, e = 1, pm = not v)
def tglHiLi():
    av = cmds.getPanel(wf = 1)
    v = cmds.modelEditor(av, q = 1, sel = 1)
    cmds.modelEditor(av, e = 1, sel = not v)
    
if cmds.window('toggle_display', q = 1, ex = 1) == 1:
    cmds.deleteUI('toggle_display', window = 1)
    
cmds.window('toggle_display',t = 'Tgl_Win', mnb = 0, mxb = 0)
cmds.columnLayout(adj = 1)
cmds.iconTextButton(st = 'iconAndTextHorizontal', i1 = 'kinJoint.png', l = 'Joints', h = 45, c = 'tglJnts()')
cmds.iconTextButton(st = 'iconAndTextHorizontal', i1 = 'pencil.png', l = 'Curves', h = 45, c = 'tglCrvs()')
cmds.iconTextButton(st = 'iconAndTextHorizontal', i1 = 'polyCube.png', l = 'Polygons', h = 45, c ='tglPolys()')
cmds.iconTextButton(st = 'iconAndTextHorizontal', i1 = 'selectByComponent.png', l = 'Hi-Li', h = 45, c = 'tglHiLi()')
cmds.window('toggle_display', e = 1, w = 110, h = 170)
cmds.showWindow('toggle_display')
