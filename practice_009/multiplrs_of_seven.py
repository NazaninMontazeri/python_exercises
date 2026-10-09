#چاپ لیست اعداد 1 تا 100 و زوج بخش پذیر بر 7
num_list = []

#اعداد 1 تا 100
for num in range(1 , 101 , 1):
    #  بخش پذیر بر 7 و زوج
    if num % 7 == 0 and num % 2 == 0 :
        num_list.append(num)

#چاپ لیست
print("numbers list:" , num_list)