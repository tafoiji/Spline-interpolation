import matplotlib.pylab as wndpl
import matplotlib.pyplot as plt
import numpy as np
import os

#plt.style.use('_mpl-gallery')

for file_name in os.listdir():
    if file_name.endswith('.txt'):
        file_path = os.path.join('', file_name)
        x = []
        y = []
        with open(file_path) as f:
            for line in f:
                data = line.split()
                x.append(float(data[0]))
                y.append(float(data[1]))

        plt.xscale('log')

        plt.clf()
        plt.plot(x, y)  # marker='o' для отображения точек на графике
        if (file_path[:file_path.find('.')] == 'spline'):
            x = np.linspace(-2, 2, 10000)
            y = x**3 * np.cos(3 * x - 1)
            plt.plot(x, y, color="pink")
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid(True)
        fig = wndpl.gcf()
        fig.canvas.manager.set_window_title(file_path[:file_path.find('.')])
        plt.show()
        plt.clf()
