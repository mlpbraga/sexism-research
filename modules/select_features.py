import pandas as pd
import numpy as np

DEFAULT_COLUMNS = ['likes','dislikes', 'char-qty', 'word-qty', 'sexist']
def select_features(dataframe, sub=None, column=None, columns=[]):
    if sub is not None:
        X_df = dataframe[dataframe.columns[:dataframe.shape[1] - sub - 1]]
        M = np.concatenate([X_df], axis=1)
        X = pd.DataFrame(M)
    elif column == 'tf':
        X_df = dataframe[dataframe.columns[:dataframe.shape[1] - 5]]
        M = np.concatenate([X_df], axis=1)
        X = pd.DataFrame(M)
    elif column == 'tf-sexist':
        X_df = dataframe[dataframe.columns[:100]]
        M = np.concatenate([X_df], axis=1)
        X = pd.DataFrame(M)
    elif column == 'tf-no-sexist':
        X_df = dataframe[dataframe.columns[100:200]]
        M = np.concatenate([X_df], axis=1)
        X = pd.DataFrame(M)
    elif column is not None:
        X_df = dataframe[dataframe.columns[list(dataframe.columns).index(column)]]
        M = np.concatenate([X_df])
        X = pd.DataFrame(M)
    elif columns != []:
        list_features = [dataframe[dataframe.columns[list(dataframe.columns).index(x)]] for x in columns]
        X = pd.DataFrame(list_features).transpose()

    return X
