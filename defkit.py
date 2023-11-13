##########################################    ###########################################
## Last Updated :- 12th,November.2021
## Author :- Ankit Singh
## Copyright :- Only for Official Use
#####################################################################################
import maya.api.OpenMaya as om
import maya.api.OpenMayaAnim as oma
import maya.cmds as cmds 
import maya.mel as mel
import maya.OpenMaya as OpenMaya
import maya.OpenMayaAnim as OpenMayaAnim
from maya.api.OpenMaya import *
from maya.api.OpenMayaAnim import *
import math
import json
#####################################################################################
#####################################################################################
def DeformerKit():
    window = cmds.window(s=0,title='Deformer Kit UI_6.0',h=545,w=440,mnb=0,mxb=0)   
    cmds.scrollLayout(horizontalScrollBarThickness=25)
    winLayout = cmds.columnLayout(adj=1)
    cmds.separator(h=10,w=10,style='in')
    cmds.text(l='<<<<// EXTRAP CLUSTERS THROUGH SELECTION \\\\>>>>',bgc=[0,.5,0],h=30,align='center')
    cmds.separator(h=10,w=10,style='in')
    cmds.frameLayout('transFrameLayout', la='center', label='LOAD OBJECT LIST FOR CLUSTER EXTRAPTION')
    cmds.textScrollList('meshList' ,numberOfRows=2, allowMultiSelection=True)
    cmds.setParent( '..' )
    cmds.button ('loadMeshBtn', l='>>>', c=loadMeshCmd)
    cmds.separator(h=10,w=10,style='in') 
    cmds.textFieldButtonGrp('selobj',l='LOAD OBJECT SHAPE  ',tx='',bl='<<<<',bc='ObjShp()')  
    cmds.separator(h=10,w=10,style='in') 
    cmds.rowColumnLayout(nc=3)
    cmds.separator(h=10, w=200)
    cmds.separator(h=10, w=20)   
    cmds.separator(h=10, w=200)     
    cmds.button(l='<<< Extrap for list >>>',bgc=[1,1,1],c='listExtrap()')
    cmds.separator(h=10,w=10,style='in')  
    cmds.button(l='<<< Extrap for object >>>',bgc=[1,1,1],c='shapeExtrap()')
    cmds.separator(h=10, w=200)
    cmds.separator(h=10, w=20)
    cmds.separator(h=10, w=200)     
    cmds.setParent(winLayout)
    cmds.separator(h=10,w=10,style='in') 
    cmds.button(l='<<< CONVERT CLUSTER TO JOINT >>>',bgc=[0,0.8,1],c='convertClusterToJoint()')
    cmds.separator(h=10,w=10,style='in')
    cmds.rowColumnLayout(nc=3)
    cmds.separator(h=10, w=200)
    cmds.separator(h=10, w=20)   
    cmds.separator(h=10, w=200)     
    cmds.button(l='<<< Export Clusters >>>', c='exportClusters()', w=200, bgc=(1, .5, .3))
    cmds.separator(w=20)    
    cmds.button(l='<<< Import Clusters >>>', c='importClusters()', w=200, bgc=(1, .5, .3))
    cmds.separator(h=10, w=200)
    cmds.separator(h=10, w=20)
    cmds.separator(h=10, w=200)     
    cmds.setParent(winLayout)  	
    cmds.text(l='<<<<// TRANSFER SKIN WEIGHTS \\\\>>>>',bgc=[0,.5,0],h=30,align='center')
    cmds.rowColumnLayout(nc=3)
    cmds.separator(h=10, w=200)
    cmds.separator(h=10, w=20)   
    cmds.separator(h=10, w=200)     
    cmds.button(l='<<< Export Skin Weights >>>', c='exportSkinWeights()', w=200, bgc=(1, .5, .3))
    cmds.separator(w=20)    
    cmds.button(l='<<< Import Skin Weights >>>', c='importSkinWeights()', w=200, bgc=(1, .5, .3))
    cmds.separator(h=10, w=200)
    cmds.separator(h=10, w=20)
    cmds.separator(h=10, w=200)     
    cmds.setParent(winLayout)  
    cmds.rowColumnLayout(nc=3)
    cmds.separator(h=10, w=200)
    cmds.separator(h=10, w=20)   
    cmds.separator(h=10, w=200)     
    cmds.button(l='<<< Export DQ Weights >>>', c='exportDQWeights()', w=200, bgc=(1, .5, .3))
    cmds.separator(w=20)    
    cmds.button(l='<<< Import DQ Weights >>>', c='importDQWeights()', w=200, bgc=(1, .5, .3))
    cmds.separator(h=10, w=200)
    cmds.separator(h=10, w=20)
    cmds.separator(h=10, w=200)     
    cmds.setParent(winLayout)      
    cmds.separator(h=10,w=10,style='in')
    cmds.button(l='<<< Import Skeleton >>>',bgc=[1,0.5,0.3],c='importSkeleton()')
    cmds.separator(h=10,w=10,style='in')     	
    cmds.text(l='<<<<// TRANSFER DEFORMER WEIGHTS MESH 2 MESH \\\\>>>>',bgc=[0,.5,0],h=30,align='center')
    cmds.separator(h=10,w=10,style='in')
    cmds.textFieldButtonGrp('fromObj',l='Load From Mesh',tx='',bl='<<<<',bc='FromMesh()')  
    cmds.separator(h=10,w=10,style='in') 
    cmds.textFieldButtonGrp('toObj',l='Load To Mesh',tx='',bl='<<<<',bc='ToMesh()')  
    cmds.separator(h=10,w=10,style='in')
    cmds.textFieldButtonGrp('fromDef',l='Load From Deformer',tx='',bl='<<<<',bc='FromDeformer()')  
    cmds.separator(h=10,w=10,style='in') 
    cmds.textFieldGrp('deformerName',l='Deformer Transform Node',tx='',ed=1)  
    cmds.separator(h=10,w=10,style='in') 
    cmds.textFieldButtonGrp('toDef',l='Load To Deformer',tx='',bl='<<<<',bc='ToDeformer()')  
    cmds.separator(h=10,w=10,style='in') 	 
    cmds.button(l='<<< TRANSFER DEFORMER WEIGHTS >>>',bgc=[1,1,1],c=transferWeights)
    cmds.separator(h=10,w=10,style='in')	
    cmds.text(l='<<<<// TRANSFER SKIN WEIGHTS FROM JOINT 2 JOINT \\\\>>>>',bgc=[0,.5,0],h=30,align='center')
    cmds.separator(h=10,w=10,style='in')   
    cmds.textFieldButtonGrp('fromJoint',l='Load From Joint',tx='',bl='<<<<',bc='FromJoint()')  
    cmds.separator(h=10,w=10,style='in') 
    cmds.textFieldButtonGrp('toJoint',l='Load To Joint',tx='',bl='<<<<',bc='ToJoint()')  
    cmds.separator(h=10,w=10,style='in') 	 
    cmds.button(l='<<< TRANSFER SKIN WEIGHTS >>>',bgc=[1,1,1],c=transferWeightToJoint)
    cmds.separator(h=10,w=10,style='in')         
    cmds.frameLayout('TypeFrameLayout', label='MIRROR TYPE', w=400 ,bgc=[0,.5,0], la='center')
    cmds.separator(height=10, style='none')
    cmds.radioButtonGrp('typeSwitch', la3=['Mirror Cluster', 'Mirror Weight', 'Flip Weight'], sl=1 , nrb=3, cw3=[150,150,150],en3=0)
    cmds.setParent( '..' )
    cmds.separator( height=10, w=400)    
    cmds.frameLayout('AxisFrameLayout', label='AXIS :', w=400 ,bgc=[0,.5,0], la='center')
    cmds.separator(height=10, style='none')
    cmds.rowColumnLayout ('traRowLayout', numberOfColumns=4, columnWidth=[(1, 101), (2, 101), (3, 101), (4, 100)])
    cmds.radioCollection('axisSwitch')
    cmds.radioButton('X', l='X',sl=1)
    cmds.radioButton('Y', l='Y')
    cmds.radioButton('Z', l='Z')
    cmds.checkBox('PosNegCheck', label='Pos to Neg',v=1 )
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    cmds.separator( height=10, w=400, style='none')
    cmds.separator( height=10, w=400)    
    cmds.rowColumnLayout ('mirDefRowLayout', numberOfColumns=3, columnWidth=[(1, 195), (2, 5),(3, 200)])    
    cmds.setParent( '..' )        
    cmds.button(l='<<< MIRROR DEFORMER >>>',bgc=[1,1,1],c='mirrorDeformer()')
    cmds.separator(h=10,w=10,style='in') 
    cmds.separator(h=10,w=10,style='in')
    cmds.separator(h=10,w=10,style='in')
    cmds.button(l='<<< LATTICE TO SKINCLUSTER >>>',bgc=[0,0.8,1],c='latSkin()')
    cmds.separator(h=10,w=10,style='in') 
    cmds.button(l='<<< WIRE TO SKINCLUSTER >>>',bgc=[0,0.8,1],c='wireSkin()')
    cmds.separator(h=10,w=10,style='in') 
    cmds.button(l='<<< SOFTSELECTION CLUSTER >>>',bgc=[0,0.8,1],c='softSelClu()')
    cmds.separator(h=10,w=10,style='in')
    cmds.separator(h=10,w=10,style='in')
    cmds.separator(h=10,w=10,style='in')    
    cmds.button(l='<<< REORDER HISTORY >>>',bgc=[0.8,0.2,0.5],c='reorderHistory()')
    cmds.separator(h=10,w=10,style='in')
    cmds.separator(h=10,w=10,style='in')
    cmds.text(l='<<<<// REORDER ATTRIBUTES \\\\>>>>',bgc=[0,.5,0],h=20,align='center')
    cmds.separator(h=10,w=10,style='in')
    cmds.rowColumnLayout(nc=3)
    cmds.separator(h=10, w=200)
    cmds.separator(h=10, w=20)   
    cmds.separator(h=10, w=200)     
    cmds.button(l='<<< MOVE UP >>>', c='moveAttributeUp()', w=200, bgc=(1, .5, .3))
    cmds.separator(w=20)    
    cmds.button(l='<<< MOVE DOWN >>>', c='moveAttributeDown()', w=200, bgc=(1, .5, .3))
    cmds.separator(h=10, w=200)
    cmds.separator(h=10, w=20)
    cmds.separator(h=10, w=200)     
    cmds.setParent(winLayout)  
    cmds.separator(h=10,w=10,style='in')
    cmds.button(l='<<< OPEN TOOLKIT >>>',bgc=[1,0.9,0],c='tlkit()')
    cmds.separator(h=10,w=10,style='in')
    cmds.button(l='<<< OPEN SOFTCLUSTER TOOL >>>',bgc=[1,0.9,0],c='sftCluTool()')
    cmds.separator(h=10,w=10,style='in')
    cmds.button(l='<<< OPEN EYELID TOOL >>>',bgc=[1,0.9,0],c='eyelidUI()')
    cmds.separator(h=10,w=10,style='in')
    cmds.separator(h=10,w=10,style='in')
    cmds.separator(h=10,w=10,style='in')
    cmds.text(l="Developed By- Ankit Singh",h=10,al="center")
    cmds.separator(w=10, h=10)
    cmds.text(l="Contact- +91-79731-60350 (ank14ban1013@gmail.com)",h=10,al="center")
    cmds.separator(w=10, h=10)
    cmds.text(l="<<<<  UPDATED FOR REDEFINE USE ONLY >>>>",h=10,al="center")
    cmds.separator(w=10, h=10)
    cmds.showWindow(window)
#####################################################################################
def convertClusterToJoint():
    selectList = cmds.ls (sl=1)
    baseJoint = cmds.createNode('joint',n='base_weight_jnt',ss=1)
    for deformObject in selectList: 
        clusterShape = cmds.listRelatives(deformObject, s=1)[0]
        defFrom = cmds.listConnections(clusterShape, d=1, s=0)[0]
        clusterGeoShape = cmds.cluster(deformObject,q=1,g=1)[0]
        meshObject = cmds.listRelatives(clusterGeoShape,p=1)[0]   
        skinCluster = mel.eval("findRelatedSkinCluster {}".format(clusterGeoShape))
        joint = cmds.createNode('joint',n='{}_jnt'.format(deformObject),ss=1)
        cmds.delete(cmds.parentConstraint(deformObject,joint,mo=0))
        if len(skinCluster) == 0:
            bindSkin = cmds.skinCluster(baseJoint, clusterGeoShape, tsb=1) 
            addSkin = cmds.skinCluster(clusterGeoShape, e=1, ai=joint, wt=0) 
        else:
            addSkin = cmds.skinCluster(clusterGeoShape, e=1, ai=joint, wt=0) 
        skinCluster = mel.eval("findRelatedSkinCluster {}".format(clusterGeoShape)) 
          
        transferElements = cmds.ls(skinCluster,defFrom,baseJoint,joint)
        if not len(transferElements) == 4:
            cmds.warning ('Validation Error: geometry skinCluster, deformerCluster or loaded joints')   
        else : 
            vertexCount = cmds.select('{}.vtx[*]'.format(meshObject))
            meshToVert = cmds.ls(sl=1,fl=1)        
            gMainProgressBar = mel.eval('$tmp = $gMainProgressBar')    
            for i in range(len(meshToVert)):
                deformerWeights = cmds.percent (defFrom, meshToVert[i], q=1, v=1)
                bindWeights = cmds.skinPercent(skinCluster, meshToVert[i], t = baseJoint, q=True )
                cmds.progressBar(gMainProgressBar,e=1,bp=1,max=(len(meshToVert))) 
                cmds.progressBar(gMainProgressBar,e=1,st=('transferring deformer weight.. '),s=1)
                if bindWeights > 0:       
                    weightDifference = bindWeights - deformerWeights[0]
                    cmds.skinPercent(skinCluster, meshToVert[i], tv=[(baseJoint, weightDifference), (joint, deformerWeights[0])] )
                    print i        
            cmds.progressBar(gMainProgressBar,e=1,ep=1)
            cmds.select (cl=1)
#####################################################################################
def importSkeleton(skeletonGroup='joint_grp'):
    basicFilter = "*.json"
    filePath = cmds.fileDialog2(fileFilter=basicFilter,dialogStyle = 4,okc = 'Open',cap = 'Open')
    joint_Pos_Data = json.loads(open(filePath[0],"r").read())
    if cmds.objExists(skeletonGroup):
        cmds.delete(skeletonGroup)
    skeleton_grp = cmds.group(em=1,w=1,n=skeletonGroup)
    for joint, values in joint_Pos_Data.items():
        jointName = values["jointName"]
        worldPosition = values["worldPosition"]
        translation = values["translation"]
        scale = values["scale"]
        jointOrient = values["jointOrient"]
        parentJoint = values["parentJoint"]   
        rotation = values["rotation"]
        cmds.select(cl=1)
        createJoint = cmds.joint(p=(worldPosition[0],worldPosition[1],worldPosition[2]),n=jointName)          
        
        cmds.setAttr('%s.jointOrientX'% createJoint, rotation[0])
        cmds.setAttr('%s.jointOrientY'% createJoint, rotation[1])
        cmds.setAttr('%s.jointOrientZ'% createJoint, rotation[2])
        cmds.setAttr('%s.scaleX'% createJoint, scale[0])
        cmds.setAttr('%s.scaleY'% createJoint, scale[1])
        cmds.setAttr('%s.scaleZ'% createJoint, scale[2])
    for joint, values in joint_Pos_Data.items():  
        jointName = values["jointName"]
        parentJoint = values["parentJoint"]
        cmds.parent(jointName,parentJoint)
#####################################################################################
def exportClusters():
    clusters = cmds.ls(sl=1)
    clu_wgt= {}
    if not clusters:
        cmds.error("Kindly select the atleast one object.")
    for i in range(len(clusters)):
        clusterName = clusters[i]
        shape_node = cmds.listRelatives(clusters[i], shapes=True)[0]
        deformerNode = cmds.listConnections(shape_node, d=1, s=0)[0]
        clusterPosition = cmds.xform(clusters[i],q=1,ws=1,piv=1)
        geoShape_node = cmds.cluster (deformerNode, q=1, g=1)
        vertexCount = cmds.polyListComponentConversion(geoShape_node, tv=1)
        cmds.select(vertexCount)
        selVertex = cmds.ls (sl=1, fl=1);cmds.select(cl=1)    
        cluWeights = cmds.percent (deformerNode, selVertex, q=1,v=1) 
        clu_wgt[shape_node] = {}    
        clu_wgt[shape_node]["clusterName"] = clusterName
        clu_wgt[shape_node]["deformerName"] = deformerNode
        clu_wgt[shape_node]["geometryName"] = geoShape_node
        clu_wgt[shape_node]["clusterPosition"]= clusterPosition
        clu_wgt[shape_node]["obj_weights"] = cluWeights
    
    basicFilter = "*.json"
    file_path = cmds.fileDialog2(fileFilter=basicFilter, dialogStyle=0)
    with open(file_path[0], 'w') as outfile:
        json.dump(clu_wgt, outfile)
    print clu_wgt
#####################################################################################
def exportDQWeights():
    # dump DQ data
    mesh = cmds.ls(sl=1)
    dq_wgt= {}
    if not mesh:
        cmds.error("Kindly select the atleast one object.")
    for i in range(len(mesh)):
        shape_node = cmds.listRelatives(mesh[i], shapes=True)[0]
        skin_cluster = mel.eval("findRelatedSkinCluster {}".format(shape_node))
        cmds.setAttr('{}.skinningMethod'.format(skin_cluster),2)        
        dqWeights = cmds.getAttr(skin_cluster + '.ptw')
        dq_wgt[shape_node] = {}
        dq_wgt[shape_node]["skin_cluster"] = skin_cluster
        dq_wgt[shape_node]["obj_weights"] = dqWeights
    basicFilter = "*.json"
    file_path = cmds.fileDialog2(fileFilter=basicFilter,dialogStyle = 0)
    with open(file_path[0], 'w') as outfile:
        json.dump(dq_wgt, outfile)
    print dq_wgt
#####################################################################################
def importDQWeights():
    basicFilter = "*.json"
    filePath = cmds.fileDialog2(fileFilter=basicFilter,dialogStyle = 4,okc = 'Open',cap = 'Open')
    dq_wait_data = json.loads(open(filePath[0],"r").read())
    for mesh, values in dq_wait_data.items():
        skin_cluster = values["skin_cluster"]
        waights = values["obj_weights"]
        [cmds.setAttr(skin_cluster + '.blendWeights[{}]'.format(i), val) for i, val in enumerate(waights)]
        cmds.setAttr(skin_cluster + ".skinningMethod" ,2)
        cmds.setAttr(skin_cluster + ".dqsSupportNonRigid", l=0)
        cmds.setAttr(skin_cluster + ".dqsSupportNonRigid", 1,l=1)
        if cmds.objExists('base_global_transform'):
            cmds.connectAttr('base_global_transform.scale','{}.dqsScale'.format(skin_cluster),f=1)
            cmds.setAttr('{}.dqsScale'.format(skin_cluster),l=1)
#####################################################################################
# dump Skin Weight data
def exportSkinWeights():
    meshes = cmds.ls(sl=1)
    skin_wgt= {}
    for mesh in meshes:
        shapeName = cmds.listRelatives(mesh, shapes=True)[0]
        clusterName = mel.eval("findRelatedSkinCluster {}".format(shapeName))
        jointList = cmds.skinCluster(clusterName,query=True,inf=True)
        
        # get the MFnSkinCluster for clusterName
        selList = OpenMaya.MSelectionList()
        selList.add(clusterName)
        clusterNode = OpenMaya.MObject()
        selList.getDependNode(0, clusterNode)
        skinFn = OpenMayaAnim.MFnSkinCluster(clusterNode)
    
        # get the MDagPath for all influence
        infDags = OpenMaya.MDagPathArray()
        skinFn.influenceObjects(infDags)
        
        # create a dictionary whose key is the MPlug indice id and 
        # whose value is the influence list id
        infIds = {}
        infs = []
        for x in xrange(infDags.length()):
            	infPath = infDags[x].fullPathName()
            	infId = int(skinFn.indexForInfluenceObject(infDags[x]))
            	infIds[infId] = x
            	infs.append(infPath)
        
        # get the MPlug for the weightList and weights attributes
        wlPlug = skinFn.findPlug('weightList')
        wPlug = skinFn.findPlug('weights')
        wlAttr = wlPlug.attribute()
        wAttr = wPlug.attribute()
        wInfIds = OpenMaya.MIntArray()
        
        
        # the weights are stored in dictionary, the key is the vertId, 
        # the value is another dictionary whose key is the influence id and 
        # value is the weight for that influence
        weightList = {}
        for vId in xrange(wlPlug.numElements()):
            	vWeights = {}
            	# tell the weights attribute which vertex id it represents
            	wPlug.selectAncestorLogicalIndex(vId, wlAttr)
            	
            	# get the indice of all non-zero weights for this vert
            	wPlug.getExistingArrayAttributeIndices(wInfIds)
            
            	# create a copy of the current wPlug
            	infPlug = OpenMaya.MPlug(wPlug)
            	for infId in wInfIds:
            		# tell the infPlug it represents the current influence id
            		infPlug.selectAncestorLogicalIndex(infId, wAttr)
            		
            		# add this influence and its weight to this verts weights
            		try:
            			vWeights[infIds[infId]] = infPlug.asDouble()
            		except KeyError:
            			# assumes a removed influence
            			pass
            	weightList[vId] = vWeights
            
        skin_wgt[shapeName] = {}
        skin_wgt[shapeName]["clusterName"] = clusterName
        skin_wgt[shapeName]["obj_weights"] = weightList
        skin_wgt[shapeName]["jointList"] = jointList
        skin_wgt[shapeName]["mesh"] = mesh
    
        
    basicFilter = "*.json"
    file_path = cmds.fileDialog2(fileFilter=basicFilter,dialogStyle = 0)
    with open(file_path[0], 'w') as outfile:
        json.dump(skin_wgt, outfile)
    print skin_wgt
