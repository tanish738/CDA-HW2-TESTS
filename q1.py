OK_FORMAT = True

test = {   'name': 'q1',
    'points': None,
    'suites': [   {   'cases': [   {'code': ">>> assert np.isclose(sigmoid(0), 0.5), 'Sigmoid at 0 should be 0.5'\n", 'hidden': False, 'locked': False, 'points': 0.5},
                                   {   'code': ">>> assert np.isclose(sigmoid(10), 0.9999546, atol=1e-05), 'Sigmoid at 10 should be approximately 0.9999546'\n",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.5}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
