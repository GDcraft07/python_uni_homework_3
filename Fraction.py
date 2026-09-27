class Fraction:
    @staticmethod
    def gcd(number_1: int, number_2: int) -> int:
        while number_2:
            number_1, number_2 = number_2, number_1 % number_2

        return number_1 if number_1 >= 0 else -number_1


    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

        if self.denominator == 0:
            raise ZeroDivisionError("Знаменатель равен нулю")

        if self.denominator < 0:
            self.denominator *= -1
            self.numerator *= -1

        numerator_denominator_gcd = self.gcd(self.numerator, self.denominator)
        
        self.numerator //= numerator_denominator_gcd
        self.denominator //= numerator_denominator_gcd


    def __str__(self) -> str:
        if self.denominator == 1 or self.numerator == 0:
            return f"{self.numerator}"
        
        if self.numerator > 0:
            if self.numerator > self.denominator:
                return f"{self.numerator // self.denominator} {self.numerator - (self.numerator // self.denominator)}/{self.denominator}"

            return f"{self.numerator}/{self.denominator}"

        else:
            abs_numerator = -self.numerator
            if abs_numerator > self.denominator:
                return f"-{abs_numerator // self.denominator} {abs_numerator - (abs_numerator // self.denominator)}/{self.denominator}"
            
            return f"{self.numerator}/{self.denominator}"


    def sumFractions(self, other):
        other_numerator, other_denominator = other.getInfo()
        return Fraction(self.numerator * other_denominator + other_numerator * self.denominator, self.denominator * other_denominator)


    def multiFractions(self, other):
        other_numerator, other_denominator = other.getInfo()
        return Fraction(self.numerator * other_numerator, self.denominator * other_denominator)


    def subFractions(self, other):
        return self.sumFractions(other.multiFractions(-1, 1))


    def divFractions(self, other):
        other_numerator, other_denominator = other.getInfo()
        return self.multiFractions(Fraction(other_denominator, other_numerator))


    def getInfo(self) -> tuple:
        return (self.numerator, self.denominator)
    