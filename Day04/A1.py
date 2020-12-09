# Write a function that gets a celsius degree number
# and converts it to a Kelvingrad number.

# Return the calculated value.

# Bonus
# Specify another parameter that says whether to convert to K or F.
# Return the correct calculation in each case.

# Fahrenheit: (1°C × 9/5) + 32

def c_to_k(c):
    return c + 273.15

cel = float(input('Celsiusgradzahl: '))
kel = c_to_k(cel)
# print(kel, 'Kelvin')

### Bonus

def c_to_f(c):
    return (c * 9 / 5) + 32

def convert(c, temp = 'k'):
    if temp == 'k':
        return c_to_k(c)
    elif temp == 'f':
        return c_to_f(c)
    else:
        print('Falsche Eingabe!')
        return c


print(convert(cel))
print(convert(cel, 'f'))
print(convert(cel, 'sdkjf'))
