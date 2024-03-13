import bpy

bl_info = {
    "name": "Pivot tools",
    "description": "Quickly set the pivot of your object to whatever you have selected in edit mode",
    "author": "Jeroen Gorissen",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Tools",
    "category": "Object"
}

# Define custom operator
class OBJECT_OT_MyOperator(bpy.types.Operator):
    bl_idname = "object.my_operator"
    bl_label = "My Operator"

    def execute(self, context):
        # Your operator code here
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        return {'FINISHED'}

# Define custom panel
class OBJECT_PT_MyPanel(bpy.types.Panel):
    bl_label = "Pivot tools"
    bl_idname = "OBJECT_PT_pivot_tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Pivot tools'

    def draw(self, context):
        layout = self.layout
        layout.operator("object.my_operator", text="Set pivot to selected")

# Register and unregister functions
def register():
    bpy.utils.register_class(OBJECT_OT_MyOperator)
    bpy.utils.register_class(OBJECT_PT_MyPanel)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_MyOperator)
    bpy.utils.unregister_class(OBJECT_PT_MyPanel)

# Allow running as a script
if __name__ == "__main__":
    register()
