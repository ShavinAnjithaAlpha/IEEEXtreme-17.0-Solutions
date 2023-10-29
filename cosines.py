import math

T = int(input())

for _ in range(T):
    angle = float(input())

    # find the minimu integer n such that cos(n.a) is minimal
    tmp_angle = angle
    n = 1
    while (True):
        while (tmp_angle > 90 and tmp_angle < 270):
            angle *= n
            tmp_angle = angle % 360
            n += 1