#####################################################################################
def importSkinWeights():   
    basicFilter = "*.json"
    filePath = cmds.fileDialog2(fileFilter=basicFilter,dialogStyle = 4,okc = 'Open',cap = 'Open')
    skin_wait_data = json.loads(open(filePath[0],"r").read())  
    
    for mesh, values in skin_wait_data.items():
        clusterName = values["clusterName"] 
        weights = values["obj_weights"] 
        jointList = values["jointList"] 
        mesh = values["mesh"]    
        
        shape_node = cmds.listRelatives(mesh, shapes=True)[0]
        deformedShape_node = shape_node+'Deformed'
        geoSkinCluster = cmds.skinCluster(jointList, shape_node,tsb=1,n=clusterName)[0]
    
        # get the MFnSkinCluster for clusterName
        selList = OpenMaya.MSelectionList()
        selList.add(clusterName)
        clusterNode = OpenMaya.MObject()
        selList.getDependNode(0, clusterNode)
        skinFn = OpenMayaAnim.MFnSkinCluster(clusterNode)
        
        # get the MDagPath for all influence
        infDags = OpenMaya.MDagPathArray()
        skinFn.influenceObjects(infDags)
        
        # create a dictionary whose key is the MPlug indice id and 
        # whose value is the influence list id
        infIds = {}
        infs = []
        for x in xrange(infDags.length()):
        	infPath = infDags[x].fullPathName()
        	infId = int(skinFn.indexForInfluenceObject(infDags[x]))
        	infIds[infId] = x
        	infs.append(infPath)
        # unlock influences used by skincluster
        for inf in infs:
        	cmds.setAttr('%s.liw' % inf)
        
        # normalize needs turned off for the prune to work
        skinNorm = cmds.getAttr('%s.normalizeWeights' % clusterName)
        if skinNorm != 0:
        	cmds.setAttr('%s.normalizeWeights' % clusterName, 0)
        cmds.skinPercent(clusterName, deformedShape_node, nrm=False, prw=100)
    
        # restore normalize setting
        if skinNorm != 0:
        	cmds.setAttr('%s.normalizeWeights' % clusterName, skinNorm)
        	
        # set weights
        for vertId, weightData in weights.items():
        	wlAttr = '%s.weightList[%s]' % (clusterName, vertId)
        	for infId, infValue in weightData.items():
        		wAttr = '.weights[%s]' % infId
        		cmds.setAttr(wlAttr + wAttr, infValue)        		
    cmds.select(cl=1)
#####################################################################################
def importClusters():
    basicFilter = "*.json"
    filePath = cmds.fileDialog2(fileFilter=basicFilter,dialogStyle = 4,okc = 'Open',cap = 'Open')
    clu_wait_data = json.loads(open(filePath[0],"r").read())
    for clusters, values in clu_wait_data.items():
        clusterName = values["clusterName"]
        deformerName = values["deformerName"]
        geometryName = values["geometryName"]
        cluster_xyz = values["clusterPosition"]
        vertexCount = cmds.polyListComponentConversion(geometryName, tv=1)
        cmds.select(vertexCount)
        selVertex = cmds.ls (sl=1, fl=1);cmds.select(cl=1)  
        applyCluster = cmds.cluster(geometryName,n=clusterName)  
            
        waights = values["obj_weights"]
            
        [cmds.percent (clusterName, selVertex[i], v=val) for i, val in enumerate(waights)]
        cmds.setAttr('%s.rotatePivotX'% applyCluster[1], cluster_xyz[0])
        cmds.setAttr('%s.rotatePivotY'% applyCluster[1], cluster_xyz[1])
        cmds.setAttr('%s.rotatePivotZ'% applyCluster[1], cluster_xyz[2])
        cmds.setAttr('%s.scalePivotX'% applyCluster[1], cluster_xyz[0])
        cmds.setAttr('%s.scalePivotY'% applyCluster[1], cluster_xyz[1])
        cmds.setAttr('%s.scalePivotZ'% applyCluster[1], cluster_xyz[2])  
        clusterShape = cmds.listRelatives (applyCluster[1], s=1)         
        cmds.setAttr('%s.originX'% clusterShape[0], cluster_xyz[0])
        cmds.setAttr('%s.originY'% clusterShape[0], cluster_xyz[1])
        cmds.setAttr('%s.originZ'% clusterShape[0], cluster_xyz[2])
#####################################################################################       
def ObjShp():
    obj=cmds.listRelatives(s=1)
    cmds.textFieldButtonGrp('selobj',e=1,tx=obj[0])
#####################################################################################
def loadMeshCmd(*args) :
    cmds.textScrollList ('meshList', e=1, ra=1)    
    selection = cmds.ls(sl=1)
    tranSelection = cmds.listRelatives (selection, s=1)
    if len(selection) >> 0 :       
        for eachTrans in tranSelection :
            type = cmds.objectType(eachTrans, isType='mesh')
            if type == 1 :
                interValue = cmds.getAttr((eachTrans + '.intermediateObject'))
                if interValue == 0 :
                    cmds.textScrollList ('meshList', e=1, a=eachTrans)
            else :
                cmds.warning ('Please select the mesh')
#####################################################################################
def loadShapeList():
    cmds.textScrollList ('meshList', e=1, ra=1)    
    selection = cmds.ls(sl=1)
    tranSelection = cmds.listRelatives (selection, s=1)
    if len(selection) >> 0 :       
        for eachTrans in tranSelection :
            type = cmds.objectType(eachTrans, isType='mesh')
            if type == 1 :
                interValue = cmds.getAttr((eachTrans + '.intermediateObject'))
                if interValue == 0 :
                    cmds.textScrollList ('meshList', e=1, a=eachTrans)
            else :
                cmds.warning ('Please select the mesh')
#####################################################################################
def FromMesh(*args):
    obj=cmds.ls(sl=1)
    cmds.textFieldButtonGrp('fromObj',e=1,tx=obj[0])
#####################################################################################
def ToMesh(*args):
    obj=cmds.ls(sl=1)
    cmds.textFieldButtonGrp('toObj',e=1,tx=obj[0])
#####################################################################################
def FromDeformer(*args):
    selectDeformer = cmds.ls(sl=1)
    deformerShape = cmds.listRelatives (selectDeformer[0], s=1)
    deformerName = cmds.listConnections( deformerShape[0], d=1, s=0)
    for eachOutput in deformerName:
        deformerNode = cmds.nodeType(eachOutput)
        if deformerNode == 'wire':
            cmds.textFieldButtonGrp ('fromDef', e=1, tx=eachOutput)    
            cmds.textFieldGrp ('deformerName', e=1, tx=selectDeformer[0])    
        elif deformerNode == 'cluster':
            cmds.textFieldButtonGrp ('fromDef', e=1, tx=eachOutput)
            cmds.textFieldGrp ('deformerName', e=1, tx=selectDeformer[0])  
#####################################################################################
def mirrorDeformer(*args):    
    defTran = cmds.textFieldGrp ('deformerName', q=1, tx=1)
    defName = cmds.textFieldButtonGrp ('fromDef', q=1, tx=1)
    mirrorAction = cmds.radioButtonGrp('typeSwitch', q=1, sl=1)
    mirrorAxis = cmds.radioCollection('axisSwitch', q=1, sl=1)
    PosToNeg = cmds.checkBox('PosNegCheck',q=1,v=1)
    cluGeo = cmds.cluster (defName, q=1, g=1)
    
    #create an mirror cluter as per axis
    if mirrorAction == 1:
        mirrorClu = cmds.cluster (cluGeo)

        for eachGeo in cluGeo:
            vertexCount = cmds.polyListComponentConversion(eachGeo, tv=1)
            cmds.select (vertexCount)
            selVertex = cmds.ls (sl=1, fl=1)
            cmds.symmetricModelling (s=1, a='world', ax=mirrorAxis)
            for index in range (len(selVertex)) :
                cluWeight = cmds.percent (mirrorClu[0], selVertex[index], v=0)                
                cmds.select (selVertex[index], r=1, sym=1)
                mirrorVertex = cmds.ls (sl=1)
                weights = cmds.percent (defName, mirrorVertex, q=1, v=1)                
                if PosToNeg == 1 :
                    if len(mirrorVertex) == 2 :
                        cluWeight = cmds.percent (mirrorClu[0], mirrorVertex[1], v=weights[0])
                        cluWeight = cmds.percent (mirrorClu[0], mirrorVertex[0], v=weights[1])
                    elif len(mirrorVertex) == 1 :
                        cluWeight = cmds.percent (mirrorClu[0], mirrorVertex[0], v=weights[0])

            cmds.symmetricModelling (s=0, a='world', ax=mirrorAxis)
            cmds.select (cl=1)
                
        cluster_xyz                 = cmds.xform (defTran, q=1, ws=1, piv=1)
        clusterShape                = cmds.listRelatives (mirrorClu[1], s=1) 
        
        if mirrorAxis == 'X' :
            cmds.setAttr ('%s.rotatePivotX'% mirrorClu[1], -(cluster_xyz[0]))
            cmds.setAttr ('%s.rotatePivotY'% mirrorClu[1], cluster_xyz[1])
            cmds.setAttr ('%s.rotatePivotZ'% mirrorClu[1], cluster_xyz[2])
            cmds.setAttr ('%s.scalePivotX'% mirrorClu[1], -(cluster_xyz[0]))
            cmds.setAttr ('%s.scalePivotY'% mirrorClu[1], cluster_xyz[1])
            cmds.setAttr ('%s.scalePivotZ'% mirrorClu[1], cluster_xyz[2])
           
            cmds.setAttr ('%s.originX'% clusterShape[0], -(cluster_xyz[0]))
            cmds.setAttr ('%s.originY'% clusterShape[0], cluster_xyz[1])
            cmds.setAttr ('%s.originZ'% clusterShape[0], cluster_xyz[2])
            
        elif mirrorAxis == 'Y' :
            cmds.setAttr ('%s.rotatePivotX'% mirrorClu[1], cluster_xyz[0])
            cmds.setAttr ('%s.rotatePivotY'% mirrorClu[1], -(cluster_xyz[1]))
            cmds.setAttr ('%s.rotatePivotZ'% mirrorClu[1], cluster_xyz[2])
            cmds.setAttr ('%s.scalePivotX'% mirrorClu[1], cluster_xyz[0])
            cmds.setAttr ('%s.scalePivotY'% mirrorClu[1], -(cluster_xyz[1]))
            cmds.setAttr ('%s.scalePivotZ'% mirrorClu[1], cluster_xyz[2])
           
            cmds.setAttr ('%s.originX'% clusterShape[0], cluster_xyz[0])
            cmds.setAttr ('%s.originY'% clusterShape[0], -(cluster_xyz[1]))
            cmds.setAttr ('%s.originZ'% clusterShape[0], cluster_xyz[2])
            
        elif mirrorAxis == 'Z' :
            cmds.setAttr ('%s.rotatePivotX'% mirrorClu[1], cluster_xyz[0])
            cmds.setAttr ('%s.rotatePivotY'% mirrorClu[1], cluster_xyz[1])
            cmds.setAttr ('%s.rotatePivotZ'% mirrorClu[1], -(cluster_xyz[2]))
            cmds.setAttr ('%s.scalePivotX'% mirrorClu[1], cluster_xyz[0])
            cmds.setAttr ('%s.scalePivotY'% mirrorClu[1], cluster_xyz[1])
            cmds.setAttr ('%s.scalePivotZ'% mirrorClu[1], -(cluster_xyz[2]))
           
            cmds.setAttr ('%s.originX'% clusterShape[0], cluster_xyz[0])
            cmds.setAttr ('%s.originY'% clusterShape[0], cluster_xyz[1])
            cmds.setAttr ('%s.originZ'% clusterShape[0], -(cluster_xyz[2]))
        
    elif mirrorAction == 2:
                
        for eachGeo in cluGeo:
            vertexCount = cmds.polyListComponentConversion(eachGeo, tv=1)
            cmds.select (vertexCount)
            selVertex = cmds.ls (sl=1, fl=1)
            cmds.symmetricModelling (s=1, a='world', ax=mirrorAxis)
        
            for index in range (len(selVertex)) :
                cmds.select (selVertex[index], r=1, sym=1)
                mirrorVertex = cmds.ls (sl=1)
                weights = cmds.percent (defName, mirrorVertex, q=1, v=1)
                print weights
            
                if PosToNeg == 1 :
                    if len(mirrorVertex) == 2 :
                        cluWeight = cmds.percent (defName, mirrorVertex[1], v=weights[0])
                else :
                    if len(mirrorVertex) == 2 :
                        cluWeight = cmds.percent (defName, mirrorVertex[0], v=weights[1])
        
            cmds.symmetricModelling (s=0, a='world', ax=mirrorAxis)
            cmds.select (cl=1)
#####################################################################################
def ToDeformer(*args):
    selectDeformer = cmds.ls(sl=1)
    deformerShape = cmds.listRelatives (selectDeformer[0], s=1)
    deformerName = cmds.listConnections( deformerShape[0], d=1, s=0)
    for eachOutput in deformerName:
        deformerNode = cmds.nodeType(eachOutput)
        if deformerNode == 'wire':
            cmds.textFieldButtonGrp ('toDef', e=1, tx=eachOutput)        
        elif deformerNode == 'cluster':
            cmds.textFieldButtonGrp ('toDef', e=1, tx=eachOutput)
#####################################################################################
def FromJoint():
    obj=cmds.ls(sl=1,typ='transform')
    cmds.textFieldButtonGrp('fromJoint',e=1,tx=obj[0])    
#####################################################################################
def ToJoint():
    obj=cmds.ls(sl=1,typ='transform')
    cmds.textFieldButtonGrp('toJoint',e=1,tx=obj[0])    
#####################################################################################   
def listExtrap():
    sel = cmds.ls(sl=1)
    for i in range(len(sel)):
        cmds.select(sel[i])
        listClusterExtrap()
#####################################################################################   
def shapeExtrap():
    sel = cmds.ls(sl=1)
    for i in range(len(sel)):
        cmds.select(sel[i])
        shapeClusterExtrap()        
#####################################################################################
def shapeClusterExtrap():
    selectList = cmds.ls (sl=1)
    
    for deformObject in selectList :
        meshObject = cmds.textFieldButtonGrp('selobj',q=1,tx=True)
    #deformObject = 'cluster3Handle'
    
    #Input object to  Dag Path 
    meshSelectionList = om.MSelectionList()
    meshSelectionList.add (meshObject)
    meshDagPath = meshSelectionList.getDagPath(0)
    
    deformSelectionList = om.MSelectionList()
    deformSelectionList.add (deformObject)
    deformDagPath = deformSelectionList.getDagPath (0)
    
    #Get the vertex Orig Position
    mfnMesh = om.MFnMesh(meshDagPath)
    origPositionList = mfnMesh.getPoints (om.MSpace.kObject)
    
    #Set the transform value to deformer
    mfnTransform = om.MFnTransform (deformDagPath)
    xyzMVector = om.MVector (1,0,0)
    mfnTransform.setTranslation (xyzMVector, om.MSpace.kTransform)
    
    deformPositionList = mfnMesh.getPoints (om.MSpace.kObject)
    
    
    
    weightList = []
    for index in range (len(origPositionList)) :
        origMVector = om.MVector (origPositionList[index])
        deformMVector = om.MVector (deformPositionList[index])
        
        length = origMVector-deformMVector
        weight = length.length()
        weightList.append (weight)
    
    zeroMVector = om.MVector (0,0,0)
    mfnTransform.setTranslation(zeroMVector,om.MSpace.kTransform)
      
    #Create New Cluster
    
    newCluster = cmds.cluster (meshObject, n='New_Cluster')
    
    
    #Set Weights to vertex
    for index in range (len(weightList)) :
        cmds.setAttr('%s.weightList[0].w[%s]'%(newCluster[0], index), weightList[index])
        
    #Change the cluster Position
    cluster_xyz = cmds.xform(deformObject, q=1,ws=1,piv=1)
    clusterShape = cmds.listRelatives (newCluster[1], s=1)
    
    cmds.setAttr('%s.rotatePivotX'% newCluster[1], cluster_xyz[0])
    cmds.setAttr('%s.rotatePivotY'% newCluster[1], cluster_xyz[1])
    cmds.setAttr('%s.rotatePivotZ'% newCluster[1], cluster_xyz[2])
    cmds.setAttr('%s.scalePivotX'% newCluster[1], cluster_xyz[0])
    cmds.setAttr('%s.scalePivotY'% newCluster[1], cluster_xyz[1])
    cmds.setAttr('%s.scalePivotZ'% newCluster[1], cluster_xyz[2])  
         
    cmds.setAttr('%s.originX'% clusterShape[0], cluster_xyz[0])
    cmds.setAttr('%s.originY'% clusterShape[0], cluster_xyz[1])
    cmds.setAttr('%s.originZ'% clusterShape[0], cluster_xyz[2])
    
    print '\n#Successfully created New Cluster'
#####################################################################################
def listClusterExtrap():
    selectList = cmds.ls (sl=1)
    meshNode = cmds.textScrollList ("meshList", q=1, allItems=1)
    
    for deformObject in selectList :
        mainCluster = cmds.cluster(meshNode)
        cmds.percent(mainCluster[0],meshNode,v=0.0)
        for meshObject in meshNode:
            vertexName = cmds.listRelatives (meshObject, p=1)       
          
            #Input object to  Dag Path 
            meshSelectionList = om.MSelectionList()
            meshSelectionList.add (meshObject)
            meshDagPath = meshSelectionList.getDagPath(0)
            
            deformSelectionList = om.MSelectionList()
            deformSelectionList.add (deformObject)
            deformDagPath = deformSelectionList.getDagPath (0)
            
            #Get the vertex Orig Position
            mfnMesh = om.MFnMesh(meshDagPath)
            origPositionList = mfnMesh.getPoints (om.MSpace.kObject)
            
            #Set the transform value to deformer
            mfnTransform = om.MFnTransform (deformDagPath)
            xyzMVector = om.MVector (1,0,0)
            mfnTransform.setTranslation (xyzMVector, om.MSpace.kTransform)
            
            deformPositionList = mfnMesh.getPoints (om.MSpace.kObject)  
            
            weightList = []
            for index in range (len(origPositionList)) :
                origMVector = om.MVector (origPositionList[index])
                deformMVector = om.MVector (deformPositionList[index])
                
                length = origMVector-deformMVector
                weight = length.length()
                weightList.append (weight)
            
            zeroMVector = om.MVector (0,0,0)
            mfnTransform.setTranslation(zeroMVector,om.MSpace.kTransform)
            
            #Set Weights to vertex
            vertexCountEx = cmds.polyListComponentConversion(meshObject, tv=1)
            cmds.select (vertexCountEx)
            selVertex = cmds.ls (sl=1, fl=1)
            
            gMainProgressBar = maya.mel.eval('$tmp = $gMainProgressBar')
            cmds.progressBar(gMainProgressBar,e=1,beginProgress=1,maxValue=(len(selVertex)))
            
            for index in range (len(selVertex)) : 
                cmds.progressBar(gMainProgressBar,e=1,status=('extracting cluster.. ' + deformObject + ' ' + meshObject),step=1)
                if weightList[index] > 0 :
                    cluWeight = cmds.percent (mainCluster[0], selVertex[index], v=weightList[index])
            
            cmds.progressBar(gMainProgressBar,e=1,endProgress=1)
            cmds.select (cl=1)   
                
            #Change the cluster Position
            cluster_xyz = cmds.xform(deformObject, q=1,ws=1,piv=1)
            clusterShape = cmds.listRelatives (mainCluster[1], s=1)
            
            cmds.setAttr('%s.rotatePivotX'% mainCluster[1], cluster_xyz[0])
            cmds.setAttr('%s.rotatePivotY'% mainCluster[1], cluster_xyz[1])
            cmds.setAttr('%s.rotatePivotZ'% mainCluster[1], cluster_xyz[2])
            cmds.setAttr('%s.scalePivotX'% mainCluster[1], cluster_xyz[0])
            cmds.setAttr('%s.scalePivotY'% mainCluster[1], cluster_xyz[1])
            cmds.setAttr('%s.scalePivotZ'% mainCluster[1], cluster_xyz[2])  
                 
            cmds.setAttr('%s.originX'% clusterShape[0], cluster_xyz[0])
            cmds.setAttr('%s.originY'% clusterShape[0], cluster_xyz[1])
            cmds.setAttr('%s.originZ'% clusterShape[0], cluster_xyz[2])
            
            print '\n#Successfully created New Cluster'
