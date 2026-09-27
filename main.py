from Fraction import Fraction

def handler_fraction(number: int) -> Fraction:
    fraction = input(f"Введите дробь №{number}: ").split("/")

    if len(fraction) != 2:
        raise ValueError("Дробь не вида a/b")

    numerator, denominator = fraction

    if not numerator.strip("-").isdigit() or not denominator.strip("-").isdigit():
        raise ValueError("Числитель или знаменатель не целые числа")

    return Fraction(int(numerator), int(denominator))

def main():
    try:
        fraction_1 = handler_fraction(1)
        
        sign = input("Введите знак: ")
        
        fraction_2 = handler_fraction(2)

        if sign == "+":
            print(fraction_1.sumFractions(fraction_2))
        
        elif sign == "-":
            print(fraction_1.subFractions(fraction_2))

        elif sign == "*":
            print(fraction_1.multiFractions(fraction_2))

        elif sign == "/":
            print(fraction_1.divFractions(fraction_2))

        else:
            raise ValueError("Неверная знак")

    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()