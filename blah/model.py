import numpy as np


class Simulation:
    plate_length = 50
    max_iter_time = 50

    alpha = 2
    delta_x = 1

    delta_t = (delta_x**2) / (4 * alpha)
    gamma = (alpha * delta_t) / (delta_x**2)

    def __init__(self):
        # Initial condition everywhere inside the grid
        self.u_initial = 0

        # Initialize solution: the grid of u(k, i, j)
        self.u = np.full(
            (self.max_iter_time, self.plate_length, self.plate_length), self.u_initial)

        # Boundary conditions
        self.u_top = 100.0
        self.u_left = 0.0
        self.u_bottom = 0.0
        self.u_right = 0.0

        # Set the boundary conditions
        self.u[:, (self.plate_length - 1):, :] = self.u_top
        self.u[:, :, :1] = self.u_left
        self.u[:, :1, 1:] = self.u_bottom
        self.u[:, :, (self.plate_length - 1):] = self.u_right

    def calculate(self):
        mu = self.u.copy()

        for k in range(0, self.max_iter_time - 1, 1):
            for i in range(1, self.plate_length - 1, self.delta_x):
                for j in range(1, self.plate_length - 1, self.delta_x):
                    mu[k + 1, i, j] = self.gamma * (mu[k][i + 1][j] + mu[k][i - 1][j] +
                                         mu[k][i][j + 1] + mu[k][i][j - 1] -
                                         4 * mu[k][i][j]) + mu[k][i][j]

        return mu

