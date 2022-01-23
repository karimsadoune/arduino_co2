import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

def animate(i):
    # lire le ficher data.csv
    data = pd.read_csv('data.csv')
    t = data['t']
    x = data['x']
    # pour effacer les axes
    plt.cla()

    # pour creer le graph
    plt.plot(t, x, label='CO2')

    # pour attacher la legend a gauche du graph
    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()