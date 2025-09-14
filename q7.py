OK_FORMAT = True

test = {   'name': 'q7',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> def test_gini_impurity_pure_node():\n'
                                               '...     dt = DecisionTreeFromScratch()\n'
                                               '...     y = np.array([1, 1, 1, 1])\n'
                                               "...     assert dt.gini_impurity(y) == 0.0, f'Gini impurity of a pure node should be 0, but got {dt.gini_impurity(y)}'\n"
                                               '>>> def test_best_split_simple_case():\n'
                                               '...     dt = DecisionTreeFromScratch()\n'
                                               '...     X = np.array([[1], [2], [3], [10], [11], [12]])\n'
                                               '...     y = np.array([0, 0, 0, 1, 1, 1])\n'
                                               '...     feat, thresh = dt._best_split(X, y)\n'
                                               '...     assert feat == 0\n'
                                               "...     assert 3 <= thresh <= 10, f'Threshold should be between 3 and 10, but got {thresh}'\n"
                                               '>>> test_best_split_simple_case()\n'
                                               '>>> test_gini_impurity_pure_node()\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 4}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
