#محاسبه مساحت و بررسی مجوز
length = int(input("enter the length:"))
width = int(input("enter the width:"))

#محاسبه مساحت
area = length * width

#چاپ مساحت
print("area:",area)

match area :

    case _ if 0 <= area <= 100 :
        print("permission not required")

    case _ if 100 < area <= 200 :
        print("must get permission")

    case _ if 200 < area :
        print("permission is not included")

    case _ :
        print("area is not correct")

