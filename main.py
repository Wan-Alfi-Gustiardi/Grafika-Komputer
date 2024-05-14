import glfw
from OpenGL.GL import *
from utils import *
from meshes import *

vertex_src = """
# version 330

layout(location = 0) in vec3 a_position;
layout(location = 1) in vec2 a_texture;
layout(location = 2) in vec3 a_normal;

uniform mat4 model;
uniform mat4 projection;
uniform mat4 view;

out vec2 v_texture;

void main()
{
    gl_Position = projection * view * model * vec4(a_position, 1.0);
    v_texture = a_texture;
}
"""

fragment_src = """
# version 330

in vec2 v_texture;

out vec4 out_color;

uniform sampler2D s_texture;

void main()
{
    out_color = texture(s_texture, v_texture);
}
"""

def window_resize(window, width, height):
    glViewport(0, 0, width, height)
    projection = create_perspective_projection_matrix(45, width / height, 0.1, 100)
    glUniformMatrix4fv(projection_loc, 1, GL_FALSE, projection)

window = Window(1280, 720, "3D World")
window.set_resize_callback(window_resize)

shader_program = Shader(vertex_src, fragment_src)
shader_program.use()

# Load Bed Textures
frame_texture_id = glGenTextures(1)
load_texture("textures/wood.png", frame_texture_id)
mattress_texture_id = glGenTextures(1)
load_texture("textures/fabric-base.png", mattress_texture_id)
first_pillow_texture_id = glGenTextures(1)
load_texture("textures/fabric-color.png", first_pillow_texture_id)
second_pillow_texture_id = glGenTextures(1)
load_texture("textures/fabric-color.png", second_pillow_texture_id)
blanket_texture_id = glGenTextures(1)
load_texture("textures/fleece-blue.png", blanket_texture_id)
back_side_blanket_texture_id = glGenTextures(1)
load_texture("textures/fleece-orange.png", back_side_blanket_texture_id)

# Load Lamp Textures
lamp_texture_id = glGenTextures(1)
load_texture("textures/glass.png", lamp_texture_id)
base_texture_id = glGenTextures(1)
load_texture("textures/rustic-wood-black.png", base_texture_id)

# Load Cupboard Textures
wardrobe_texture_id = glGenTextures(1)
load_texture("textures/wood-fine.png", wardrobe_texture_id)
door_texture_id = glGenTextures(1)
load_texture("textures/wood-fine.png", door_texture_id)
handle_texture_id = glGenTextures(1)
load_texture("textures/stainless-steel.png", handle_texture_id)

# Load Bed Model
frame_model = Model(frame_buffer, frame_indices, frame_texture_id)
mattress_model = Model(mattress_buffer, mattress_indices, mattress_texture_id)
first_pillow_model = Model(first_pillow_buffer, first_pillow_indices, first_pillow_texture_id)
second_pillow_model = Model(second_pillow_buffer, second_pillow_indices, second_pillow_texture_id)
blanket_model = Model(blanket_buffer, blanket_indices, blanket_texture_id)
back_side_blanket_model = Model(back_side_blanket_buffer, back_side_blanket_indices, back_side_blanket_texture_id)

# Load Lamp Model
lamp_model = Model(lamp_buffer, lamp_indices, lamp_texture_id)
base_model = Model(base_buffer, base_indices, base_texture_id)

# Load Cupboard Model
wardrobe_model = Model(wardrobe_buffer, wardrobe_indices, wardrobe_texture_id)
door_model = Model(door_buffer, door_indices, door_texture_id)
handle_model = Model(handle_buffer, handle_indices, handle_texture_id)

glClearColor(0.2, 0.2, 0.2, 1)
glEnable(GL_DEPTH_TEST)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

# Perpective Projection
projection = create_perspective_projection_matrix(45, 1280 / 720, 0.1, 100)

# Bed Model Position
bed_position = Matrix44.translation_matrix(to_list((Vector3([-0.2, 0, 1]))))

# Lamp Model Position
lamp_position = Matrix44.translation_matrix(to_list((Vector3([0.3, 0.4, 14]))))

# Cupboard Model Position
cupboard_position = Matrix44.translation_matrix(to_list((Vector3([0.6, 0.3, 0]))))

# eye, target, up
view = create_look_at([2, 2, 4], [0, 0, 0], [0, 1, 0])

model_loc = glGetUniformLocation(shader_program.program, "model")
projection_loc = glGetUniformLocation(shader_program.program, "projection")
view_loc = glGetUniformLocation(shader_program.program, "view")

glUniformMatrix4fv(projection_loc, 1, GL_FALSE, projection)
glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)

# the main application loop
while not window.should_close():
    window.poll_events()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    rot_y = rotation_matrix_y(0.8 * glfw.get_time())
    
    scale_bed = matrix_multiply(bed_position, scale_matrix(1.4))
    model_bed = matrix_multiply(rot_y, bed_position)
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, scale_bed)

    # Draw Bed Model
    glBindTexture(GL_TEXTURE_2D, frame_texture_id)
    frame_model.draw()
    glBindTexture(GL_TEXTURE_2D, mattress_texture_id)
    mattress_model.draw()
    glBindTexture(GL_TEXTURE_2D, first_pillow_texture_id)
    first_pillow_model.draw()
    glBindTexture(GL_TEXTURE_2D, second_pillow_texture_id)
    second_pillow_model.draw()
    glBindTexture(GL_TEXTURE_2D, blanket_texture_id)
    blanket_model.draw()
    glBindTexture(GL_TEXTURE_2D, back_side_blanket_texture_id)
    back_side_blanket_model.draw()

    scale_lamp = matrix_multiply(lamp_position, scale_matrix(0.19))
    model_lamp = matrix_multiply(rot_y, lamp_position)
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, scale_lamp)

    # Draw Lamp Model
    glBindTexture(GL_TEXTURE_2D, lamp_texture_id)
    lamp_model.draw()
    glBindTexture(GL_TEXTURE_2D, base_texture_id)
    base_model.draw()

    scale_cupboard = matrix_multiply(cupboard_position, scale_matrix(1.5))
    model_cupboard = matrix_multiply(rot_y, cupboard_position)
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, scale_cupboard)

    # Draw Cupboard Model
    glBindTexture(GL_TEXTURE_2D, wardrobe_texture_id)
    wardrobe_model.draw()
    glBindTexture(GL_TEXTURE_2D, door_texture_id)
    door_model.draw()
    glBindTexture(GL_TEXTURE_2D, handle_texture_id)
    handle_model.draw()

    window.swap_buffers()