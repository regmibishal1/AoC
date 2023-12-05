import math


def checkVel(area, vxi, vyi):
    xvel, yvel = vxi, vyi
    x, y = 0, 0
    while y > area[2] and x < area[1]:
        x += xvel
        y += yvel
        xvel = 0 if xvel - 1 < 0 else xvel - 1
        yvel -= 1
        if area[0] <= x <= area[1] and area[2] <= y <= area[3]:
            return 1
    return 0


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    data = lines[0].strip().split()[2:]
    data = [points.strip(',').strip('y=').strip('x=').split('..') for points in data]
    xi, xf = int(data[0][0]), int(data[0][1])
    yi, yf = int(data[1][0]), int(data[1][1])

    lvx, hvx = int(math.floor(math.sqrt(xi))), xf + 1
    lvy, hvy = -abs(xf + 1), abs(xf + 1)

    total = 0
    for vx in range(lvx, hvx):
        for vy in range(lvy, hvy):
            total += checkVel([xi, xf, yi, yf], vx, vy)
    print(total)
