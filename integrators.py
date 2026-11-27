"""Модуль реалізації класів чисельного інтегрування."""


class BaseIntegrator:
    """Базовий клас для чисельного обчислення визначених інтегралів."""
    order = 1
    method_name = "Базовий метод"

    def __init__(self, func, a, b):
        """Ініціалізує підінтегральну функцію та межі інтегрування."""
        self.func=func
        self.a=a
        self.b=b

    @classmethod

    def from_dict(cls, func, params):
        """Альтернативний конструктор для створення інтегратора зі словника."""
        a=params.get("a")
        b=params.get("b")
        cls.validate_bounds(a, b)
        return cls(func, a, b)
    
    @staticmethod

    def validate_bounds(a, b):
        """Перевіряє коректність меж інтегрування."""
        if a>=b:
            raise ValueError("Нижня межа a повинна бути меншою за верхню межу b.")
        
    def integrate(self, n):
        """Обчислює наближене значення інтеграла для n розбиттів."""
        raise NotImplementedError("Метод integrate має бути реалізований у підкласі.")
    
    def adaptive_integrate(self, eps, initial_n=2):
        """Знаходить інтеграл із заданою точністю eps за правилом Рунге."""
        n=initial_n
        integral_n=self.integrate(n)
        print(f'{self.method_name} на відрізку [{self.a};{self.b}] (порядок точності О(h^{self.order}))')
        print(f"n = {n} -> I = {integral_n:.7}")
        while True:
            n*=2
            integral_2n=self.integrate(n)
            print(f"n = {n} -> I = {integral_2n:.7f}")
            error_estimate=abs(integral_2n-integral_n)/(2**self.order-1)
            if error_estimate<eps:
                integral_2n+=error_estimate
                return f'Уточнений результат: {integral_2n:.7f} (n_min={n}, похибка ≈ {error_estimate:.2e})\n\n'
            integral_n=integral_2n

    def __str__(self):
        """Повертає рядкове представлення об'єкта інтегратора."""

        return f"{self.method_name}: [{self.a}, {self.b}]"


class RectangleIntegrator(BaseIntegrator):
    """Обчислення інтеграла складеною формулою середніх прямокутників."""
    order = None
    method_name = "Формула прямокутників"

    def __init__(self, func, a, b):
        super().__init__(func, a, b)
        self.order=2

    def integrate(self, n):
        h=(self.b-self.a)/n
        integral=0
        for i in range(n):
            x=self.a+(i+0.5)*h
            integral+=self.func(x)
        integral*=h
        return integral


class TrapezoidIntegrator(BaseIntegrator):
    """Обчислення інтеграла складеною формулою трапецій."""
    order = None
    method_name = "Формула трапецій"

    def __init__(self, func, a, b):
        super().__init__(func, a, b)
        self.order=2

    def integrate(self, n):
        if ZeroDivisionError==True:
            a+=0.00001
        h=(self.b-self.a)/n
        integral=0.5*(self.func(self.a)+self.func(self.b))
        for i in range(1,n):
            x=self.a+i*h
            integral+=self.func(x)
        integral*=h
        return integral


class SimpsonIntegrator(BaseIntegrator):
    """Обчислення інтеграла складеною формулою Сімпсона."""
    order = None
    method_name = "Формула Сімпсона"
    
    def __init__(self, func, a, b):
        super().__init__(func, a, b)
        self.order=4
    
    def integrate(self, n):
        h=(self.b-self.a)/n
        integral=self.func(self.a)+self.func(self.b)
        for i in range(1, n, 2):
            x=self.a+i*h
            integral+=4*self.func(x)
        for i in range(2, n, 2):
            x=self.a+i*h
            integral+=2*self.func(x)
        integral*=h/3
        return integral