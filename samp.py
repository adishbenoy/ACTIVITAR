import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.multioutput import MultiOutputClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def predict(new_data):
    # Read CSV file into a pandas dataframe
    data = pd.read_csv(r'C:\Users\hp\OneDrive\Desktop\gym_manage_copy2\gym_manage_copy\gym_manage_copy\gym_manage\data.csv')

    # Convert target variable to DataFrame
    y = data[['Body Type', 'Food Plan', 'Diet Explanation', 'Workout', 'Workout Info']]

    # Select the features
    selected_features = ["Height (cm)", "Weight (kg)", "Calorie Intake", "Exercise Weekly", "Job"]
    X = data[selected_features]  # features

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Preprocessing: one-hot encoding for categorical variable 'Job' and standardization
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(drop='first'), ['Job']),
            ('num', StandardScaler(), ['Height (cm)', 'Weight (kg)', 'Calorie Intake', 'Exercise Weekly'])
        ])

    # Define the pipeline
    pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                               ('classifier', MultiOutputClassifier(KNeighborsClassifier()))])

    # Convert 'Job' column to lowercase
    X_train['Job'] = X_train['Job'].str.lower()
    X_test['Job'] = X_test['Job'].str.lower()
    new_data[4] = new_data[4].lower()  # Convert the job in new_data to lowercase

    # Define the parameter grid to search for the best k value
    param_grid = {'classifier__estimator__n_neighbors': range(1, 21)}

    # Perform grid search to find the best k value
    grid_search = GridSearchCV(pipeline, param_grid, cv=5)
    grid_search.fit(X_train, y_train)

    # Get the best k value
    best_k = grid_search.best_params_['classifier__estimator__n_neighbors']

    # Train the classifier with the best k value
    pipeline.set_params(classifier__estimator__n_neighbors=best_k)
    pipeline.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = pipeline.predict(X_test)


    # Make predictions on new data
    new_data_df = pd.DataFrame([new_data], columns=selected_features)
    predictions = pipeline.predict(new_data_df)

    return predictions[0]


