print("This is a proyect that supports the mad scientist in his linear regression research")

#1.CALCULATE ERROR

def get_y(m, b, x):
    y = m*x+b
    return y

def calculate_error(m, b, point):
    x_point = point[0]
    y_point = point[1]
    y = get_y(m, b, x_point)
    distance = abs(y - y_point)
    return distance

def calculate_all_error(m, b, points):
    total = 0
    for point in points:
        total += calculate_error(m, b, point)
    return total

#2.TRY A BUNCH OF SLOPES AND INTERCEPTS!

possible_ms = [i * 0.1 for i in range(-100, 101)]
possible_bs = [i * 0.1 for i in range(-200, 201)]
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
smallest_error = float("inf")
best_m = 0
best_b = 0
for m in possible_ms:
    for b in possible_bs:
        if calculate_all_error(m, b, datapoints) < smallest_error:
            best_m = m
            best_b = b
            smallest_error = calculate_all_error(m, b, datapoints)
print(best_m, best_b, smallest_error)
