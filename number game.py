num = 87#عدد مورد نظر
for _ in range(3):# 3 دست بازی
    
    p = int(input("Enter a number: "))#عدد کاربر
    if p == num:#اگر کاربر درست حدس بزند
        print("true")#درست است
        break#اتمام برنامه
    elif p >= num:#اگر کاربر عددی بزرگتر حدس بزند
        print("your number is big!")#بزرگ است
    elif p <= num:#اگر کاربر عددی کوچک تر حدس بزند
        print("your number is small!")#کوچک است