#####################################################################################
def latSkin():
    selectList = cmds.ls (sl=1)
    latticeShape = cmds.listRelatives(selectList[0], type='lattice')[0]
    ffd = cmds.listConnections(latticeShape, type='ffd')[0]
    skincluster = cmds.listConnections(latticeShape, type='skinCluster')[0]
    geometry = cmds.lattice(latticeShape, q=1, g=1)[0]
    jointList = cmds.skinCluster(skincluster, q=1, inf=1)
    cmds.parent(jointList,w=1)
    cmds.select(cl=1)
    #Geo to Dag Path
    meshMSelection = om.MSelectionList()
    meshMSelection.add(geometry)
    meshDagPath = meshMSelection.getDagPath(0)
    
    #Get the mesh Origin Position
    mFnMesh = om.MFnMesh(meshDagPath)
    geoPosition = mFnMesh.getPoints(om.MSpace.kObject)
    
    #Get Weight for each joints
    weightList = []
    for index in range(len(jointList)):
        jointMSelection = om.MSelectionList()
        jointMSelection.add(jointList[index])
        jointDagPath = jointMSelection.getDagPath(0)
        
        #Set and reset deformation value for joints
        mFnTransform = om.MFnTransform(jointDagPath)
        world = mFnTransform.translation(om.MSpace.kWorld)
        moveWorld = om.MVector(world.x+1, world.y, world.z)
        mFnTransform.setTranslation (moveWorld, om.MSpace.kWorld)
        movePosition = mFnMesh.getPoints(om.MSpace.kObject)
        jointWeights = []
        for vertexIndex in range(len(movePosition)):
            length = movePosition[vertexIndex]-geoPosition[vertexIndex]
            weight = length.length()
            jointWeights.append(weight)
        weightList.append(jointWeights)    
        mFnTransform.setTranslation (world, om.MSpace.kWorld)
        
    #Set Weight for each joints
    geoSkinCluster = cmds.skinCluster(jointList, geometry)[0]
    skinMSelection = om.MSelectionList()
    skinMSelection.add(geoSkinCluster)
    skinMObject = skinMSelection.getDependNode(0)
    mFnSkinCluster = oma.MFnSkinCluster(skinMObject)
    
    #Vertex Components
    vertexIndexList = range(len(geoPosition))
    mfnIndexComp = om.MFnSingleIndexedComponent()
    vertexComp = mfnIndexComp.create(om.MFn.kMeshVertComponent)
    mfnIndexComp.addElements(vertexIndexList)
    
    #Influences
    influenceObjects = mFnSkinCluster.influenceObjects()
    influenceList = om.MIntArray()
    for eachInfluenceObject in influenceObjects:
        currentIndex = mFnSkinCluster.indexForInfluenceObject(eachInfluenceObject)
        influenceList.append(currentIndex)
    
    #Weights
    mWeightList = om.MDoubleArray()
    for wIndex in range(len(weightList[0])):
        for jntIndex in range(len(weightList)):
            mWeightList.append(weightList[jntIndex][wIndex])
        
    mFnSkinCluster.setWeights(meshDagPath, vertexComp, influenceList, mWeightList)
    
    myNum  = len(jointList)
    ob = (myNum-1)
    for j in range(ob):
        cmds.parent(jointList[j+1], jointList[j])
    print '/nLattice Weight Transferred Successfully'
#####################################################################################
def softSelClu():
    pivot = cmds.ls(sl=1, fl=True)
    softSelection = om.MGlobal.getRichSelection ()
    richSelection = om.MRichSelection (softSelection)
    selectionList = richSelection.getSelection ()
    component = selectionList.getComponent (0)
    
    
    componentIndex = om.MFnSingleIndexedComponent(component[1])
    vertexList = componentIndex.getElements ()
    print len(vertexList)
    
    weightList = {}
    
    for loop in range (len(vertexList)) :
        weight = componentIndex.weight (loop)
        influence = weight.influence
        weightList.setdefault (vertexList[loop], influence)
    
    
    #Set soft selection range and influence to new cluster
    rangeVertexs = selectionList.getSelectionStrings ()
    myCluster = cmds.cluster (rangeVertexs, n='Extrap_Cluster')
    
    for eachWeight in weightList :
        currentVertex = eachWeight
        currentWeight = weightList[eachWeight]
        #print currentVertex, '\t', currentWeight
        cmds.setAttr ('%s.weightList[0].w[%i]'% (myCluster[0], currentVertex), currentWeight)
    
    
    #Change the cluster position
    
    xyz = cmds.xform(pivot, q=1, ws=1, t=1)
    clusterShape = cmds.listRelatives(myCluster[1], s=1)
    cmds.setAttr('%s.rotatePivotX'% myCluster[1], xyz[0])
    cmds.setAttr('%s.rotatePivotY'% myCluster[1], xyz[1])
    cmds.setAttr('%s.rotatePivotZ'% myCluster[1], xyz[2])
    cmds.setAttr('%s.scalePivotX'% myCluster[1], xyz[0])
    cmds.setAttr('%s.scalePivotY'% myCluster[1], xyz[1])
    cmds.setAttr('%s.scalePivotZ'% myCluster[1], xyz[2])
    cmds.setAttr('%s.originX'% clusterShape[0], xyz[0])
    cmds.setAttr('%s.originY'% clusterShape[0], xyz[1])
    cmds.setAttr('%s.originZ'% clusterShape[0], xyz[2])
    
    
    print 'Successfully created My Soft Cluster'    
#####################################################################################
def transferWeights(*args):
    meshFrom = cmds.textFieldButtonGrp('fromObj',q=1,tx=True)
    meshTo = cmds.textFieldButtonGrp('toObj',q=1,tx=True)
    
    defFrom = cmds.textFieldButtonGrp('fromDef',q=1,tx=True)
    defTo = cmds.textFieldButtonGrp('toDef',q=1,tx=True)
    
    meshToVert = cmds.select('{}.vtx[*]'.format(meshTo))
    meshToVertCount = cmds.ls(sl=1,fl=1)
    meshFromVert = cmds.select('{}.vtx[*]'.format(meshFrom))
    meshFromVertCount =  cmds.ls(sl=1,fl=1)   

    if len(meshToVertCount) == len(meshFromVertCount):
        gMainProgressBar = maya.mel.eval('$tmp = $gMainProgressBar')
        cmds.progressBar(gMainProgressBar,e=1,beginProgress=1,maxValue=len(meshToVertCount))
        for i in range(len(meshToVertCount)):
            queryWgt = cmds.percent(defFrom,meshFromVertCount[i],q=1,v=1)
            transferWgt = cmds.percent(defTo,meshToVertCount[i],v=queryWgt[0])
        cmds.progressBar(gMainProgressBar,e=1,endProgress=1)
        cmds.select (cl=1)
        print "weight transfer done."                
    else:
        cmds.warning( "Source and target mesh count are not same" )
#####################################################################################
def transferWeightToJoint(*args):    
    meshObject =  cmds.textFieldButtonGrp('selobj',q=1,tx=True)
    defFrom = cmds.textFieldButtonGrp('fromDef',q=1,tx=True)
    transferFromJT = cmds.textFieldButtonGrp('fromJoint',q=1,tx=True)
    transferToJT = cmds.textFieldButtonGrp('toJoint',q=1,tx=True)
    skc = mel.eval("findRelatedSkinCluster {}".format(meshObject))
    transferElements = cmds.ls(skc,defFrom,transferFromJT,transferToJT)
    if not len(transferElements) == 4:
        cmds.warning ('Validation Error: geometry skinCluster, deformerCluster or loaded joints')   
    else : 
        vertexCount = cmds.select('{}.vtx[*]'.format(meshObject))
        meshToVert = cmds.ls(sl=1,fl=1)        
        gMainProgressBar = mel.eval('$tmp = $gMainProgressBar')    
        for i in range(len(meshToVert)):
            deformerWeights = cmds.percent (defFrom, meshToVert[i], q=1, v=1)
            bindWeights = cmds.skinPercent(skc, meshToVert[i], t = transferFromJT, q=True )
            cmds.progressBar(gMainProgressBar,e=1,bp=1,max=(len(meshToVert))) 
            cmds.progressBar(gMainProgressBar,e=1,st=('transferring deformer weight.. '),s=1)
            if bindWeights > 0:       
                weightDifference = bindWeights - deformerWeights[0]
                cmds.skinPercent(skc, meshToVert[i], tv=[(transferFromJT, weightDifference), (transferToJT, deformerWeights[0])] )
                print i        
        cmds.progressBar(gMainProgressBar,e=1,ep=1)
        cmds.select (cl=1)
#####################################################################################       
def wireSkin():
    selectList = cmds.ls (sl=1)
    wireShape = cmds.listRelatives(selectList[0], type='nurbsCurve')[0]
    wire = cmds.listConnections(wireShape, type='wire')[0]
    skincluster = cmds.listConnections(wireShape, type='skinCluster')[0]
    geometry = cmds.wire(wireShape, q=1, g=1)[0]
    jointList = cmds.skinCluster(skincluster, q=1, inf=1)
    #Geo to Dag Path
    meshMSelection = om.MSelectionList()
    meshMSelection.add(geometry)
    meshDagPath = meshMSelection.getDagPath(0)
    
    #Get the mesh Origin Position
    mFnMesh = om.MFnMesh(meshDagPath)
    geoPosition = mFnMesh.getPoints(om.MSpace.kObject)
    
    #Get Weight for each joints
    weightList = []
    for index in range(len(jointList)):
        jointMSelection = om.MSelectionList()
        jointMSelection.add(jointList[index])
        jointDagPath = jointMSelection.getDagPath(0)
        
        #Set and reset deformation value for joints
        mFnTransform = om.MFnTransform(jointDagPath)
        world = mFnTransform.translation(om.MSpace.kWorld)
        moveWorld = om.MVector(world.x+1, world.y, world.z)
        mFnTransform.setTranslation (moveWorld, om.MSpace.kWorld)
        movePosition = mFnMesh.getPoints(om.MSpace.kObject)
        jointWeights = []
        for vertexIndex in range(len(movePosition)):
            length = movePosition[vertexIndex]-geoPosition[vertexIndex]
            weight = length.length()
            jointWeights.append(weight)
        weightList.append(jointWeights)    
        mFnTransform.setTranslation (world, om.MSpace.kWorld)
        
    #Set Weight for each joints
    geoSkinCluster = cmds.skinCluster(jointList, geometry)[0]
    skinMSelection = om.MSelectionList()
    skinMSelection.add(geoSkinCluster)
    skinMObject = skinMSelection.getDependNode(0)
    mFnSkinCluster = oma.MFnSkinCluster(skinMObject)
    
    #Vertex Components
    vertexIndexList = range(len(geoPosition))
    mfnIndexComp = om.MFnSingleIndexedComponent()
    vertexComp = mfnIndexComp.create(om.MFn.kMeshVertComponent)
    mfnIndexComp.addElements(vertexIndexList)
    
    #Influences
    influenceObjects = mFnSkinCluster.influenceObjects()
    influenceList = om.MIntArray()
    for eachInfluenceObject in influenceObjects:
        currentIndex = mFnSkinCluster.indexForInfluenceObject(eachInfluenceObject)
        influenceList.append(currentIndex)
    
    #Weights
    mWeightList = om.MDoubleArray()
    for wIndex in range(len(weightList[0])):
        for jntIndex in range(len(weightList)):
            mWeightList.append(weightList[jntIndex][wIndex])
        
    mFnSkinCluster.setWeights(meshDagPath, vertexComp, influenceList, mWeightList)
    
    print '/nWire Weight Transferred Successfully'
#####################################################################################
def tlkit():
    mel.eval('source "/jobs/jsre/departments/rigging/common_Scripts/toolkit.mel"')
#####################################################################################
def sftCluTool():
    import SoftClusterEX
    reload(SoftClusterEX)
    SoftClusterEX.launch()
#####################################################################################	
def reorderHistory():
    geos = cmds.ls(sl = True,l =True)
    listOrder = ['sculpts','nonLinears','wires','ffds','skinClusters','clusters','blendshapes']
    for geo in geos:
        print geo,'.............................................'
        cmds.select(geo)
        reorderHistoryNode(listOrder, [geo])        
def reorderHistoryNode (listOrder,geos):
    for geo in geos:
        
        blendShapes = []
        
        clusters = []
        mainClusters = []
        
        ffds = []
        skinClusters = []
        wires = []
        
        nonLinears = []
        bends = []
        squashes = []
        
        sculpts = [] 

        if cmds.nodeType(geo) == 'transform':
            geo = cmds.listRelatives(type = 'shape')
        
        history = cmds.listHistory(geo,il = 2,pdo = 1)
        for input in history:
            
            if cmds.nodeType(input) == 'blendShape':
                blendShapes.append(input)
                
            if cmds.nodeType(input) == 'cluster':
                clusters.append(input)
                
            if cmds.nodeType(input) == 'ffd':
                ffds.append(input)

            if cmds.nodeType(input) == 'wire':
                wires.append(input)
                
            if cmds.nodeType(input) == 'nonLinear':
                nonLinears.append(input)
                
            if cmds.nodeType(input) == 'sculpt':
                sculpts.append(input)
                
            if cmds.nodeType(input) == 'skinCluster':
                skinClusters.append(input)
       
        for cluster in clusters[:]:
               
            try:
                match = re.search('Main',cluster)
                s = match.start()
                mainClusters.append(cluster)
                clusters.remove(cluster)
            except:
                pass

        for deformer in nonLinears[:]:
           
            try:
                match = re.search('squash',deformer.lower())
                s = match.start()
                squashes.append(deformer)
                nonLinears.remove(deformer)
                print 'added squash'
            except:
                try:
                    match = re.search('bend',deformer.lower())
                    s = match.start()
                    bends.append(deformer)
                    nonLinears.remove(deformer)
                    print 'added bend'
                except:
                    pass

        blendShapes.sort()       
        clusters.sort()
        mainClusters.sort()
        ffds.sort()
        skinClusters.sort()
        wires.sort()
        nonLinears.sort()
        bends.sort()
        squashes.sort()
        sculpts.sort()
        
        allDeformers = {}
        allDeformers['blendshapes'] = blendShapes
        allDeformers['clusters'] = [mainClusters,clusters]
        allDeformers['ffds'] = ffds
        allDeformers['skinClusters'] = skinClusters
        allDeformers['wires'] = wires
        allDeformers['nonLinears'] = [bends,squashes,nonLinears]
        allDeformers['sculpts'] = sculpts
        
        orderedDeformers = []
        
        for i in range(len(listOrder)):
              
            if listOrder[i] == 'clusters':
                
                for set in allDeformers['clusters']:
                    for deformer in set:
                        orderedDeformers.append(deformer)
        
            elif listOrder[i] == 'nonLinears':
                
                for set in allDeformers['nonLinears']:
                    for deformer in set:
                        orderedDeformers.append(deformer)
        
            else:
                deformers = allDeformers.get(listOrder[i])
                if not deformers == None:
                    for deformer in deformers:
                        orderedDeformers.append(deformer)  
        
        print orderedDeformers            
        for i in range(len(orderedDeformers)-1):
            print (orderedDeformers[i],orderedDeformers[i-1])
            try:
                cmds.reorderDeformers(orderedDeformers[i],orderedDeformers[i+1],geo)
                print 'reodered'
            except:
                pass      
#####################################################################################
def moveAttributeUp():
    currentObj = cmds.ls(sl = True)[0]
    customAttrs = cmds.listAttr(ud = True)
    currentAttr = cmds.channelBox('mainChannelBox',q = True,sma = True)
    customAttrCount = len(customAttrs)
    currentAttrIndexStart = customAttrs.index(currentAttr[0])
    currentAttrIndexEnd = customAttrs.index(currentAttr[-1])
    attrsAbove = customAttrs[0:currentAttrIndexStart] #@UnusedVariable
    attrsBelow = customAttrs[currentAttrIndexEnd+1:customAttrCount]
    print attrsBelow
    print attrsAbove
    cmds.deleteAttr(currentObj,attribute = customAttrs[currentAttrIndexStart-1])
    cmds.undo()            
    for attr in attrsBelow:        
        cmds.deleteAttr(currentObj,attribute = attr)
        cmds.undo()       
#####################################################################################                
def moveAttributeDown():
    currentObj = cmds.ls(sl = True)[0]
    customAttrs = cmds.listAttr(ud = True)
    currentAttr = cmds.channelBox('mainChannelBox',q = True,sma = True)
    customAttrCount = len(customAttrs)
    currentAttrIndexStart = customAttrs.index(currentAttr[0])
    currentAttrIndexEnd = customAttrs.index(currentAttr[-1])
    attrsAbove = customAttrs[0:currentAttrIndexStart] #@UnusedVariable
    attrsBelow = customAttrs[currentAttrIndexEnd+1:customAttrCount]
    print attrsBelow
    print attrsAbove      
    for attr in currentAttr:
        cmds.deleteAttr(currentObj,attribute = attr)
        cmds.undo()    
    for attr in attrsBelow:        
        if attr == attrsBelow[0]:
            pass            
        else:
            cmds.deleteAttr(currentObj,attribute = attr)
            cmds.undo()
            
#####################################################################################
#########
#########              Eyelid Creator Tool For SRRRE
#########
#####################################################################################

def eyelidUI():
    winName = 'eyeLid_Creator'   
    if cmds.window('winName', q=True,exists=True):
        cmds.deleteUI('winName')       
    cmds.window('winName',t='eyeLid_Creator', w=120)
    mainLayout = cmds.columnLayout(adj=True)
    cmds.separator(h=10)
    cmds.button(l='CHECK EYEBALL',c='checkEyeBall()', bgc=(.0,.5,0))     
    cmds.separator(h=10)
    cmds.frameLayout(l='Select closest Loops for eyelash')
    cmds.separator(h=10,w=10,style='in') 
    cmds.rowColumnLayout(nc=3)
    cmds.separator(h=10, w=200)
    cmds.separator(h=10, w=20)   
    cmds.separator(h=10, w=200)     
    cmds.button(l='upper_Loop', c='upperLid()', w=200, bgc=(1, .5, .3))
    cmds.separator(w=20)    
    cmds.button(l='lower_Loop', c='lowerLid()', w=200, bgc=(1, .5, .3))
    cmds.separator(h=10, w=200)
    cmds.separator(h=10, w=20)
    cmds.separator(h=10, w=200)     
    cmds.setParent(mainLayout)    
    cmds.frameLayout(l='Finalized The setup')
    cmds.separator(h=10,w=10,style='in') 
    cmds.button(l='BUILD EYE SETUP',c='finish()', bgc=(1,1,1)) 
    cmds.separator(h=10,w=10,style='in') 
    cmds.button(l='SELECT SKIN JOINTS',c='selectSkinJoints()', bgc=(.4, .2, .4))     
    cmds.separator(h=10,w=10,style='in')   
    cmds.button(l='CONNECT TOONY AND BLENDS',c='connectToonyAndEyelid()', bgc=(.4, .2, .4))     
    cmds.separator(h=10,w=10,style='in')     
    cmds.showWindow('winName')

def upperLid():
    upper_wireCrv = cmds.polyToCurve(dg=1,ch=False, n='L_upper_Wire_crv')
    cmds.reverseCurve(upper_wireCrv,ch=0,rpo=1)
    upper_bsCurve = cmds.duplicate(upper_wireCrv, n='L_upper_bs_crv')
    upper_cntrlCrv = cmds.duplicate(upper_wireCrv, n='L_upper_Main_Control_crv')
    cmds.rebuildCurve(upper_cntrlCrv,d=3,s=4,ch=False)
    cmds.delete(upper_cntrlCrv[0]+'.cv[1]', upper_cntrlCrv[0]+'.cv[5]')        
    upper_closedCrv = cmds.duplicate(upper_cntrlCrv, n='L_upper_Closed_Curve')        
    upper_cmdslosedCrv = cmds.duplicate(upper_cntrlCrv, n='L_mid_Closed_Curve')
    
def lowerLid():
    lower_wireCrv = cmds.polyToCurve(dg=1,ch=False,n='L_lower_Wire_crv')
    lower_bsCurve = cmds.duplicate(lower_wireCrv, n='L_lower_bs_crv')
    lower_cntrlCrv = cmds.duplicate(lower_wireCrv, n='L_lower_Main_Control_crv')
    cmds.rebuildCurve(lower_cntrlCrv,d=3,s=4,ch=False)
    cmds.delete(lower_cntrlCrv[0]+'.cv[1]', lower_cntrlCrv[0]+'.cv[5]')        
    lower_closedCrv = cmds.duplicate(lower_cntrlCrv, n='L_lower_Closed_Curve')        

