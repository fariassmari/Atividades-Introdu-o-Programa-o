num1 = int(input())

def mes(num1: int) -> str:
    if num1 == 1:
        return 'January'
    elif num1 == 2:
        return 'February'
    elif num1 == 3:
        return 'March'
    elif num1 == 4:
        return 'April'
    elif num1 == 5:
        return 'May'
    elif num1 == 6:
        return 'June'
    elif num1 == 7:
        return 'July'
    elif num1 == 8:
        return 'August'
    elif num1 == 9:
        return 'September'
    elif num1 == 10:
        return 'October'
    elif num1 == 11:
        return 'November'
    elif num1 == 12:
        return 'December'

resultado = mes(num1)

if resultado is not None:
    print(resultado)
