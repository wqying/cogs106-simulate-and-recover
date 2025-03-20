import unittest
import numpy as np
from src.recover import recover_parameters
from src.simulate import simulate_data  # Importing correct simulation function


class TestRecover(unittest.TestCase):
    def test_recovery_accuracy(self):
        """
        Test if recovered parameters are reasonably close to simulated ones.
        """
        N = 500  # Moderate N for stable recovery
        alpha_true, nu_true, tau_true, R_obs, M_obs, V_obs = simulate_data(N)  # Simulate observed data

        recovered_params = recover_parameters(R_obs, M_obs, V_obs)
        self.assertIsNotNone(recovered_params)  # Ensure function returns a result
        alpha_est, nu_est, tau_est = recovered_params

        # Check if recovered values are close to the originals
        self.assertAlmostEqual(alpha_true, alpha_est, delta=0.3)
        self.assertAlmostEqual(nu_true, nu_est, delta=0.2)
        self.assertAlmostEqual(tau_true, tau_est, delta=0.1)

    def test_invalid_input(self):
        """Test recovery function behavior when given extreme R_obs values (0 or 1)."""
        self.assertIsNone(recover_parameters(0, 0.5, 0.02))
        self.assertIsNone(recover_parameters(1, 0.5, 0.02))


if __name__ == "__main__":
    unittest.main()
