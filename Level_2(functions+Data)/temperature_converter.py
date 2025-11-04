#celsius to fahrenheit
def fahrenheit(temp):
 return temp*1.8+32
f=fahrenheit(35)
print('temperature in Fahrenheit is',f)
#celsius to kelvin
def kelvin(temp):
    return temp+273.15
k=kelvin(35)
print("temperature in Kelvin is",k)
#kelvin to fahrenheit
def kelvin_2_fahrenheit(temp):
    return temp-273.15*1.8+32
print('temperature in fahrenheit from kelvin',kelvin_2_fahrenheit(35))
#kelvin to celsius
def kelvin_2_celsius(temp):
    return temp+273.15
print('temperature in celsius from kelvin',kelvin_2_celsius(35))