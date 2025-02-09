# Real-Estate-Price-Prediction

# Project Overview

This project is a machine learning-based web application that predicts real estate prices based on user input. The model considers features such as the number of bedrooms, bathrooms, and total area in square feet to provide an estimated price. The project is built using Python, Streamlit, and Scikit-Learn, making it easy to use and deploy.

# How It Works

The user enters details such as the number of bedrooms, bathrooms, and total house size (sq. ft.).
The input values are scaled and transformed to match the trained model's data.
The trained machine learning model predicts the estimated house price.
The predicted price is displayed in the application interface.

# Project Components

***1. Data Preprocessing & Cleaning (model.ipynb)***
Before training the model, the dataset was preprocessed to improve accuracy. The key steps included:

Handling missing data by either removing incomplete entries or filling them with appropriate values.
Selecting important features such as bedrooms, bathrooms, and house size for price prediction.
Normalizing the numerical features using StandardScaler to bring them to the same scale.
Identifying and removing outliers to prevent extreme values from skewing predictions.
Encoding categorical variables (if applicable) to ensure they are properly interpreted by the model.
Splitting the dataset into training and testing sets to evaluate model performance.

***2. Model Training (model.ipynb)***
Different machine learning models were tested, including Linear Regression, Decision Trees, and Random Forest, to find the best performer.

The final model was trained on the processed dataset and evaluated on test data.
Cross-validation and hyperparameter tuning were applied to improve accuracy.
The trained model (model.pkl) and the data scaler (scaler.pkl) were saved using joblib for deployment.

***3. Web App (app.py)***
The web application was built using Streamlit, which provides an interactive and user-friendly interface.

The app loads the pre-trained model and scaler to process user inputs.
Users enter the number of bedrooms, bathrooms, and house size in square feet.
The input is transformed using the scaler to match the trained model’s format.
The model predicts the price, which is displayed in the interface.
A “Predict” button triggers the calculation and presents the estimated price.

# Technologies Used

Python – Core programming language for data analysis and modeling.

Scikit-Learn – Used for training and evaluating the machine learning model.

Joblib – For saving and loading the trained model.

Streamlit – To create an interactive web application.

NumPy & Pandas – For data manipulation and preprocessing.

# How to Use the Project
To use this project, start by cloning the repository from GitHub. Open a terminal or command prompt and run the following command:

Then, navigate to the project directory:

Next, install the required dependencies using pip. Ensure you have Python 3.7+ installed before running:

Once the dependencies are installed, you can launch the web application using Streamlit by running:

This command will start a local web server, and the application will open in your browser.

To make a prediction, enter the number of bedrooms, bathrooms, and total house size in the input fields. Click the "Predict" button, and the estimated price will be displayed.

# Future Enhancements

Expand Feature Set: Incorporate additional factors such as house location, age of the property, and amenities.

Improve Model Accuracy: Experiment with more advanced machine learning models and hyperparameter tuning.

Enhance UI/UX: Improve the user interface with better visuals and interactive elements.

Deploy Online: Host the application using Streamlit Sharing, AWS, or Heroku for broader accessibility.

# Conclusion
This project demonstrates how machine learning can be used for real estate price prediction. It highlights key concepts such as data preprocessing, feature selection, model training, and deployment using Streamlit.

If you find this project useful, feel free to explore the code, contribute, or provide feedback! 🚀
