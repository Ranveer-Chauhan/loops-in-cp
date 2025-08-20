a = int(input("enter a number:"))
b = int(input("enter b number:"))
c = int(input("enter c number:"))
if(a==90 or b==90 or c==90):
    print("the triangle is right")
elif(a>90 or b>90 or c>90):
    print("the triangle is obtuse")
else:
    print("the tringle is acute")