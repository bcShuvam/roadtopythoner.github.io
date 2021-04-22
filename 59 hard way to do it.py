def to_calculate_area_of_circle(r):
    """ To calculate area of circle whose radius is 7 """
    area_of_circle = 22/7*r*r
    return f"Answer: {area_of_circle} cm2\n"

def to_convert_fahrenheit_into_Celsius():
    """ To convert fahrenheit into Celsius """
    f = input("Enter temperature in fahrenheit.\n>> ")
    f_to_c = (float(f)-32)*5/9
    print(f"Answer : {f}°f = {f_to_c}°C")

print(to_calculate_area_of_circle(7))
to_convert_fahrenheit_into_Celsius()