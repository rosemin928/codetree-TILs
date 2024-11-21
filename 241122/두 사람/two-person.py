one_age, one_gen = input().split()
two_age, two_gen = input().split()

if (int(one_age) >= 19 and one_gen == "M") or (int(two_age) >= 19 and two_gen == "M"):
    print(1)
else:
    print(0)