import re

if __name__ == "__main__":
    filename = "input.txt"
    # filename = 'input_sample.txt'
    with open(filename) as f:
        lines = f.readlines()

    numList = []
    for i in lines:
        onlyNums = re.sub('[^0-9]', '', i)
        numList.append(int(onlyNums[0] + onlyNums[-1]))
    print(sum(numList))
