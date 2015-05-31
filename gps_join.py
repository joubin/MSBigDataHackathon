import numpy as np
import pandas as pd

from sklearn.neighbors import KDTree

def concat_features_by_neighbors(df_labels, df_features,
                                 X_names=['Offense Type'],
                                 grid=["Latitude", "Longitude"],
                                 radius=1./500.,
                                 scale=np.array([1.,1.])):

    df_labels = df_labels.dropna(subset=grid)
    df_features = df_features.dropna(subset=grid)

    X = df_features.as_matrix(X_names)
    xy_features = df_features.as_matrix(grid)
    xy_labels = df_labels.as_matrix(grid)
    tree = KDTree(xy_features*scale)

    vocabulary = set()
    features = []
    for nei in tree.query_radius(xy_labels*scale, radius):
        U,I = np.unique(X[nei], return_inverse=True)
        D = dict(zip(U,np.bincount(I)))
        map(vocabulary.add, D)
        features.append(D)

    return pd.concat([df_labels, pd.DataFrame([map(fi.get, vocabulary)
                      for fi in features],
                      index=df_labels.index,
                      columns=vocabulary).fillna(0.)], axis=1)
