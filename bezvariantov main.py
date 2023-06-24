class CustomException1(BaseException):
    pass

class CustomException2(BaseException):
    pass

class CustomException3(BaseException):
    pass

class Calculator:
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Деление на ноль недопустимо")
        return a / b

    def power(self, x, n):
        if n < 0:
            raise ValueError("Негативные значения не поддерживаются")
        return x ** n

    def sqrt(self, x):
        if x < 0:
            raise ValueError("Квадратный корень из отрицательного числа не определен")
        return math.sqrt(x)
        
class CalculatorHandler:
    def __init__(self):
        self.calculator = Calculator()

    def perform_division(self, a, b):
        try:
            result = self.calculator.divide(a, b)
            return result
        except ValueError as e:
            print("Ошибка при делении:", str(e))
            return None

    def perform_power(self, x, n):
        try:
            result = self.calculator.power(x, n)
            return result
        except ValueError as e:
            print("Ошибка при возведении в степень:", str(e))
            return None

    def perform_sqrt(self, x):
        try:
            result = self.calculator.sqrt(x)
            return result
        except ValueError as e:
            print("Ошибка при вычислении квадратного корня:", str(e))
            return None