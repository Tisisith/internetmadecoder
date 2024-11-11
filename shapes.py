import math
def circle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi*(radius*radius)
    print(f"The area of the circle with radius {radius} is {area}\n")

def triangle():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    print(f'The are of the triangle with base {base} and height {height} is {0.5*base*height}\n')

def rectangle():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    print(f'The are of the rectangle with length {length} and width {width} is {length*width}\n')

def square_perimeter():
    side = float(input("What is the side length of the square? "))
    return side * 4

def circle_details(r):
    circumference = 2*(math.pi*r)
    area = math.pi*r**r
    return circumference, area

def geometry(side,radius):
    square_perimeter = side * 4
    square_area = side * side
    circle_perimeter = 2*(math.pi*radius)
    circle_area = math.pi*radius**radius
    if square_perimeter > circle_perimeter and square_area > circle_area:
        print('The Square has a larger perimeter')
        print('The square has a larger area')
    elif square_perimeter > circle_perimeter and square_area < circle_area:
        print('The Square has a larger perimeter')
        print('The circle has a larger area')
    elif square_perimeter < circle_perimeter and square_area > circle_area:
        print('The circle has a larger perimeter')
        print('The square has a larger area')
    else:
        print('The circle has a larger perimeter')
        print('The circle has a larger area')

print(circle_details(3))

geometry(5,4.75)


