OK_FORMAT = True

test = {   'name': 'q2',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> theta_p = np.array([0.0, 0.0])\n'
                                               '>>> X_p = np.array([[1, 1], [1, -1]])\n'
                                               '>>> y_p = np.array([1, 0])\n'
                                               ">>> assert np.isclose(sigmoid(0), 0.5), 'Sigmoid at 0 should be 0.5'\n"
                                               ">>> assert np.isclose(cost_function(theta_p, X_p, y_p), 0.6931, atol=0.001), 'Initial cost should be approximately 0.6931'\n",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 2.0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
