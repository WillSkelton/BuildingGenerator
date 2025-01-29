import bpy # type: ignore
import sys

BLOCK_HEIGHT   = 4 # mm
CITY_BLOCK     = 24 # mm
BASE_TOLERANCE = 0.15 # mm
BLOCK_WIDTH    = CITY_BLOCK - BASE_TOLERANCE
BLOCK_HEIGHT   = 4 # mm
BUILDING_APOTHEM = 10 # mm


SimpleCityBlock = {
  "vertexList": [
    # Bottom face
    (0,           0,           0), 
    (BLOCK_WIDTH, 0,           0),
    (BLOCK_WIDTH, BLOCK_WIDTH, 0), 
    (0,           BLOCK_WIDTH, 0), 
    # Top face
    (0,           0,           BLOCK_HEIGHT), 
    (BLOCK_WIDTH, 0,           BLOCK_HEIGHT), 
    (BLOCK_WIDTH, BLOCK_WIDTH, BLOCK_HEIGHT), 
    (0,           BLOCK_WIDTH, BLOCK_HEIGHT) 
  ],
   # Define edges (for reference, but we're focusing on faces)
  "edgeList": [
      (0, 1), (1, 2), (2, 3), (3, 0),  # Bottom face
      (4, 5), (5, 6), (6, 7), (7, 4),  # Top face
      (0, 4), (1, 5), (2, 6), (3, 7)   # Vertical edges
  ],
   # Define faces
  "faceList": [
      (0, 1, 2, 3),  # Bottom face
      (4, 5, 6, 7),  # Top face
      (0, 1, 5, 4),  # Front face
      (1, 2, 6, 5),  # Right face
      (2, 3, 7, 6),  # Back face
      (3, 0, 4, 7)   # Left face
  ]
}



PlainBuilding = {
   "vertexList": [
    # Bottom face of base
    (0,           0,           0), # 0
    (BLOCK_WIDTH, 0,           0), # 1
    (BLOCK_WIDTH, BLOCK_WIDTH, 0), # 2
    (0,           BLOCK_WIDTH, 0), # 3
    # Top face of base
    (0,           0,           BLOCK_HEIGHT), # 4
    (BLOCK_WIDTH, 0,           BLOCK_HEIGHT), # 5
    (BLOCK_WIDTH, BLOCK_WIDTH, BLOCK_HEIGHT), # 6
    (0,           BLOCK_WIDTH, BLOCK_HEIGHT), # 7
    # Bottom face of building,
    ((BLOCK_WIDTH/2)+BUILDING_APOTHEM, (BLOCK_WIDTH/2)+BUILDING_APOTHEM, BLOCK_HEIGHT), # 8
    ((BLOCK_WIDTH/2)-BUILDING_APOTHEM, (BLOCK_WIDTH/2)+BUILDING_APOTHEM, BLOCK_HEIGHT), # 9
    ((BLOCK_WIDTH/2)-BUILDING_APOTHEM, (BLOCK_WIDTH/2)-BUILDING_APOTHEM, BLOCK_HEIGHT), # 10
    ((BLOCK_WIDTH/2)+BUILDING_APOTHEM, (BLOCK_WIDTH/2)-BUILDING_APOTHEM, BLOCK_HEIGHT), # 11
    # Top face of building,
    ((BLOCK_WIDTH/2)+BUILDING_APOTHEM, (BLOCK_WIDTH/2)+BUILDING_APOTHEM, BLOCK_HEIGHT+50), # 12
    ((BLOCK_WIDTH/2)-BUILDING_APOTHEM, (BLOCK_WIDTH/2)+BUILDING_APOTHEM, BLOCK_HEIGHT+50), # 13
    ((BLOCK_WIDTH/2)-BUILDING_APOTHEM, (BLOCK_WIDTH/2)-BUILDING_APOTHEM, BLOCK_HEIGHT+50), # 14
    ((BLOCK_WIDTH/2)+BUILDING_APOTHEM, (BLOCK_WIDTH/2)-BUILDING_APOTHEM, BLOCK_HEIGHT+50), # 15
  ],
   # Define edges (for reference, but we're focusing on faces)
  "edgeList": [
      (0, 1), (1, 2), (2, 3), (3, 0),  # Bottom face
      (4, 5), (5, 6), (6, 7), (7, 4),  # Top face
      (0, 4), (1, 5), (2, 6), (3, 7),   # Vertical edges

      (8, 9), (9, 10), (10, 11), (11, 8),     # Bottom face of building
      (12, 13), (13, 14), (14, 15), (15, 12), # Top face of building
      (8, 12), (9, 13), (10, 14), (11, 15)    # Vertical edges of building
  ],
   # Define faces
  "faceList": [
      (0, 1, 2, 3), # Bottom face
      (4, 5, 6, 7), # Top face
      (0, 1, 5, 4), # Front face
      (1, 2, 6, 5), # Right face
      (2, 3, 7, 6), # Back face
      (3, 0, 4, 7), # Left face
      (8, 9, 10, 11),   # Bottom face
      (12, 13, 14, 15), # Top face
      (8, 9, 13, 12),   # Front face
      (9, 10, 14, 13),  # Right face
      (10, 11, 15, 14), # Back face
      (11, 8, 12, 15)   # Left face
  ]
}

def clearObjects():
  # Delete all existing objects (including the default cube)
  bpy.ops.object.select_all(action='SELECT')
  bpy.ops.object.delete()

def generateFiles(outputPath:str,modelName:str):
  # Set Blender to use millimeters
  bpy.context.scene.unit_settings.system = 'METRIC'
  bpy.context.scene.unit_settings.scale_length = 0.001  # 1 Blender unit = 1 mm

  clearObjects()  

  # Create a new mesh and object
  meshData = bpy.data.meshes.new("building")
  meshData.from_pydata(
    PlainBuilding["vertexList"], 
    PlainBuilding["edgeList"], 
    PlainBuilding["faceList"]
  ) # Now including faces
  meshData.update()

  objectData = bpy.data.objects.new("building", meshData)
  bpy.context.collection.objects.link(objectData)

  # Ensure the object is active and in object mode
  bpy.context.view_layer.objects.active = objectData
  bpy.ops.object.mode_set(mode='OBJECT')
  

  # Export as STL
  bpy.ops.wm.stl_export(filepath=f"{outputPath}/{modelName}.stl")
  # And also .blend so I can inspect it if I need to
  bpy.ops.wm.save_as_mainfile(filepath=f"{outputPath}/{modelName}.blend")


generateFiles("./models", "rectangle")

