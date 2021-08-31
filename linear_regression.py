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

#this is a line that looks like y = x, so (3, 3) should lie on it. thus, error should be 0:
print(calculate_error(1, 0, (3, 3)))
#the point (3, 4) should be 1 unit away from the line y = x:
print(calculate_error(1, 0, (3, 4)))
#the point (3, 3) should be 1 unit away from the line y = x - 1:
print(calculate_error(1, -1, (3, 3)))
#the point (3, 3) should be 5 units away from the line y = -x + 1:
print(calculate_error(-1, 1, (3, 3)))

def calculate_all_error(m, b, points):
    total = 0
    for point in points:
        total += calculate_error(m, b, point)
    return total

#every point in this dataset lies upon y=x, so the total error should be zero:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 0, datapoints))

#every point in this dataset is 1 unit away from y = x + 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 1, datapoints))

#every point in this dataset is 1 unit away from y = x - 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, -1, datapoints))


#the points in this dataset are 1, 5, 9, and 3 units away from y = -x + 1, respectively, so total error should be
# 1 + 5 + 9 + 3 = 18
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(-1, 1, datapoints))

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

#3.WHAT DOES OUR MODEL PREDICT?

print(get_y(best_m, best_b, 6))

print("Our model predicts that the 6cm ball will bounce 3.5m. \nNow, Reggie can use this model to predict the bounce of all kinds \nof sizes of balls he may choose to include in the ball pit!")
