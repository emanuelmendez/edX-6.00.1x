
order = "salad water hamburger salad hamburger" # test

# function definition
def item_order (order):
    salad = 0
    hamburger = 0
    water = 0
    for index in range(0, len(order)):
        if order[index:index+len("salad")] == "salad":
            salad += 1
        if order[index:index+len("hamburger")] == "hamburger":
            hamburger += 1
        if order[index:index+len("water")] == "water":
            water += 1
    s = "salad:{0} hamburger:{1} water:{2}".format(salad, hamburger, water)
    return s

# program output
print item_order(order)