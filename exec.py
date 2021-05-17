# 윤년 확인
print("-- 윤년 확인 프로그램 --")
year = int(input("년도: "))
if (year%4 == 0 and year%100 != 0) or year%400 == 0:
    print("-> {}은 윤년이에요 <-".format(year))
else:
    print("-> {}은 윤년이 아니에요 <-".format(year))