def checkEyeBall():
    if cmds.objExists('eye_grp'):
        cls = cmds.cluster('L_eyeCornea__organic_eyesArchetype_geo', n='L_proxy_cls')
        cmds.createNode('joint', n='L_proxy_eyeJnt', ss=True)
        cmds.delete(cmds.pointConstraint(cls[1], 'L_proxy_eyeJnt'))
        cmds.rotate(0, -90, 0, 'L_proxy_eyeJnt')
        cmds.makeIdentity('L_proxy_eyeJnt', a=True)
        cmds.delete('L_proxy_cls')
        cls = cmds.cluster('R_eyeCornea__organic_eyesArchetype_geo', n='R_proxy_cls')
        cmds.createNode('joint', n='R_proxy_eyeJnt', ss=True)
        cmds.delete(cmds.pointConstraint(cls[1], 'R_proxy_eyeJnt'))
        cmds.rotate(0, -90, 0, 'R_proxy_eyeJnt')
        cmds.makeIdentity('R_proxy_eyeJnt', a=True)
        cmds.delete('R_proxy_cls')
    if not cmds.objExists('face_eyelid_msh'):
        cmds.duplicate('face__organic_skin_geo',n='face_eyelid_msh')
    eyeController= ['L_face_picker_eye_null','R_face_picker_eye_null'] 
    cmds.createNode('joint',n=eyeController[0],ss=1)
    cmds.createNode('joint',n=eyeController[1],ss=1)
    attributes = ['translate','rotate','scale']
    for i in eyeController:        
        cmds.addAttr(i,ln='blink',at='double',min=0,max=10,dv=0,k=1)
        cmds.addAttr(i,ln='blinkCenter',at='double',min=0,max=10,dv=1,k=1)
        cmds.addAttr(i,ln='upperLid',at='double',min=-10,max=10,dv=0,k=1)
        cmds.addAttr(i,ln='lowerLid',at='double',min=-25,max=10,dv=0,k=1)
        cmds.addAttr(i,ln='upperLidOut',at='double',min=0,max=10,dv=0,k=1)    
        cmds.addAttr(i,ln='lowerLidOut',at='double',min=0,max=10,dv=0,k=1)    
        cmds.addAttr(i,ln='eyelidDriver',at='enum',en='--------------:',k=1)
        cmds.setAttr('{}.eyelidDriver'.format(i),l=1)
        cmds.addAttr(i,ln='upperLidFollow',at='double',min=0,max=10,dv=3,k=1)
        cmds.addAttr(i,ln='lowerLidFollow',at='double',min=0,max=10,dv=2,k=1)
        cmds.addAttr(i,ln='blinkDriver',at='enum',en='--------------:',k=1)
        cmds.setAttr('{}.blinkDriver'.format(i),l=1)
        cmds.addAttr(i,ln='upperLidOutAuto',at='double',min=0,max=10,dv=0,k=1)
        cmds.addAttr(i,ln='lowerLidOutAuto',at='double',min=0,max=10,dv=0,k=1) 
        cmds.setAttr('{}.visibility'.format(i),l=1,k=0)  
        for channel in attributes:
            for axis in 'XYZ':
                cmds.setAttr('{}.{}{}'.format(i,channel,axis),l=1,k=0)
                 

