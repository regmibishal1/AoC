import re

if __name__ == "__main__":
    filename = "input.txt"
    # filename = 'input_sample.txt'

    with open(filename) as f:
        lines = f.readlines()
        times = [int(num) for num in re.findall(r'-?[\d]+', lines[0])]
        distance = [int(num) for num in re.findall(r'-?[\d]+', lines[1])]

    prod = 1
    for i, time in enumerate(times):
        calc_dist = 0
        iter = 0
        while calc_dist <= distance[i]:
            iter += 1
            calc_dist = iter * (time - iter)

        prod *= len(list(range(time))[iter:-(iter-1)])

    print(prod)







