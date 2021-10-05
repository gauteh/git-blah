import matplotlib.pyplot as plt
import blah

def test_plot():
    s = blah.Simulation()
    u = s.calculate()
    blah.az.plotheatmap(u[40, ...], 40, s.delta_t)
    plt.show()

def test_animate():
    s = blah.Simulation()
    u = s.calculate()
    a = blah.az.animate(u, s.delta_t)
    plt.show()
