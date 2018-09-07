# Program to take base and height from user and to calculate area of triangle
# as output.

base = float(input("Enter the Base of triangle: "))
height = float(input("Enter the Height of triangle: "))
def area_triangle(base,height):
    return base * height /2
result = area_triangle(base,height)
print("The area of triangle is " + str(result))

