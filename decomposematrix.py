############DecomposeMatrix for ctrl Double deformation################
######Naveen.M########

import maya.cmds as cmds

# Get the selected controller(s)
selected_controllers = cmds.ls(sl=True)

for controller in selected_controllers:
    # Check if the selected object is a transform (controller)
    if cmds.nodeType(controller) == 'transform':
        # Create a decomposeMatrix node
        decompose_node = cmds.shadingNode("decomposeMatrix", asUtility=True)
        decompose_node_name = cmds.rename(decompose_node, controller + "_DMAT")

        # Connect the controller's inverseMatrix to decomposeMatrix's inputMatrix
        cmds.connectAttr(controller + ".inverseMatrix", decompose_node_name + ".inputMatrix")

        # Get the top group (parent) of the controller
        top_group = cmds.listRelatives(controller, parent=True)

        # Connect decomposeMatrix's output to the top group's rotation, translation, and scale
        if top_group:
            top_group_name = top_group[0]  # Assuming there's only one parent
            cmds.connectAttr(decompose_node_name + ".outputRotate", top_group_name + ".rotate")
            cmds.connectAttr(decompose_node_name + ".outputTranslate", top_group_name + ".translate")
            cmds.connectAttr(decompose_node_name + ".outputScale", top_group_name + ".scale")
            print("Connected {} to {}.".format(controller, top_group_name))
        else:
            print("No parent group found for {}. Skipping.".format(controller))
    else:
        print("Selected object {} is not a transform (controller). Skipping.".format(controller))
