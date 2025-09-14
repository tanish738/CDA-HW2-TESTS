OK_FORMAT = True

test = {   'name': 'q3',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> theta_p = np.array([0.0, 0.0])\n'
                                               '>>> X_p = np.array([[1, 1], [1, -1]])\n'
                                               '>>> y_p = np.array([1, 0])\n'
                                               '>>> grad_p = gradient_update(theta_p, X_p, y_p)\n'
                                               ">>> assert np.allclose(grad_p, np.array([0.0, -0.5]), atol=1e-06), f'Expected gradient [0.0, -0.5], but got {grad_p}'\n",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 2.5}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