def finish():    
    cmds.createNode('joint', n='Proxy_root_jnt', ss=True)
    grpName = ['eyeLid_Jnt_grp','eyeLid_Loc_grp','eyeLid_Curve_grp','eyeLid_ctrl_grp']
    for i in grpName:
        cmds.group(n=i,em=True)
        cmds.setAttr('{}.v'.format(i), 0, l=False)
    cmds.select('L_upper_bs_crv.cv[*]')
    upper_vertSel = cmds.ls(sl =True, fl = True)
    for i in range(len(upper_vertSel)):
        vertPos = cmds.xform(upper_vertSel[i], q = True, ws = True, t = True)
        startJnt = cmds.createNode('joint', n='L_upper_eyeLid_Center_Jnt_'+ str(i+1), ss=True)
        startJnt_grp = cmds.group(n='L_upper_eyeLid_Center_jnt_'+str(i+1)+'_grp', em=True)
        cmds.parent(startJnt, startJnt_grp)
        cmds.delete(cmds.parentConstraint('L_proxy_eyeJnt', startJnt_grp))
        loc = cmds.spaceLocator(n='L_upper_eyeLid_Loc_'+ str(i+1))
        cmds.scale(.05,.05,.05)
        pointCrv = cmds.createNode('pointOnCurveInfo', n='L_upper_PointOnCurve_'+str(i+1), ss=True)
        crvShape = cmds.listRelatives('L_upper_bs_crv', s = True)
        cmds.connectAttr(crvShape[0]+'.worldSpace[0]', pointCrv+'.inputCurve')
        cmds.connectAttr(pointCrv+'.position', loc[0]+'.translate')
        cmds.setAttr(pointCrv+'.turnOnPercentage', 1)
        vtxCount = cmds.getAttr(crvShape[0]+'.spans')
        cmds.setAttr(pointCrv+'.parameter', i*(float(1)/float(vtxCount)))
        cmds.aimConstraint(loc, startJnt, mo=0)
        endJnt = cmds.createNode('joint', n = 'L_upper_eyeLid_End_'+ str(i)+'_jnt', ss=True)
        cmds.delete(cmds.pointConstraint(loc, endJnt))
        cmds.parent(endJnt, startJnt)
        cmds.setAttr(endJnt+'.jointOrientX',0)
        cmds.setAttr(endJnt+'.jointOrientY',0)
        cmds.setAttr(endJnt+'.jointOrientZ',0)
        cmds.parent(startJnt_grp, 'eyeLid_Jnt_grp')  
        cmds.parent(loc, 'eyeLid_Loc_grp')                 
        cmds.select(cl=True)
    cmds.select('L_lower_bs_crv.cv[*]')
    lower_vertSel = cmds.ls(sl =True, fl = True)
    for i in range(len(lower_vertSel)):
        vertPos = cmds.xform(lower_vertSel[i], q = True, ws = True, t = True)
        startJnt = cmds.createNode('joint', n='L_lower_eyeLid_Center_Jnt_'+ str(i+1), ss=True)
        startJnt_grp = cmds.group(n='L_lower_eyeLid_Center_jnt_'+str(i+1)+'_grp', em=True)
        cmds.parent(startJnt, startJnt_grp)
        cmds.delete(cmds.parentConstraint('L_proxy_eyeJnt', startJnt_grp))
        loc = cmds.spaceLocator(n='L_lower_eyeLid_Loc_'+ str(i+1))
        cmds.scale(.05,.05,.05)
        pointCrv = cmds.createNode('pointOnCurveInfo', n='L_lower_PointOnCurve_'+str(i+1), ss=True)
        crvShape = cmds.listRelatives('L_lower_bs_crv', s = True)
        cmds.connectAttr(crvShape[0]+'.worldSpace[0]', pointCrv+'.inputCurve')
        cmds.connectAttr(pointCrv+'.position', loc[0]+'.translate')
        cmds.setAttr(pointCrv+'.turnOnPercentage', 1)
        vtxCount = cmds.getAttr(crvShape[0]+'.spans')
        cmds.setAttr(pointCrv+'.parameter', i*(float(1)/float(vtxCount)))
        cmds.aimConstraint(loc, startJnt, mo=0)
        endJnt = cmds.createNode('joint', n = 'L_lower_eyeLid_End_'+ str(i)+'_jnt', ss=True)
        cmds.delete(cmds.pointConstraint(loc, endJnt))
        cmds.parent(endJnt, startJnt)
        cmds.setAttr(endJnt+'.jointOrientX',0)
        cmds.setAttr(endJnt+'.jointOrientY',0)
        cmds.setAttr(endJnt+'.jointOrientZ',0)
        cmds.parent(startJnt_grp, 'eyeLid_Jnt_grp')  
        cmds.parent(loc, 'eyeLid_Loc_grp')                 
        cmds.select(cl=True)                
    ############ upper Lid Setup
    upWire = cmds.wire('L_upper_Wire_crv', w='L_upper_Closed_Curve', n='upperLid_Wire')
    cmds.setAttr(upWire[0]+'.dropoffDistance[0]', 50)
    cmds.setAttr(upWire[0]+'.rotation', 0)
    cmds.blendShape('L_upper_Wire_crv', 'L_upper_bs_crv', n='L_upperLid_Connect_bs')
    cmds.setAttr('L_upperLid_Connect_bs.L_upper_Wire_crv', 1)        
    ### Applying BlendShape for Blink
    cmds.blendShape('L_upper_Main_Control_crv', 'L_lower_Main_Control_crv', 'L_mid_Closed_Curve', n='L_Blink_bs')
    cmds.blendShape('L_lower_Main_Control_crv', 'L_mid_Closed_Curve', 'L_lower_Closed_Curve', n='L_lower_Closed_bs')
    cmds.blendShape('L_upper_Main_Control_crv', 'L_mid_Closed_Curve', 'L_upper_Closed_Curve', n='L_upper_Closed_bs')
    cmds.createNode('multiplyDivide', n='L_Blink_Center_MD_1', ss=True)
    cmds.createNode('reverse', n='L_Blink_Center_RE_1', ss=True)
    cmds.connectAttr('L_face_picker_eye_null.blinkCenter', 'L_Blink_Center_MD_1.input1X', f=True)
    cmds.connectAttr('L_Blink_Center_MD_1.outputX', 'L_Blink_Center_RE_1.inputX', f=True)
    cmds.connectAttr('L_Blink_Center_MD_1.outputX', 'L_Blink_bs.L_upper_Main_Control_crv', f=True)
    cmds.connectAttr('L_Blink_Center_RE_1.outputX', 'L_Blink_bs.L_lower_Main_Control_crv', f=True)
    cmds.setAttr('L_Blink_Center_MD_1.input2X', .1)
    #### upper Blink
    cmds.createNode('multiplyDivide', n='L_upper_Blink_MD_1', ss=True)
    cmds.createNode('plusMinusAverage', n='L_upper_Blink_PM_1', ss=True)
    cmds.createNode('reverse', n='L_upper_Blink_RE_1', ss=True)
    cmds.connectAttr('L_face_picker_eye_null.blink', 'L_upper_Blink_MD_1.input1X', f=True)
    cmds.connectAttr('L_face_picker_eye_null.upperLid', 'L_upper_Blink_MD_1.input1Y', f=True)
    cmds.setAttr('L_upper_Blink_MD_1.input2X', .105)
    cmds.setAttr('L_upper_Blink_MD_1.input2Y', .105)
    cmds.connectAttr('L_upper_Blink_MD_1.outputX', 'L_upper_Blink_PM_1.input1D[0]', f=True)
    cmds.connectAttr('L_upper_Blink_MD_1.outputY', 'L_upper_Blink_PM_1.input1D[1]', f=True)
    cmds.connectAttr('L_upper_Blink_PM_1.output1D', 'L_upper_Closed_bs.L_mid_Closed_Curve', f=True)
    cmds.connectAttr('L_upper_Blink_RE_1.outputX', 'L_upper_Closed_bs.L_upper_Main_Control_crv', f=True)
    cmds.connectAttr('L_upper_Blink_PM_1.output1D', 'L_upper_Blink_RE_1.inputX')
    
    ############ lower Lid Setup
    lowWire = cmds.wire('L_lower_Wire_crv', w='L_lower_Closed_Curve', n='lowerLid_Wire')
    cmds.setAttr(upWire[0]+'.dropoffDistance[0]', 50)
    cmds.setAttr(upWire[0]+'.rotation', 0)
    cmds.blendShape('L_lower_Wire_crv', 'L_lower_bs_crv', n='L_lowerLid_Connect_bs')        
    cmds.setAttr('L_lowerLid_Connect_bs.L_lower_Wire_crv', 1)        
    #### upper Blink
    cmds.createNode('multiplyDivide', n='L_lower_Blink_MD_1', ss=True)
    cmds.createNode('plusMinusAverage', n='L_lower_Blink_PM_1', ss=True)
    cmds.createNode('reverse', n='L_lower_Blink_RE_1', ss=True)
    cmds.connectAttr('L_face_picker_eye_null.blink', 'L_lower_Blink_MD_1.input1X', f=True)
    cmds.connectAttr('L_face_picker_eye_null.lowerLid', 'L_lower_Blink_MD_1.input1Y', f=True)
    cmds.setAttr('L_lower_Blink_MD_1.input2X', .105)
    cmds.setAttr('L_lower_Blink_MD_1.input2Y', .105)
    cmds.connectAttr('L_lower_Blink_MD_1.outputX', 'L_lower_Blink_PM_1.input1D[0]', f=True)
    cmds.connectAttr('L_lower_Blink_MD_1.outputY', 'L_lower_Blink_PM_1.input1D[1]', f=True)
    cmds.connectAttr('L_lower_Blink_PM_1.output1D', 'L_lower_Closed_bs.L_mid_Closed_Curve', f=True)
    cmds.connectAttr('L_lower_Blink_RE_1.outputX', 'L_lower_Closed_bs.L_lower_Main_Control_crv', f=True)
    cmds.connectAttr('L_lower_Blink_PM_1.output1D', 'L_lower_Blink_RE_1.inputX')
    
    for c in range(0,5):
        ctrlPos = cmds.xform('L_upper_Main_Control_crv.cv['+str(c)+']', q=True, ws=True, t=True)
        cmds.select(cl=True)
        tipJnt = cmds.joint(n='L_Control_Tip_Jnt_'+str(c+1), p=ctrlPos, rad=.5)
        cmds.select(cl=True)
        rotateGrp = cmds.group(em=True, n='L_Control_Tip_Jnt_'+str(c+1)+'_Rotate_grp')
        offGrp = cmds.group(em=True, n='L_Control_Tip_Jnt_'+str(c+1)+'_offsetgrp')
        cmds.parent(rotateGrp, offGrp)    
        cmds.delete(cmds.parentConstraint(tipJnt, offGrp))
        cmds.parent(tipJnt, rotateGrp)            
        cmds.select(cl=True)
        cJnt = cmds.joint(n='L_Control_Center_Jnt_'+str(c+1))
        cJntGrp = cmds.group(n='L_Control_Center_Jnt_grp_'+str(c+1))
        cmds.delete(cmds.parentConstraint('L_proxy_eyeJnt', cJntGrp))
        cmds.parent(offGrp, cJnt)
        
    for c in range(0,3):
        ctrlPos = cmds.xform('L_lower_Main_Control_crv.cv['+str(c+1)+']', q=True, ws=True, t=True)
        cmds.select(cl=True)
        tipJnt = cmds.joint(n='L_Control_Tip_Jnt_'+str(c+6), p=ctrlPos, rad=.5)
        cmds.select(cl=True)
        rotateGrp = cmds.group(em=True, n='L_Control_Tip_Jnt_'+str(c+6)+'_Rotate_grp')
        offGrp = cmds.group(em=True, n='L_Control_Tip_Jnt_'+str(c+6)+'_offsetgrp')
        cmds.parent(rotateGrp, offGrp)    
        cmds.delete(cmds.parentConstraint(tipJnt, offGrp))
        cmds.parent(tipJnt, rotateGrp)            
        cmds.select(cl=True)
        cJnt = cmds.joint(n='L_Control_Center_Jnt_'+str(c+6))
        cJntGrp = cmds.group(n='L_Control_Center_Jnt_grp_'+str(c+6))
        cmds.delete(cmds.parentConstraint('L_proxy_eyeJnt', cJntGrp))
        cmds.parent(offGrp, cJnt)  
        sel = cmds.ls('L_Control_Tip_Jnt_*_offsetgrp')
    
    for s in range(len(sel)):
        ctrl = cmds.circle(n='L_eyeLid_'+str(s+1)+'_ctrl', nr=(0,0,1), r=.05, ch=False)
        grp = cmds.group(n='L_eyeLid_'+str(s+1)+'_ctrl_grp')
        cmds.delete(cmds.parentConstraint(sel[s], grp))
    cmds.select('L_Control_Center_Jnt_grp_*')
    cmds.group(n='L_Control_Center_Jnt_grp')
    cmds.select('L_eyeLid_*_ctrl_grp')
    cmds.group(n='L_eyeLid_ctrl_grp')
    ##################################
    cmds.addAttr('L_eyeLid_*_ctrl', ln='Eye_Follow', min=0, max=1, dv=0, k=True)
    cmds.addAttr('L_eyeLid_2_ctrl', ln='mid_ctrl_Follow', min=0, max=1, dv=0, k=True)
    cmds.addAttr('L_eyeLid_2_ctrl', ln='Corner_ctrl_Follow', min=0, max=1, dv=0, k=True)
    cmds.addAttr('L_eyeLid_4_ctrl', ln='mid_ctrl_Follow', min=0, max=1, dv=0, k=True)
    cmds.addAttr('L_eyeLid_4_ctrl', ln='Corner_ctrl_Follow', min=0, max=1, dv=0, k=True)
    cmds.addAttr('L_eyeLid_6_ctrl', ln='mid_ctrl_Follow', min=0, max=1, dv=0, k=True)
    cmds.addAttr('L_eyeLid_6_ctrl', ln='Corner_ctrl_Follow', min=0, max=1, dv=0, k=True)
    cmds.addAttr('L_eyeLid_8_ctrl', ln='mid_ctrl_Follow', min=0, max=1, dv=0, k=True)
    cmds.addAttr('L_eyeLid_8_ctrl', ln='Corner_ctrl_Follow', min=0, max=1, dv=0, k=True)
    sel = cmds.ls('L_eyeLid_*_ctrl')
    for s in sel:
        cmds.setAttr(s+'.Eye_Follow', .05)
    sel = cmds.ls('L_eyeLid_4_ctrl','L_eyeLid_2_ctrl','L_eyeLid_6_ctrl','L_eyeLid_8_ctrl')
    for s in sel:
        cmds.setAttr(s+'.mid_ctrl_Follow', .5)
        cmds.setAttr(s+'.Corner_ctrl_Follow', .5)       
    ###############################################################            
    cmds.addAttr('L_face_picker_eye_null', ln='Corner_Follow', min=0, max=1, dv=.1, k=True)
    cmds.addAttr('R_face_picker_eye_null', ln='Corner_Follow', min=0, max=1, dv=.1, k=True)
    sel = cmds.ls('L_Control_Center_Jnt_*', typ='joint')
    for s in range(len(sel)):
        cmds.pointConstraint('L_proxy_eyeJnt', sel[s])
        ## Creating Multiply Devide Node for each control Joints
        cmds.createNode('multiplyDivide', n='L_eyeLid_Follow_MD_'+str(s+1), ss=True)
        cmds.connectAttr('L_proxy_eyeJnt.rotate', 'L_eyeLid_Follow_MD_'+str(s+1)+'.input1', f=True)
        cmds.connectAttr('L_eyeLid_Follow_MD_'+str(s+1)+'.output', 'L_Control_Center_Jnt_'+str(s+1)+'.rotate', f=True)
    ### Creating Node for upper lower and Corner lid Follow    
    cmds.createNode('multiplyDivide', n='L_upperLid_Follow_MD_01', ss=True)
    cmds.createNode('multiplyDivide', n='L_lowerLid_Follow_MD_01', ss=True)
    cmds.createNode('multiplyDivide', n='L_Corner_Follow_MD_01', ss=True)
    ### Connecting upper Lid Attributes
    cmds.connectAttr('L_face_picker_eye_null.upperLidFollow','L_upperLid_Follow_MD_01.input1X', f=True)
    cmds.connectAttr('L_face_picker_eye_null.upperLidFollow','L_upperLid_Follow_MD_01.input1Y', f=True)
    cmds.connectAttr('L_face_picker_eye_null.upperLidFollow','L_upperLid_Follow_MD_01.input1Z', f=True)
    ### Connecting lowerLid Attributes
    cmds.connectAttr('L_face_picker_eye_null.lowerLidFollow','L_lowerLid_Follow_MD_01.input1X', f=True)
    cmds.connectAttr('L_face_picker_eye_null.lowerLidFollow','L_lowerLid_Follow_MD_01.input1Y', f=True)
    cmds.connectAttr('L_face_picker_eye_null.lowerLidFollow','L_lowerLid_Follow_MD_01.input1Z', f=True)
    ##Connceting Corner Lid Attr
    cmds.connectAttr('L_face_picker_eye_null.Corner_Follow','L_Corner_Follow_MD_01.input1X', f=True)
    cmds.connectAttr('L_face_picker_eye_null.Corner_Follow','L_Corner_Follow_MD_01.input1Y', f=True)
    cmds.connectAttr('L_face_picker_eye_null.Corner_Follow','L_Corner_Follow_MD_01.input1Z', f=True)
    ## eyeLid Controler to MD
    cmds.connectAttr('L_eyeLid_2_ctrl.Eye_Follow','L_upperLid_Follow_MD_01.input2X', f=True)
    cmds.connectAttr('L_eyeLid_3_ctrl.Eye_Follow','L_upperLid_Follow_MD_01.input2Y', f=True)
    cmds.connectAttr('L_eyeLid_4_ctrl.Eye_Follow','L_upperLid_Follow_MD_01.input2Z', f=True)
    ## eyeLid Controler to MD
    cmds.connectAttr('L_eyeLid_6_ctrl.Eye_Follow','L_lowerLid_Follow_MD_01.input2X', f=True)
    cmds.connectAttr('L_eyeLid_7_ctrl.Eye_Follow','L_lowerLid_Follow_MD_01.input2Y', f=True)
    cmds.connectAttr('L_eyeLid_8_ctrl.Eye_Follow','L_lowerLid_Follow_MD_01.input2Z', f=True)
    ## eyeLid Controler to MD
    cmds.connectAttr('L_eyeLid_1_ctrl.Eye_Follow','L_Corner_Follow_MD_01.input2X', f=True)
    cmds.connectAttr('L_eyeLid_5_ctrl.Eye_Follow','L_Corner_Follow_MD_01.input2Y', f=True)
    
    cmds.connectAttr('L_Corner_Follow_MD_01.outputY','L_eyeLid_Follow_MD_1.input2X', f=True)
    cmds.connectAttr('L_Corner_Follow_MD_01.outputY','L_eyeLid_Follow_MD_1.input2Y', f=True)
    cmds.connectAttr('L_Corner_Follow_MD_01.outputY','L_eyeLid_Follow_MD_1.input2Z', f=True)
    
    cmds.connectAttr('L_Corner_Follow_MD_01.outputX','L_eyeLid_Follow_MD_5.input2X', f=True)
    cmds.connectAttr('L_Corner_Follow_MD_01.outputX','L_eyeLid_Follow_MD_5.input2Y', f=True)
    cmds.connectAttr('L_Corner_Follow_MD_01.outputX','L_eyeLid_Follow_MD_5.input2Z', f=True)
    
    cmds.connectAttr('L_upperLid_Follow_MD_01.outputX','L_eyeLid_Follow_MD_2.input2X', f=True)
    cmds.connectAttr('L_upperLid_Follow_MD_01.outputX','L_eyeLid_Follow_MD_2.input2Y', f=True)
    cmds.connectAttr('L_upperLid_Follow_MD_01.outputX','L_eyeLid_Follow_MD_2.input2Z', f=True)
    
    cmds.connectAttr('L_upperLid_Follow_MD_01.outputY','L_eyeLid_Follow_MD_3.input2X', f=True)
    cmds.connectAttr('L_upperLid_Follow_MD_01.outputY','L_eyeLid_Follow_MD_3.input2Y', f=True)
    cmds.connectAttr('L_upperLid_Follow_MD_01.outputY','L_eyeLid_Follow_MD_3.input2Z', f=True)
    
    cmds.connectAttr('L_upperLid_Follow_MD_01.outputZ','L_eyeLid_Follow_MD_4.input2X', f=True)
    cmds.connectAttr('L_upperLid_Follow_MD_01.outputZ','L_eyeLid_Follow_MD_4.input2Y', f=True)
    cmds.connectAttr('L_upperLid_Follow_MD_01.outputZ','L_eyeLid_Follow_MD_4.input2Z', f=True)
    
    cmds.connectAttr('L_lowerLid_Follow_MD_01.outputX','L_eyeLid_Follow_MD_6.input2X', f=True)
    cmds.connectAttr('L_lowerLid_Follow_MD_01.outputX','L_eyeLid_Follow_MD_6.input2Y', f=True)
    cmds.connectAttr('L_lowerLid_Follow_MD_01.outputX','L_eyeLid_Follow_MD_6.input2Z', f=True)
    
    cmds.connectAttr('L_lowerLid_Follow_MD_01.outputY','L_eyeLid_Follow_MD_7.input2X', f=True)
    cmds.connectAttr('L_lowerLid_Follow_MD_01.outputY','L_eyeLid_Follow_MD_7.input2Y', f=True)
    cmds.connectAttr('L_lowerLid_Follow_MD_01.outputY','L_eyeLid_Follow_MD_7.input2Z', f=True)
    
    cmds.connectAttr('L_lowerLid_Follow_MD_01.outputZ','L_eyeLid_Follow_MD_8.input2X', f=True)
    cmds.connectAttr('L_lowerLid_Follow_MD_01.outputZ','L_eyeLid_Follow_MD_8.input2Y', f=True)
    cmds.connectAttr('L_lowerLid_Follow_MD_01.outputZ','L_eyeLid_Follow_MD_8.input2Z', f=True)
    
    ### eyeLid Rotate Pivot Change for Rotation or S curve shape
    upmidPos = cmds.xform('L_Control_Tip_Jnt_3', q=True, ws=True, t=True)
    cmds.move(upmidPos[0],upmidPos[1],upmidPos[2],'L_Control_Tip_Jnt_4_Rotate_grp.rotatePivot', 'L_Control_Tip_Jnt_4_Rotate_grp.scalePivot', a=True)
    cmds.move(upmidPos[0],upmidPos[1],upmidPos[2],'L_Control_Tip_Jnt_2_Rotate_grp.rotatePivot', 'L_Control_Tip_Jnt_2_Rotate_grp.scalePivot', a=True)
    
    lowmidPos = cmds.xform('L_Control_Tip_Jnt_7', q=True, ws=True, t=True)
    cmds.move(lowmidPos[0],lowmidPos[1],lowmidPos[2],'L_Control_Tip_Jnt_6_Rotate_grp.rotatePivot', 'L_Control_Tip_Jnt_6_Rotate_grp.scalePivot', a=True)
    cmds.move(lowmidPos[0],lowmidPos[1],lowmidPos[2],'L_Control_Tip_Jnt_8_Rotate_grp.rotatePivot', 'L_Control_Tip_Jnt_8_Rotate_grp.scalePivot', a=True)
    
    ##################################################################
    sel = cmds.ls('L_eyeLid_*_ctrl')
    for s in range(len(sel)):
        md = cmds.createNode('multiplyDivide', n='L_eyeLid_ctrl_MD_'+str(s+1), ss=True)
        pm = cmds.createNode('plusMinusAverage', n='L_eyeLid_ctrl_PM_'+str(s+1), ss=True)
        cmds.connectAttr('L_eyeLid_'+str(s+1)+'_ctrl.translate', md+'.input1', f=True)
        cmds.connectAttr(md+'.output', pm+'.input3D[0]', f=True)
        cmds.connectAttr(pm+'.output3D', 'L_Control_Tip_Jnt_'+str(s+1)+'.translate')
    
    cmds.createNode('multiplyDivide', n='L_eyeLid_ctrl_MD_9', ss=True)
    cmds.createNode('multiplyDivide', n='L_eyeLid_ctrl_MD_10', ss=True)
    cmds.createNode('multiplyDivide', n='L_eyeLid_ctrl_MD_11', ss=True)
    cmds.createNode('multiplyDivide', n='L_eyeLid_ctrl_MD_12', ss=True)
    
    cmds.createNode('multiplyDivide', n='L_eyeLid_ctrl_MD_13', ss=True)
    cmds.createNode('multiplyDivide', n='L_eyeLid_ctrl_MD_14', ss=True)
    cmds.createNode('multiplyDivide', n='L_eyeLid_ctrl_MD_15', ss=True)
    cmds.createNode('multiplyDivide', n='L_eyeLid_ctrl_MD_16', ss=True)
    
    cmds.connectAttr('L_eyeLid_3_ctrl.translate', 'L_eyeLid_ctrl_MD_9.input1', f=True)
    cmds.connectAttr('L_eyeLid_3_ctrl.translate', 'L_eyeLid_ctrl_MD_10.input1', f=True)
    
    cmds.connectAttr('L_eyeLid_7_ctrl.translate', 'L_eyeLid_ctrl_MD_11.input1', f=True)
    cmds.connectAttr('L_eyeLid_7_ctrl.translate', 'L_eyeLid_ctrl_MD_12.input1', f=True)
    
    cmds.connectAttr('L_eyeLid_1_ctrl.translate', 'L_eyeLid_ctrl_MD_13.input1', f=True)
    cmds.connectAttr('L_eyeLid_1_ctrl.translate', 'L_eyeLid_ctrl_MD_14.input1', f=True)
    
    cmds.connectAttr('L_eyeLid_5_ctrl.translate', 'L_eyeLid_ctrl_MD_15.input1', f=True)
    cmds.connectAttr('L_eyeLid_5_ctrl.translate', 'L_eyeLid_ctrl_MD_16.input1', f=True)
    
    cmds.connectAttr('L_eyeLid_ctrl_MD_16.output','L_eyeLid_ctrl_PM_8.input3D[1]', f=True)
    cmds.connectAttr('L_eyeLid_ctrl_MD_15.output','L_eyeLid_ctrl_PM_4.input3D[1]', f=True)
    
    cmds.connectAttr('L_eyeLid_ctrl_MD_12.output','L_eyeLid_ctrl_PM_8.input3D[2]', f=True)
    cmds.connectAttr('L_eyeLid_ctrl_MD_11.output','L_eyeLid_ctrl_PM_6.input3D[1]', f=True)
    
    cmds.connectAttr('L_eyeLid_ctrl_MD_13.output','L_eyeLid_ctrl_PM_2.input3D[1]', f=True)
    cmds.connectAttr('L_eyeLid_ctrl_MD_14.output','L_eyeLid_ctrl_PM_6.input3D[2]', f=True)
    
    cmds.connectAttr('L_eyeLid_ctrl_MD_9.output','L_eyeLid_ctrl_PM_2.input3D[2]', f=True)
    cmds.connectAttr('L_eyeLid_ctrl_MD_10.output','L_eyeLid_ctrl_PM_4.input3D[2]', f=True)
    
    cmds.createNode('multiplyDivide', n='L_upperLid_Rotate_MD_01', ss=True)
    cmds.createNode('multiplyDivide', n='L_lowerLid_Rotate_MD_01', ss=True)
    
    cmds.setAttr('L_upperLid_Rotate_MD_01.input2X', .5)
    cmds.setAttr('L_upperLid_Rotate_MD_01.input2Y', .5)
    cmds.setAttr('L_upperLid_Rotate_MD_01.input2Z', .5)
    cmds.setAttr('L_lowerLid_Rotate_MD_01.input2X', .5)
    cmds.setAttr('L_lowerLid_Rotate_MD_01.input2Y', .5)
    cmds.setAttr('L_lowerLid_Rotate_MD_01.input2Z', .5)
    
    cmds.connectAttr('L_eyeLid_3_ctrl.rotate', 'L_upperLid_Rotate_MD_01.input1')
    cmds.connectAttr('L_eyeLid_7_ctrl.rotate', 'L_lowerLid_Rotate_MD_01.input1')
    
    cmds.connectAttr('L_upperLid_Rotate_MD_01.output', 'L_Control_Tip_Jnt_2_Rotate_grp.rotate')
    cmds.connectAttr('L_upperLid_Rotate_MD_01.output', 'L_Control_Tip_Jnt_4_Rotate_grp.rotate')
    
    cmds.connectAttr('L_lowerLid_Rotate_MD_01.output', 'L_Control_Tip_Jnt_6_Rotate_grp.rotate')
    cmds.connectAttr('L_lowerLid_Rotate_MD_01.output', 'L_Control_Tip_Jnt_8_Rotate_grp.rotate')
    
    ##### Skin Bind To Control Curve
    upperSel = cmds.ls('L_Control_Tip_Jnt_4', 'L_Control_Tip_Jnt_3', 'L_Control_Tip_Jnt_2', 'L_Control_Tip_Jnt_1', 'L_Control_Tip_Jnt_5')
    lowerSel = cmds.ls('L_Control_Tip_Jnt_6', 'L_Control_Tip_Jnt_7', 'L_Control_Tip_Jnt_8', 'L_Control_Tip_Jnt_1', 'L_Control_Tip_Jnt_5')
    upperCrv = 'L_upper_Main_Control_crv'
    lowerCrev = 'L_lower_Main_Control_crv'
    cmds.skinCluster(upperSel, upperCrv, n='upper_crv_SkinCluster')
    cmds.skinCluster(lowerSel, lowerCrev, n='lower_crv_SkinCluster')
    ####################################################
    #### upper Lid Out
    loopSel = cmds.ls('L_upper_eyeLid_End_1_jnt')
    totalLoop = len(loopSel)
    loopVal = float(1)/totalLoop
    for l in range(len(loopSel)):
        sel = cmds.ls('L_upper_eyeLid_End_*_jnt')
        totalJnt = len(sel)
        midJnt = totalJnt/2
        val = (float(1)-(float(l)*float(loopVal)))/float(totalJnt)
        for s in range(len(sel)):
            md = cmds.createNode('multiplyDivide', n='L_upper_eyeLid_Out_MD_'+str(l+1)+'_'+str(s+1), ss=True)
            blinkMd = cmds.createNode('multiplyDivide', n='L_upper_eyeLid_Blink_Out_MD_'+str(l+1)+'_'+str(s+1), ss=True)
            autoMd = cmds.createNode('multiplyDivide', n='L_upper_eyeLid_Auto_Out_MD_'+str(l+1)+'_'+str(s+1), ss=True)
            pm = cmds.createNode('plusMinusAverage', n='L_upper_eyeLid_Out_PM_'+str(l+1)+'_'+str(s+1), ss=True)       
            cmds.connectAttr('L_face_picker_eye_null.upperLidOut', 'L_upper_eyeLid_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input2X', f=True)
            cmds.connectAttr('L_face_picker_eye_null.upperLidOutAuto', 'L_upper_eyeLid_Auto_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input2X', f=True)   
            cmds.connectAttr('L_face_picker_eye_null.blink', 'L_upper_eyeLid_Blink_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input2.input2X', f=True)   
            cmds.connectAttr('L_upper_eyeLid_Blink_Out_MD_'+str(l+1)+'_'+str(s+1)+'.outputX', 'L_upper_eyeLid_Auto_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input1X', f=True)   
            cmds.connectAttr('L_upper_eyeLid_Auto_Out_MD_'+str(l+1)+'_'+str(s+1)+'.outputX', 'L_upper_eyeLid_Out_PM_'+str(l+1)+'_'+str(s+1)+'.input1D[0]', f=True)   
            cmds.connectAttr('L_upper_eyeLid_Out_MD_'+str(l+1)+'_'+str(s+1)+'.outputX', 'L_upper_eyeLid_Out_PM_'+str(l+1)+'_'+str(s+1)+'.input1D[1]', f=True)   
            tVal = cmds.getAttr(sel[s]+'.translateX')
            cmds.setAttr('L_upper_eyeLid_Out_PM_'+str(l+1)+'_'+str(s+1)+'.input1D[2]', tVal)
            cmds.connectAttr('L_upper_eyeLid_Out_PM_'+str(l+1)+'_'+str(s+1)+'.output1D', sel[s]+'.translateX', f=True)     
            if s < midJnt:
                cmds.setAttr('L_upper_eyeLid_Blink_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input1X', (s*val))
                cmds.setAttr('L_upper_eyeLid_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input1X', (s*val))
            if s == midJnt:
                cmds.setAttr('L_upper_eyeLid_Blink_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input1X', ((s-.5)*val))
                cmds.setAttr('L_upper_eyeLid_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input1X', ((s-.5)*val))    
        mdSel = cmds.ls('L_upper_eyeLid_Blink_Out_MD_'+str(l+1)+'_*')
        oMdSel = cmds.ls('L_upper_eyeLid_Out_MD_'+str(l+1)+'_*')
        revOmdSel = oMdSel[::-1]
        revSel = mdSel[::-1]      
        for r in range(len(revSel)):
                if r < midJnt:
                    cmds.setAttr(revSel[r]+'.input1X', (r*val))
                    cmds.setAttr(revOmdSel[r]+'.input1X', (r*val))
       
    #### lower Lid Out
    loopSel = cmds.ls('L_lower_eyeLid_End_1_jnt')
    totalLoop = len(loopSel)
    loopVal = (float(1)/totalLoop)/10
    for l in range(len(loopSel)):
        sel = cmds.ls('L_lower_eyeLid_End_*_jnt')
        totalJnt = len(sel)
        midJnt = totalJnt/2
        val = (float(1)-(float(l)*float(loopVal)))/float(totalJnt)
        for s in range(len(sel)):
            md = cmds.shadingNode('multiplyDivide',au=True, n='L_lower_eyeLid_Out_MD_'+str(l+1)+'_'+str(s+1))
            blinkMd = cmds.shadingNode('multiplyDivide', au=True, n='L_lower_eyeLid_Blink_Out_MD_'+str(l+1)+'_'+str(s+1))
            autoMd = cmds.shadingNode('multiplyDivide', au=True, n='L_lower_eyeLid_Auto_Out_MD_'+str(l+1)+'_'+str(s+1))
            pm = cmds.shadingNode('plusMinusAverage', au=True, n='L_lower_eyeLid_Out_PM_'+str(l+1)+'_'+str(s+1))
           
            cmds.connectAttr('L_face_picker_eye_null.lowerLidOut', 'L_lower_eyeLid_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input2X', f=True)
            cmds.connectAttr('L_face_picker_eye_null.lowerLidOutAuto', 'L_lower_eyeLid_Auto_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input2X', f=True)   
            cmds.connectAttr('L_face_picker_eye_null.blink', 'L_lower_eyeLid_Blink_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input2.input2X', f=True)   
            cmds.connectAttr('L_lower_eyeLid_Blink_Out_MD_'+str(l+1)+'_'+str(s+1)+'.outputX', 'L_lower_eyeLid_Auto_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input1X', f=True)   
            cmds.connectAttr('L_lower_eyeLid_Auto_Out_MD_'+str(l+1)+'_'+str(s+1)+'.outputX', 'L_lower_eyeLid_Out_PM_'+str(l+1)+'_'+str(s+1)+'.input1D[0]', f=True)   
            cmds.connectAttr('L_lower_eyeLid_Out_MD_'+str(l+1)+'_'+str(s+1)+'.outputX', 'L_lower_eyeLid_Out_PM_'+str(l+1)+'_'+str(s+1)+'.input1D[1]', f=True)   
            tVal = cmds.getAttr(sel[s]+'.translateX')
            cmds.setAttr('L_lower_eyeLid_Out_PM_'+str(l+1)+'_'+str(s+1)+'.input1D[2]', tVal)
            cmds.connectAttr('L_lower_eyeLid_Out_PM_'+str(l+1)+'_'+str(s+1)+'.output1D', sel[s]+'.translateX', f=True)
         
            if s < midJnt:
                cmds.setAttr('L_lower_eyeLid_Blink_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input1X', (s*val))
                cmds.setAttr('L_lower_eyeLid_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input1X', (s*val))
            if s == midJnt:
                cmds.setAttr('L_lower_eyeLid_Blink_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input1X', ((s-.5)*val))
                cmds.setAttr('L_lower_eyeLid_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input1X', ((s-.5)*val))
        
        mdSel = cmds.ls('L_lower_eyeLid_Blink_Out_MD_'+str(l+1)+'_*')
        oMdSel = cmds.ls('L_lower_eyeLid_Out_MD_'+str(l+1)+'_*')
        revOmdSel = oMdSel[::-1]
        revSel = mdSel[::-1]      
        for r in range(len(revSel)):
                if r < midJnt:
                    cmds.setAttr(revSel[r]+'.input1X', (r*val))
                    cmds.setAttr(revOmdSel[r]+'.input1X', (r*val))         


    ################################################################################################################################
    ######
    ######   Right Side Lid
    ######
    #################################################################################################################################
    chanel_list = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v']    
    cmds.duplicate('L_upper_Wire_crv', n='R_upper_Wire_crv')
    cmds.scale(-1, 1, 1, 'R_upper_Wire_crv')
    cmds.makeIdentity('R_upper_Wire_crv', a=True)
    cmds.duplicate('L_upper_bs_crv', n='R_upper_bs_crv')
    cmds.scale(-1, 1, 1, 'R_upper_bs_crv')
    cmds.makeIdentity('R_upper_bs_crv', a=True)    
    cmds.duplicate('L_upper_Main_Control_crv', n='R_upper_Main_Control_crv')
    for c in chanel_list:
        cmds.setAttr('R_upper_Main_Control_crv.'+c, l=False)    
    cmds.scale(-1, 1, 1, 'R_upper_Main_Control_crv')
    cmds.makeIdentity('R_upper_Main_Control_crv', a=True)    
    cmds.duplicate('L_upper_Closed_Curve', n='R_upper_Closed_Curve')
    cmds.scale(-1, 1, 1, 'R_upper_Closed_Curve')
    cmds.makeIdentity('R_upper_Closed_Curve', a=True)    
    cmds.duplicate('L_mid_Closed_Curve', n='R_mid_Closed_Curve')
    cmds.scale(-1, 1, 1, 'R_mid_Closed_Curve')
    cmds.makeIdentity('R_mid_Closed_Curve', a=True)    
    cmds.duplicate('L_lower_Wire_crv', n='R_lower_Wire_crv')
    cmds.scale(-1, 1, 1, 'R_lower_Wire_crv')
    cmds.makeIdentity('R_lower_Wire_crv', a=True)    
    cmds.duplicate('L_lower_bs_crv', n='R_lower_bs_crv')
    cmds.scale(-1, 1, 1, 'R_lower_bs_crv')
    cmds.makeIdentity('R_lower_bs_crv', a=True)    
    cmds.duplicate('L_lower_Main_Control_crv', n='R_lower_Main_Control_crv')
    for c in chanel_list:
        cmds.setAttr('R_lower_Main_Control_crv.'+c, l=False)      
    cmds.scale(-1, 1, 1, 'R_lower_Main_Control_crv')
    cmds.makeIdentity('R_lower_Main_Control_crv', a=True)    
    cmds.duplicate('L_lower_Closed_Curve', n='R_lower_Closed_Curve')
    cmds.scale(-1, 1, 1, 'R_lower_Closed_Curve')
    cmds.makeIdentity('R_lower_Closed_Curve', a=True)  
        
    cmds.select('R_upper_bs_crv.cv[*]')
    upper_vertSel = cmds.ls(sl =True, fl = True)
    for i in range(len(upper_vertSel)):
        vertPos = cmds.xform(upper_vertSel[i], q = True, ws = True, t = True)
        startJnt = cmds.createNode('joint', n='R_upper_eyeLid_Center_Jnt_'+ str(i+1), ss=True)
        startJnt_grp = cmds.group(n='R_upper_eyeLid_Center_jnt_'+str(i+1)+'_grp', em=True)
        cmds.parent(startJnt, startJnt_grp)
        cmds.delete(cmds.parentConstraint('R_proxy_eyeJnt', startJnt_grp))
        loc = cmds.spaceLocator(n='R_upper_eyeLid_Loc_'+ str(i+1))
        cmds.scale(.05,.05,.05)
        pointCrv = cmds.createNode('pointOnCurveInfo', n='R_upper_PointOnCurve_'+str(i+1), ss=True)
        crvShape = cmds.listRelatives('R_upper_bs_crv', s = True)
        cmds.connectAttr(crvShape[0]+'.worldSpace[0]', pointCrv+'.inputCurve')
        cmds.connectAttr(pointCrv+'.position', loc[0]+'.translate')
        cmds.setAttr(pointCrv+'.turnOnPercentage', 1)
        vtxCount = cmds.getAttr(crvShape[0]+'.spans')
        cmds.setAttr(pointCrv+'.parameter', i*(float(1)/float(vtxCount)))
        cmds.aimConstraint(loc, startJnt, mo=0)
        endJnt = cmds.createNode('joint', n = 'R_upper_eyeLid_End_'+ str(i)+'_jnt', ss=True)
        cmds.delete(cmds.pointConstraint(loc, endJnt))
        cmds.parent(endJnt, startJnt)
        cmds.setAttr(endJnt+'.jointOrientX',0)
        cmds.setAttr(endJnt+'.jointOrientY',0)
        cmds.setAttr(endJnt+'.jointOrientZ',0)
        cmds.parent(startJnt_grp, 'eyeLid_Jnt_grp')  
        cmds.parent(loc, 'eyeLid_Loc_grp')                 
        cmds.select(cl=True)
    cmds.select('R_lower_bs_crv.cv[*]')
    lower_vertSel = cmds.ls(sl =True, fl = True)
    for i in range(len(lower_vertSel)):
        vertPos = cmds.xform(lower_vertSel[i], q = True, ws = True, t = True)
        startJnt = cmds.createNode('joint', n='R_lower_eyeLid_Center_Jnt_'+ str(i+1), ss=True)
        startJnt_grp = cmds.group(n='R_lower_eyeLid_Center_jnt_'+str(i+1)+'_grp', em=True)
        cmds.parent(startJnt, startJnt_grp)
        cmds.delete(cmds.parentConstraint('R_proxy_eyeJnt', startJnt_grp))
        loc = cmds.spaceLocator(n='R_lower_eyeLid_Loc_'+ str(i+1))
        cmds.scale(.05,.05,.05)
        pointCrv = cmds.createNode('pointOnCurveInfo', n='R_lower_PointOnCurve_'+str(i+1), ss=True)
        crvShape = cmds.listRelatives('R_lower_bs_crv', s = True)
        cmds.connectAttr(crvShape[0]+'.worldSpace[0]', pointCrv+'.inputCurve')
        cmds.connectAttr(pointCrv+'.position', loc[0]+'.translate')
        cmds.setAttr(pointCrv+'.turnOnPercentage', 1)
        vtxCount = cmds.getAttr(crvShape[0]+'.spans')
        cmds.setAttr(pointCrv+'.parameter', i*(float(1)/float(vtxCount)))
        cmds.aimConstraint(loc, startJnt, mo=0)
        endJnt = cmds.createNode('joint', n = 'R_lower_eyeLid_End_'+ str(i)+'_jnt', ss=True)
        cmds.delete(cmds.pointConstraint(loc, endJnt))
        cmds.parent(endJnt, startJnt)
        cmds.setAttr(endJnt+'.jointOrientX',0)
        cmds.setAttr(endJnt+'.jointOrientY',0)
        cmds.setAttr(endJnt+'.jointOrientZ',0)
        cmds.parent(startJnt_grp, 'eyeLid_Jnt_grp')  
        cmds.parent(loc, 'eyeLid_Loc_grp')                 
        cmds.select(cl=True)                
    ############ upper Lid Setup
    upWire = cmds.wire('R_upper_Wire_crv', w='R_upper_Closed_Curve', n='upperLid_Wire')
    cmds.setAttr(upWire[0]+'.dropoffDistance[0]', 50)
    cmds.setAttr(upWire[0]+'.rotation', 0)
    cmds.blendShape('R_upper_Wire_crv', 'R_upper_bs_crv', n='R_upperLid_Connect_bs')
    cmds.setAttr('R_upperLid_Connect_bs.R_upper_Wire_crv', 1)        
    ### Applying BlendShape for Blink
    cmds.blendShape('R_upper_Main_Control_crv', 'R_lower_Main_Control_crv', 'R_mid_Closed_Curve', n='R_Blink_bs')
    cmds.blendShape('R_lower_Main_Control_crv', 'R_mid_Closed_Curve', 'R_lower_Closed_Curve', n='R_lower_Closed_bs')
    cmds.blendShape('R_upper_Main_Control_crv', 'R_mid_Closed_Curve', 'R_upper_Closed_Curve', n='R_upper_Closed_bs')
    cmds.createNode('multiplyDivide', n='R_Blink_Center_MD_1', ss=True)
    cmds.createNode('reverse', n='R_Blink_Center_RE_1', ss=True)
    cmds.connectAttr('R_face_picker_eye_null.blinkCenter', 'R_Blink_Center_MD_1.input1X', f=True)
    cmds.connectAttr('R_Blink_Center_MD_1.outputX', 'R_Blink_Center_RE_1.inputX', f=True)
    cmds.connectAttr('R_Blink_Center_MD_1.outputX', 'R_Blink_bs.R_upper_Main_Control_crv', f=True)
    cmds.connectAttr('R_Blink_Center_RE_1.outputX', 'R_Blink_bs.R_lower_Main_Control_crv', f=True)
    cmds.setAttr('R_Blink_Center_MD_1.input2X', .1)
    #### upper Blink
    cmds.createNode('multiplyDivide', n='R_upper_Blink_MD_1', ss=True)
    cmds.createNode('plusMinusAverage', n='R_upper_Blink_PM_1', ss=True)
    cmds.createNode('reverse', n='R_upper_Blink_RE_1', ss=True)
    cmds.connectAttr('R_face_picker_eye_null.blink', 'R_upper_Blink_MD_1.input1X', f=True)
    cmds.connectAttr('R_face_picker_eye_null.upperLid', 'R_upper_Blink_MD_1.input1Y', f=True)
    cmds.setAttr('R_upper_Blink_MD_1.input2X', .105)
    cmds.setAttr('R_upper_Blink_MD_1.input2Y', .105)
    cmds.connectAttr('R_upper_Blink_MD_1.outputX', 'R_upper_Blink_PM_1.input1D[0]', f=True)
    cmds.connectAttr('R_upper_Blink_MD_1.outputY', 'R_upper_Blink_PM_1.input1D[1]', f=True)
    cmds.connectAttr('R_upper_Blink_PM_1.output1D', 'R_upper_Closed_bs.R_mid_Closed_Curve', f=True)
    cmds.connectAttr('R_upper_Blink_RE_1.outputX', 'R_upper_Closed_bs.R_upper_Main_Control_crv', f=True)
    cmds.connectAttr('R_upper_Blink_PM_1.output1D', 'R_upper_Blink_RE_1.inputX')
    
    ############ lower Lid Setup
    lowWire = cmds.wire('R_lower_Wire_crv', w='R_lower_Closed_Curve', n='lowerLid_Wire')
    cmds.setAttr(upWire[0]+'.dropoffDistance[0]', 50)
    cmds.setAttr(upWire[0]+'.rotation', 0)
    cmds.blendShape('R_lower_Wire_crv', 'R_lower_bs_crv', n='R_lowerLid_Connect_bs')        
    cmds.setAttr('R_lowerLid_Connect_bs.R_lower_Wire_crv', 1)        
    #### upper Blink
    cmds.createNode('multiplyDivide', n='R_lower_Blink_MD_1', ss=True)
    cmds.createNode('plusMinusAverage', n='R_lower_Blink_PM_1', ss=True)
    cmds.createNode('reverse', n='R_lower_Blink_RE_1', ss=True)
    cmds.connectAttr('R_face_picker_eye_null.blink', 'R_lower_Blink_MD_1.input1X', f=True)
    cmds.connectAttr('R_face_picker_eye_null.lowerLid', 'R_lower_Blink_MD_1.input1Y', f=True)
    cmds.setAttr('R_lower_Blink_MD_1.input2X', .105)
    cmds.setAttr('R_lower_Blink_MD_1.input2Y', .105)
    cmds.connectAttr('R_lower_Blink_MD_1.outputX', 'R_lower_Blink_PM_1.input1D[0]', f=True)
    cmds.connectAttr('R_lower_Blink_MD_1.outputY', 'R_lower_Blink_PM_1.input1D[1]', f=True)
    cmds.connectAttr('R_lower_Blink_PM_1.output1D', 'R_lower_Closed_bs.R_mid_Closed_Curve', f=True)
    cmds.connectAttr('R_lower_Blink_RE_1.outputX', 'R_lower_Closed_bs.R_lower_Main_Control_crv', f=True)
    cmds.connectAttr('R_lower_Blink_PM_1.output1D', 'R_lower_Blink_RE_1.inputX')
    
    for c in range(0,5):
        ctrlPos = cmds.xform('R_upper_Main_Control_crv.cv['+str(c)+']', q=True, ws=True, t=True)
        cmds.select(cl=True)
        tipJnt = cmds.joint(n='R_Control_Tip_Jnt_'+str(c+1), p=ctrlPos, rad=.5)
        cmds.select(cl=True)
        rotateGrp = cmds.group(em=True, n='R_Control_Tip_Jnt_'+str(c+1)+'_Rotate_grp')
        offGrp = cmds.group(em=True, n='R_Control_Tip_Jnt_'+str(c+1)+'_offsetgrp')
        cmds.parent(rotateGrp, offGrp)    
        cmds.delete(cmds.parentConstraint(tipJnt, offGrp))
        cmds.parent(tipJnt, rotateGrp)            
        cmds.select(cl=True)
        cJnt = cmds.joint(n='R_Control_Center_Jnt_'+str(c+1))
        cJntGrp = cmds.group(n='R_Control_Center_Jnt_grp_'+str(c+1))
        cmds.delete(cmds.parentConstraint('R_proxy_eyeJnt', cJntGrp))
        cmds.parent(offGrp, cJnt)
        
    for c in range(0,3):
        ctrlPos = cmds.xform('R_lower_Main_Control_crv.cv['+str(c+1)+']', q=True, ws=True, t=True)
        cmds.select(cl=True)
        tipJnt = cmds.joint(n='R_Control_Tip_Jnt_'+str(c+6), p=ctrlPos, rad=.5)
        cmds.select(cl=True)
        rotateGrp = cmds.group(em=True, n='R_Control_Tip_Jnt_'+str(c+6)+'_Rotate_grp')
        offGrp = cmds.group(em=True, n='R_Control_Tip_Jnt_'+str(c+6)+'_offsetgrp')
        cmds.parent(rotateGrp, offGrp)    
        cmds.delete(cmds.parentConstraint(tipJnt, offGrp))
        cmds.parent(tipJnt, rotateGrp)            
        cmds.select(cl=True)
        cJnt = cmds.joint(n='R_Control_Center_Jnt_'+str(c+6))
        cJntGrp = cmds.group(n='R_Control_Center_Jnt_grp_'+str(c+6))
        cmds.delete(cmds.parentConstraint('R_proxy_eyeJnt', cJntGrp))
        cmds.parent(offGrp, cJnt)  
    sel = cmds.ls('R_Control_Tip_Jnt_*_offsetgrp')
    for s in range(len(sel)):
        ctrl = cmds.circle(n='R_eyeLid_'+str(s+1)+'_ctrl', nr=(0,0,1), r=.05, ch=False)
        grp = cmds.group(n='R_eyeLid_'+str(s+1)+'_ctrl_grp')
        cmds.delete(cmds.parentConstraint(sel[s], grp))
    cmds.select('R_Control_Center_Jnt_grp_*')
    cmds.group(n='R_Control_Center_Jnt_grp')
    cmds.select('R_eyeLid_*_ctrl_grp')
    cmds.group(n='R_eyeLid_ctrl_grp')
    ##################################
    cmds.addAttr('R_eyeLid_*_ctrl', ln='Eye_Follow', min=0, max=1, dv=0, k=True)
    cmds.addAttr('R_eyeLid_2_ctrl', ln='mid_ctrl_Follow', min=0, max=1, dv=0, k=True)
    cmds.addAttr('R_eyeLid_2_ctrl', ln='Corner_ctrl_Follow', min=0, max=1, dv=0, k=True)
    cmds.addAttr('R_eyeLid_4_ctrl', ln='mid_ctrl_Follow', min=0, max=1, dv=0, k=True)
    cmds.addAttr('R_eyeLid_4_ctrl', ln='Corner_ctrl_Follow', min=0, max=1, dv=0, k=True)
    cmds.addAttr('R_eyeLid_6_ctrl', ln='mid_ctrl_Follow', min=0, max=1, dv=0, k=True)
    cmds.addAttr('R_eyeLid_6_ctrl', ln='Corner_ctrl_Follow', min=0, max=1, dv=0, k=True)
    cmds.addAttr('R_eyeLid_8_ctrl', ln='mid_ctrl_Follow', min=0, max=1, dv=0, k=True)
    cmds.addAttr('R_eyeLid_8_ctrl', ln='Corner_ctrl_Follow', min=0, max=1, dv=0, k=True)
    sel = cmds.ls('R_eyeLid_*_ctrl')
    for s in sel:
        cmds.setAttr(s+'.Eye_Follow', .05)
    sel = cmds.ls('R_eyeLid_4_ctrl','R_eyeLid_2_ctrl','R_eyeLid_6_ctrl','R_eyeLid_8_ctrl')
    for s in sel:
        cmds.setAttr(s+'.mid_ctrl_Follow', .5)
        cmds.setAttr(s+'.Corner_ctrl_Follow', .5)       
    ###############################################################            
    sel = cmds.ls('R_Control_Center_Jnt_*', typ='joint')
    for s in range(len(sel)):
        cmds.pointConstraint('R_proxy_eyeJnt', sel[s])
        ## Creating Multiply Devide Node for each control Joints
        cmds.createNode('multiplyDivide', n='R_eyeLid_Follow_MD_'+str(s+1), ss=True)
        cmds.connectAttr('R_proxy_eyeJnt.rotate', 'R_eyeLid_Follow_MD_'+str(s+1)+'.input1', f=True)
        cmds.connectAttr('R_eyeLid_Follow_MD_'+str(s+1)+'.output', 'R_Control_Center_Jnt_'+str(s+1)+'.rotate', f=True)
    ### Creating Node for upper lower and Corner lid Follow    
    cmds.createNode('multiplyDivide', n='R_upperLid_Follow_MD_01', ss=True)
    cmds.createNode('multiplyDivide', n='R_lowerLid_Follow_MD_01', ss=True)
    cmds.createNode('multiplyDivide', n='R_Corner_Follow_MD_01', ss=True)
    ### Connecting upper Lid Attributes
    cmds.connectAttr('R_face_picker_eye_null.upperLidFollow','R_upperLid_Follow_MD_01.input1X', f=True)
    cmds.connectAttr('R_face_picker_eye_null.upperLidFollow','R_upperLid_Follow_MD_01.input1Y', f=True)
    cmds.connectAttr('R_face_picker_eye_null.upperLidFollow','R_upperLid_Follow_MD_01.input1Z', f=True)
    ### Connecting lowerLid Attributes
    cmds.connectAttr('R_face_picker_eye_null.lowerLidFollow','R_lowerLid_Follow_MD_01.input1X', f=True)
    cmds.connectAttr('R_face_picker_eye_null.lowerLidFollow','R_lowerLid_Follow_MD_01.input1Y', f=True)
    cmds.connectAttr('R_face_picker_eye_null.lowerLidFollow','R_lowerLid_Follow_MD_01.input1Z', f=True)
    ##Connceting Corner Lid Attr
    cmds.connectAttr('R_face_picker_eye_null.Corner_Follow','R_Corner_Follow_MD_01.input1X', f=True)
    cmds.connectAttr('R_face_picker_eye_null.Corner_Follow','R_Corner_Follow_MD_01.input1Y', f=True)
    cmds.connectAttr('R_face_picker_eye_null.Corner_Follow','R_Corner_Follow_MD_01.input1Z', f=True)
    ## eyeLid Controler to MD
    cmds.connectAttr('R_eyeLid_2_ctrl.Eye_Follow','R_upperLid_Follow_MD_01.input2X', f=True)
    cmds.connectAttr('R_eyeLid_3_ctrl.Eye_Follow','R_upperLid_Follow_MD_01.input2Y', f=True)
    cmds.connectAttr('R_eyeLid_4_ctrl.Eye_Follow','R_upperLid_Follow_MD_01.input2Z', f=True)
    ## eyeLid Controler to MD
    cmds.connectAttr('R_eyeLid_6_ctrl.Eye_Follow','R_lowerLid_Follow_MD_01.input2X', f=True)
    cmds.connectAttr('R_eyeLid_7_ctrl.Eye_Follow','R_lowerLid_Follow_MD_01.input2Y', f=True)
    cmds.connectAttr('R_eyeLid_8_ctrl.Eye_Follow','R_lowerLid_Follow_MD_01.input2Z', f=True)
    ## eyeLid Controler to MD
    cmds.connectAttr('R_eyeLid_1_ctrl.Eye_Follow','R_Corner_Follow_MD_01.input2X', f=True)
    cmds.connectAttr('R_eyeLid_5_ctrl.Eye_Follow','R_Corner_Follow_MD_01.input2Y', f=True)
    
    cmds.connectAttr('R_Corner_Follow_MD_01.outputY','R_eyeLid_Follow_MD_1.input2X', f=True)
    cmds.connectAttr('R_Corner_Follow_MD_01.outputY','R_eyeLid_Follow_MD_1.input2Y', f=True)
    cmds.connectAttr('R_Corner_Follow_MD_01.outputY','R_eyeLid_Follow_MD_1.input2Z', f=True)
    
    cmds.connectAttr('R_Corner_Follow_MD_01.outputX','R_eyeLid_Follow_MD_5.input2X', f=True)
    cmds.connectAttr('R_Corner_Follow_MD_01.outputX','R_eyeLid_Follow_MD_5.input2Y', f=True)
    cmds.connectAttr('R_Corner_Follow_MD_01.outputX','R_eyeLid_Follow_MD_5.input2Z', f=True)
    
    cmds.connectAttr('R_upperLid_Follow_MD_01.outputX','R_eyeLid_Follow_MD_2.input2X', f=True)
    cmds.connectAttr('R_upperLid_Follow_MD_01.outputX','R_eyeLid_Follow_MD_2.input2Y', f=True)
    cmds.connectAttr('R_upperLid_Follow_MD_01.outputX','R_eyeLid_Follow_MD_2.input2Z', f=True)
    
    cmds.connectAttr('R_upperLid_Follow_MD_01.outputY','R_eyeLid_Follow_MD_3.input2X', f=True)
    cmds.connectAttr('R_upperLid_Follow_MD_01.outputY','R_eyeLid_Follow_MD_3.input2Y', f=True)
    cmds.connectAttr('R_upperLid_Follow_MD_01.outputY','R_eyeLid_Follow_MD_3.input2Z', f=True)
    
    cmds.connectAttr('R_upperLid_Follow_MD_01.outputZ','R_eyeLid_Follow_MD_4.input2X', f=True)
    cmds.connectAttr('R_upperLid_Follow_MD_01.outputZ','R_eyeLid_Follow_MD_4.input2Y', f=True)
    cmds.connectAttr('R_upperLid_Follow_MD_01.outputZ','R_eyeLid_Follow_MD_4.input2Z', f=True)
    
    cmds.connectAttr('R_lowerLid_Follow_MD_01.outputX','R_eyeLid_Follow_MD_6.input2X', f=True)
    cmds.connectAttr('R_lowerLid_Follow_MD_01.outputX','R_eyeLid_Follow_MD_6.input2Y', f=True)
    cmds.connectAttr('R_lowerLid_Follow_MD_01.outputX','R_eyeLid_Follow_MD_6.input2Z', f=True)
    
    cmds.connectAttr('R_lowerLid_Follow_MD_01.outputY','R_eyeLid_Follow_MD_7.input2X', f=True)
    cmds.connectAttr('R_lowerLid_Follow_MD_01.outputY','R_eyeLid_Follow_MD_7.input2Y', f=True)
    cmds.connectAttr('R_lowerLid_Follow_MD_01.outputY','R_eyeLid_Follow_MD_7.input2Z', f=True)
    
    cmds.connectAttr('R_lowerLid_Follow_MD_01.outputZ','R_eyeLid_Follow_MD_8.input2X', f=True)
    cmds.connectAttr('R_lowerLid_Follow_MD_01.outputZ','R_eyeLid_Follow_MD_8.input2Y', f=True)
    cmds.connectAttr('R_lowerLid_Follow_MD_01.outputZ','R_eyeLid_Follow_MD_8.input2Z', f=True)
    
    ### eyeLid Rotate Pivot Change for Rotation or S curve shape
    upmidPos = cmds.xform('R_Control_Tip_Jnt_3', q=True, ws=True, t=True)
    cmds.move(upmidPos[0],upmidPos[1],upmidPos[2],'R_Control_Tip_Jnt_4_Rotate_grp.rotatePivot', 'R_Control_Tip_Jnt_4_Rotate_grp.scalePivot', a=True)
    cmds.move(upmidPos[0],upmidPos[1],upmidPos[2],'R_Control_Tip_Jnt_2_Rotate_grp.rotatePivot', 'R_Control_Tip_Jnt_2_Rotate_grp.scalePivot', a=True)
    
    lowmidPos = cmds.xform('R_Control_Tip_Jnt_7', q=True, ws=True, t=True)
    cmds.move(lowmidPos[0],lowmidPos[1],lowmidPos[2],'R_Control_Tip_Jnt_6_Rotate_grp.rotatePivot', 'R_Control_Tip_Jnt_6_Rotate_grp.scalePivot', a=True)
    cmds.move(lowmidPos[0],lowmidPos[1],lowmidPos[2],'R_Control_Tip_Jnt_8_Rotate_grp.rotatePivot', 'R_Control_Tip_Jnt_8_Rotate_grp.scalePivot', a=True)
    
    ##################################################################
    sel = cmds.ls('R_eyeLid_*_ctrl')
    for s in range(len(sel)):
        md = cmds.createNode('multiplyDivide', n='R_eyeLid_ctrl_MD_'+str(s+1), ss=True)
        pm = cmds.createNode('plusMinusAverage', n='R_eyeLid_ctrl_PM_'+str(s+1), ss=True)
        cmds.connectAttr('R_eyeLid_'+str(s+1)+'_ctrl.translate', md+'.input1', f=True)
        cmds.connectAttr(md+'.output', pm+'.input3D[0]', f=True)
        cmds.connectAttr(pm+'.output3D', 'R_Control_Tip_Jnt_'+str(s+1)+'.translate')
    
    cmds.createNode('multiplyDivide', n='R_eyeLid_ctrl_MD_9', ss=True)
    cmds.createNode('multiplyDivide', n='R_eyeLid_ctrl_MD_10', ss=True)
    cmds.createNode('multiplyDivide', n='R_eyeLid_ctrl_MD_11', ss=True)
    cmds.createNode('multiplyDivide', n='R_eyeLid_ctrl_MD_12', ss=True)
    
    cmds.createNode('multiplyDivide', n='R_eyeLid_ctrl_MD_13', ss=True)
    cmds.createNode('multiplyDivide', n='R_eyeLid_ctrl_MD_14', ss=True)
    cmds.createNode('multiplyDivide', n='R_eyeLid_ctrl_MD_15', ss=True)
    cmds.createNode('multiplyDivide', n='R_eyeLid_ctrl_MD_16', ss=True)
    
    cmds.connectAttr('R_eyeLid_3_ctrl.translate', 'R_eyeLid_ctrl_MD_9.input1', f=True)
    cmds.connectAttr('R_eyeLid_3_ctrl.translate', 'R_eyeLid_ctrl_MD_10.input1', f=True)
    
    cmds.connectAttr('R_eyeLid_7_ctrl.translate', 'R_eyeLid_ctrl_MD_11.input1', f=True)
    cmds.connectAttr('R_eyeLid_7_ctrl.translate', 'R_eyeLid_ctrl_MD_12.input1', f=True)
    
    cmds.connectAttr('R_eyeLid_1_ctrl.translate', 'R_eyeLid_ctrl_MD_13.input1', f=True)
    cmds.connectAttr('R_eyeLid_1_ctrl.translate', 'R_eyeLid_ctrl_MD_14.input1', f=True)
    
    cmds.connectAttr('R_eyeLid_5_ctrl.translate', 'R_eyeLid_ctrl_MD_15.input1', f=True)
    cmds.connectAttr('R_eyeLid_5_ctrl.translate', 'R_eyeLid_ctrl_MD_16.input1', f=True)
    
    cmds.connectAttr('R_eyeLid_ctrl_MD_16.output','R_eyeLid_ctrl_PM_8.input3D[1]', f=True)
    cmds.connectAttr('R_eyeLid_ctrl_MD_15.output','R_eyeLid_ctrl_PM_4.input3D[1]', f=True)
    
    cmds.connectAttr('R_eyeLid_ctrl_MD_12.output','R_eyeLid_ctrl_PM_8.input3D[2]', f=True)
    cmds.connectAttr('R_eyeLid_ctrl_MD_11.output','R_eyeLid_ctrl_PM_6.input3D[1]', f=True)
    
    cmds.connectAttr('R_eyeLid_ctrl_MD_13.output','R_eyeLid_ctrl_PM_2.input3D[1]', f=True)
    cmds.connectAttr('R_eyeLid_ctrl_MD_14.output','R_eyeLid_ctrl_PM_6.input3D[2]', f=True)
    
    cmds.connectAttr('R_eyeLid_ctrl_MD_9.output','R_eyeLid_ctrl_PM_2.input3D[2]', f=True)
    cmds.connectAttr('R_eyeLid_ctrl_MD_10.output','R_eyeLid_ctrl_PM_4.input3D[2]', f=True)
    
    cmds.createNode('multiplyDivide', n='R_upperLid_Rotate_MD_01', ss=True)
    cmds.createNode('multiplyDivide', n='R_lowerLid_Rotate_MD_01', ss=True)
    
    cmds.setAttr('R_upperLid_Rotate_MD_01.input2X', .5)
    cmds.setAttr('R_upperLid_Rotate_MD_01.input2Y', .5)
    cmds.setAttr('R_upperLid_Rotate_MD_01.input2Z', .5)
    cmds.setAttr('R_lowerLid_Rotate_MD_01.input2X', .5)
    cmds.setAttr('R_lowerLid_Rotate_MD_01.input2Y', .5)
    cmds.setAttr('R_lowerLid_Rotate_MD_01.input2Z', .5)
    
    cmds.connectAttr('R_eyeLid_3_ctrl.rotate', 'R_upperLid_Rotate_MD_01.input1')
    cmds.connectAttr('R_eyeLid_7_ctrl.rotate', 'R_lowerLid_Rotate_MD_01.input1')
    
    cmds.connectAttr('R_upperLid_Rotate_MD_01.output', 'R_Control_Tip_Jnt_2_Rotate_grp.rotate')
    cmds.connectAttr('R_upperLid_Rotate_MD_01.output', 'R_Control_Tip_Jnt_4_Rotate_grp.rotate')
    
    cmds.connectAttr('R_lowerLid_Rotate_MD_01.output',
                     'R_Control_Tip_Jnt_6_Rotate_grp.rotate')
    cmds.connectAttr('R_lowerLid_Rotate_MD_01.output',
                    'R_Control_Tip_Jnt_8_Rotate_grp.rotate')
    
    ##### Skin Bind To Control Curve
    upperSel = cmds.ls('R_Control_Tip_Jnt_4', 'R_Control_Tip_Jnt_3',
                        'R_Control_Tip_Jnt_2', 'R_Control_Tip_Jnt_1', 'R_Control_Tip_Jnt_5')
    lowerSel = cmds.ls('R_Control_Tip_Jnt_6', 'R_Control_Tip_Jnt_7',
                        'R_Control_Tip_Jnt_8', 'R_Control_Tip_Jnt_1', 'R_Control_Tip_Jnt_5')
    upperCrv = 'R_upper_Main_Control_crv'
    lowerCrev = 'R_lower_Main_Control_crv'
    cmds.skinCluster(upperSel, upperCrv, n='upper_crv_SkinCluster')
    cmds.skinCluster(lowerSel, lowerCrev, n='lower_crv_SkinCluster')
    ####################################################
    #### upper Lid Out
    loopSel = cmds.ls('R_upper_eyeLid_End_1_jnt')
    totalLoop = len(loopSel)
    loopVal = float(1)/totalLoop
    for l in range(len(loopSel)):
        sel = cmds.ls('R_upper_eyeLid_End_*_jnt')
        totalJnt = len(sel)
        midJnt = totalJnt/2
        val = (float(1)-(float(l)*float(loopVal)))/float(totalJnt)
        for s in range(len(sel)):
            md = cmds.createNode('multiplyDivide', n='R_upper_eyeLid_Out_MD_'+str(l+1)+'_'+str(s+1), ss=True)
            blinkMd = cmds.createNode('multiplyDivide', n='R_upper_eyeLid_Blink_Out_MD_'+str(l+1)+'_'+str(s+1), ss=True)
            autoMd = cmds.createNode('multiplyDivide', n='R_upper_eyeLid_Auto_Out_MD_'+str(l+1)+'_'+str(s+1), ss=True)
            pm = cmds.createNode('plusMinusAverage', n='R_upper_eyeLid_Out_PM_'+str(l+1)+'_'+str(s+1), ss=True)       
            cmds.connectAttr('R_face_picker_eye_null.upperLidOut',
                            'R_upper_eyeLid_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input2X', f=True)
            cmds.connectAttr('R_face_picker_eye_null.upperLidOutAuto',
                            'R_upper_eyeLid_Auto_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input2X', f=True)   
            cmds.connectAttr('R_face_picker_eye_null.blink',
                            'R_upper_eyeLid_Blink_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input2.input2X', f=True)   
            cmds.connectAttr('R_upper_eyeLid_Blink_Out_MD_'+str(l+1)+'_'+str(s+1)+'.outputX',
                            'R_upper_eyeLid_Auto_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input1X', f=True)   
            cmds.connectAttr('R_upper_eyeLid_Auto_Out_MD_'+str(l+1)+'_'+str(s+1)+'.outputX',
                            'R_upper_eyeLid_Out_PM_'+str(l+1)+'_'+str(s+1)+'.input1D[0]', f=True)   
            cmds.connectAttr('R_upper_eyeLid_Out_MD_'+str(l+1)+'_'+str(s+1)+'.outputX',
                            'R_upper_eyeLid_Out_PM_'+str(l+1)+'_'+str(s+1)+'.input1D[1]', f=True)   
            tVal = cmds.getAttr(sel[s]+'.translateX')
            cmds.setAttr('R_upper_eyeLid_Out_PM_'+str(l+1)+'_'+str(s+1)+'.input1D[2]', tVal)
            cmds.connectAttr('R_upper_eyeLid_Out_PM_'+str(l+1)+'_'+str(s+1)+'.output1D', sel[s]+'.translateX', f=True)     
            if s < midJnt:
                cmds.setAttr('R_upper_eyeLid_Blink_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input1X', (s*val))
                cmds.setAttr('R_upper_eyeLid_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input1X', (s*val))
            if s == midJnt:
                cmds.setAttr('R_upper_eyeLid_Blink_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input1X', ((s-.5)*val))
                cmds.setAttr('R_upper_eyeLid_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input1X', ((s-.5)*val))    
        mdSel = cmds.ls('R_upper_eyeLid_Blink_Out_MD_'+str(l+1)+'_*')
        oMdSel = cmds.ls('R_upper_eyeLid_Out_MD_'+str(l+1)+'_*')
        revOmdSel = oMdSel[::-1]
        revSel = mdSel[::-1]      
        for r in range(len(revSel)):
                if r < midJnt:
                    cmds.setAttr(revSel[r]+'.input1X', (r*val))
                    cmds.setAttr(revOmdSel[r]+'.input1X', (r*val))
       
    #### lower Lid Out
    loopSel = cmds.ls('R_lower_eyeLid_End_1_jnt')
    totalLoop = len(loopSel)
    loopVal = (float(1)/totalLoop)/10
    for l in range(len(loopSel)):
        sel = cmds.ls('R_lower_eyeLid_End_*_jnt')
        totalJnt = len(sel)
        midJnt = totalJnt/2
        val = (float(1)-(float(l)*float(loopVal)))/float(totalJnt)
        for s in range(len(sel)):
            md = cmds.shadingNode('multiplyDivide',au=True, n='R_lower_eyeLid_Out_MD_'+str(l+1)+'_'+str(s+1))
            blinkMd = cmds.shadingNode('multiplyDivide', au=True, n='R_lower_eyeLid_Blink_Out_MD_'+str(l+1)+'_'+str(s+1))
            autoMd = cmds.shadingNode('multiplyDivide', au=True, n='R_lower_eyeLid_Auto_Out_MD_'+str(l+1)+'_'+str(s+1))
            pm = cmds.shadingNode('plusMinusAverage', au=True, n='R_lower_eyeLid_Out_PM_'+str(l+1)+'_'+str(s+1))
           
            cmds.connectAttr('R_face_picker_eye_null.lowerLidOut',
                            'R_lower_eyeLid_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input2X', f=True)
            cmds.connectAttr('R_face_picker_eye_null.lowerLidOutAuto',
                             'R_lower_eyeLid_Auto_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input2X', f=True)   
            cmds.connectAttr('R_face_picker_eye_null.blink',
                            'R_lower_eyeLid_Blink_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input2.input2X', f=True)   
            cmds.connectAttr('R_lower_eyeLid_Blink_Out_MD_'+str(l+1)+'_'+str(s+1)+'.outputX',
                            'R_lower_eyeLid_Auto_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input1X', f=True)   
            cmds.connectAttr('R_lower_eyeLid_Auto_Out_MD_'+str(l+1)+'_'+str(s+1)+'.outputX',
                            'R_lower_eyeLid_Out_PM_'+str(l+1)+'_'+str(s+1)+'.input1D[0]', f=True)   
            cmds.connectAttr('R_lower_eyeLid_Out_MD_'+str(l+1)+'_'+str(s+1)+'.outputX',
                            'R_lower_eyeLid_Out_PM_'+str(l+1)+'_'+str(s+1)+'.input1D[1]', f=True)   
            tVal = cmds.getAttr(sel[s]+'.translateX')
            cmds.setAttr('R_lower_eyeLid_Out_PM_'+str(l+1)+'_'+str(s+1)+'.input1D[2]', tVal)
            cmds.connectAttr('R_lower_eyeLid_Out_PM_'+str(l+1)+'_'+str(s+1)+'.output1D', sel[s]+'.translateX', f=True)
         
            if s < midJnt:
                cmds.setAttr('R_lower_eyeLid_Blink_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input1X', (s*val))
                cmds.setAttr('R_lower_eyeLid_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input1X', (s*val))
            if s == midJnt:
                cmds.setAttr('R_lower_eyeLid_Blink_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input1X', ((s-.5)*val))
                cmds.setAttr('R_lower_eyeLid_Out_MD_'+str(l+1)+'_'+str(s+1)+'.input1X', ((s-.5)*val))
        
        mdSel = cmds.ls('R_lower_eyeLid_Blink_Out_MD_'+str(l+1)+'_*')
        oMdSel = cmds.ls('R_lower_eyeLid_Out_MD_'+str(l+1)+'_*')
        revOmdSel = oMdSel[::-1]
        revSel = mdSel[::-1]      
        for r in range(len(revSel)):
                if r < midJnt:
                    cmds.setAttr(revSel[r]+'.input1X', (r*val))
                    cmds.setAttr(revOmdSel[r]+'.input1X', (r*val))         

    cmds.parent('*_Control_Center_Jnt_grp', 'eyeLid_Jnt_grp')
    cmds.parent('*_eyeLid_ctrl_grp', 'eyeLid_ctrl_grp')
    cmds.parent('*_Wire_crv', '*_bs_crv', '*_Main_Control_crv', '*_Closed_Curve',
                '*_mid_Closed_Curve', '*_Closed_CurveBaseWire', 'eyeLid_Curve_grp')
    cmds.parent('*_proxy_eyeJnt', 'eyeLid_Jnt_grp')
    cmds.group(n='eyelid_def_grp', em=True)
    cmds.parent('Proxy_root_jnt', 'eyeLid_Jnt_grp')
    cmds.parent('eyeLid_Jnt_grp', 'eyeLid_Loc_grp', 'eyeLid_Curve_grp', 'eyelid_def_grp')
        
    cmds.connectAttr('L_eyeLid_4_ctrl.mid_ctrl_Follow', 'L_eyeLid_ctrl_MD_10.input2X')
    cmds.connectAttr('L_eyeLid_4_ctrl.mid_ctrl_Follow', 'L_eyeLid_ctrl_MD_10.input2Y')
    cmds.connectAttr('L_eyeLid_4_ctrl.mid_ctrl_Follow', 'L_eyeLid_ctrl_MD_10.input2Z')
    cmds.connectAttr('L_eyeLid_2_ctrl.mid_ctrl_Follow', 'L_eyeLid_ctrl_MD_9.input2X')
    cmds.connectAttr('L_eyeLid_2_ctrl.mid_ctrl_Follow', 'L_eyeLid_ctrl_MD_9.input2Y')
    cmds.connectAttr('L_eyeLid_2_ctrl.mid_ctrl_Follow', 'L_eyeLid_ctrl_MD_9.input2Z')
    cmds.connectAttr('L_eyeLid_6_ctrl.mid_ctrl_Follow', 'L_eyeLid_ctrl_MD_11.input2X')
    cmds.connectAttr('L_eyeLid_6_ctrl.mid_ctrl_Follow', 'L_eyeLid_ctrl_MD_11.input2Y')
    cmds.connectAttr('L_eyeLid_6_ctrl.mid_ctrl_Follow', 'L_eyeLid_ctrl_MD_11.input2Z')
    cmds.connectAttr('L_eyeLid_8_ctrl.mid_ctrl_Follow', 'L_eyeLid_ctrl_MD_12.input2X')
    cmds.connectAttr('L_eyeLid_8_ctrl.mid_ctrl_Follow', 'L_eyeLid_ctrl_MD_12.input2Y')
    cmds.connectAttr('L_eyeLid_8_ctrl.mid_ctrl_Follow', 'L_eyeLid_ctrl_MD_12.input2Z')
    
    cmds.connectAttr('L_eyeLid_4_ctrl.Corner_ctrl_Follow', 'L_eyeLid_ctrl_MD_15.input2X')
    cmds.connectAttr('L_eyeLid_4_ctrl.Corner_ctrl_Follow', 'L_eyeLid_ctrl_MD_15.input2Y')
    cmds.connectAttr('L_eyeLid_4_ctrl.Corner_ctrl_Follow', 'L_eyeLid_ctrl_MD_15.input2Z')
    cmds.connectAttr('L_eyeLid_2_ctrl.Corner_ctrl_Follow', 'L_eyeLid_ctrl_MD_13.input2X')
    cmds.connectAttr('L_eyeLid_2_ctrl.Corner_ctrl_Follow', 'L_eyeLid_ctrl_MD_13.input2Y')
    cmds.connectAttr('L_eyeLid_2_ctrl.Corner_ctrl_Follow', 'L_eyeLid_ctrl_MD_13.input2Z')
    cmds.connectAttr('L_eyeLid_6_ctrl.Corner_ctrl_Follow', 'L_eyeLid_ctrl_MD_14.input2X')
    cmds.connectAttr('L_eyeLid_6_ctrl.Corner_ctrl_Follow', 'L_eyeLid_ctrl_MD_14.input2Y')
    cmds.connectAttr('L_eyeLid_6_ctrl.Corner_ctrl_Follow', 'L_eyeLid_ctrl_MD_14.input2Z')
    cmds.connectAttr('L_eyeLid_8_ctrl.Corner_ctrl_Follow', 'L_eyeLid_ctrl_MD_16.input2X')
    cmds.connectAttr('L_eyeLid_8_ctrl.Corner_ctrl_Follow', 'L_eyeLid_ctrl_MD_16.input2Y')
    cmds.connectAttr('L_eyeLid_8_ctrl.Corner_ctrl_Follow', 'L_eyeLid_ctrl_MD_16.input2Z')
       
    cmds.connectAttr('R_eyeLid_4_ctrl.mid_ctrl_Follow', 'R_eyeLid_ctrl_MD_10.input2X')
    cmds.connectAttr('R_eyeLid_4_ctrl.mid_ctrl_Follow', 'R_eyeLid_ctrl_MD_10.input2Y')
    cmds.connectAttr('R_eyeLid_4_ctrl.mid_ctrl_Follow', 'R_eyeLid_ctrl_MD_10.input2Z')
    cmds.connectAttr('R_eyeLid_2_ctrl.mid_ctrl_Follow', 'R_eyeLid_ctrl_MD_9.input2X')
    cmds.connectAttr('R_eyeLid_2_ctrl.mid_ctrl_Follow', 'R_eyeLid_ctrl_MD_9.input2Y')
    cmds.connectAttr('R_eyeLid_2_ctrl.mid_ctrl_Follow', 'R_eyeLid_ctrl_MD_9.input2Z')
    cmds.connectAttr('R_eyeLid_6_ctrl.mid_ctrl_Follow', 'R_eyeLid_ctrl_MD_11.input2X')
    cmds.connectAttr('R_eyeLid_6_ctrl.mid_ctrl_Follow', 'R_eyeLid_ctrl_MD_11.input2Y')
    cmds.connectAttr('R_eyeLid_6_ctrl.mid_ctrl_Follow', 'R_eyeLid_ctrl_MD_11.input2Z')
    cmds.connectAttr('R_eyeLid_8_ctrl.mid_ctrl_Follow', 'R_eyeLid_ctrl_MD_12.input2X')
    cmds.connectAttr('R_eyeLid_8_ctrl.mid_ctrl_Follow', 'R_eyeLid_ctrl_MD_12.input2Y')
    cmds.connectAttr('R_eyeLid_8_ctrl.mid_ctrl_Follow', 'R_eyeLid_ctrl_MD_12.input2Z')
    
    cmds.connectAttr('R_eyeLid_4_ctrl.Corner_ctrl_Follow', 'R_eyeLid_ctrl_MD_15.input2X')
    cmds.connectAttr('R_eyeLid_4_ctrl.Corner_ctrl_Follow', 'R_eyeLid_ctrl_MD_15.input2Y')
    cmds.connectAttr('R_eyeLid_4_ctrl.Corner_ctrl_Follow', 'R_eyeLid_ctrl_MD_15.input2Z')
    cmds.connectAttr('R_eyeLid_2_ctrl.Corner_ctrl_Follow', 'R_eyeLid_ctrl_MD_13.input2X')
    cmds.connectAttr('R_eyeLid_2_ctrl.Corner_ctrl_Follow', 'R_eyeLid_ctrl_MD_13.input2Y')
    cmds.connectAttr('R_eyeLid_2_ctrl.Corner_ctrl_Follow', 'R_eyeLid_ctrl_MD_13.input2Z')
    cmds.connectAttr('R_eyeLid_6_ctrl.Corner_ctrl_Follow', 'R_eyeLid_ctrl_MD_14.input2X')
    cmds.connectAttr('R_eyeLid_6_ctrl.Corner_ctrl_Follow', 'R_eyeLid_ctrl_MD_14.input2Y')
    cmds.connectAttr('R_eyeLid_6_ctrl.Corner_ctrl_Follow', 'R_eyeLid_ctrl_MD_14.input2Z')
    cmds.connectAttr('R_eyeLid_8_ctrl.Corner_ctrl_Follow', 'R_eyeLid_ctrl_MD_16.input2X')
    cmds.connectAttr('R_eyeLid_8_ctrl.Corner_ctrl_Follow', 'R_eyeLid_ctrl_MD_16.input2Y')
    cmds.connectAttr('R_eyeLid_8_ctrl.Corner_ctrl_Follow', 'R_eyeLid_ctrl_MD_16.input2Z')
    
    jointList = cmds.ls('R_Control_Tip_Jnt_*_offsetgrp',type='transform')
    controlList = cmds.ls('R_eyeLid_*_ctrl_grp',type='transform')
    for i in range(len(controlList)):
        cmds.setAttr('{}.rotateY'.format(controlList[i]),180)
        cmds.setAttr('{}.rotateY'.format(jointList[i]),270)
        cmds.setAttr('{}.scaleZ'.format(controlList[i]),-1)
        cmds.setAttr('{}.scaleZ'.format(controlList[i]),-1)  
        
    controllerSet = cmds.ls('*_eyeLid_*_ctrl',type='transform')
    for i in range(len(controllerSet)):
        cmds.setAttr('{}.v'.format(controllerSet[i]),k=0,l=1,cb=0)
        abvGrp = cmds.pickWalk('{}'.format(controllerSet[i]),d='up')
        grp = cmds.group(em=1,n=controllerSet[i]+"_Offset_Grp")
        cmds.delete(cmds.parentConstraint(controllerSet[i], grp, mo=0))
        cmds.delete(cmds.scaleConstraint(controllerSet[i], grp, mo=0))
        cmds.parent(grp,abvGrp)
        cmds.parent(controllerSet[i],grp)
        cmds.select(grp);cmds.FreezeTransformations()
    for axis in ['X','Y','Z']:
        cmds.setAttr('{}.rotate{}'.format(controllerSet[i],axis),k=0,l=1,cb=0)
        cmds.setAttr('{}.scale{}'.format(controllerSet[i],axis),k=0,l=1,cb=0)           

