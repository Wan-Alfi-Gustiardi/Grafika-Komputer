import numpy as np

base_buffer = [
    -0.624417, -0.348375, 0.62761, 0.166667, 0.5, -1.0, -0.0, -0.0, 
    -0.624417, -0.453606, -0.62761, 0.314815, 0.0, -1.0, -0.0, -0.0, 
    -0.624417, -0.453606, 0.62761, 0.314815, 0.5, -1.0, -0.0, -0.0, 
    -0.624417, -0.348375, -0.62761, 0.314815, 0.5, -0.0, -0.0, -1.0, 
    0.624417, -0.453606, -0.62761, 0.462963, 0.0, -0.0, -0.0, -1.0, 
    -0.624417, -0.453606, -0.62761, 0.462963, 0.5, -0.0, -0.0, -1.0, 
    0.624417, -0.348375, -0.62761, 0.462963, 0.5, 1.0, -0.0, -0.0, 
    0.624417, -0.453606, 0.62761, 0.611111, 0.0, 1.0, -0.0, -0.0, 
    0.624417, -0.453606, -0.62761, 0.611111, 0.5, 1.0, -0.0, -0.0, 
    0.624417, -0.348375, 0.62761, 0.166667, 1.0, -0.0, -0.0, 1.0, 
    -0.624417, -0.453606, 0.62761, 0.314815, 0.5, -0.0, -0.0, 1.0, 
    0.624417, -0.453606, 0.62761, 0.314815, 1.0, -0.0, -0.0, 1.0, 
    0.624417, -0.453606, -0.62761, 0.462963, 1.0, -0.0, -1.0, -0.0, 
    -0.624417, -0.453606, 0.62761, 0.314815, 0.5, -0.0, -1.0, -0.0, 
    -0.624417, -0.453606, -0.62761, 0.462963, 0.5, -0.0, -1.0, -0.0, 
    -0.624417, -0.348375, -0.62761, 0.611111, 1.0, -0.0, 1.0, -0.0, 
    0.624417, -0.348375, 0.62761, 0.462963, 0.5, -0.0, 1.0, -0.0, 
    0.624417, -0.348375, -0.62761, 0.611111, 0.5, -0.0, 1.0, -0.0, 
    -0.624417, -0.348375, 0.62761, 0.166667, 0.5, -1.0, -0.0, -0.0, 
    -0.624417, -0.348375, -0.62761, 0.166667, 0.0, -1.0, -0.0, -0.0, 
    -0.624417, -0.453606, -0.62761, 0.314815, 0.0, -1.0, -0.0, -0.0, 
    -0.624417, -0.348375, -0.62761, 0.314815, 0.5, -0.0, -0.0, -1.0, 
    0.624417, -0.348375, -0.62761, 0.314815, 0.0, -0.0, -0.0, -1.0, 
    0.624417, -0.453606, -0.62761, 0.462963, 0.0, -0.0, -0.0, -1.0, 
    0.624417, -0.348375, -0.62761, 0.462963, 0.5, 1.0, -0.0, -0.0, 
    0.624417, -0.348375, 0.62761, 0.462963, 0.0, 1.0, -0.0, -0.0, 
    0.624417, -0.453606, 0.62761, 0.611111, 0.0, 1.0, -0.0, -0.0, 
    0.624417, -0.348375, 0.62761, 0.166667, 1.0, -0.0, -0.0, 1.0, 
    -0.624417, -0.348375, 0.62761, 0.166667, 0.5, -0.0, -0.0, 1.0, 
    -0.624417, -0.453606, 0.62761, 0.314815, 0.5, -0.0, -0.0, 1.0, 
    0.624417, -0.453606, -0.62761, 0.462963, 1.0, -0.0, -1.0, -0.0, 
    0.624417, -0.453606, 0.62761, 0.314815, 1.0, -0.0, -1.0, -0.0, 
    -0.624417, -0.453606, 0.62761, 0.314815, 0.5, -0.0, -1.0, -0.0, 
    -0.624417, -0.348375, -0.62761, 0.611111, 1.0, -0.0, 1.0, -0.0, 
    -0.624417, -0.348375, 0.62761, 0.462963, 1.0, -0.0, 1.0, -0.0, 
    0.624417, -0.348375, 0.62761, 0.462963, 0.5, -0.0, 1.0, -0.0
]

base_indices = [
    1, 2, 0, 
    3, 6, 2, 
    7, 4, 6, 
    5, 0, 4, 
    6, 0, 2, 
    3, 5, 7, 
    1, 3, 2, 
    3, 7, 6, 
    7, 5, 4, 
    5, 1, 0, 
    6, 4, 0, 
    3, 1, 5
]

base_buffer = np.array(base_buffer, dtype=np.float32)
base_indices = np.array(base_indices, dtype=np.uint32)
