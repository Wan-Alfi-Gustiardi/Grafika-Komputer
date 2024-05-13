import numpy as np
from OpenGL.GL import *
import ctypes
from meshes.lamp import Lamp
from Textureloader import load_texture
from PIL import Image

class LampModel:
    def __init__(self):
        self.get_lamp_model()
        self.VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBufferData(GL_ARRAY_BUFFER, self.lamp_vertices.nbytes, self.lamp_vertices, GL_STATIC_DRAW)
        
        self.EBO = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.EBO)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.lamp_indices.nbytes, self.lamp_indices, GL_STATIC_DRAW)

        self.setup_vertex_attributes()
    
    def get_lamp_model(self):
        frame_vertices, frame_indices = Lamp.get_frame_data()
        
        base_vertices, base_indices = Lamp.get_base_data()

        base_indices = base_indices + int(len(frame_vertices) / 6)

        self.lamp_vertices = np.concatenate([frame_vertices, base_vertices])
        self.lamp_indices = np.concatenate([frame_indices, base_indices])
        self.texture_coordinates = np.concatenate([frame_vertices, base_vertices, frame_indices, base_indices])

        return self.lamp_vertices, self.lamp_indices, self.texture_coordinates

    def setup_vertex_attributes(self):
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))

        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, self.lamp_vertices.itemsize * 13, ctypes.c_void_p(24))

        texture = glGenTextures(1)
        frame_texture = load_texture ("textures\\Glass.jpeg", texture)

    def draw(self):
        glDrawElements(GL_TRIANGLES, len(self.lamp_indices), GL_UNSIGNED_INT, None)
