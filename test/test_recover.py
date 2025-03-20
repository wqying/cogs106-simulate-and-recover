import unittest
import numpy as np
from src.model.recover import recover_parameters
from src.model.simulate import simulate_data


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
        """
        Test recovery function behavior when given extreme R_obs values (0 or 1).
        """
        self.assertIsNone(recover_parameters(0, 0.5, 0.02))
        self.assertIsNone(recover_parameters(1, 0.5, 0.02))

    def test_bias_without_noise(self):
        """
        Test if bias is exactly 0 when observed values match predicted values.
        """
        # Choose arbitrary true parameters
        alpha_true, nu_true, tau_true = 1.2, 1.5, 0.3

        # Compute predicted values directly from the equations (no noise)
        y = np.exp(-alpha_true * nu_true)
        R_pred = 1 / (y + 1)
        M_pred = tau_true + (alpha_true / (2 * nu_true)) * ((1 - y) / (1 + y))
        V_pred = (alpha_true / (2 * (nu_true ** 3))) * ((1 - (2 * alpha_true * nu_true * y) - y ** 2) / (y + 1) ** 2)

        # Since there's no noise, recovered parameters should match the true ones exactly
        recovered_params = recover_parameters(R_pred, M_pred, V_pred)
        self.assertIsNotNone(recovered_params)
        alpha_est, nu_est, tau_est = recovered_params

        # Check that bias is exactly 0
        self.assertAlmostEqual(alpha_true, alpha_est, places=6)
        self.assertAlmostEqual(nu_true, nu_est, places=6)
        self.assertAlmostEqual(tau_true, tau_est, places=6)
        

if __name__ == "__main__":
    unittest.main()
