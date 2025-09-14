OK_FORMAT = True

test = {   'name': 'q8',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> def test_knn_simple_case():\n'
                                               '...     """\n'
                                               '...     Case 1: Simple linearly separable dataset\n'
                                               '...     Expect predictions to perfectly match since k=1.\n'
                                               '...     """\n'
                                               '...     X_train = np.array([[1], [2], [3], [10], [11], [12]])\n'
                                               '...     y_train = np.array([0, 0, 0, 1, 1, 1])\n'
                                               '...     model = KNNFromScratch(k=1)\n'
                                               '...     model.fit(X_train, y_train)\n'
                                               '...     X_test = np.array([[2], [11]])\n'
                                               '...     preds = model.predict(X_test)\n'
                                               "...     assert np.array_equal(preds, np.array([0, 1])), f'Expected [0,1], got {preds}'\n"
                                               '>>> def test_knn_with_k3_majority():\n'
                                               '...     """\n'
                                               '...     Case 2: Test majority voting with k=3.\n'
                                               '...     """\n'
                                               '...     X_train = np.array([[0], [1], [2], [10], [11], [12]])\n'
                                               '...     y_train = np.array([0, 0, 1, 1, 1, 0])\n'
                                               '...     model = KNNFromScratch(k=3)\n'
                                               '...     model.fit(X_train, y_train)\n'
                                               '...     X_test = np.array([[1], [11]])\n'
                                               '...     preds = model.predict(X_test)\n'
                                               '...     expected = np.array([0, 1])\n'
                                               "...     assert np.array_equal(preds, expected), f'Expected {expected}, got {preds}'\n"
                                               '>>> test_knn_simple_case()\n'
                                               '>>> test_knn_with_k3_majority()\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 4}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
