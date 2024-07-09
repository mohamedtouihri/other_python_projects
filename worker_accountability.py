user_lenght = float(input("Please Type lenght: \n"))
user_widht = float(input("Please Type widht:   \n"))
user_meter = float(input("How much for 1 meter?: \n"))
area = user_lenght * user_widht
user_area = str(area)
print('The total area is: ' + user_area + ' m')
money = str(user_meter * area)
print('Give The Guy: ' + money + " TND")