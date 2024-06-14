import glfw
from OpenGL.GL import *
from utils import *
from meshes import *
import math

cam = Camera()
WIDTH, HEIGHT = 1280, 720
lastX, lastY = WIDTH / 2, HEIGHT / 2
first_mouse = True
left, right, forward, backward = False, False, False, False

def key_input_clb(window, key, scancode, action, mode):
    global left, right, forward, backward
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, True)

    if key == glfw.KEY_W and action == glfw.PRESS:
        forward = True
    if key == glfw.KEY_S and action == glfw.PRESS:
        backward = True
    if key == glfw.KEY_A and action == glfw.PRESS:
        left = True
    if key == glfw.KEY_D and action == glfw.PRESS:
        right = True

    if key in [glfw.KEY_W, glfw.KEY_S, glfw.KEY_D, glfw.KEY_A] and action == glfw.RELEASE:
        left, right, forward, backward = False, False, False, False

def do_movement():
    if left:
        cam.process_keyboard("LEFT", 0.005)
    if right:
        cam.process_keyboard("RIGHT", 0.005)
    if forward:
        cam.process_keyboard("FORWARD", 0.005)
    if backward:
        cam.process_keyboard("BACKWARD", 0.005)

def mouse_look_clb(window, xpos, ypos):
    global first_mouse, lastX, lastY

    if first_mouse:
        lastX = xpos
        lastY = ypos
        first_mouse = False

    xoffset = xpos - lastX
    yoffset = lastY - ypos

    lastX = xpos
    lastY = ypos

    cam.process_mouse_movement(xoffset, yoffset)


vertex_src = """
# version 330

layout(location = 0) in vec3 a_position;
layout(location = 1) in vec2 a_texture;
layout(location = 2) in vec3 a_normal;

uniform mat4 model;
uniform mat4 projection;
uniform mat4 view;

out vec2 v_texture;
out vec3 v_normal;
out vec3 v_fragPos;

void main()
{
    gl_Position = projection * view * model * vec4(a_position, 1.0);
    v_texture = a_texture;
    v_normal = mat3(transpose(inverse(model))) * a_normal;
    v_fragPos = vec3(model * vec4(a_position, 1.0));
}

"""

fragment_src = """
# version 330

in vec2 v_texture;
in vec3 v_normal;
in vec3 v_fragPos;

out vec4 out_color;

uniform sampler2D s_texture;
uniform vec3 lightPos;
uniform vec3 viewPos;
uniform vec3 lightColor;
uniform vec3 objectColor;

void main()
{
    // Ambient
    float ambientStrength = 0.1;
    vec3 ambient = ambientStrength * lightColor;
    
    // Diffuse 
    vec3 norm = normalize(v_normal);
    vec3 lightDir = normalize(lightPos - v_fragPos);
    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = diff * lightColor;
    
    // Specular
    float specularStrength = 0.5;
    vec3 viewDir = normalize(viewPos - v_fragPos);
    vec3 reflectDir = reflect(-lightDir, norm);
    float spec = pow(max(dot(viewDir, reflectDir), 0.0), 32);
    vec3 specular = specularStrength * spec * lightColor;  
    
    vec3 result = (ambient + diffuse + specular) * objectColor * texture(s_texture, v_texture).rgb;
    out_color = vec4(result, 1.0);
}

"""

def window_resize(window, width, height):
    glViewport(0, 0, width, height)
    projection = create_perspective_projection_matrix(45, width / height, 0.1, 100)
    glUniformMatrix4fv(projection_loc, 1, GL_FALSE, projection)

window = Window(WIDTH, HEIGHT, "3D World")
window.set_resize_callback(window_resize)

window.set_cursor_pos_callback(mouse_look_clb)
window.set_key_callback(key_input_clb)
window.set_input_mode()

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

# Load Cupboard Textures
wardrobe_texture_id = glGenTextures(1)
load_texture("textures/wood-fine.png", wardrobe_texture_id)
door_texture_id = glGenTextures(1)
load_texture("textures/wood-fine.png", door_texture_id)
handle_texture_id = glGenTextures(1)
load_texture("textures/stainless-steel.png", handle_texture_id)

# Load Nightstand Textures
carcass_texture_id = glGenTextures(1)
load_texture("textures/wood-fine.png", carcass_texture_id)
drawers_texture_id = glGenTextures(1)
load_texture("textures/light-blue-wood.png", drawers_texture_id)
knobs_texture_id = glGenTextures(1)
load_texture("textures/stainless-steel.png", knobs_texture_id)

# Load Floor and Wall Textures
floor_texture_id = glGenTextures(1)
load_texture('textures/floor.png', floor_texture_id)
wall_texture_id = glGenTextures(1)
load_texture('textures/wall.png', wall_texture_id)

