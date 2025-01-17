import numpy as np


####################Just an example###################################


# Binocular camera internal parameters
class stereoCamera(object):
    def __init__(self):
        # left lens parameters
        self.cam_matrix_left = np.array([   [272.96,   0,  342.96],
                                            [       0,  273.46,  192.47],
                                            [       0,         0,         1]
                                        ])
        # right lens parameters
        self.cam_matrix_right = np.array([  [272.6,  0,  341.27],
                                            [       0,  272.86,  193.19],
                                            [       0,         0,         1]
                                        ])

        # distortion coefficients of the two lens:[k1, k2, p1, p2, k3]
        self.distortion_l = np.array([[-0.105265017799570, 0.157165318318889, -0.0000, 0.000, -0.103599296237389]])
        self.distortion_r = np.array([[-0.105196659221942, 0.140002373264707, -0.0000,  0.00,  -0.0758443922994477]])

        # Rotation Matrix
        self.R = np.array([ [  1,  -0.000951991440114949, 0.00710352567907917],
                            [0.000959875596771750,  1.0000, -0.00110656671796462],
                            [ -0.00710246461547760,  0.00111335679839518,  1.0000]
                            ])

        # Translation matrix
        self.T = np.array([[119.38], [-0.0435], [0.3445]])

        # focal length
        self.focal_length = 272.6 # 默认值，一般取立体校正后的重投影矩阵Q中的 Q[2,3]

        # baseline
        self.baseline = 119.70 # 单位：mm， 为平移向量的第一个参数（取绝对值）
