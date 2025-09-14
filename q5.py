OK_FORMAT = True

test = {   'name': 'q5',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> def test_kernel_function():\n'
                                               '...     model = KernelOneClassSVM()\n'
                                               '...     X1 = np.array([[0.0], [1.0]])\n'
                                               '...     X2 = np.array([[0.0], [2.0]])\n'
                                               '...     model.gamma = 0.5\n'
                                               '...     expected = np.array([[1.0, np.exp(-0.5 * 4.0)], [np.exp(-0.5 * 1.0), np.exp(-0.5 * 1.0)]])\n'
                                               '...     result = model._kernel_function(X1, X2)\n'
                                               "...     assert np.allclose(result, expected), f'Kernel mismatch: expected {expected}, got {result}'\n"
                                               '>>> def test_objective():\n'
                                               '...     model = KernelOneClassSVM()\n'
                                               '...     model.K_train = np.array([[2.0, 0.5], [0.5, 1.0]])\n'
                                               '...     mu = np.array([0.3, 0.7])\n'
                                               '...     expected = 0.5 * mu.T @ model.K_train @ mu\n'
                                               '...     result = model._objective(mu)\n'
                                               "...     assert np.isclose(result, expected), f'Objective mismatch: expected {expected}, got {result}'\n"
                                               '>>> def test_objective_gradient():\n'
                                               '...     model = KernelOneClassSVM()\n'
                                               '...     model.K_train = np.array([[2.0, 0.5], [0.5, 1.0]])\n'
                                               '...     mu = np.array([0.3, 0.7])\n'
                                               '...     expected = np.array([2.0 * 0.3 + 0.5 * 0.7, 0.5 * 0.3 + 1.0 * 0.7])\n'
                                               '...     result = model._objective_gradient(mu)\n'
                                               "...     assert np.allclose(result, expected), f'Gradient mismatch: expected {expected}, got {result}'\n"
                                               '>>> test_kernel_function()\n'
                                               '>>> test_objective()\n'
                                               '>>> test_objective_gradient()\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 7}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
