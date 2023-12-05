if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    data = lines[0].strip().split()[2:]
    data = [points.strip(',').strip('y=').strip('x=').split('..') for points in data]
    xi, xf = data[0]
    yi, yf = data[1]

    print(int(yi) * (int(yi) + 1) // 2)


