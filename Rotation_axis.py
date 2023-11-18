import math
# Taking user input
rotation_axis = input("Enter rotation, rx,ry,rz: ")
angle_degrees = int(input("Enter angle_radians of rotation: "))


# Convert angle_radians to radians
angle_radians = angle_degrees * (math.pi / 180)

#print("angle_radians in radians:", math.sin(angle_radians))
# Printing the user input
#print("You entered:", rotation_axis)
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: ")) 

if rotation_axis == "rx":
    x_prime = x
    print(math.cos(angle_radians))
    y_prime = y*math.cos(angle_radians) - z*math.sin(angle_radians)
    z_prime = y*math.sin(angle_radians) + z*math.cos(angle_radians)
    print("x_prime:", x_prime)
    print("y_prime:", y_prime)
    print("z_prime:", z_prime)
    
elif rotation_axis == "ry":
    x_prime = x*math.cos(angle_radians) + z*math.sin(angle_radians)
    y_prime = y
    z_prime = -x*math.sin(angle_radians) + z*math.cos(angle_radians)
    print("x_prime:", x_prime)
    print("y_prime:", y_prime)
    print("z_prime:", z_prime)

elif rotation_axis == "rz":
    x_prime = x*math.cos(angle_radians) - y*math.sin(angle_radians)
    y_prime = x*math.sin(angle_radians) + y*math.cos(angle_radians)
    z_prime = z
    print("x_prime:", x_prime)
    print("y_prime:", y_prime)
    print("z_prime:", z_prime)
    
    