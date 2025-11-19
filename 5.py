B5000 = 5000
B2000 = 2000
B1000 = 1000
B500 = 500
B200 = 200
B100 = 100


def main():
    """Основная функция работы банкомата"""
    amount = int(input("Введите сумму для снятия (кратную 100)>>> "))

    count_5000 = amount // B5000
    remain_1 = amount - count_5000 * B5000

    count_2000 = remain_1 // B2000
    remain_2 = remain_1 - count_2000 * B2000

    count_1000 = remain_2 // B1000
    remain_3 = remain_2 - count_1000 * B1000

    count_500 = remain_3 // B500
    remain_4 = remain_3 - count_500 * B500

    count_200 = remain_4 // B200
    remain_5 = remain_4 - count_200 * B200

    count_100 = remain_5 // B100

    print(f"Выдача: {amount} руб.")
    print("Количество купюр к выдаче:")

    print(f"  {B5000:4d} руб. × {count_5000:2d} = {count_5000 * B5000:6d} руб.")
    print(f"  {B2000:4d} руб. × {count_2000:2d} = {count_2000 * B2000:6d} руб.")
    print(f"  {B1000:4d} руб. × {count_1000:2d} = {count_1000 * B1000:6d} руб.")
    print(f"  {B500:4d} руб. × {count_500:2d} = {count_500 * B500:6d} руб.")
    print(f"  {B200:4d} руб. × {count_200:2d} = {count_200 * B200:6d} руб.")
    print(f"  {B100:4d} руб. × {count_100:2d} = {count_100 * B100:6d} руб.")

    total= (count_5000 * B5000 + count_2000 * B2000 + count_1000 * B1000 +
                    count_500 * B500 + count_200 * B200 + count_100 * B100)
    print(f"Итого выдано: {total} руб.")

main()