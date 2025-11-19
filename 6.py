import math


def calculate_distance(x1, y1, x2, y2):
    """
    Вычисляет расстояние между 2 точками на плоскости

    Args:
        x1, y1 (float): Координаты точки1
        x2, y2 (float): Координаты точки2

    Returns:
        float: Расстояние между точками
    """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def calculate_triangle_area(a, b, c):
    """
    Вычисляет площадь треугольника по трем сторонам (формула Герона)

    Args:
        a, b, c (float): Длины сторон треугольника

    Returns:
        float: Площадь треугольника
    """
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area


def main():
    print("Введите координаты 3 вершины треугольника>>> ")

    x1, y1 = map(float, input("Точка A (x y): ").split())
    x2, y2 = map(float, input("Точка B (x y): ").split())
    x3, y3 = map(float, input("Точка C (x y): ").split())

    side_ab = calculate_distance(x1, y1, x2, y2)
    side_bc = calculate_distance(x2, y2, x3, y3)
    side_ca = calculate_distance(x3, y3, x1, y1)

    area = calculate_triangle_area(side_ab, side_bc, side_ca)
    print(f"Результаты расчета:")
    print(f"Сторона AB: {side_ab:.2f}")
    print(f"Сторона BC: {side_bc:.2f}")
    print(f"Сторона CA: {side_ca:.2f}")
    print(f"Площадь треугольника: {area:.2f}")
main()