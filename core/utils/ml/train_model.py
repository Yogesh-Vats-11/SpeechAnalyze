import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import joblib  
BASE_ML_DIR = 'core/utils/ml'

df = pd.read_csv(f'{BASE_ML_DIR}/data/synthetic_speech_defect_data.csv')

df.columns = df.columns.str.strip()

X = df[['Jitter (%)', 'Shimmer (%)', 'WPM (Words per Minute)', 'Pauses (Duration in sec)']]
y = df['Severity of Defect']

from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)  

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['Jitter (%)', 'Shimmer (%)', 'WPM (Words per Minute)', 'Pauses (Duration in sec)'])
    ]
)

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression())
])

param_grid = {
    'classifier__C': [0.1, 1, 10]
}

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy', n_jobs=-1)

grid_search.fit(X_train, y_train)

best_model = grid_search.best_estimator_

y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"\nBest Parameters: {grid_search.best_params_}")
print(f"Test Accuracy: {accuracy}")

joblib.dump(best_model, f'{BASE_ML_DIR}/model/model_speech_defect_logistic_regression.pkl')
joblib.dump(label_encoder, f'{BASE_ML_DIR}/model/label_speech_defect_logistic_regression.pkl')

print("\nModel saved successfully in 'core/utils/ml/model' directory.")
print("Label encoder saved successfully in 'core/utils/ml/model' directory.")