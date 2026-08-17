basic = float(input("enter basic salary"))
if basic <= 20000:
    hra = basic * 20 / 100
    da = basic * 50 / 100
elif basic <= 40000:
    hra = basic * 25 / 100
    da = basic * 60 / 100
else:
    hra = basic * 30 / 100
    da = basic * 70 / 100
gross = basic + hra + da
print("basic salary =", basic)
print("hra =", hra)
print("da =", da)
print("gross salary =", gross)
