from constants import R_EARTH
import numpy as np
import matplotlib.pyplot as plt


def plot_simple(x, y):
    """Plots y vs x"""
    plt.plot(x,y)
    plt.show()

    
def plot_position_earth(x, y):
    """Plots Earth circumference and x-, y-position"""
    th = np.linspace(0, 2*np.pi,100)
    xearth = R_EARTH*np.cos(th)
    yearth = R_EARTH*np.sin(th)
    plt.plot(xearth, yearth)
    plt.plot(x[0], y[0], 'ko', x, y, x[-1], y[-1], 'r^')
    plt.axis('equal')
    plt.show()
