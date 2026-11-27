'''
Лабораторна робота №6
Об'єктно-орієнтоване проєктування чисельних методів інтегрування в Python
Панков Максим
Студент групи №2
Номер варіанта: 9
'''
"""Головний модуль запуску чисельного інтегрування."""
import math
from integrators import (RectangleIntegrator,SimpsonIntegrator,TrapezoidIntegrator,)
global x

def test_function(x):
    """Тестова функція для перевірки методу"""
    if abs(x)<=1e-8:
        return -0.5
    return (math.cos(x)-1)/(x**2)
    
def target_function(x):
    """Підінтегральна функція згідно з індивідуальним варіантом."""
    return math.sin(2*x)*math.exp(-x**2)

def main():
    """Точка входу програми."""
    a=0
    b=1
    eps=1e-4
    print("Тестова функція:")
    print(RectangleIntegrator(test_function,a,b).adaptive_integrate(eps,2))
    print(TrapezoidIntegrator(test_function,a,b).adaptive_integrate(eps,2))
    print(SimpsonIntegrator(test_function,a,b).adaptive_integrate(eps,2))
    a=1
    b=2
    eps=0.00007
    print("Функція, та що із заданого варіанту")
    print(RectangleIntegrator(target_function,a,b).adaptive_integrate(eps,2))
    print(TrapezoidIntegrator(target_function,a,b).adaptive_integrate(eps,2))
    print(SimpsonIntegrator(target_function,a,b).adaptive_integrate(eps,2))
    eps*=0.1
    print("Функція, та що із заданого варіанту та з видозміненим ε")
    print(RectangleIntegrator(target_function,a,b).adaptive_integrate(eps,2))
    print(TrapezoidIntegrator(target_function,a,b).adaptive_integrate(eps,2))
    print(SimpsonIntegrator(target_function,a,b).adaptive_integrate(eps,2))
if __name__ == "__main__":
    main()
