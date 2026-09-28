#میانگین 5 نمره
scores = {}

# وارد کردن 5 درس و نمرهای مربوط به هر درس
for i in range (5):
    subject = input("enter subject name :")
    score = float(input("enter the score for subject :"))

    #بررسی نمره بین 0 تا 20 باشد
    if 0 <= score <= 20 :
        scores[subject] = score
    else:
        print("score is not correct")

#چاپ دیکشنری درسها و نمره ها
print("scores:",scores)

#چاپ و محاسبه میانگین
avg = sum(scores.values()) / len(scores)
print("average:", avg)