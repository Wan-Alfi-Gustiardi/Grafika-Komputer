import numpy as np
from OpenGL.GL import *
import ctypes
from meshes.bed import Bed
from PIL import Image

class BedModel:
    def __init__(self):
        self.get_bed_model()
        self.VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBufferData(GL_ARRAY_BUFFER, self.bed_vertices.nbytes, self.bed_vertices, GL_STATIC_DRAW)
        self.texture = self.load_texture("textures\\CRATE.jpeg")

        self.EBO = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.EBO)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.bed_indices.nbytes, self.bed_indices, GL_STATIC_DRAW)

        self.setup_vertex_attributes()

    def load_texture(self, path):
        texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        image = Image.open(path)
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
        img_data = image.convert("RGBA").tobytes()
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)

        return texture


    def get_bed_model(self):
        frame_vertices, frame_indices = Bed.get_frame_data()
        mattress_vertices, mattress_indices = Bed.get_mattress_data()
        first_pillow_vertices, first_pillow_indices = Bed.get_first_pillow_data()
        second_pillow_vertices, second_pillow_indices = Bed.get_second_pillow_data()
        blanket_vertices, blanket_indices = Bed.get_blanket_data()
        back_side_blanket_vertices, back_side_blanket_indices = Bed.get_back_side_blanket_data()

        mattress_indices = mattress_indices + int(len(frame_vertices) / 6)

        total_length = len(frame_vertices) + len(mattress_vertices)
        first_pillow_indices = first_pillow_indices + int(total_length / 6)

        total_length = total_length + len(first_pillow_vertices)
        second_pillow_indices = second_pillow_indices + int(total_length / 6)

        total_length = total_length + len(second_pillow_vertices)
        blanket_indices = blanket_indices + int(total_length / 6)

        total_length = total_length + len(blanket_vertices)
        back_side_blanket_indices = back_side_blanket_indices + int(total_length / 6)
        
        self.bed_vertices = np.concatenate([frame_vertices, mattress_vertices, first_pillow_vertices, second_pillow_vertices, blanket_vertices, back_side_blanket_vertices])
        self.bed_indices = np.concatenate([frame_indices, mattress_indices, first_pillow_indices, second_pillow_indices, blanket_indices, back_side_blanket_indices])
        self.texture_coordinates = np.concatenate([frame_vertices])


        return self.bed_vertices, self.bed_indices, self.texture_coordinates

    def setup_vertex_attributes(self):
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))

        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(20))

        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, self.bed_vertices.itemsize * 8, ctypes.c_void_p(20))


    def draw(self):
        glBindTexture(GL_TEXTURE_2D, self.texture) 
        glDrawElements(GL_TRIANGLES, len(self.bed_indices), GL_UNSIGNED_INT, None)
