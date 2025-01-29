import bpy # type: ignore
import sys

BLOCK_HEIGHT   = 4 # mm
CITY_BLOCK     = 24 # mm
BASE_TOLERANCE = 0.15 # mm
BLOCK_WIDTH    = CITY_BLOCK - BASE_TOLERANCE
BLOCK_HEIGHT   = 4 # mm

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
    (0, BLOCK_WIDTH,           BLOCK_HEIGHT) 
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
  meshData = bpy.data.meshes.new("RectangularPrism")
  meshData.from_pydata(
    SimpleCityBlock["vertexList"], 
    SimpleCityBlock["edgeList"], 
    SimpleCityBlock["faceList"]
  ) # Now including faces
  meshData.update()

  objectData = bpy.data.objects.new("RectangularPrism", meshData)
  bpy.context.collection.objects.link(objectData)

  # Ensure the object is active and in object mode
  bpy.context.view_layer.objects.active = objectData
  bpy.ops.object.mode_set(mode='OBJECT')

  # Export as STL
  # bpy.ops.export_mesh.stl(filepath=bpy.path.abspath("//rectangularPrism.stl"))
  bpy.ops.wm.stl_export(filepath=f"{outputPath}/{modelName}.stl")
  bpy.ops.wm.save_as_mainfile(filepath=f"{outputPath}/{modelName}.blend")


generateFiles("./models", "rectangle")

