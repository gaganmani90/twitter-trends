# importing the required module 
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, year=None, salary=None):
        if year is None:
            year = []
        if salary is None:
            salary = []
        self._x = year
        self._y = salary

    def draw_graph(self, title, x_label, y_label):
        plt.plot(self._x, self._y)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
