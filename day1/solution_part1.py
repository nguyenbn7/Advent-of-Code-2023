with open("input.txt") as input:
    calibrations = []
    while line := input.readline():
        calibration = ""

        for i in range(len(line)):
            if line[i].isdigit():
                calibration += line[i]
                break

        for i in range(len(line) - 1, -1, -1):
            if line[i].isdigit():
                calibration += line[i]
                break
        
        calibrations.append(int(calibration))

print(sum(calibrations))