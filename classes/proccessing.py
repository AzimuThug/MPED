import numpy as np
import math

class Proccessing:

    @staticmethod
    def antiShift(data):
        out_data = []
        avg = sum(data) / len(data)
        for i in range(len(data)):
            out_data.append(data[i] - avg)
        return out_data

    @staticmethod
    def antiSpike(data):
        out_data = data
        for i in range(1, len(out_data)-1):
            if math.fabs(out_data[i]*5) > math.fabs(out_data[i+1]):
                out_data[i] = (out_data[i-1]+out_data[i+1])/2
        return out_data

    @staticmethod
    def antiTrendLinear(data, N):
        out_data = []
        for i in range(N - 1):
            out_data.append(data[i + 1] - data[i])
        return out_data

    @staticmethod
    def antiTrendNonLinear(data, N, W):
        out_data = []
        for i in range(N - W):
            x_n = 0
            for k in range(W):
                x_n += data[i + k]
            x_n = x_n / W
            out_data.append(x_n)
        return out_data

    @staticmethod
    def antiNoise(data1, data2, N, M):
        out_data = []
        for i in range(N):
            avg = 0
            for j in range(M):
                avg += data[j]
            avg = avg / M
            out_data.append(avg)
        return out_data

    @staticmethod
    def lpf(fc, m, dt):
        d = [0.35577019, 0.2436983, 0.07211497, 0.00630165]
        fact = fc * dt
        lpw = []
        lpw.append(fact)
        arg = fact * math.pi
        for i in range(1, m + 1):
            lpw.append(np.sin(arg * i) / (math.pi * i))
        lpw[m] = lpw[m] / 2
        sumg = lpw[0]
        for i in range(1, m + 1):
            sum = d[0]
            arg = math.pi * i / m
            for k in range(1, 4):
                sum += 2 * d[k] * np.cos(arg * k)
            lpw[i] = lpw[i] * sum
            sumg += 2 * lpw[i]
        for i in range(m + 1):
            lpw[i] = lpw[i] / sumg
        return lpw

    @staticmethod
    def lpf_reverse(lpw):
        return lpw[:0:-1] + lpw

    @staticmethod
    def hpf(fc, m, dt):
        lpw = Proccessing.lpf_reverse(Proccessing.lpf(fc, m, dt))
        hpw = []
        Loper = 2 * m + 1
        for k in range(Loper):
            if k == m:
                hpw.append(1 - lpw[k])
            else:
                hpw.append(- lpw[k])
        return hpw

    @staticmethod
    def bpf(fc1, fc2, m, dt):
        lpw1 = Proccessing.lpf_reverse(Proccessing.lpf(fc1, m, dt))
        lpw2 = Proccessing.lpf_reverse(Proccessing.lpf(fc2, m, dt))
        bpw = []
        Loper = 2 * m + 1
        for k in range(Loper):
            bpw.append(lpw2[k] - lpw1[k])
        return bpw

    @staticmethod
    def bsf(fc1, fc2, m, dt):
        bsw = []
        lpw1 = Proccessing.lpf_reverse(Proccessing.lpf(fc1, m, dt))
        lpw2 = Proccessing.lpf_reverse(Proccessing.lpf(fc2, m, dt))
        Loper = 2 * m + 1
        for k in range(0, Loper):
            if k == m:
                bsw.append(1. + lpw1[k] - lpw2[k])
            else:
                bsw.append(lpw1[k] - lpw2[k])
        return bsw

    @staticmethod
    def frequencyResponse(data, N):
        out_data = []
        for i in range(N):
            out_data.append(data[i] * N)
        return out_data