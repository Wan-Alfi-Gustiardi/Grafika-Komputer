import numpy as np

floor_buffer = [
    1.0, 0.0, 1.0, 1.0, 0.0, -0.0, 1.0, -0.0, 
    -1.0, 0.0, -1.0, 0.0, 1.0, -0.0, 1.0, -0.0, 
    -1.0, 0.0, 1.0, 0.0, 0.0, -0.0, 1.0, -0.0, 
    1.0, 0.0, 1.0, 1.0, 0.0, -0.0, 1.0, -0.0, 
    1.0, 0.0, -1.0, 1.0, 1.0, -0.0, 1.0, -0.0, 
    -1.0, 0.0, -1.0, 0.0, 1.0, -0.0, 1.0, -0.0
]

floor_indices = [
    1, 2, 0, 
    1, 3, 2
]

floor_buffer = np.array(floor_buffer, dtype=np.float32)
floor_indices = np.array(floor_indices, dtype=np.uint32)