# Load Bed Model
frame_model = Model(frame_buffer, frame_indices, frame_texture_id)
mattress_model = Model(mattress_buffer, mattress_indices, mattress_texture_id)
first_pillow_model = Model(first_pillow_buffer, first_pillow_indices, first_pillow_texture_id)
second_pillow_model = Model(second_pillow_buffer, second_pillow_indices, second_pillow_texture_id)
blanket_model = Model(blanket_buffer, blanket_indices, blanket_texture_id)
back_side_blanket_model = Model(back_side_blanket_buffer, back_side_blanket_indices, back_side_blanket_texture_id)

# Load Cupboard Model
wardrobe_model = Model(wardrobe_buffer, wardrobe_indices, wardrobe_texture_id)
door_model = Model(door_buffer, door_indices, door_texture_id)
handle_model = Model(handle_buffer, handle_indices, handle_texture_id)

# Load Nightstand Model
carcass_model = Model(carcass_buffer, carcass_indices, carcass_texture_id)
drawers_model = Model(drawers_buffer, drawers_indices, drawers_texture_id)
knobs_model = Model(knobs_buffer, knobs_indices, knobs_texture_id)

# Load Floor and Wall Model
floor_model = Model(floor_buffer, floor_indices, floor_texture_id)
wall_model = Model(wall_buffer, wall_indices, wall_texture_id)

glClearColor(0.2, 0.2, 0.2, 1)
glEnable(GL_DEPTH_TEST)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

# Perpective Projection
projection = create_perspective_projection_matrix(45, WIDTH / HEIGHT, 0.1, 100)

# Bed Model Position
bed_position = Matrix44.translation_matrix(to_list((Vector3([0.6, 2.5, -1]))))

# Cupboard Model Position
cupboard_position = Matrix44.translation_matrix(to_list((Vector3([-0.8, 2.687, 0]))))

# Nightstand Model Position
nightstand_position = Matrix44.translation_matrix(to_list((Vector3([0, 8.49, -4.06]))))

# Floor and Wall Model Position
floor_and_wall_position = Matrix44.translation_matrix(to_list((Vector3([0.05, 1.795, -0.1]))))

# eye, target, up
# view = create_look_at([2, 2, 4], [0, 0, 0], [0, 1, 0])

model_loc = glGetUniformLocation(shader_program.program, "model")
projection_loc = glGetUniformLocation(shader_program.program, "projection")
view_loc = glGetUniformLocation(shader_program.program, "view")

glUniformMatrix4fv(projection_loc, 1, GL_FALSE, projection)
# glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)

# Light properties
light_pos = [1.0, 4.0, -1.0]
light_color = [1.0, 1.0, 1.0]
object_color = [1.0, 1.0, 1.0]

light_pos_loc = glGetUniformLocation(shader_program.program, "lightPos")
view_pos_loc = glGetUniformLocation(shader_program.program, "viewPos")
light_color_loc = glGetUniformLocation(shader_program.program, "lightColor")
object_color_loc = glGetUniformLocation(shader_program.program, "objectColor")

# Set the light and material properties
glUniform3fv(light_pos_loc, 1, light_pos)
glUniform3fv(light_color_loc, 1, light_color)
glUniform3fv(object_color_loc, 1, object_color)

# the main application loop
while not window.should_close():
    window.poll_events()
    do_movement()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    view = cam.get_view_matrix()
    glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)

    rot_y = rotation_matrix_y(90 * (math.pi / 180))

    scale_bed = matrix_multiply(bed_position, scale_matrix(1.4))
    model_bed = matrix_multiply(rot_y, scale_bed)
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model_bed)

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
    
    rot_y = rotation_matrix_y(-90 * (math.pi / 180))

    scale_cupboard = matrix_multiply(cupboard_position, scale_matrix(1.5))
    model_cupboard = matrix_multiply(rot_y, scale_cupboard)
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model_cupboard)

    # Draw Cupboard Model
    glBindTexture(GL_TEXTURE_2D, wardrobe_texture_id)
    wardrobe_model.draw()
    glBindTexture(GL_TEXTURE_2D, door_texture_id)
    door_model.draw()
    glBindTexture(GL_TEXTURE_2D, handle_texture_id)
    handle_model.draw()

    rot_y = rotation_matrix_y(90 * (math.pi / 180))

    scale_nightstand = matrix_multiply(nightstand_position, scale_matrix(0.4))
    model_nightstand = matrix_multiply(rot_y, scale_nightstand)
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model_nightstand)

    # Draw Nightstand Model
    glBindTexture(GL_TEXTURE_2D, carcass_texture_id)
    carcass_model.draw()
    glBindTexture(GL_TEXTURE_2D, drawers_texture_id)
    drawers_model.draw()
    glBindTexture(GL_TEXTURE_2D, knobs_texture_id)
    knobs_model.draw()

    scale_floor_and_wall = matrix_multiply(floor_and_wall_position, scale_matrix(1.8))
    model_floor_and_wall = matrix_multiply(rot_y, scale_floor_and_wall)
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model_floor_and_wall)

    # Draw Floor and Wall Model
    glBindTexture(GL_TEXTURE_2D, floor_texture_id)
    floor_model.draw()
    glBindTexture(GL_TEXTURE_2D, wall_texture_id)
    wall_model.draw()

    window.swap_buffers()