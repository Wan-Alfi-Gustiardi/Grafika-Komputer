from OpenGL.GL import *

class Model:
    def __init__(self, vertices, indices, textures):
        self.VAO = glGenVertexArrays(1)
        self.VBO = glGenBuffers(1)
        self.indices_count = len(indices)

        glBindVertexArray(self.VAO)
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

        # Position attribute
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices.itemsize * 8, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)
        # Texture attribute
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, vertices.itemsize * 8, ctypes.c_void_p(12))
        glEnableVertexAttribArray(1)
        # Normal attribute
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, vertices.itemsize * 8, ctypes.c_void_p(20))
        glEnableVertexAttribArray(2)

        self.textures = textures

    def draw(self):
        glBindVertexArray(self.VAO)
        glDrawArrays(GL_TRIANGLES, 0, self.indices_count)