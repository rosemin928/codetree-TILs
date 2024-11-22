one_diagnos, one_temp = input().split()
two_diagnos, two_temp = input().split()
three_diagnos, three_temp = input().split()

if one_diagnos == "Y" and int(one_temp) >= 37:
    if two_diagnos == "Y" and int(two_temp) >= 37:
        print("E")
    else:
        if three_diagnos == "Y" and int(three_temp) >= 37:
            print("E")
        else:
            print("N")
else:
    if two_diagnos == "Y" and int(two_temp) >= 37:
        if three_diagnos == "Y" and int(three_temp) >= 37:
            print("E")
        else:
            print("N")
    else:
        print("N")