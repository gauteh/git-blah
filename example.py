import matplotlib.pyplot as plt
import blah

s = blah.Simulation()
u = s.calculate()
a = blah.az.animate(u, s.delta_t)
plt.show()
