def calculate_bwi(weight,height):
    """
    Args:
        weight (float): масса тела в кг
        height (float): рост в метрах
    Returns:
        float: значение ИМТ
    """
    bwi = weight / (height ** 2)
    return bwi
def maim():
    user_input=input('Введите ваш вес и рост через пробел >>> ')
    weight, height = map(float, user_input.split())
    bwi = calculate_bwi(weight, height)
    print(f"Ваш ИМТ>>> {bwi:,.1f}.")
maim()