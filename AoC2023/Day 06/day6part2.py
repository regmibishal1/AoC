import re

if __name__ == "__main__":
    filename = "input.txt"
    # filename = 'input_sample.txt'

    with open(filename) as f:
        lines = f.readlines()

        times = [int(num) for num in re.findall(r'-?[\d]+', lines[0].replace(' ', ''))]
        distance = [int(num) for num in re.findall(r'-?[\d]+', lines[1].replace(' ', ''))]

    prod = 1
    for i, time in enumerate(times):
        calc_dist = 0
        iter_ind = 0
        while calc_dist <= distance[i]:
            iter_ind += 1
            calc_dist = iter_ind * (time - iter_ind)

        prod *= len(list(range(time))[iter_ind:-(iter_ind-1)])

    print(prod)





