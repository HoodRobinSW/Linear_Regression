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
