number_letters = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

with open("input.txt") as input:
    calibrations = []
    while line := input.readline():
        first_digit, second_digit = "", ""

        temp = []
        for num_letter in number_letters.keys():
            start_idx = line.find(num_letter)
            if start_idx != -1:
                temp.append((num_letter, start_idx))
        
        temp.sort(key=lambda a: a[1])

        for i in range(len(line)):
            if line[i].isdigit():
                if not len(temp):
                    first_digit = line[i]
                else:
                    if len(temp) and i < temp[0][1]:
                        first_digit = line[i]
                    else:
                        first_digit = number_letters[temp[0][0]]
                break
        
        if not first_digit:
            first_digit = number_letters[temp[0][0]]
        
        temp.clear()

        for num_letter in number_letters.keys():
            start_idx = line.rfind(num_letter)
            if start_idx != -1:
                temp.append((num_letter, start_idx))
        
        temp.sort(key=lambda a: a[1], reverse=True)
        
        for i in range(len(line) - 1, -1, -1):
            if line[i].isdigit():
                if not len(temp):
                    second_digit = line[i]
                else:
                    if i > temp[0][1]:
                        second_digit = line[i]
                    else:
                        second_digit = number_letters[temp[0][0]]
                break

        if not second_digit:
            second_digit = number_letters[temp[0][0]]
        
        calibrations.append(int(first_digit + second_digit))

print(sum(calibrations))