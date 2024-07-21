a = 0#متغیر 
b = 0#متغیر
for _ in range(5):#تکرار 5 تایی
    u1 = input("enter your choice(""rock"",""paper"",""scissors""): ")#کاربر 1
    u2 = input("enter your choice(""rock"",""paper"",""scissors""): ")#کاربر 2

#شرط ها
    if u1 == u2:#اگر مساوی بشوند
        print("draw")#بنویس مساوی
    elif u1 == "rock":#اگر کاربر 1 سنگ باشد
        if u2 == "scissors":#یا اگر کاربر 2 قیچی باشد
            print("user1 win")#کاربر 1 برنده
            a += 1# یک امتیاز برای کاربر 1
        if u2 == "paper":#یا اگر کاربر 2 کاغذ باشد
            print("user2 win") #کابر 2 برنده است
            b += 1#یک امتیاز برای کاربر 2
    elif u1 == "scissors":#حالا اگر کاربر 1 قیچی باشد
        if u2 == "rock":#و اگر کاربر 2 سنگ باشد
            print("user2 win")#کاربر 2 برنده است
            b += 1 #یک امتیاز برای کاربر 2 است
        if u2 == "paper":#یا اگر کاربر 2 کاغذ باشد
            print("user1 win")#کاربر 1 برنده است
            a += 1 #یک امتیاز برای کاربر 1 است
    elif u1 == "paper":#حالا اگر کاربر 1 کاغذ باشد
        if u2 == "rock":#و اگر کاربر 2 سنگ باشد
            print("user1 win") #کاربر 1 برنده است
            a += 1#یک امتیاز برای کاربر 1است
        if u2 == "scissors":#یا اگر کاربر 2 قیچی باشد
            print("user2 win")#کاربر 2 برنده است
            b += 1 #یک امتیاز برای کاربر 2 است
    else:#و اما در غیر این صورت
        print("invalid input") #این را مینویسد
print("user1:")#امتیاز کاربر 1
print(a)
print("user2:")#امتیاز کاربر 2
print(b)

if a == b:#مساوی
    print("not win")
elif b >= a:#کاربر 2 برنده
    print("u2 is win")
elif a >= b:#کاربر 1 برنده
    print("u1 is win")
else:#غیر از این صورت
    print("not win")
    

