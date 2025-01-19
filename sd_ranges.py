def find_max(values):
    if values:
        max_value = values[0]
        for value in values:
            if value > max_value:
                max_value = value
        return max_value


def find_min(values):
    if values:
        min_value = values[0]
        for value in values:
            if value < min_value:
                min_value = value
        return min_value


def calculate_sum(values):
    if values:
        sum = 0
        for value in values:
            sum += value
        return sum


def calculate_mean(values):
    if values:
        mean = calculate_sum(values) / len(values)
        return mean


def calculate_squared_diffs(values, mean):
    if values:
        squared_diffs = []
        for value in values:
            diff = value - mean
            squared_diff = diff ** 2
            squared_diffs.append(squared_diff)
        return squared_diffs


def read_valid_num_of(description):
    while True:
        try:
            num = int(input(f"Enter {description} : "))
            if 0 <= num <= 100:
                return num
            else:
                print("Number must be between 0 and 100")
        except ValueError:
            print("Please enter a valid number")


def read_degrees():
    sub_num = read_valid_num_of("subjects count")
    std_num = read_valid_num_of("students count")
    degrees = [[0] * std_num for _ in range(sub_num)]
    for sub in range(sub_num):
        for std in range(std_num):
            degrees[sub][std] = read_valid_num_of(f'degree of student {std + 1} for subject {sub + 1}')
    return degrees


def filter_passing_degrees(degrees, passing_degree):
    passing_degrees = []
    for subject_degrees in degrees:
        passing_degrees.append([degree for degree in subject_degrees if degree >= passing_degree])
    return passing_degrees


def calculate_subjects_ranges(degrees):
    ranges = []
    for subject_degrees in degrees:
        if subject_degrees:
            subject_range = find_max(subject_degrees) - find_min(subject_degrees)
            ranges.append(subject_range)
    return ranges


def calculate_std_deviation(values):
    if values:
        mean = calculate_mean(values)
        squared_diffs = calculate_squared_diffs(values, mean)
        variance = calculate_mean(squared_diffs)
        std_deviation = variance ** 0.5
        return std_deviation


def main():
    degrees = [
        [85, 78, 92, 88, 76, 95, 89, 77, 84, 91],
        [75, 82, 79, 88, 90, 85, 80, 78, 92, 84],
        [65, 48, 72, 86, 34, 55, 19, 87, 99, 24],
        [15, 12, 23, 37, 46, 34, 41, 19, 34, 18],
    ]

    print("Sample data :\n", degrees)
    answer = input("Input new data? (Enter Yes or No) : ")
    while answer.upper() != 'YES' and answer.upper() != 'NO':
        answer = input("Input new data? (Enter Yes or No) : ")
    if bool(answer.upper() == 'YES'):
        degrees = read_degrees()
        print("Your data :\n", degrees)

    passing_degrees = filter_passing_degrees(degrees, 50)
    print("Passing_degrees :\n", passing_degrees)

    ranges = calculate_subjects_ranges(passing_degrees)
    print("Ranges :\n", ranges)

    std_deviation = calculate_std_deviation(ranges)
    if std_deviation is not None:
        print("Std deviation of range degrees >=50 : ", round(std_deviation, 2))
    else:
        print("No passed degrees >=50")


if __name__ == '__main__':
    # main()
    print("sd = ", calculate_std_deviation([50,60,70]))
