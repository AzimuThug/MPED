import numpy as np
import math

class Proccessing:

    def shift_2d(self, array, c):
        # new_arr = array.copy()
        # for i in range(new_arr.shape[0]):
        #     for j in range(new_arr.shape[1]):
        #         new_arr[i, j] = new_arr[i, j] + c
        c_arr = np.full(array.shape, c)
        return array + c_arr