
import numpy as np

class RandomWindower:

    def __init__(self, base_window=[217.3, 87.1],
                 p_shift=0.0,
                 p_scale=0.0,
                 range_level=[11.5, 152.9],
                 range_scale=[141.2, 325.9]):

        self.base_width, self.base_level = base_window
        self.p_shift = p_shift
        self.p_scale = p_scale
        self.shift_min, self.shift_max = range_level
        self.scale_min, self.scale_max = range_scale

    def __call__(self, x):
        
        # Set base viewing window
        w_width, w_level = self.base_width, self.base_level
        
        # Change window level (shifting)
        if np.random.uniform() < self.p_shift:
            w_level = np.random.uniform(self.shift_min, self.shift_max)

        # Change window width (scaling)
        if np.random.uniform() < self.p_scale:
            w_width = np.random.uniform(self.scale_min, self.scale_max)

        # Compute bounds
        floor = w_level - w_width / 2   
        ceil = w_level + w_width / 2

        # Clip the values to the range [floor, ceil]
        x = np.clip(x, floor, ceil)

        # Normalize to [0, 1]
        x = (x - floor) / (ceil - floor)
        return x
    
