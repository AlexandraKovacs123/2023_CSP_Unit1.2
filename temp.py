# Stage 1
'''
number = 1
star = "*"
'''
'''
for stars in range(5):
    print(star * number)
    number = number + 1
'''


# Bonus

def stars():
    spaces = " "
    num = 4
    number = 1
    star = "* "
    for stars in range(5):
        # print(spaces * num)
        print(spaces * num, star * number)
        number = number + 1
        num = num - 1

stars()
