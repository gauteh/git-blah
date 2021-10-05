import numpy as np


class Simulation:
    plate_length = 50
    max_iter_time = 50

    alpha = 2
    delta_x = 1

    delta_t = (delta_x**2) / (4 * alpha)
    gamma = (alpha * delta_t) / (delta_x**2)

    def __init__(self):
        # Initialize solution: the grid of u(k, i, j)
        self.u = np.empty(
            (self.max_iter_time, self.plate_length, self.plate_length))

        # Initial condition everywhere inside the grid
        self.u_initial = 0

        # Boundary conditions
        self.u_top = 100.0
        self.u_left = 0.0
        self.u_bottom = 0.0
        self.u_right = 0.0

        # Set the initial condition
        self.u.fill(self.u_initial)

        # Set the boundary conditions
        self.u[:, (self.plate_length - 1):, :] = self.u_top
        self.u[:, :, :1] = self.u_left
        self.u[:, :1, 1:] = self.u_bottom
        self.u[:, :, (self.plate_length - 1):] = self.u_right

    def calculate(self):
        u = self.u.copy()

        for k in range(0, self.max_iter_time - 1, 1):
            for i in range(1, self.plate_length - 1, self.delta_x):
                for j in range(1, self.plate_length - 1, self.delta_x):
                    u[k + 1, i,
                      j] = self.gamma * (u[k][i + 1][j] + u[k][i - 1][j] +
                                         u[k][i][j + 1] + u[k][i][j - 1] -
                                         4 * u[k][i][j]) + u[k][i][j]

        return u

