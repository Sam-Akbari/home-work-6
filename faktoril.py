sum = 0#مجهول جمع
while True:#اگر شرط برقرار باشد
    n = int(input("Enter a number: "))#عدد از کاربر درخواست میشود
    if n == 0:#اگر عدد برابر صفر بود
        break#اتمام برنامه
    sum += n#مجهول با عدد کاربر جمع میشود
    print(sum)#عدد مورد نظر چاپ میشود