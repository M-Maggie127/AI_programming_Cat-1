from math import pi
def circle_area(radius):
    if radius <=0:
        return "Invalid radius"
    area = pi *radius* radius 
    return round(area, 2) 
print(circle_area(5))       