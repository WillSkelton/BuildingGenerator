import bpy  # type: ignore
import PlainBuilding
import Building


def clearObjects():
    # Delete all existing objects (including the default cube)
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()


def generateFiles(outputPath: str, modelName: str):
    # Set Blender to use millimeters
    bpy.context.scene.unit_settings.system = 'METRIC'
    bpy.context.scene.unit_settings.scale_length = 0.001  # 1 Blender unit = 1 mm

    clearObjects()

    # Create a new mesh and object
    meshData = bpy.data.meshes.new("building")
    meshData.from_pydata(
        PlainBuilding.Model["vertexList"],
        PlainBuilding.Model["edgeList"],
        PlainBuilding.Model["faceList"]
    )  # Now including Model
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


# generateFiles("./models", "rectangle")


b = Building.Building()
b.printMatrix()
b.addPoint((1, 2, 3))
b.printMatrix()
