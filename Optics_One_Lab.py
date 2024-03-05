# define function to return average of a list of numbers passed to it
# function named "average" is passed on parameter which is referred to as "data" in the definition
# numbers variable is set to reference the list "data"
# sum variable is instantiated and set to null value "None"
# "for loop" that runs the code inside of it as the variable n is iterated.
# n is iterated from 0 over the range len(numbers) or length of the list numbers
# the code in the loop is just taking each numbers list element and adding it to the sum: sum + numbers[n]
# numbers[n] addresses the list element of the numbers list that is in the index n
# set average to the result of the sum divided by the lenght of the list of numbers
def average(data):
    numbers = data
    sum = None
    for n in range(len(numbers)):
        sum = sum + numbers[n]
    average = sum / len(numbers)
    return average


# define mirror_equation as accepting two parameters (this can be done with more variability/versatility using solve function
# but was not necessary here and would have been added complexity)
# pass paramters p and q for distance to object and distance to image, respectively
# set p in the function as equal to integer dist_p and q integer dist_q
# solve the mirror equation for focal length. by taking the RHS to the -1 power
# f = (1/p + 1/q)^(-1)
# using f string print a statement telling the relationship between p and q and f
# return f to the the function that called mirror_equation()
def mirror_equation(dist_p, dist_q):
    p = int(dist_p)
    q = int(dist_q)
    f = pow((1 / p + 1 / q), -1)
    print(f"Using {p} as the object distance and {q} as the image distance the focal length is: {f}.")
    return f


# define a sum of focal lengths focal_equation that is passed parameters focal_one and focal_total
# the sum of the inverses equals the inverse of the total
# solve algebraically
def focal_equation(focal_one, focal_total):
    f1 = focal_one
    f2 = None
    ff = focal_total

    f2 = pow(1 / ff - 1 / f1, -1)
    return f2


# define focal length function
# creates empty set for the data to be input
# runs loop 5 times for the five rows of data
# accepts obj_distance and img_distance as inputs
# appends the result of calling the mirror_equation with params passed being the obj distance and image distance
# prints the list of the focal lengths for each trial by cycling through a for loop that prints each value in focal_lengths list

# runs the average function on all the results

def focal_length():
    focal_lengths = []
    for x in range(5):
        obj_dist = None
        img_dist = None
        obj_dist = input(f"Enter the object distance: ")
        img_dist = input(f"Enter the image distance: ")
        focal_lengths.append(mirror_equation(obj_dist, img_dist))
    print("The list of focal lengths for you entries are : ")
    for x in range(len(focal_lengths)):
        print(f"{x + 1}: {focal_lengths[x]}.")

    avg = average(focal_lengths)
    print(f"Average is: {avg}.")
    return avg


# calls a variety of hte aforementioned functions to solve the second question regarding the combination lens
def concave_from_combination(convex_length):
    convex_experimental = convex_length
    combined_length = focal_length()
    concave_focal_length = focal_equation(combined_length, convex_experimental)
    return concave_focal_length


# this is the main function itself
# this calls the functions that are defined above in order to carry out the tasks in the correct order

def main():
    print("Convex lengths: ")
    convex = focal_length()
    print(f"Convex Length: {convex}.")

    print("Concave lengths: ")
    concave = concave_from_combination(convex)
    print(f"Concave Length: {concave}.")


# runs main()
main()
