import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation


def plotheatmap(u_k, k, delta_t):
    # Clear the current plot figure
    plt.clf()

    plt.title(f"Temperature at t = {k*delta_t:.3f} unit time")
    plt.xlabel("x")
    plt.ylabel("y")

    # This is to plot u_k (u at time-step k)
    plt.pcolormesh(u_k, cmap=plt.cm.jet, vmin=0, vmax=100)
    plt.colorbar()

    return plt



def animate(u, delta_t, max_iter_time = 50):
    def inner_animate(k):
        plotheatmap(u[k], k, delta_t)

    anim = FuncAnimation(plt.figure(),
                        inner_animate,
                        interval=1,
                        frames=max_iter_time,
                        repeat=False)
    return anim
    # plt.show()
    # anim.save("heat_equation_solution.gif")
