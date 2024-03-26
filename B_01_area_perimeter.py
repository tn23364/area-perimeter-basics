# ask user for width and loop until they enter a number that is more than zero
def num_check(question):

# main routine starts here
keep_going = ''
while keep_going = '':

    # get width and height
    width = num_check("Width: ")
    height = num_check("Width: ")

    # calculate area / perimeter
    area = width * height
    perimeter = 2 * (width + height)

    # display output
    print()
    print(f'Perimeter: {perimeter} units')
    print(f'Area: {area} square units')

    # ask user if they want to keep going
    keep_going = input('Press enter to keep going or any key to quit. ')
    print()

print('Thank you for using the area / perimeter calculator')