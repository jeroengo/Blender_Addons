import bpy
import os

bl_info = {
    "name": "Batch Export for Unity",
    "description": "This add-on allows you to export all selected objects with custom settings for Unity",
    "author": "Jeroen Gorissen",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Tools",
    "category": "Object"
}

# Define custom operator
class OBJECT_OT_UnityBatchExport(bpy.types.Operator):
    bl_idname = "object.unity_batch_export"
    bl_label = "Unity Batch Export"

    def execute(self, context):
        # Set the directory where you want to save the FBX files
        output_directory = context.scene.my_directory

        # Ensure the output directory exists
        os.makedirs(output_directory, exist_ok=True)

        # Get the selected objects
        selected_objects = context.selected_objects

        # Loop through each selected object and export as FBX
        for obj in selected_objects:
            # Deselect all objects
            bpy.ops.object.select_all(action='DESELECT')
            
            # Select the object to be exported
            obj.select_set(True)
            
            # Set the output FBX filename
            fbx_filename = obj.name + ".fbx"
            output_path = os.path.join(output_directory, fbx_filename)
            
            # Export the selected object as FBX
            bpy.ops.export_scene.fbx(filepath=output_path, use_selection=True, bake_space_transform=True)

            print("Exported:", fbx_filename)

        print("Batch export completed.")

        print(context.scene.my_directory)
        return {'FINISHED'}

# Define custom panel
class OBJECT_PT_UnityBatchExportPanel(bpy.types.Panel):
    bl_label = "Unity Batch Export"
    bl_idname = "OBJECT_PT_unity_batch_export_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'My Addon'

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene, "my_directory")
        layout.operator("object.unity_batch_export", text="Batch export for Unity")

# Register and unregister functions
def register():
    bpy.utils.register_class(OBJECT_OT_UnityBatchExport)
    bpy.utils.register_class(OBJECT_PT_UnityBatchExportPanel)
    bpy.types.Scene.my_directory = bpy.props.StringProperty(name="My Directory", subtype='DIR_PATH')

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_UnityBatchExport)
    bpy.utils.unregister_class(OBJECT_PT_UnityBatchExportPanel)
    del bpy.types.Scene.my_directory

# Allow running as a script
if __name__ == "__main__":
    register()
