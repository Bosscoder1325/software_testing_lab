print("Enter three sides of the triangle")
a = int(input())
b = int(input())
c = int(input())

if (a<b+c) and (b<a+c) and (c<a+b):
    
    if a==b and b==c:
        print("Equilateral triangle")
    elif a!=b and a!=c and b!=c:
        print("Scalene triangle")
    else:
        print("Isosceles triangle")
        
else:
    print("triangle can't be formed")
        