def selectSkinJoints():
    cmds.select('*_eyeLid_End_*_jnt', 'Proxy_root_jnt')

def connectToonyAndEyelid():    
    if cmds.objExists('faceBlendBLS.eyeLeftBlinkDN'):
        cmds.setDrivenKeyframe('faceBlendBLS.eyeLeftBlinkDN', cd = 'L_face_picker_eye_null.blink', v = 0, dv = 0, itt = "linear", ott="linear")
        cmds.setDrivenKeyframe('faceBlendBLS.eyeLeftBlinkDN', cd = 'L_face_picker_eye_null.blink', v = 1, dv = 10, itt = "linear", ott="linear")
    
    if cmds.objExists('faceBlendBLS.eyeLeftBlinkUP'):
        cmds.createNode('addDoubleLinear',n='leftBlinkCenter_ADL',ss=1)
        cmds.createNode('multiplyDivide',n='leftBlinkCenter_MD',ss=1)     
        cmds.connectAttr('L_face_picker_eye_null.blink','leftBlinkCenter_ADL.input1',f=1)
        cmds.connectAttr('L_face_picker_eye_null.blinkCenter','leftBlinkCenter_ADL.input2',f=1)             
        cmds.connectAttr('leftBlinkCenter_ADL.output','leftBlinkCenter_MD.input1X',f=1)  
        cmds.delete('faceBlendBLS_eyeLeftBlinkDN')      
        cmds.setDrivenKeyframe('faceBlendBLS.eyeLeftBlinkUP', cd = 'leftBlinkCenter_MD.input1X', v = 0, dv = 11, itt = "linear", ott="linear")
        cmds.setDrivenKeyframe('faceBlendBLS.eyeLeftBlinkUP', cd = 'leftBlinkCenter_MD.input1X', v = 1, dv = 20, itt = "linear", ott="linear")
        cmds.setDrivenKeyframe('faceBlendBLS.eyeLeftBlinkDN', cd = 'leftBlinkCenter_MD.input1X', v = 0, dv = 20, itt = "linear", ott="linear")
        cmds.setDrivenKeyframe('faceBlendBLS.eyeLeftBlinkDN', cd = 'leftBlinkCenter_MD.input1X', v = 1, dv = 11, itt = "linear", ott="linear")
        cmds.setDrivenKeyframe('faceBlendBLS.eyeLeftBlinkDN', cd = 'leftBlinkCenter_MD.input1X', v = 0, dv = 1, itt = "linear", ott="linear")
    
    if cmds.objExists('faceBlendBLS.eyeRightBlinkDN'):
        cmds.setDrivenKeyframe('faceBlendBLS.eyeRightBlinkDN', cd = 'R_face_picker_eye_null.blink', v = 0, dv = 0, itt = "linear", ott="linear")
        cmds.setDrivenKeyframe('faceBlendBLS.eyeRightBlinkDN', cd = 'R_face_picker_eye_null.blink', v = 1, dv = 10, itt = "linear", ott="linear")
    
    if cmds.objExists('faceBlendBLS.eyeRightBlinkUP'):
        cmds.createNode('addDoubleLinear',n='rightBlinkCenter_ADL',ss=1)
        cmds.createNode('multiplyDivide',n='rightBlinkCenter_MD',ss=1)        
        cmds.connectAttr('R_face_picker_eye_null.blink','rightBlinkCenter_ADL.input1',f=1)
        cmds.connectAttr('R_face_picker_eye_null.blinkCenter','rightBlinkCenter_ADL.input2',f=1)        
        cmds.connectAttr('rightBlinkCenter_ADL.output','rightBlinkCenter_MD.input1X',f=1)   
        cmds.delete('faceBlendBLS_eyeRightBlinkDN')       
        cmds.setDrivenKeyframe('faceBlendBLS.eyeRightBlinkUP', cd = 'rightBlinkCenter_MD.input1X', v = 0, dv = 11, itt = "linear", ott="linear")
        cmds.setDrivenKeyframe('faceBlendBLS.eyeRightBlinkUP', cd = 'rightBlinkCenter_MD.input1X', v = 1, dv = 20, itt = "linear", ott="linear")
        cmds.setDrivenKeyframe('faceBlendBLS.eyeRightBlinkDN', cd = 'rightBlinkCenter_MD.input1X', v = 0, dv = 20, itt = "linear", ott="linear")
        cmds.setDrivenKeyframe('faceBlendBLS.eyeRightBlinkDN', cd = 'rightBlinkCenter_MD.input1X', v = 1, dv = 11, itt = "linear", ott="linear")
        cmds.setDrivenKeyframe('faceBlendBLS.eyeRightBlinkDN', cd = 'rightBlinkCenter_MD.input1X', v = 0, dv = 1, itt = "linear", ott="linear")
    
    if cmds.objExists('faceBlendBLS.upperLidLeftDN'):
        cmds.setDrivenKeyframe('faceBlendBLS.upperLidLeftDN', cd = 'L_face_picker_eye_null.upperLid', v = 0, dv = 0, itt = "linear", ott="linear")
        cmds.setDrivenKeyframe('faceBlendBLS.upperLidLeftDN', cd = 'L_face_picker_eye_null.upperLid', v = 1, dv = 10, itt = "linear", ott="linear")
    
    if cmds.objExists('faceBlendBLS.upperLidLeftUP'):
        cmds.setDrivenKeyframe('faceBlendBLS.upperLidLeftUP', cd = 'L_face_picker_eye_null.upperLid', v = 0, dv = 0, itt = "linear", ott="linear")
        cmds.setDrivenKeyframe('faceBlendBLS.upperLidLeftUP', cd = 'L_face_picker_eye_null.upperLid', v = 1, dv = -10, itt = "linear", ott="linear")
    
    if cmds.objExists('faceBlendBLS.lowerLidLeftDN'):
        cmds.setDrivenKeyframe('faceBlendBLS.lowerLidLeftDN', cd = 'L_face_picker_eye_null.lowerLid', v = 0, dv = 0, itt = "linear", ott="linear")
        cmds.setDrivenKeyframe('faceBlendBLS.lowerLidLeftDN', cd = 'L_face_picker_eye_null.lowerLid', v = 1, dv = -25, itt = "linear", ott="linear")
    
    if cmds.objExists('faceBlendBLS.lowerLidLeftUP'):
        cmds.setDrivenKeyframe('faceBlendBLS.lowerLidLeftUP', cd = 'L_face_picker_eye_null.lowerLid', v = 0, dv = 0, itt = "linear", ott="linear")
        cmds.setDrivenKeyframe('faceBlendBLS.lowerLidLeftUP', cd = 'L_face_picker_eye_null.lowerLid', v = 1, dv = 10, itt = "linear", ott="linear")
    
    if cmds.objExists('faceBlendBLS.upperLidRightDN'):
        cmds.setDrivenKeyframe('faceBlendBLS.upperLidRightDN', cd = 'R_face_picker_eye_null.upperLid', v = 0, dv = 0, itt = "linear", ott="linear")
        cmds.setDrivenKeyframe('faceBlendBLS.upperLidRightDN', cd = 'R_face_picker_eye_null.upperLid', v = 1, dv = 10, itt = "linear", ott="linear")
    
    if cmds.objExists('faceBlendBLS.upperLidRightUP'):
        cmds.setDrivenKeyframe('faceBlendBLS.upperLidRightUP', cd = 'R_face_picker_eye_null.upperLid', v = 0, dv = 0, itt = "linear", ott="linear")
        cmds.setDrivenKeyframe('faceBlendBLS.upperLidRightUP', cd = 'R_face_picker_eye_null.upperLid', v = 1, dv = -10, itt = "linear", ott="linear")
    
    if cmds.objExists('faceBlendBLS.lowerLidRightDN'):
        cmds.setDrivenKeyframe('faceBlendBLS.lowerLidRightDN', cd = 'R_face_picker_eye_null.lowerLid', v = 0, dv = 0, itt = "linear", ott="linear")
        cmds.setDrivenKeyframe('faceBlendBLS.lowerLidRightDN', cd = 'R_face_picker_eye_null.lowerLid', v = 1, dv = -25, itt = "linear", ott="linear")
    
    if cmds.objExists('faceBlendBLS.lowerLidRightUP'):
        cmds.setDrivenKeyframe('faceBlendBLS.lowerLidRightUP', cd = 'R_face_picker_eye_null.lowerLid', v = 0, dv = 0, itt = "linear", ott="linear")
        cmds.setDrivenKeyframe('faceBlendBLS.lowerLidRightUP', cd = 'R_face_picker_eye_null.lowerLid', v = 1, dv = 10, itt = "linear", ott="linear")
    
    if cmds.objExists('faceBlendBLS.eyeLeftSideLSpherical'):
        cmds.setDrivenKeyframe('faceBlendBLS.eyeLeftSideLSpherical', cd = 'L_eyeLid_1_ctrl.roundness', v = 0, dv = 0, itt = "linear", ott="linear")
        cmds.setDrivenKeyframe('faceBlendBLS.eyeLeftSideLSpherical', cd = 'L_eyeLid_1_ctrl.roundness', v = 1, dv = 10, itt = "linear", ott="linear")
    
    if cmds.objExists('faceBlendBLS.eyeLeftSideRSpherical'):
        cmds.setDrivenKeyframe('faceBlendBLS.eyeLeftSideRSpherical', cd = 'L_eyeLid_5_ctrl.roundness', v = 0, dv = 0, itt = "linear", ott="linear")
        cmds.setDrivenKeyframe('faceBlendBLS.eyeLeftSideRSpherical', cd = 'L_eyeLid_5_ctrl.roundness', v = 1, dv = 10, itt = "linear", ott="linear")
        
    if cmds.objExists('faceBlendBLS.eyeRightSideLSpherical'):
        cmds.setDrivenKeyframe('faceBlendBLS.eyeRightSideLSpherical', cd = 'R_eyeLid_1_ctrl.roundness', v = 0, dv = 0, itt = "linear", ott="linear")
        cmds.setDrivenKeyframe('faceBlendBLS.eyeRightSideLSpherical', cd = 'R_eyeLid_1_ctrl.roundness', v = 1, dv = 10, itt = "linear", ott="linear")
    
    if cmds.objExists('faceBlendBLS.eyeRightSideRSpherical'):
        cmds.setDrivenKeyframe('faceBlendBLS.eyeRightSideRSpherical', cd = 'R_eyeLid_5_ctrl.roundness', v = 0, dv = 0, itt = "linear", ott="linear")
        cmds.setDrivenKeyframe('faceBlendBLS.eyeRightSideRSpherical', cd = 'R_eyeLid_5_ctrl.roundness', v = 1, dv = 10, itt = "linear", ott="linear")
    
    if cmds.objExists('faceBlendBLS.mouthLeftBend'):
        cmds.setDrivenKeyframe('faceBlendBLS.mouthLeftBend', cd = 'toony_jaw_ctrl.tx', v = 0, dv = 0, itt = "linear", ott="linear")
        cmds.setDrivenKeyframe('faceBlendBLS.mouthLeftBend', cd = 'toony_jaw_ctrl.tx', v = 1, dv = 1, itt = "linear", ott="linear")
    
    if cmds.objExists('faceBlendBLS.mouthRightBend'):
        cmds.setDrivenKeyframe('faceBlendBLS.mouthRightBend', cd = 'toony_jaw_ctrl.tx', v = 0, dv = 0, itt = "linear", ott="linear")
        cmds.setDrivenKeyframe('faceBlendBLS.mouthRightBend', cd = 'toony_jaw_ctrl.tx', v = 1, dv = -1, itt = "linear", ott="linear")
    
    if cmds.objExists('faceBlendBLS.mouthFrontBend'):
        cmds.setDrivenKeyframe('faceBlendBLS.mouthFrontBend', cd = 'toony_jaw_ctrl.tz', v = 0, dv = 0, itt = "linear", ott="linear")
        cmds.setDrivenKeyframe('faceBlendBLS.mouthFrontBend', cd = 'toony_jaw_ctrl.tz', v = 1, dv = 1, itt = "linear", ott="linear")
    
    if cmds.objExists('faceBlendBLS.mouthBackBend'):
        cmds.setDrivenKeyframe('faceBlendBLS.mouthBackBend', cd = 'toony_jaw_ctrl.tz', v = 0, dv = 0, itt = "linear", ott="linear")
        cmds.setDrivenKeyframe('faceBlendBLS.mouthBackBend', cd = 'toony_jaw_ctrl.tz', v = 1, dv = -1, itt = "linear", ott="linear")
    
    if cmds.objExists('faceBlendBLS.mouthStretch'):
        cmds.setDrivenKeyframe('faceBlendBLS.mouthStretch', cd = 'toony_jaw_ctrl.ty', v = 0, dv = 0, itt = "linear", ott="linear")
        cmds.setDrivenKeyframe('faceBlendBLS.mouthStretch', cd = 'toony_jaw_ctrl.ty', v = 1, dv = -1, itt = "linear", ott="linear")
    
    if cmds.objExists('faceBlendBLS.mouthSquash'):
        cmds.setDrivenKeyframe('faceBlendBLS.mouthSquash', cd = 'toony_jaw_ctrl.ty', v = 0, dv = 0, itt = "linear", ott="linear")
        cmds.setDrivenKeyframe('faceBlendBLS.mouthSquash', cd = 'toony_jaw_ctrl.ty', v = 1, dv = 1, itt = "linear", ott="linear")
