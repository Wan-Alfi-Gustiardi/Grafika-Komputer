import numpy as np

handle_buffer = [
    0.068684, 0.073103, 0.054716, 0.763562, 0.415757, -0.0, -0.0, 1.0, 
    0.032995, -0.080626, 0.054716, 0.958835, 0.610079, -0.0, -0.0, 1.0, 
    0.068684, -0.080626, 0.054716, 0.764038, 0.610555, -0.0, -0.0, 1.0, 
    0.027938, 0.094884, 0.036135, 0.235895, 0.389445, -0.0, -0.0, -1.0, 
    0.073741, -0.102408, 0.036135, 0.486505, 0.638834, -0.0, -0.0, -1.0, 
    0.027938, -0.102408, 0.036135, 0.236506, 0.639445, -0.0, -0.0, -1.0, 
    0.027938, 0.094884, 0.036135, 0.485283, 0.138835, -0.0, 1.0, -0.0, 
    0.073741, 0.094884, 0.046675, 0.708293, 0.388291, -0.0, 1.0, -0.0, 
    0.073741, 0.094884, 0.036135, 0.485894, 0.388834, -0.0, 1.0, -0.0, 
    0.027938, 0.094884, 0.046675, 0.013496, 0.389989, -1.0, -0.0, -0.0, 
    0.027938, -0.102408, 0.036135, 0.236506, 0.639445, -1.0, -0.0, -0.0, 
    0.027938, -0.102408, 0.046675, 0.014107, 0.639988, -1.0, -0.0, -0.0, 
    0.073741, 0.094884, 0.036135, 0.485894, 0.388834, 1.0, -0.0, -0.0, 
    0.073741, -0.102408, 0.046675, 0.708904, 0.63829, 1.0, -0.0, -0.0, 
    0.073741, -0.102408, 0.036135, 0.486505, 0.638834, 1.0, -0.0, -0.0, 
    0.032995, -0.080626, 0.054716, 0.958835, 0.610079, -0.8465, -0.0, 0.5324, 
    0.027938, 0.094884, 0.046675, 0.985893, 0.387613, -0.8465, -0.0, 0.5324, 
    0.027938, -0.102408, 0.046675, 0.986504, 0.637612, -0.8465, -0.0, 0.5324, 
    0.068684, -0.080626, 0.054716, 0.764038, 0.610555, 0.8465, -0.0, 0.5324, 
    0.073741, 0.094884, 0.046675, 0.708293, 0.388291, 0.8465, -0.0, 0.5324, 
    0.068684, 0.073103, 0.054716, 0.763562, 0.415757, 0.8465, -0.0, 0.5324, 
    0.073741, -0.102408, 0.046675, 0.736504, 0.638223, -0.0, -0.3463, 0.9381, 
    0.032995, -0.080626, 0.054716, 0.958835, 0.610079, -0.0, -0.3463, 0.9381, 
    0.027938, -0.102408, 0.046675, 0.986504, 0.637612, -0.0, -0.3463, 0.9381, 
    0.027938, 0.094884, 0.046675, 0.985893, 0.387613, -0.0, 0.3463, 0.9381, 
    0.068684, 0.073103, 0.054716, 0.763562, 0.415757, -0.0, 0.3463, 0.9381, 
    0.073741, 0.094884, 0.046675, 0.735893, 0.388224, -0.0, 0.3463, 0.9381, 
    0.073741, -0.102408, 0.036135, 0.486505, 0.638834, -0.0, -1.0, -0.0, 
    0.027938, -0.102408, 0.046675, 0.709514, 0.88829, -0.0, -1.0, -0.0, 
    0.027938, -0.102408, 0.036135, 0.487116, 0.888833, -0.0, -1.0, -0.0, 
    0.068684, 0.073103, 0.054716, 0.763562, 0.415757, -0.0, -0.0, 1.0, 
    0.032995, 0.073103, 0.054716, 0.958359, 0.415281, -0.0, -0.0, 1.0, 
    0.032995, -0.080626, 0.054716, 0.958835, 0.610079, -0.0, -0.0, 1.0, 
    0.027938, 0.094884, 0.036135, 0.235895, 0.389445, -0.0, -0.0, -1.0, 
    0.073741, 0.094884, 0.036135, 0.485894, 0.388834, -0.0, -0.0, -1.0, 
    0.073741, -0.102408, 0.036135, 0.486505, 0.638834, -0.0, -0.0, -1.0, 
    0.027938, 0.094884, 0.036135, 0.485283, 0.138835, -0.0, 1.0, -0.0, 
    0.027938, 0.094884, 0.046675, 0.707682, 0.138292, -0.0, 1.0, -0.0, 
    0.073741, 0.094884, 0.046675, 0.708293, 0.388291, -0.0, 1.0, -0.0, 
    0.027938, 0.094884, 0.046675, 0.013496, 0.389989, -1.0, -0.0, -0.0, 
    0.027938, 0.094884, 0.036135, 0.235895, 0.389445, -1.0, -0.0, -0.0, 
    0.027938, -0.102408, 0.036135, 0.236506, 0.639445, -1.0, -0.0, -0.0, 
    0.073741, 0.094884, 0.036135, 0.485894, 0.388834, 1.0, -0.0, -0.0, 
    0.073741, 0.094884, 0.046675, 0.708293, 0.388291, 1.0, -0.0, -0.0, 
    0.073741, -0.102408, 0.046675, 0.708904, 0.63829, 1.0, -0.0, -0.0, 
    0.032995, -0.080626, 0.054716, 0.958835, 0.610079, -0.8465, -0.0, 0.5324, 
    0.032995, 0.073103, 0.054716, 0.958359, 0.415281, -0.8465, -0.0, 0.5324, 
    0.027938, 0.094884, 0.046675, 0.985893, 0.387613, -0.8465, -0.0, 0.5324, 
    0.068684, -0.080626, 0.054716, 0.764038, 0.610555, 0.8465, -0.0, 0.5324, 
    0.073741, -0.102408, 0.046675, 0.708904, 0.63829, 0.8465, -0.0, 0.5324, 
    0.073741, 0.094884, 0.046675, 0.708293, 0.388291, 0.8465, -0.0, 0.5324, 
    0.073741, -0.102408, 0.046675, 0.736504, 0.638223, -0.0, -0.3463, 0.9381, 
    0.068684, -0.080626, 0.054716, 0.764038, 0.610555, -0.0, -0.3463, 0.9381, 
    0.032995, -0.080626, 0.054716, 0.958835, 0.610079, -0.0, -0.3463, 0.9381, 
    0.027938, 0.094884, 0.046675, 0.985893, 0.387613, -0.0, 0.3463, 0.9381, 
    0.032995, 0.073103, 0.054716, 0.958359, 0.415281, -0.0, 0.3463, 0.9381, 
    0.068684, 0.073103, 0.054716, 0.763562, 0.415757, -0.0, 0.3463, 0.9381, 
    0.073741, -0.102408, 0.036135, 0.486505, 0.638834, -0.0, -1.0, -0.0, 
    0.073741, -0.102408, 0.046675, 0.708904, 0.63829, -0.0, -1.0, -0.0, 
    0.027938, -0.102408, 0.046675, 0.709514, 0.88829, -0.0, -1.0, -0.0, 
    -0.032995, 0.073103, 0.054716, 0.763562, 0.415757, -0.0, -0.0, 1.0, 
    -0.068684, -0.080626, 0.054716, 0.958835, 0.610079, -0.0, -0.0, 1.0, 
    -0.032995, -0.080626, 0.054716, 0.764038, 0.610555, -0.0, -0.0, 1.0, 
    -0.073741, 0.094884, 0.036135, 0.235895, 0.389445, -0.0, -0.0, -1.0, 
    -0.027938, -0.102408, 0.036135, 0.486505, 0.638834, -0.0, -0.0, -1.0, 
    -0.073741, -0.102408, 0.036135, 0.236506, 0.639445, -0.0, -0.0, -1.0, 
    -0.073741, 0.094884, 0.036135, 0.485283, 0.138835, -0.0, 1.0, -0.0, 
    -0.027938, 0.094884, 0.046675, 0.708293, 0.388291, -0.0, 1.0, -0.0, 
    -0.027938, 0.094884, 0.036135, 0.485894, 0.388834, -0.0, 1.0, -0.0, 
    -0.073741, 0.094884, 0.046675, 0.013496, 0.389989, -1.0, -0.0, -0.0, 
    -0.073741, -0.102408, 0.036135, 0.236506, 0.639445, -1.0, -0.0, -0.0, 
    -0.073741, -0.102408, 0.046675, 0.014107, 0.639988, -1.0, -0.0, -0.0, 
    -0.027938, 0.094884, 0.036135, 0.485894, 0.388834, 1.0, -0.0, -0.0, 
    -0.027938, -0.102408, 0.046675, 0.708904, 0.63829, 1.0, -0.0, -0.0, 
    -0.027938, -0.102408, 0.036135, 0.486505, 0.638834, 1.0, -0.0, -0.0, 
    -0.068684, -0.080626, 0.054716, 0.958835, 0.610079, -0.8465, -0.0, 0.5324, 
    -0.073741, 0.094884, 0.046675, 0.985893, 0.387613, -0.8465, -0.0, 0.5324, 
    -0.073741, -0.102408, 0.046675, 0.986504, 0.637612, -0.8465, -0.0, 0.5324, 
    -0.032995, -0.080626, 0.054716, 0.764038, 0.610555, 0.8465, -0.0, 0.5323, 
    -0.027938, 0.094884, 0.046675, 0.708293, 0.388291, 0.8465, -0.0, 0.5323, 
    -0.032995, 0.073103, 0.054716, 0.763562, 0.415757, 0.8465, -0.0, 0.5323, 
    -0.027938, -0.102408, 0.046675, 0.736504, 0.638223, -0.0, -0.3463, 0.9381, 
    -0.068684, -0.080626, 0.054716, 0.958835, 0.610079, -0.0, -0.3463, 0.9381, 
    -0.073741, -0.102408, 0.046675, 0.986504, 0.637612, -0.0, -0.3463, 0.9381, 
    -0.073741, 0.094884, 0.046675, 0.985893, 0.387613, -0.0, 0.3463, 0.9381, 
    -0.032995, 0.073103, 0.054716, 0.763562, 0.415757, -0.0, 0.3463, 0.9381, 
    -0.027938, 0.094884, 0.046675, 0.735893, 0.388224, -0.0, 0.3463, 0.9381, 
    -0.027938, -0.102408, 0.036135, 0.486505, 0.638834, -0.0, -1.0, -0.0, 
    -0.073741, -0.102408, 0.046675, 0.709514, 0.88829, -0.0, -1.0, -0.0, 
    -0.073741, -0.102408, 0.036135, 0.487116, 0.888833, -0.0, -1.0, -0.0, 
    -0.032995, 0.073103, 0.054716, 0.763562, 0.415757, -0.0, -0.0, 1.0, 
    -0.068684, 0.073103, 0.054716, 0.958359, 0.415281, -0.0, -0.0, 1.0, 
    -0.068684, -0.080626, 0.054716, 0.958835, 0.610079, -0.0, -0.0, 1.0, 
    -0.073741, 0.094884, 0.036135, 0.235895, 0.389445, -0.0, -0.0, -1.0, 
    -0.027938, 0.094884, 0.036135, 0.485894, 0.388834, -0.0, -0.0, -1.0, 
    -0.027938, -0.102408, 0.036135, 0.486505, 0.638834, -0.0, -0.0, -1.0, 
    -0.073741, 0.094884, 0.036135, 0.485283, 0.138835, -0.0, 1.0, -0.0, 
    -0.073741, 0.094884, 0.046675, 0.707682, 0.138292, -0.0, 1.0, -0.0, 
    -0.027938, 0.094884, 0.046675, 0.708293, 0.388291, -0.0, 1.0, -0.0, 
    -0.073741, 0.094884, 0.046675, 0.013496, 0.389989, -1.0, -0.0, -0.0, 
    -0.073741, 0.094884, 0.036135, 0.235895, 0.389445, -1.0, -0.0, -0.0, 
    -0.073741, -0.102408, 0.036135, 0.236506, 0.639445, -1.0, -0.0, -0.0, 
    -0.027938, 0.094884, 0.036135, 0.485894, 0.388834, 1.0, -0.0, -0.0, 
    -0.027938, 0.094884, 0.046675, 0.708293, 0.388291, 1.0, -0.0, -0.0, 
    -0.027938, -0.102408, 0.046675, 0.708904, 0.63829, 1.0, -0.0, -0.0, 
    -0.068684, -0.080626, 0.054716, 0.958835, 0.610079, -0.8465, -0.0, 0.5323, 
    -0.068684, 0.073103, 0.054716, 0.958359, 0.415281, -0.8465, -0.0, 0.5323, 
    -0.073741, 0.094884, 0.046675, 0.985893, 0.387613, -0.8465, -0.0, 0.5323, 
    -0.032995, -0.080626, 0.054716, 0.764038, 0.610555, 0.8465, -0.0, 0.5324, 
    -0.027938, -0.102408, 0.046675, 0.708904, 0.63829, 0.8465, -0.0, 0.5324, 
    -0.027938, 0.094884, 0.046675, 0.708293, 0.388291, 0.8465, -0.0, 0.5324, 
    -0.027938, -0.102408, 0.046675, 0.736504, 0.638223, -0.0, -0.3463, 0.9381, 
    -0.032995, -0.080626, 0.054716, 0.764038, 0.610555, -0.0, -0.3463, 0.9381, 
    -0.068684, -0.080626, 0.054716, 0.958835, 0.610079, -0.0, -0.3463, 0.9381, 
    -0.073741, 0.094884, 0.046675, 0.985893, 0.387613, -0.0, 0.3463, 0.9381, 
    -0.068684, 0.073103, 0.054716, 0.958359, 0.415281, -0.0, 0.3463, 0.9381, 
    -0.032995, 0.073103, 0.054716, 0.763562, 0.415757, -0.0, 0.3463, 0.9381, 
    -0.027938, -0.102408, 0.036135, 0.486505, 0.638834, -0.0, -1.0, -0.0, 
    -0.027938, -0.102408, 0.046675, 0.708904, 0.63829, -0.0, -1.0, -0.0, 
    -0.073741, -0.102408, 0.046675, 0.709514, 0.88829, -0.0, -1.0, -0.0
]

handle_indices = [
    10, 4, 8, 
    1, 2, 0, 
    1, 11, 3, 
    7, 0, 5, 
    3, 9, 2, 
    4, 7, 5, 
    8, 11, 10, 
    9, 4, 5, 
    7, 10, 11, 
    2, 5, 0, 
    10, 6, 4, 
    1, 3, 2, 
    1, 7, 11, 
    7, 1, 0, 
    3, 11, 9, 
    4, 6, 7, 
    8, 9, 11, 
    9, 8, 4, 
    7, 6, 10, 
    2, 9, 5, 
    22, 16, 20, 
    13, 14, 12, 
    13, 23, 15, 
    19, 12, 17, 
    15, 21, 14, 
    16, 19, 17, 
    20, 23, 22, 
    21, 16, 17, 
    19, 22, 23, 
    14, 17, 12, 
    22, 18, 16, 
    13, 15, 14, 
    13, 19, 23, 
    19, 13, 12, 
    15, 23, 21, 
    16, 18, 19, 
    20, 21, 23, 
    21, 20, 16, 
    19, 18, 22, 
    14, 21, 17
]

handle_buffer = np.array(handle_buffer, dtype=np.float32)
handle_indices = np.array(handle_buffer, dtype=np.uint32)