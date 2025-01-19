# 👨‍💻 Technical Programming Symposium Contests at https://EbubekirDers.Online
# 👨‍🎓 For Online IT and Programming Courses, please contact: +90 552 433 32 31
# 🤼 Note: This project is for learning purposes. Math and coding are not ideal.
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


def calculate_std_dev(values):
    if values:
        mean = calculate_mean(values)
        squared_diffs = calculate_squared_diffs(values, mean)
        variance = calculate_mean(squared_diffs)
        std_dev = variance ** 0.5
        return std_dev


def calculate_zscores(values):
    if len(values) > 1:
        mean = calculate_mean(values)
        std_dev = calculate_std_dev(values)
        z_scores = [round((x - mean) / std_dev, 2) for x in values]
        return z_scores


def calculate_median(values):
    if values:
        sorted_values = sorted(values)
        n = len(sorted_values)
        if n % 2 == 0:
            median = (sorted_values[n // 2 - 1] + sorted_values[n // 2]) / 2
        else:
            median = sorted_values[n // 2]
        return round(median,2)


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


def filter_passing_degrees(degrees, passing_deg):
    passing_degrees = []
    for subject_degrees in degrees:
        passing_degrees.append([degree for degree in subject_degrees if degree >= passing_deg])
    return passing_degrees


def calculate_subjects_ranges(degrees):
    ranges = []
    for subject_degrees in degrees:
        if subject_degrees:
            subject_range = find_max(subject_degrees) - find_min(subject_degrees)
            ranges.append(subject_range)
    return ranges


def calculate_subjects_zscores(degrees):
    zscores = []
    for subject_degrees in degrees:
        if subject_degrees:
            subject_zcores = calculate_zscores(subject_degrees)
            zscores.append(subject_zcores)
    return zscores


def calculate_subjects_medians(degrees):
    medians = []
    for subject_degrees in degrees:
        if subject_degrees:
            subject_median = calculate_median(subject_degrees)
            medians.append(subject_median)
    return medians


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

    passing_degree = read_valid_num_of('passing degree')
    passing_degrees = filter_passing_degrees(degrees, passing_degree)
    print("Passing_degrees :\n", passing_degrees)

    ranges = calculate_subjects_ranges(passing_degrees)
    print("Ranges :\n", ranges)

    std_dev = calculate_std_dev(ranges)
    if std_dev is not None:
        print(f"Std dev. of range  of degrees >={passing_degree} : \n", round(std_dev, 2))
    else:
        print(f"No passed degrees >={passing_degree}")

    zscores = calculate_subjects_zscores(passing_degrees)
    print("Zscores :\n", zscores)

    medians = calculate_subjects_medians(zscores)
    if medians:
        print(f"Median values of z-scores of degrees >={passing_degree} : \n", medians)
    else:
        print(f"No passed degrees >={passing_degree}")


if __name__ == '__main__':
    main()
