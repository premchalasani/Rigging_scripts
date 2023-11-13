import maya.cmds as cmds

##### UI ######
if cmds.window('ikTool', q = 1, ex = 1):
    cmds.deleteUI('ikTool', window = 1)
cmds.window('ikTool', t = 'ikSplineTool')
cmds.rowColumnLayout(nc = 2, cs = [(1, 20),(2,20)], cw = [(1,110),(2,110)], rs = (1,4))
cmds.text(l= "Joint Amount")
jntAmountIF = cmds.intField(v=5, min = 2)
cmds.text(l= "No of Ctrls")
ctrlAmountIF = cmds.intField(v=5, min = 2)
cmds.checkBox('Curve', l = 'Rebuild Curve')
cmds.checkBox('Ctrl', l = 'IKFK Ctrl')
cmds.button(l= "Create", w= 240, c = "ctrlMaking()",align='center')
cmds.showWindow('ikTool') 

#Rebuild given Curve
def rebuildCrv():
    selCurve = ""
    spanCount = cmds.intField(ctrlAmountIF, q=1, v=1)
    curveSelected = cmds.ls(sl=1)
    if cmds.checkBox('Curve', q=1, v=1) == 1 :
        selCurve = cmds.rebuildCurve(curveSelected, ch = 0, rt = 0, end=1, kr= 0, kcp = 0, kep = 1, kt=0, s = (spanCount-1), d=3, tol= 0.01)
    else:
        selCurve = curveSelected
    return selCurve  

#Creating Joints on given Curve
def createJntAlongCurve(crvSel, num):
    count = cmds.intField(num , q=1, v=1)
    previousJnt = ""
    rootJnt = ""
    lastJnt = ""
    jntList = []
    for i in range(0, count):
    	cmds.select(cl=1)  
    	newJnt = cmds.joint()
    	motionPath = cmds.pathAnimation(newJnt, c = crvSel, fractionMode = True)
    	cmds.cutKey(motionPath+".u", time=())
    	cmds.setAttr(motionPath+".u", i * (1.0/(count - 1) ))
    	cmds.delete(newJnt + ".tx", icn =1 )
    	cmds.delete(newJnt + ".ty", icn =1 )
    	cmds.delete(newJnt + ".tz", icn =1 )
    	cmds.delete(motionPath)
    	jntList.append(newJnt)
    
        if i == 0:
            previousJnt = newJnt
            rootJnt = newJnt
            continue 
        if i == (count - 1):
            lastJnt = newJnt    
            
        cmds.parent(newJnt, previousJnt)
        previousJnt = newJnt
    cmds.joint(rootJnt, e=1, oj="xyz", sao= 'yup', ch=1, zso= 1)
    cmds.setAttr(lastJnt+".jointOrientX", 0)
    cmds.setAttr(lastJnt+".jointOrientY", 0)
    cmds.setAttr(lastJnt+".jointOrientZ", 0)
    return (rootJnt, lastJnt, jntList)

#Creating IKSplineHandle
def createIkSpline():
    crvRes = rebuildCrv()[0]
    res  = createJntAlongCurve(crvRes, jntAmountIF)
    cmds.select(res[0])
    cmds.select(res[1], add=1)
    cmds.select(crvRes, add=1)
    cmds.ikHandle(sol = "ikSplineSolver", createCurve = 0, simplifyCurve = 0, parentCurve = 0, n="ikHandle")
    cmds.setAttr("ikHandle.v", 0)
    ikHndleGrp = cmds.group(em=1, n="ikHandle_Gp")
    cmds.parent("ikHandle", ikHndleGrp)
    cmds.parent(crvRes, ikHndleGrp)
    if cmds.objExists('Deformation_Gp'):
        cmds.parent(ikHndleGrp, 'Deformation_Gp')
    sknJnt = []
    sknRenJnt = []
    for a in res[2]:
        sknRenJnt.append(a)
    sknJntLen = len(sknRenJnt)
    nameList = []
    index = []
    for i in range(0, sknJntLen):
        x = sknRenJnt.index(sknRenJnt[i])
        index.append(i)

    for (a,b) in zip(sknRenJnt, index):
        sknJnt.append(cmds.rename(a, crvRes+"_"+str(b)+"_Skn_Jnt"))      
    rootSknJnt = sknJnt[0]
    return (crvRes, rootSknJnt, sknJnt)
          
