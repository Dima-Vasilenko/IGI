from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
import datahandler

class FigureColor:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value):
        self._color = value

class Figure(ABC):
    def __init__(self, color):
        self.color = FigureColor(color)
    
    @abstractmethod
    def area(self):
        pass

class Rectangle(Figure):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = FigureColor(color) 
    
    def area(self):
        return self.width * self.height

class Square(Figure):
    def __init__(self, size, color):
        self.size = size
        self.color = FigureColor(color) 
    
    def area(self):
        return self.size * self.size

class Circle(Figure):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = FigureColor(color) 
    
    def area(self):
        return self.radius**2 * math.pi

class Diamond(Figure):
    def __init__(self, side, angel,  color):
        self.side = side
        self.angel = angel
        self.color = FigureColor(color) 
    
    def area(self):
        return self.side**2 * math.sin(self.angel)

class Triangel(Figure):
    def __init__(self, a, b, angel,  color):
        self.a = a
        self.b = b
        self.angel = angel
        self.color = FigureColor(color) 
    
    def area(self):
        return self.a * self.b * 0.5 * math.sin(self.angel)

class InfoMixin:
    def __init__(self, *args, **kwargs):    
        super().__init__(*args, **kwargs)

    def get_info(self):
        """Возвращает информацию"""
        return "{} color: {} and it's area: {}".format(self.get_name(), self.color.color, self.area())

class Hexagon(InfoMixin, Figure):
    def __init__(self, name, side, color):
        super().__init__(color)
        self.side = side
        self.name = name

    def get_name(self):
        """Возвращает имя"""
        return self.name
    
    def area(self):
        """Вычисляет площадь"""
        return self.side**2 * 3 * math.sqrt(3) / 2

    def get_vertices(self):
        """Вычисляет вершины шестиугольника"""
        vertices = []
        for i in range(6):
            angle = math.pi / 2 + i * math.pi / 3
            x = self.side * math.cos(angle)
            y = self.side * math.sin(angle)
            vertices.append((x, y))
        return vertices
    
    def draw(self):
        """Рисует шестиугольник"""
        fig, ax = plt.subplots(figsize=(8, 8))
        
        vertices = self.get_vertices()
        
        hexagon = patches.Polygon( vertices, closed=True, linewidth=2, edgecolor='black', facecolor=self.color.color)
        
        ax.add_patch(hexagon)

        margin = self.side * 1.2
        ax.set_xlim(-margin, margin)
        ax.set_ylim(-margin, margin)
        ax.set_aspect('equal')

        ax.grid(True)
        ax.set_title(self.get_name())
        plt.show()
        plt.savefig("hexagon.jpeg")


class FigureHandler:
    def __init__(self):
        pass

    def accure(self):
        side = datahandler.DataHandler.get_float("Введите значение длины стороны шестиугольника: ")
        name = input("Введите название фигуры: ")
        color = input("Введите значение цвета: ")
        hexagon = Hexagon(name, side, color)
        print(hexagon.get_info())
        hexagon.draw()