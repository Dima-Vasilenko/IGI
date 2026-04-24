import math
from collections import Counter
import matplotlib.pyplot as plt

class Calculating:
    def __init__(self, eps, graph):
        self.eps = eps
        self.sequence = []
        self.graph = graph

    def calculate(self, x):
        '''function that calculate cos seriese'''
        result = 0
        func_result = math.cos(x)
        for i in range(500):
            value = (-1)**i * (x ** (2*i)) / math.factorial(2*i)
            result += value
            self.sequence.append(value)
            if (abs(func_result - result) < self.eps):
                break
        return [x, i, result, func_result, self.eps]
    
    def average(self):
        return sum(self.sequence) / len(self.sequence)
    
    def mediana(self):
        sorted_seq = sorted(self.sequence)
        n = len(sorted_seq)
        mid = n // 2
        if n % 2 == 1:
            return sorted_seq[mid]
        else:
            return (sorted_seq[mid-1] + sorted_seq[mid]) / 2
    
    def moda(self):
        counter = Counter(self.sequence)
        max_count = max(counter.values())
        modes = [val for val, count in counter.items() if count == max_count]
        return modes if len(modes) > 1 else modes[0]

    def dispercy(self):
        if len(self.sequence) <= 1:
            return 0
        av_val = self.average()
        squared_diff = sum((x - av_val) ** 2 for x in self.sequence)
        return squared_diff / len(self.sequence)

    def sko(self):
        return math.sqrt(self.dispercy())
    
    def get_results(self, x):
        list_results = self.calculate(x)
        print("| x = ", list_results[0], "| n = ", list_results[1], "| F(x) = ", list_results[2], " | Math F(x) = ", list_results[3], " | eps = ", list_results[4], " |")
        print("Среднее значение последовательности: ", self.average())
        print("Медиана последовательности: ", self.mediana())
        print("Мода последовательности ", self.moda())
        print("Дисперсия последовательности ", self.dispercy())
        print("СКО последовательности: ", self.sko())
        print("Строю график....")
        self.graph.create(self)


class GriphBuilder:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.grid(True)
        self.ax.set_xlabel("OX")
        self.ax.set_ylabel("OY")
        self.ax.set_title("Comparing graphics")

    def create(self, calculater):
        start = 0
        x = []
        y = []
        y_true = []
        while start < 1:
            el = calculater.calculate(start)
            y.append(el[2])
            y_true.append(math.cos(start))
            x.append(start)
            start += 0.05
        line1 = self.ax.plot(x, y, 'b', linewidth=3, label="F(x)")[0]
        line2 = self.ax.plot(x, y_true, 'r', linewidth=3, label="cos(x)")[0]
        self.ax.legend(handles=[line1, line2])

        self.ax.text(0.5, -0.1, "отображение графиков\nкосинусов", transform=self.ax.transAxes, ha='center', va='top', fontsize=10)
    
        self.ax.annotate("График косинуса", xy=(0.1, 0.9), xycoords='axes fraction', xytext=(0.35, 0.7), textcoords='axes fraction', arrowprops=dict(arrowstyle="->"))
    


        plt.savefig("graphic.jpeg")
        plt.show()