#####################################################################################
def ExtrapCorrectivesWindow() :
    if cmds.window('extractCorrectivesWin', exists=True):
        cmds.deleteUI('extractCorrectivesWin')
        
    cmds.window('extractCorrectivesWin' ,title='Extract Correctives', widthHeight=(252, 300),s=1)
    cmds.columnLayout ('extMaincolumnLayout',adjustableColumn=True)
    cmds.separator(height=5)
    cmds.frameLayout('transFrameLayout', label='BlendMeshes', w=250, h=100 )
    cmds.textScrollList('blendsList' ,numberOfRows=5, allowMultiSelection=True)
    cmds.setParent( '..' )
    cmds.button ('loadTransBtn', l='>>', c=loadBlendShapes)
    
    cmds.separator(h=10,w=10,style='in')
    cmds.textFieldButtonGrp('neutralObj',l='Load Neutral Mesh',tx='',bl='<<<<',bc='neutralGeo()')  
    cmds.separator(h=10,w=10,style='in')  
    
    cmds.separator(h=10,w=10,style='in')
    cmds.textFieldButtonGrp('comboObj',l='Load Combo Shape',tx='',bl='<<<<',bc='comboTarget()')  
    cmds.separator(h=10,w=10,style='in')          
    
    cmds.separator( height=5, style='none')
    cmds.button ('extractBtn',height=30 ,l='Extract Delta', c=extract)
    cmds.separator(height=10)
    
    cmds.showWindow('extractCorrectivesWin')
    
