import numpy as np

door_buffer = [
    0.361225, -0.518269, 0.036135, 0.469183, 0.978196, -0.0, -0.0, 1.0, 
    0.0023, 0.518713, 0.036135, 0.002763, 0.636996, -0.0, -0.0, 1.0, 
    0.0023, -0.518269, 0.036135, 0.469183, 0.636996, -0.0, -0.0, 1.0, 
    0.0023, 0.518713, 0.026256, 0.471659, 0.088063, -0.0, -0.0, -1.0, 
    0.361225, -0.518269, 0.026256, 0.005238, 0.429263, -0.0, -0.0, -1.0, 
    0.0023, -0.518269, 0.026256, 0.005238, 0.088063, -0.0, -0.0, -1.0, 
    0.361225, 0.518713, 0.036135, 0.474925, 0.540571, -0.0, 1.0, -0.0, 
    0.0023, 0.518713, 0.026256, 0.70417, 0.517094, -0.0, 1.0, -0.0, 
    0.0023, 0.518713, 0.036135, 0.70417, 0.540571, -0.0, 1.0, -0.0, 
    0.361225, -0.518269, 0.036135, 0.471302, 0.549542, 1.0, -0.0, -0.0, 
    0.361225, 0.518713, 0.026256, 0.004881, 0.573019, 1.0, -0.0, -0.0, 
    0.361225, 0.518713, 0.036135, 0.004881, 0.549542, 1.0, -0.0, -0.0, 
    0.0023, -0.518269, 0.036135, 0.479954, 0.474266, -0.0, -1.0, -0.0, 
    0.361225, -0.518269, 0.026256, 0.709199, 0.450789, -0.0, -1.0, -0.0, 
    0.361225, -0.518269, 0.036135, 0.709199, 0.474266, -0.0, -1.0, -0.0, 
    0.0023, 0.518713, 0.036135, 0.47023, 0.515563, -1.0, -0.0, -0.0, 
    0.0023, -0.518269, 0.026256, 0.00381, 0.53904, -1.0, -0.0, -0.0, 
    0.0023, -0.518269, 0.036135, 0.00381, 0.515563, -1.0, -0.0, -0.0, 
    -0.0023, 0.518713, 0.036135, 0.940221, 0.637116, -0.0, -0.0, 1.0, 
    -0.361225, -0.518269, 0.036135, 0.4738, 0.978316, -0.0, -0.0, 1.0, 
    -0.0023, -0.518269, 0.036135, 0.4738, 0.637116, -0.0, -0.0, 1.0, 
    -0.361225, -0.518269, 0.026256, 0.48766, 0.080478, -0.0, -0.0, -1.0, 
    -0.0023, 0.518713, 0.026256, 0.95408, 0.421678, -0.0, -0.0, -1.0, 
    -0.0023, -0.518269, 0.026256, 0.48766, 0.421678, -0.0, -0.0, -1.0, 
    -0.0023, 0.518713, 0.026256, 0.706222, 0.575163, -0.0, 1.0, -0.0, 
    -0.361225, 0.518713, 0.036135, 0.476977, 0.551686, -0.0, 1.0, -0.0, 
    -0.0023, 0.518713, 0.036135, 0.706222, 0.551686, -0.0, 1.0, -0.0, 
    -0.361225, 0.518713, 0.026256, 0.002306, 0.484002, -1.0, -0.0, -0.0, 
    -0.361225, -0.518269, 0.036135, 0.468727, 0.50748, -1.0, -0.0, -0.0, 
    -0.361225, 0.518713, 0.036135, 0.002306, 0.50748, -1.0, -0.0, -0.0, 
    -0.361225, -0.518269, 0.026256, 0.478022, 0.483752, -0.0, -1.0, -0.0, 
    -0.0023, -0.518269, 0.036135, 0.707267, 0.507229, -0.0, -1.0, -0.0, 
    -0.361225, -0.518269, 0.036135, 0.478022, 0.507229, -0.0, -1.0, -0.0, 
    -0.0023, -0.518269, 0.026256, 0.472956, 0.47849, 1.0, -0.0, -0.0, 
    -0.0023, 0.518713, 0.036135, 0.006535, 0.455012, 1.0, -0.0, -0.0, 
    -0.0023, -0.518269, 0.036135, 0.472956, 0.455012, 1.0, -0.0, -0.0, 
    0.361225, -0.518269, 0.036135, 0.469183, 0.978196, -0.0, -0.0, 1.0, 
    0.361225, 0.518713, 0.036135, 0.002763, 0.978196, -0.0, -0.0, 1.0, 
    0.0023, 0.518713, 0.036135, 0.002763, 0.636996, -0.0, -0.0, 1.0, 
    0.0023, 0.518713, 0.026256, 0.471659, 0.088063, -0.0, -0.0, -1.0, 
    0.361225, 0.518713, 0.026256, 0.471659, 0.429263, -0.0, -0.0, -1.0, 
    0.361225, -0.518269, 0.026256, 0.005238, 0.429263, -0.0, -0.0, -1.0, 
    0.361225, 0.518713, 0.036135, 0.474925, 0.540571, -0.0, 1.0, -0.0, 
    0.361225, 0.518713, 0.026256, 0.474925, 0.517094, -0.0, 1.0, -0.0, 
    0.0023, 0.518713, 0.026256, 0.70417, 0.517094, -0.0, 1.0, -0.0, 
    0.361225, -0.518269, 0.036135, 0.471302, 0.549542, 1.0, -0.0, -0.0, 
    0.361225, -0.518269, 0.026256, 0.471302, 0.573019, 1.0, -0.0, -0.0, 
    0.361225, 0.518713, 0.026256, 0.004881, 0.573019, 1.0, -0.0, -0.0, 
    0.0023, -0.518269, 0.036135, 0.479954, 0.474266, -0.0, -1.0, -0.0, 
    0.0023, -0.518269, 0.026256, 0.479954, 0.450789, -0.0, -1.0, -0.0, 
    0.361225, -0.518269, 0.026256, 0.709199, 0.450789, -0.0, -1.0, -0.0, 
    0.0023, 0.518713, 0.036135, 0.47023, 0.515563, -1.0, -0.0, -0.0, 
    0.0023, 0.518713, 0.026256, 0.47023, 0.53904, -1.0, -0.0, -0.0, 
    0.0023, -0.518269, 0.026256, 0.00381, 0.53904, -1.0, -0.0, -0.0, 
    -0.0023, 0.518713, 0.036135, 0.940221, 0.637116, -0.0, -0.0, 1.0, 
    -0.361225, 0.518713, 0.036135, 0.940221, 0.978316, -0.0, -0.0, 1.0, 
    -0.361225, -0.518269, 0.036135, 0.4738, 0.978316, -0.0, -0.0, 1.0, 
    -0.361225, -0.518269, 0.026256, 0.48766, 0.080478, -0.0, -0.0, -1.0, 
    -0.361225, 0.518713, 0.026256, 0.95408, 0.080478, -0.0, -0.0, -1.0, 
    -0.0023, 0.518713, 0.026256, 0.95408, 0.421678, -0.0, -0.0, -1.0, 
    -0.0023, 0.518713, 0.026256, 0.706222, 0.575163, -0.0, 1.0, -0.0, 
    -0.361225, 0.518713, 0.026256, 0.476977, 0.575163, -0.0, 1.0, -0.0, 
    -0.361225, 0.518713, 0.036135, 0.476977, 0.551686, -0.0, 1.0, -0.0, 
    -0.361225, 0.518713, 0.026256, 0.002306, 0.484002, -1.0, -0.0, -0.0, 
    -0.361225, -0.518269, 0.026256, 0.468727, 0.484002, -1.0, -0.0, -0.0, 
    -0.361225, -0.518269, 0.036135, 0.468727, 0.50748, -1.0, -0.0, -0.0, 
    -0.361225, -0.518269, 0.026256, 0.478022, 0.483752, -0.0, -1.0, -0.0, 
    -0.0023, -0.518269, 0.026256, 0.707267, 0.483752, -0.0, -1.0, -0.0, 
    -0.0023, -0.518269, 0.036135, 0.707267, 0.507229, -0.0, -1.0, -0.0, 
    -0.0023, -0.518269, 0.026256, 0.472956, 0.47849, 1.0, -0.0, -0.0, 
    -0.0023, 0.518713, 0.026256, 0.006535, 0.47849, 1.0, -0.0, -0.0, 
    -0.0023, 0.518713, 0.036135, 0.006535, 0.455012, 1.0, -0.0, -0.0
]

door_indices = [
    0, 3, 2, 
    7, 4, 6, 
    1, 7, 3, 
    0, 5, 1, 
    2, 4, 0, 
    3, 6, 2, 
    11, 8, 10, 
    12, 15, 14, 
    15, 9, 11, 
    13, 8, 9, 
    12, 10, 8, 
    14, 11, 10, 
    0, 1, 3, 
    7, 5, 4, 
    1, 5, 7, 
    0, 4, 5, 
    2, 6, 4, 
    3, 7, 6, 
    11, 9, 8, 
    12, 13, 15, 
    15, 13, 9, 
    13, 12, 8, 
    12, 14, 10, 
    14, 15, 11
]

door_buffer = np.array(door_buffer, dtype=np.float32)
door_indices = np.array(door_indices, dtype=np.uint32)