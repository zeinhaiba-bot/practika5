def calculate_tax(income):
    """
    Рассчет подоходный налог 13% от годового дохода.

    Args:
    income (float): годовой доход

    Returns:
        tuple: (общий доход, сумма налога )

    """
    tax_rate=0.13
    tax_amount = income * tax_rate
    net_income = income - tax_amount
    return income, tax_amount, net_income
def main():
    income= float(input('введите ваш годовой доход>>> '))
    total_income, tax, net_income = calculate_tax(income)
    print(f"Общая сумма дохода>>> {total_income:,.2f}.")
    print(f"Сумма расчитанного налога>>> {tax:,.2f}.")
    print(f"Сумма <на руки>  после вычета налога>>> {net_income:,.2f}.")
main()