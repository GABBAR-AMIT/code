# Python program to print the area of a rectangle 
# and the volume of a cylinder using square and cube symbols

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

# Calculate the area of the rectangle
area_rectangle = length * width

# Print the area of the rectangle
print("The area of the rectangle is: **²**" , area_rectangle,"\u00B2")

# Calculate the volume of the cylinder
radious = int(input("Enter the radious of the cylinder: "))
height = int(input("Enter the height of the cylinder: "))

volume_cylinder = 3.1416 * radious ** 2 * height

# Print the volume of the cylinder
print("The volume of the cylinder is: **³**", volume_cylinder,"\u00b3")

