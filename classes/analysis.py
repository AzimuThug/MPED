import numpy as np
import math

class Analysis:

    def min(self, data):
        return min(data)

    def max(self, data):
        return max(data)

    def avg(self, data):
        return sum(data) / len(data)

    def covariance(self, data, N):
        avg_x = self.avg(data)
        out_data = []
        for l in range(N):
            R_xx = 0
            for k in range(0, N - l):
                R_xx += (data[k] - avg_x) * (data[k + l] - avg_x)
            R_xx = R_xx / N
            out_data.append(R_xx)
        return out_data

    def hist(self, data, N, M):
        hist = dict()
        x_min = min(data)
        x_max = max(data)
        step = (x_max - x_min) / M
        for i in range(M):
            left_border = x_min + i * step
            right_border = left_border + step
            count = 0
            for j in range(N):
                if left_border <= data[j] <= right_border:
                    count += 1
            hist[left_border] = count
        return hist

    # def acf(self, inData, N):
    #     outData = [i for i in range(N)]
    #     for i in range(N):
    #         k = 0
    #         outData[i] = 0.0
    #         for j in range(N):
    #             if i + j < N:
    #                 k += 1
    #                 outData[i] += inData[i + j]*inData[j]
    #         outData[i] /= k
    #     return outData

    def acf(self, data, N):
        covariance = self.covariance(data, N)
        max_R_xx = self.max(covariance)
        out_data = []
        for l in range(N):
            out_data.append(covariance[l] / max_R_xx)
        return out_data

    # def acf(self, x):
    #     result = np.correlate(x, x, mode='full')
    #     return result[result.size // 2:]
    #
    # def ccf(self, x, y):
    #     result = np.correlate(x, y, mode='full')
    #     return result[result.size // 2:]

    def ccf(self, dataX, dataY, N):
        avg_x = self.avg(dataX)
        avg_y = self.avg(dataY)
        out_data = []
        for l in range(N):
            R_xy = 0
            for k in range(0, N - l):
                R_xy += (dataX[k] - avg_x) * (dataY[k + l] - avg_y)
            R_xy = R_xy / N
            out_data.append(R_xy)
        return out_data

    # Расчет прямого преобразования Фурье
    def Fourier(self, data, N):
        out_data = []
        for i in range(N):
            Re_Xn = 0
            Im_Xn = 0
            for k in range(N):
                Re_Xn += data[k] * np.cos(2 * math.pi * i * k / N)
                Im_Xn += data[k] * np.sin(2 * math.pi * i * k / N)
            Re_Xn = Re_Xn / N
            Im_Xn = Im_Xn / N
            Xn = np.sqrt((Re_Xn ** 2) + (Im_Xn ** 2))
            out_data.append(Xn)
        return out_data

    # Амплитудный спектр Фурье
    def spectrFourier(self, Xn, N, dt):
        out_data = []
        f_border = 1 / (2 * dt)
        df = 2 * f_border / N
        for i in range(N):
            out_data.append(Xn[i] * df)
        return out_data

    @staticmethod
    def diff(img_1, img_2):
        return [x - y for x, y in zip(img_1, img_2)]

    @staticmethod
    def Fourier2D(img):
        return np.fft.fft2(img)


    @staticmethod
    def inverseFourier(img):
        pass
