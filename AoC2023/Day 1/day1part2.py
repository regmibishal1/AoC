import re

NUM_STRING = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

if __name__ == "__main__":
    filename = "input.txt"
    # filename = 'input_sample.txt'
    with open(filename) as f:
        lines = f.readlines()

    numList = []
    for i in lines:
        # new_row = i
        # for key, val in NUM_STRING.items():
        #     new_row = re.sub(key, val, new_row)
        #
        # print(new_row)
        # onlyNums = re.sub('[^0-9]', '', new_row)

        # from the front of the row search for either a string value of the digit or the digit itself
        firstDigit = re.search(r'one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9', i).group()
        firstDigit = NUM_STRING.get(firstDigit, firstDigit)

        # from the back of the row search for either a string value of the digit or the digit itself
        lastDigit = re.search(r'eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|1|2|3|4|5|6|7|8|9', i[::-1]).group()
        lastDigit = NUM_STRING.get(lastDigit[::-1], lastDigit)

        numList.append(int(firstDigit + lastDigit))
    print(sum(numList))
