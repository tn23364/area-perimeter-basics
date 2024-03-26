# ask the user for their width and height (assume the put in a valid date)
width = int(input('Width? '))
height = int(input('Height? '))

# calculate the area / perimeter
area = width * height
perimeter = 2 * (width + height)

# output the area and permimeter
print()
print(f'Perimeter: {perimeter} units')
print(f'Area: {area} square units')