import numpy as np
import datahandler

class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = None


    def generate_matrix(self, a, b):
        """Генерирует матрицу n x m со случайными числами от a до b"""
        self.matrix = np.random.randint(a, b+1, size=(self.n, self.m))
    
    def get_secondary_diagonal(self):
        """Возвращает элементы побочной диагонали"""
        size = self.n if self.n <= self.m else self.m
        secondary = []
        for i in range(size):
            secondary.append(self.matrix[i][size - 1 - i])
        return secondary

    def get_min_element(self):
        """Получем минимальный элемент"""
        diag = self.get_secondary_diagonal()
        return min(diag)

    def variance_np(self):
        """Вычисляет дисперсию с помощью встроенных функций"""
        diag = self.get_secondary_diagonal()
        return round(np.var(diag), 2)
    
    def variance_formula(self):
        """Вычисляет дисперсию вручную по формуле"""
        diag = self.get_secondary_diagonal()
        n = len(diag)
        mean = sum(diag) / n
        sum_squared_diff = 0
        
        for x in diag:
            diff = x - mean
            sum_squared_diff += diff ** 2
        
        variance = sum_squared_diff / n
        return round(variance, 2)
    
class MatrixHandker:

    def generate_matrix(self):
        """Генерируем свою матрицу"""
        a = datahandler.DataHandler.get_float("Введите правую границу допустимости значений генерации: ")
        b = datahandler.DataHandler.get_float("Введите левую границу допустимости значений генерации: ")
        n = datahandler.DataHandler.get_int("Введите количество строк матрицы: ")
        m = datahandler.DataHandler.get_int("Введите количество столбцов матрицы: ")
        self.matrix = Matrix(n, m)
        self.matrix.generate_matrix(a, b)
    
    def get_results(self):
        """Запуск для получения результата"""
        print("Получившаяся матрциа: ")
        print(self.matrix.matrix)
        print("Минимальный элемент на побочной диагонали: ", self.matrix.get_min_element())
        print("Дисперсия матрицы вычисленная с использованием встроенной функции: ", self.matrix.variance_np())
        print("Дисперсия матрицы вычисленная с использованием формулы: ", self.matrix.variance_formula())

