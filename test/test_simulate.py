import unittest
from src.simulate import simulate_data

class TestSimulation(unittest.TestCase):
    def test_simulation_output(self):
        N = 100
        alpha, nu, tau = 1.0, 1.0, 0.3
        R_obs, M_obs, V_obs = simulate_data(N, alpha, nu, tau)
        self.assertGreater(R_obs, 0)
        self.assertLess(R_obs, 1)