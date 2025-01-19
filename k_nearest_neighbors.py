def read_points():
    N = int(input("Please enter count of points : "))
    X = [0] * N
    Y = [0] * N
    S = [' '] * N
    i = 0
    while i < N:
        reading_finished = False
        while not reading_finished:
            try:
                X[i] = int(input(f"Enter point's {i+1} coordinates on X axes : "))
                Y[i] = int(input(f"Enter point's {i+1} coordinates on Y axes : "))
                S[i] = input(f"Enter point's {i+1} class A or B : ")
                if S[i].lower()!='a' and S[i].lower()!= 'b':
                    raise Exception('ONLY A OR B, small letters are okay')
                reading_finished = True
            except Exception as exp:
                print(f"Not valid input ma3lesh, plz try again. LET'S ENTER AGAIN. \nDetails : {exp}")
        i = i + 1
    return X, Y, S


def calculate_distances(X, Y, x, y):
    N = len(X)
    N = len(Y)
    dist = [0] * N
    i = 0
    while i < N:
        dist[i] = ((X[i] - x) ** 2 + (Y[i] - y) ** 2) ** 0.5
        i = i + 1
    return dist


def select_k_neighbours(K, distances):
    indexes = []
    sorted_indexes = sorted(range(len(distances)), key=lambda k: distances[k])
    indexes = sorted_indexes[0:K - 1]
    return indexes


def vote_classes(class_of_points, k_points_indexes):
    A_votes = 0
    B_votes = 0
    i = 0
    n = len(k_points_indexes)
    while i < n:
        if class_of_points[k_points_indexes[i]] == 'A':
            A_votes = A_votes + 1
        else:
            B_votes = B_votes + 1
        i = i + 1
    if A_votes > B_votes:
        return "A"
    else:
        return "B"


def func5():
    print('from func5 execution')


def k_nearest_neighbor():
    print("K-Nearest Neighbours Algorithm")
    [X, Y, S] = read_points()

    print("Now enter the new point's coordinates please : ")
    x_saha = int(input("Enter point's coordinates on X axes : "))
    y_saha = int(input("Enter point's coordinates on Y axes : "))

    K = int(input("Now enter the K nearest neighbor value please : "))

    distances = calculate_distances(X, Y, x_saha, y_saha)
    k_indexes = select_k_neighbours(K, distances)

    predicted_class = vote_classes(S, k_indexes)
    print("The class of new point should be  : " + predicted_class)
    return predicted_class


if __name__ == '__main__':
    k_nearest_neighbor()
