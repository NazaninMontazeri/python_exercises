#چاپ اعداد از قرینه عدد تا خود عدد یا برعکس
num = int(input("enter a number:"))

#بررسی علامت عدد
if num == 0 :
    print("number is zero")
else:
    if num > 0 :
        step = 1
    else:
        step = -1

    #چاپ اعداد از قرینه ی عدد تا خود عدد
    for i in range (-num , num + step, step):
         print(i)