# load blendShapes in text field
def loadBlendShapes(*args) :
    cmds.textScrollList ('blendsList', e=1, ra=1)
    selection = cmds.ls(sl=1)
    if len(selection) >> 0 :       
        for eachTrans in selection :
            cmds.textScrollList ('blendsList', e=1, a=eachTrans)
            
def neutralGeo(*args):
    obj=cmds.ls(sl=1)
    cmds.textFieldButtonGrp('neutralObj',e=1,tx=obj[0])
    
def comboTarget(*args):
    obj=cmds.ls(sl=1)
    cmds.textFieldButtonGrp('comboObj',e=1,tx=obj[0])

"""
EXEMPLE:
import maya.cmds as cmds
 
import sys
 
rigDir = "/user_data/Proto/SRRRE/deltaEX"
sys.path.append(rigDir)
 
import deltaExtract as dExt
shapeList = ["A","B","C","D","E"]
 
dExt.extractDeltas(shapeList, neutralMesh, comboMesh)
"""
def extract(*args):
    shapeList = cmds.textScrollList ("blendsList", q=1, allItems=1)
    neutralMesh = cmds.textFieldButtonGrp('neutralObj',q=1,tx=True)
    comboMesh = cmds.textFieldButtonGrp('comboObj',q=1,tx=True) 
    extractDeltas(shapeList, neutralMesh, comboMesh)

def extractDeltas(shapeList, neutralMesh, comboMesh):
    """function create 1 mesh based on substraction of the shapes on the comboMesh deltas .
          
    params:
        shapeList: list of all the shapes (order does not matter)
        neutralMesh: neutral or base mesh which will be duplicate to create the _delta_mesh
        comboMesh: mesh that should be the combination reference of the firstMesh and secondMesh result
    returns:
        geometry: mesh
  
    """    
    getPoints = lambda mesh: np.array(map(
            lambda x:
            x * MMatrix(cmds.xform(mesh, m=True, q=True)).inverse(),
            rdMesh.getFn(mesh).getPoints(MSpace.kWorld))
            )
      
    neutralVtxPos = getPoints(neutralMesh)
    comboDelta  = neutralVtxPos - getPoints(comboMesh)
    shapesDelta = sum([(neutralVtxPos - getPoints(a)) for a in shapeList])
 
    fullDelta = neutralVtxPos - (comboDelta - shapesDelta)
 
    geo = cmds.duplicate(neutralMesh, n="{}_delta_mesh".format(comboMesh))[0]
  
    PointCloud = []
    for a in fullDelta:
        PointCloud.append(MPoint(a))
    moveObjectVerticesToNewPositions(geo, PointCloud)  
  
def moveObjectVerticesToNewPositions(obj, positionValues):
    objSel = MGlobal.getSelectionListByName(obj)
    dagPath = objSel.getDagPath(0)
    fnMesh = MFnMesh(dagPath)
    pointArray = MPointArray(positionValues)
    fnMesh.setPoints(pointArray)

DeformerKit()
#####################################################################################
## Last Updated :- 1st,June.2021
## Author :- Ankit Singh
## Copyright :- Only for Official Use
#####################################################################################