#Creating controls    
def ctrlMaking():
    ikCtrlGp = []
    ikJnt = []
    ikCtrl = []
    sknJnt = []
    
    res = createIkSpline()
    crvName = res[0]
    rootSknJnt = res[1]
    for x in res[2]:
        sknJnt.append(x)
       
    ctrlRes = createJntAlongCurve(res[0], ctrlAmountIF)
    ikRenJnt = []
    for a in ctrlRes[2]:
        ikRenJnt.append(a)    
    iklen = len(ikRenJnt)
    nameList = []
    index = []
    for i in range(0, iklen):
        x = ikRenJnt.index(ikRenJnt[i])
        index.append(i)

    for (a,b) in zip(ikRenJnt, index):
        ikJnt.append(cmds.rename(a, crvName+"_"+str(b)+"_Jnt")) 


    grp = cmds.group(em=1, n=crvName+"_Ctrl_Gp")
    for each in ikJnt:         
        ctrl = cmds.circle(nr=[1,0,0], ch= 0, n= each+"_Ik_Ctrl")
        ctrlGrp = cmds.group(em=1, n=each+"_Ik_Ctrl_Gp")
        cmds.parent(ctrl, ctrlGrp)
        cmds.delete(cmds.parentConstraint(each, ctrlGrp, mo=0))
        cmds.parent(each, ctrl)    
        cmds.parent(ctrlGrp, grp)
        cmds.setAttr(each+".drawStyle", 2)
        ikCtrlGp.append(ctrlGrp)
        ikCtrl.append(ctrl)
        if cmds.objExists('controls_set'):
            cmds.sets(ctrl, add='controls_set')         
    cmds.skinCluster(ikJnt, crvName, tsb=1)
    
    #mainControl Creation
    mainCtrl = cmds.curve(d=1, p=[(0,0.75,-0.75),(0,0.75,0.75),(0,-0.75,0.75),(0,-0.75,-0.75),(0,0.75,-0.75)], k=[0,1,2,3,4], n=crvName+"_Main_Ctrl")
    mainCtrlGrp = cmds.group(em=1, n=crvName+"_Main_Ctrl_Gp")
    cmds.parent(mainCtrl, mainCtrlGrp)
    cmds.delete(cmds.parentConstraint(rootSknJnt, mainCtrlGrp, mo=0))
    cmds.parent(crvName+"_Ctrl_Gp", mainCtrl)
    cmds.select(mainCtrl+".cv[0:4]")
    cmds.scale(2.5, 2.5, 2.5)
    cmds.select(cl=1)
    cmds.addAttr(mainCtrl, ln="Stretch",  at="double",  min= 0, max=1, dv=0, k=1)
    cmds.setAttr(mainCtrl+".Stretch", 1)    
    cmds.addAttr(mainCtrl, ln = "IK_Ctrl_Vis",  at="enum", en="Off:On:", k=1)
    cmds.setAttr(mainCtrl+".IK_Ctrl_Vis", 1)
    if cmds.objExists('Secondary_Controls_Gp'):
        cmds.parent(mainCtrlGrp, 'Secondary_Controls_Gp') 

    fkGrp = []
    fkCtrl = []
    if cmds.checkBox('Ctrl', q=1, v=1) == 1 :
        ikDup = cmds.duplicate(ikCtrlGp, rc=1)
        for each in ikDup:
            if "Ik_Ctrl_Gp1" in each:
                fkGrpRename = each.replace("Ik_Ctrl_Gp1", "Fk_Ctrl_Gp")
                cmds.rename(each, fkGrpRename)
                fkGrp.append(fkGrpRename)
            elif "Ik_Ctrl1" in each:
                fkCtrlRename = each.replace("Ik_Ctrl1", "Fk_Ctrl")
                cmds.rename(each, fkCtrlRename)
                fkCtrl.append(fkCtrlRename)
            else:
                cmds.delete(each)               
        cmds.addAttr(mainCtrl, ln = "FK_Ctrl_Vis",  at="enum", en="Off:On:", k=1)
        cmds.setAttr(mainCtrl+".FK_Ctrl_Vis", 1) 
        for i in fkCtrl:
            cmds.connectAttr(mainCtrl+".FK_Ctrl_Vis", i+"Shape.visibility") 
            if cmds.objExists('controls_set'):
                cmds.sets(i, add='controls_set')  

    #Creating FK Chain     
    for i in range(0, (len(fkGrp)-1)):
        cmds.parent(fkGrp[i+1], fkCtrl[i])      

    #Parenting IK Controls under FK 
    for j in range(0, (len(fkCtrl))):
        cmds.parent(ikCtrlGp[j], fkCtrl[j])
    
    #Creating MainControl
    mainCtrlChild = cmds.listRelatives(mainCtrl, c=1)
    mainCtrlShape = cmds.rename(mainCtrlChild[0], mainCtrl+"Shape")   
    cmds.setAttr(mainCtrlShape+".overrideEnabled", 1)
    cmds.setAttr(mainCtrlShape+".overrideColor", 17)
    cmds.parent(rootSknJnt, mainCtrl) 
    cmds.setAttr(mainCtrl+".v", l=1, k=0, cb=0)
    if cmds.objExists('controls_set'):
        cmds.sets(mainCtrl, add='controls_set')
    if cmds.objExists('Master_Ctrl'):
        cmds.setAttr(mainCtrl+".sx", l=1, k=0, cb=0)
        cmds.setAttr(mainCtrl+".sy", l=1, k=0, cb=0)
        cmds.setAttr(mainCtrl+".sz", l=1, k=0, cb=0)
                
    #IK Control Shape Change                
    for i in ikCtrl:
        each = i[0]
        cubeCtrl = cmds.curve(d=1, p=[(0.75, 0.75, 0.75),(0.75, 0.75, -0.75),(-0.75, 0.75, -0.75),(-0.75, 0.75, 0.75),(0.75, 0.75, 0.75),(0.75, -0.75, 0.75),(0.75, -0.75, -0.75),(0.75, 0.75, -0.75),(-0.75, 0.75, -0.75),(-0.75, -0.75, -0.75),(0.75, -0.75, -0.75),(-0.75, -0.75, -0.75),(-0.75, -0.75, 0.75),(-0.75, 0.75, 0.75),(-0.75, -0.75, 0.75),(0.75, -0.75, 0.75)], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
        crvShape = cmds.listRelatives(each, c=1)
        cubeCrvShape = cmds.listRelatives(cubeCtrl, c=1)
        cmds.select(cubeCrvShape[0])
        cmds.select(each, add=1)
        cmds.parent(r=1, s=1)
        cmds.delete(crvShape[0])
        cmds.delete(cubeCtrl)
        cmds.rename(cubeCrvShape, crvShape[0])

    #IK Control shapeSize and color change
    for x in ikCtrl:
        a = x[0]
        cmds.select(a+".cv[0:15]")
        cmds.scale(0.2, 0.8, 0.8)
        cmds.select(cl=1)
        cmds.setAttr(a+".overrideEnabled", 1)
        cmds.setAttr(a+".overrideColor", 18)
        cmds.connectAttr(mainCtrl+".IK_Ctrl_Vis", a+"Shape.visibility")
        ikc = a.replace("_Jnt", "")
        cmds.rename(a, ikc)
        cmds.setAttr(ikc+".rx", l=1, k=0, cb=0)
        cmds.setAttr(ikc+".ry", l=1, k=0, cb=0)
        cmds.setAttr(ikc+".rz", l=1, k=0, cb=0)
        cmds.setAttr(ikc+".sx", l=1, k=0, cb=0)
        cmds.setAttr(ikc+".sy", l=1, k=0, cb=0)
        cmds.setAttr(ikc+".sz", l=1, k=0, cb=0)
        cmds.setAttr(ikc+".v", l=1, k=0, cb=0)  

    #FK Control shape and color change
    for y in fkCtrl:
        cmds.setAttr(y+".overrideEnabled", 1)
        cmds.setAttr(y+".overrideColor", 6)
        fkc = y.replace("_Jnt", "")
        cmds.rename(y, fkc)
        cmds.setAttr(fkc+".sx", l=1, k=0, cb=0)
        cmds.setAttr(fkc+".sy", l=1, k=0, cb=0)
        cmds.setAttr(fkc+".sz", l=1, k=0, cb=0)
        cmds.setAttr(fkc+".v", l=1, k=0, cb=0)         

    #Renaming ikfk Groups       
    for a in ikCtrlGp:
        ikc = a.replace("_Jnt", "")
        cmds.rename(a, ikc)                  
    for b in fkGrp:
        fkc = b.replace("_Jnt", "")
        cmds.rename(b, fkc) 
               
    #Giving Stretch functionality       
    cmds.select(cl=1)
    cmds.select(crvName)
    crvInfoNode = cmds.arclen(ch=1)
    arclenValue = cmds.getAttr(crvInfoNode+".arcLength")
    scaleMdn = cmds.createNode('multiplyDivide', n = crvName + "_Scale_Mdn")
    stretchMdn = cmds.createNode('multiplyDivide', n = crvName + "_Stretch_Mdn")
    cmds.setAttr(stretchMdn+".operation", 2)
    stretchBc = cmds.createNode('blendColors', n= crvName + "_Stretch_Bc")     
    cmds.setAttr(scaleMdn+".input1X", arclenValue)
    if cmds.objExists('Master_Ctrl'):
        cmds.connectAttr("Master_Ctrl.GlobalScale", scaleMdn+".input2X") 
    else:
        cmds.connectAttr(mainCtrl+".scaleX", scaleMdn+".input2X")    
    cmds.connectAttr(crvInfoNode+".arcLength", stretchMdn+".input1X")
    cmds.connectAttr(scaleMdn+".outputX", stretchMdn+".input2X")    
    cmds.connectAttr(mainCtrl+".Stretch",  stretchBc+".blender")
    cmds.setAttr(stretchBc+".color2R", 1)
    cmds.connectAttr(stretchMdn+".outputX", stretchBc+".color1R")
    for i in sknJnt:
        jntMdn = cmds.createNode('multiplyDivide', n = i + "_Mdn")
        jntTX = cmds.getAttr(i + ".translateX")
        cmds.setAttr(jntMdn+".input1X", jntTX)
        cmds.connectAttr(stretchBc+".outputR", jntMdn+".input2X")
        cmds.connectAttr(jntMdn+".outputX", i + ".translateX") 
    

      
