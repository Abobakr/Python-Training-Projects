import numpy as np


def read_degrees_algo():
    M = int(input('please enter number of subjects : '))
    N = int(input('please enter number of students : '))
    degrees = np.zeros((M, N))
    i = 0
    while i < M:
        j = 0
        while j < N:
            degrees[i, j] = input(f'please enter degree for subject {i} student {j} ')
            j = j + 1
        i = i + 1
    return degrees


def find_max_algo(degrees):
    M, N = degrees.shape
    max_deg = degrees[0, 0]
    i = 0
    while i < M:
        j = 0
        while j < N:
            if max_deg < degrees[i, j]:
                max_deg = degrees[i, j]
            j = j + 1
        i = i + 1
    return max_deg


def main():
    degrees = read_degrees_algo()
    max_deg = find_max_algo(degrees)
    print("max degress = " + str(max_deg))


if __name__ == '__main__':
    main()
