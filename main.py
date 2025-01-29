import bpy # type: ignore
import sys


def generateFiles(modelName:str):
  # Set Blender to use millimeters
  bpy.context.scene.unit_settings.system = 'METRIC'
  bpy.context.scene.unit_settings.scale_length = 0.001  # 1 Blender unit = 1 mm

  # Delete all existing objects (including the default cube)
  bpy.ops.object.select_all(action='SELECT')
  bpy.ops.object.delete()

  # Define vertices in millimeters
  vertexList = [
      (0, 0, 0), (5, 0, 0), (5, 5, 0), (0, 5, 0),  # Bottom face
      (0, 0, 8), (5, 0, 8), (5, 5, 8), (0, 5, 8)   # Top face
  ]

  # Define edges (for reference, but we're focusing on faces)
  edgeList = [
      (0, 1), (1, 2), (2, 3), (3, 0),  # Bottom face
      (4, 5), (5, 6), (6, 7), (7, 4),  # Top face
      (0, 4), (1, 5), (2, 6), (3, 7)   # Vertical edges
  ]

  # Define faces
  faceList = [
      (0, 1, 2, 3),  # Bottom face
      (4, 5, 6, 7),  # Top face
      (0, 1, 5, 4),  # Front face
      (1, 2, 6, 5),  # Right face
      (2, 3, 7, 6),  # Back face
      (3, 0, 4, 7)   # Left face
  ]

  # Create a new mesh and object
  meshData = bpy.data.meshes.new("RectangularPrism")
  meshData.from_pydata(vertexList, edgeList, faceList)  # Now including faces
  meshData.update()

  objectData = bpy.data.objects.new("RectangularPrism", meshData)
  bpy.context.collection.objects.link(objectData)

  # Ensure the object is active and in object mode
  bpy.context.view_layer.objects.active = objectData
  bpy.ops.object.mode_set(mode='OBJECT')

  # Export as STL
  # bpy.ops.export_mesh.stl(filepath=bpy.path.abspath("//rectangularPrism.stl"))
  bpy.ops.wm.stl_export(filepath=f"./{modelName}.stl")
  bpy.ops.wm.save_as_mainfile(filepath=f"./{modelName}.blend")


generateFiles("rectangle")

