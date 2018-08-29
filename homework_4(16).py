def have_trains_crashed (v1, v2):
    time_1st = 4/v1
    time_2nd = 6/v2
    if time_1st < time_2nd:
        return False
    if time_1st == time_2nd:
        return True
    if time_1st > time_2nd:
        return True


a = have_trains_crashed(5, 6)
print(a)
