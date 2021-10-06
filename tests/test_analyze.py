import matplotlib.pyplot as plt
import blah

def test_plot(show_plot):
    s = blah.Simulation()
    u = s.calculate()
    blah.az.plotheatmap(u[40, ...], 40, s.delta_t)

    if show_plot:
        plt.show()

def test_animate(show_plot):
    s = blah.Simulation()
    u = s.calculate()
    a = blah.az.animate(u, s.delta_t)
    if show_plot:
        plt.show()
