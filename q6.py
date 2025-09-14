OK_FORMAT = True

test = {   'name': 'q6',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> def test_recall_threshold():\n'
                                               '...     X_train_normal = X_train[y_train == 0]\n'
                                               "...     model = KernelOneClassSVM(kernel='rbf', gamma=0.1, nu=0.05)\n"
                                               '...     model.fit(X_train_normal)\n'
                                               '...     y_pred = model.predict(X_test)\n'
                                               '...     y_pred_binary = np.where(y_pred == -1, 1, 0)\n'
                                               "...     recall = recall_score(y_test, y_pred_binary, average='macro')\n"
                                               "...     assert recall >= 0.5, f'Recall too low: got {recall}'\n"
                                               '>>> test_recall_threshold()\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 2}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
