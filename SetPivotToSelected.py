bl_info = {
    "name": "My Blender Plugin",
    "description": "A brief description of my plugin",
    "author": "Jeroen Gorissen",
    "version": (1, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Tools",
    "category": "Object"
}

import bpy

# Define custom operator
class MyOperator(bpy.types.Operator):
    bl_idname = "object.my_operator"
    bl_label = "My Operator"

    def execute(self, context):
        # Your operator code here
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        return {'FINISHED'}

# Define custom panel
class MyPanel(bpy.types.Panel):
    bl_label = "My Panel"
    bl_idname = "OBJECT_PT_my_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'My Addon'

    def draw(self, context):
        layout = self.layout
        layout.operator("object.my_operator", text="Set pivot to selected")

# Register and unregister functions
def register():
    bpy.utils.register_class(MyOperator)
    bpy.utils.register_class(MyPanel)

def unregister():
    bpy.utils.unregister_class(MyOperator)
    bpy.utils.unregister_class(MyPanel)

# Allow running as a script
if __name__ == "__main__":
    register()
