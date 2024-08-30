print("*****Area Calculator*****")
print("""press 1 to get the area of square
      press 2 to get area of rectangle
      press 3 to get area of circle
      press 4 to get area of triangle""")

choice = int(input("enter a number between 1-4:"))

if choice==1:
    side=float(input("enter the length of one side:"))
    area=side**2
    print("the area of square is",area)

elif choice==2:
    length=float(input("enter the length of rectangle:"))
    width=float(input("enter the width of rectangle:"))
    area=length * width
    print("the area of rectangle is",area)

elif choice==3:
    radius=float(input("enter the radius of the circle:"))
    area=((22/7)*(radius**2))
    print("the area of circle is",area)

elif choice==4:
    base=float(input("enter the base of the triangle:"))
    height=float(input("enter the base of the triangle:"))
    area=0.5*base*height
    print("the area of triangle is",area)

else:
    print("Invalid input")