usd_to_rub= float(input('Введите курс>>> '))
def convert_usd_to_rub(amount_usd):
    """
    Args:
        amount_usd (float): Сумма в долларах
    Returns:
         float: Сумма в рублях
    """
    amount_usd=amount_usd*usd_to_rub
    return amount_usd
def main():
    amount_usd= float(input('Введите сумму в долларах>>> '))
    amount_rub= convert_usd_to_rub(amount_usd)
    print(f"{amount_usd:,.2f} USD= {amount_rub:,.2f} RUB")
    print(f"Курс: 1 USD = {usd_to_rub} RUB")
main()