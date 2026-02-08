import maya.cmds as cmds

def constrain_locator_to_vertex():
    sel = cmds.ls(selection=True, flatten=True)

    if len(sel) != 2:
        cmds.error("Select a single vertex and a locator.")

    # Identify selected objects
    vertex = [s for s in sel if ".vtx[" in s]
    locator = [s for s in sel if ".vtx[" not in s]

    if not vertex or not locator:
        cmds.error("Selection must include one vertex and one locator.")

    vertex = vertex[0]
    locator = locator[0]
    
    # Get mesh and vertex index
    mesh = vertex.split(".vtx")[0]
    vertex_index = int(vertex.split("[")[-1][:-1])
    
    # Get world position of the vertex
    pos = cmds.pointPosition(vertex, world=True)
    
    # Create follicle
    follicle_shape = cmds.createNode("follicle")
    follicle_transform = cmds.listRelatives(follicle_shape, parent=True)[0]
    
    # Connect mesh to follicle
    cmds.connectAttr(f"{mesh}.outMesh", f"{follicle_shape}.inputMesh", force=True)
    cmds.connectAttr(f"{mesh}.worldMatrix[0]", f"{follicle_shape}.inputWorldMatrix", force=True)
    cmds.connectAttr(f"{follicle_shape}.outTranslate", f"{follicle_transform}.translate", force=True)
    cmds.connectAttr(f"{follicle_shape}.outRotate", f"{follicle_transform}.rotate", force=True)

    # Move follicle close to vertex position by converting world to UV (approximate)
    uvs = cmds.polyListComponentConversion(vertex, fromVertex=True, toUV=True)
    uvs = cmds.filterExpand(uvs, selectionMask=35, expand=True)
    if not uvs:
        cmds.error("Could not find UV for vertex.")
    
    uv = cmds.polyEditUV(uvs[0], query=True)
    cmds.setAttr(f"{follicle_shape}.parameterU", uv[0])
    cmds.setAttr(f"{follicle_shape}.parameterV", uv[1])

    # Parent or constrain the locator to the follicle
    cmds.parent(locator, follicle_transform)

    print(f"Locator '{locator}' is now constrained to vertex {vertex_index} on '{mesh}' via follicle.")

# Run the function
constrain_locator_to_vertex()
