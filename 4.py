import math
def calculate_rectangle_area(weigth, height):
    """
    Args:
      weight (float): weight of rectangle
      height (float): height of rectangle
    Returns:
        float: area of rectangle
    """
    return weigth * height
def calculate_circle_area(radius):
    return math.pi * radius**2
weight, height = map(float, input('Введите ширину и высоту прямоугольника: ').split())
print(f'Площадь прямоугольника со сторонами {weigth} и {height} равна {calculate_rectangle_area(weigth, height)}')
radius = float(input('Введите радиус:'))
print(f'Площадь круга с радиусом {radius} равна {calculate_circle_area(radius)}')