import unittest
import numpy as np
from src.simulate import simulate_data


class TestSimulation(unittest.TestCase):
    def test_simulation_output(self):
        """
        Test if generated parameters and observed statistics are valid.
        """
        N = 4000  # Large N for stable output
        alpha, nu, tau, R_obs, M_obs, V_obs = simulate_data(N)

        # Ensure parameters are within expected ranges
        self.assertGreaterEqual(alpha, 0.5)
        self.assertLessEqual(alpha, 2)
        self.assertGreaterEqual(nu, 0.5)
        self.assertLessEqual(nu, 2)
        self.assertGreaterEqual(tau, 0.1)
        self.assertLessEqual(tau, 0.5)

        # Ensure observed statistics are valid
        self.assertGreater(R_obs, 0)
        self.assertLess(R_obs, 1)
        self.assertGreaterEqual(V_obs, 0)


if __name__ == "__main__":
    unittest.main()
