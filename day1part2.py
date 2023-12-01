def get_first(line):
    char_number = None
    isint = None
    for i in line:
        try:
            isint = int(i)
        except:
            if char_number is None:
                char_number = i
            else:
                char_number +=i
        if isinstance(isint, int) and isint is not None:
            return isint
        elif "one" in char_number or "two" in char_number or "three" in char_number or "four" in char_number \
            or "five" in char_number or "six" in char_number or "seven" in char_number or "eight" in char_number \
            or "nine" in char_number:
            match char_number:
                case char_number if "one" in char_number:
                    return 1
                case char_number if "two" in char_number:
                    return 2
                case char_number if "three" in char_number:
                    return 3
                case char_number if "four" in char_number:
                    return 4
                case char_number if "five" in char_number:
                    return 5
                case char_number if "six" in char_number:
                    return 6
                case char_number if "seven" in char_number:
                    return 7
                case char_number if "eight" in char_number:
                    return 8
                case char_number if "nine" in char_number:
                    return 9
    return 0

def get_last(line):
    line = line.rstrip('\n')
    rev_line = line[::-1]
    char_number = None
    isint = None
    for i in rev_line:
        try:
            isint = int(i)
        except:
            if char_number is None:
                char_number = i
            else:
                char_number +=i
        if isinstance(isint, int) and isint is not None:
            return isint
        elif "one" in char_number[::-1] or "two" in char_number[::-1] or "three" in char_number[::-1] or "four" in char_number[::-1] \
            or "five" in char_number[::-1] or "six" in char_number[::-1] or "seven" in char_number[::-1] or "eight" in char_number[::-1] \
            or "nine" in char_number[::-1]:
            char_number = char_number[::-1]
            match char_number:
                case char_number if "one" in char_number:
                    return 1
                case char_number if "two" in char_number:
                    return 2
                case char_number if "three" in char_number:
                    return 3
                case char_number if "four" in char_number:
                    return 4
                case char_number if "five" in char_number:
                    return 5
                case char_number if "six" in char_number:
                    return 6
                case char_number if "seven" in char_number:
                    return 7
                case char_number if "eight" in char_number:
                    return 8
                case char_number if "nine" in char_number:
                    return 9
    return 0


inputs = open("d1in.txt", "r")
cal_line = []
numbers = []
for line in inputs.readlines():
    cal_line.append(line)

for line in cal_line:
    numbers.append(int(str(get_first(line)) + str(get_last(line))))
print(sum(numbers))