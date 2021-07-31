import joblib
from preprocessing.cleaning_data import cleaning_data
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor


def model():
    ds = cleaning_data()
    ds = ds.select_dtypes(exclude=['object'])
    X = ds.drop(['price', 'location'], axis=1)
    y = ds['price']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    GB = GradientBoostingRegressor(n_estimators=200, max_depth=4, min_samples_split=2, learning_rate=0.1, loss='ls')
    GB.fit(X_train, y_train)
    score = GB.score(X_test, y_test)
    y_predict = GB.predict(X_test)

    print(f'score:{score}')

    joblib.dump(GB, 'model_GB.pkl')
    GB = joblib.load('model_GB.pkl')

    model_columns = list(X.columns)
    joblib.dump(model_columns, 'model_columns.pkl')
    print("Models columns dumped!", model_columns)


estim = model()
estim
