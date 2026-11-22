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
def target_function(x):
    """Підінтегральна функція згідно з індивідуальним варіантом."""
    
    return math.sin(2*x)*math.exp(-x**2)
def main():
    """Точка входу програми."""

    a=1
    b=2
    print(RectangleIntegrator(target_function,a,b).integrate(2))
    print(TrapezoidIntegrator(target_function,a,b).integrate(2))
    print(SimpsonIntegrator(target_function,a,b).integrate(2))
if __name__ == "__main__":
    print(main())
