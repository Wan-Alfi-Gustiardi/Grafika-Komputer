import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '400, 200'

import glfw
from OpenGL.GL import *
import numpy as np
from window import Window
from shader import Shader
from model.lamp_model import LampModel
from model.bed_model import BedModel
from model.nakas_model import NakasModel
from model.cupboard_model import CupboardModel
import pygame
import numpy as np
import pyrr

vertex_source = """
# version 330

layout(location = 0) in vec3 a_position;
layout(location = 1) in vec3 a_color;
layout(location = 2) in vec2 a_texture;  

uniform mat4 rotation;

out vec3 v_color;
out vec2 v_texture;  

void main()
{
    gl_Position = rotation * vec4(a_position, 1.0);
    v_color = a_color;
    v_texture = a_texture; 
}
"""

fragment_source = """
# version 330

in vec3 v_color;
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

window = Window(1280, 720, "3D World")
window.set_resize_callback(window_resize)

shader_program = Shader(vertex_source, fragment_source)
shader_program.use()

# bed_model = BedModel()
# bed_vertices, bed_indices, texture_coordinates = bed_model.get_bed_model()
# lamp_model = LampModel()
# nakas_model = NakasModel()
cupboard_model = CupboardModel()

glClearColor(0.2, 0.2, 0.2, 1)
glEnable(GL_DEPTH_TEST)

rotation_loc = glGetUniformLocation(shader_program.program, "rotation")
scale_factor = 2
scale_matrix = np.array([
    [scale_factor, 0.0, 0.0, 0.0],
    [0.0, scale_factor, 0.0, 0.0],
    [0.0, 0.0, scale_factor, 0.0],
    [0.0, 0.0, 0.0, 1.0]
], dtype=np.float32)

while not window.should_close():
    window.poll_events()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    time = glfw.get_time()

    rot_x = rot_x = np.array([
        [1.0, 0.0, 0.0, 0.0],
        [0.0, np.cos(0.5 * time), -np.sin(0.5 * time), 0.0],
        [0.0, np.sin(0.5 * time), np.cos(0.5 * time), 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ], dtype=np.float32)

    rot_y = np.array([
        [np.cos(0.8 * time), 0.0, np.sin(0.8 * time), 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [-np.sin(0.8 * time), 0.0, np.cos(0.8 * time), 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ], dtype=np.float32)

    # glActiveTexture(GL_TEXTURE0)
    # glBindTexture(GL_TEXTURE_2D, bed_model.texture)

    rotation_matrix = np.dot(rot_x, rot_y)

    rotation_matrix = np.dot(rot_x, rot_y)

    transform_matrix = np.dot(rotation_matrix, scale_matrix)

    glUniformMatrix4fv(rotation_loc, 1, GL_FALSE, transform_matrix)

    # bed_model.draw()
    # lamp_model.draw()
    # nakas_model.draw()
    cupboard_model.draw()

    window.swap_buffers()