# Use a function  create a program that culculates the volume of a cylinder
height= float(input("Enter the heightof a cylinder: "))
r= int(input("Enter the r of a cylinder: "))
pie = 22/7
volume = pie * r**2* height
print(volume)
print(f" the volume of acylinder with radius{r} and height{height}is {volume:.3f}")