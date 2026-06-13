# House-Price-Prediction-using-Linear-Regression
A machine learning project that predicts house prices using Linear Regression based on features such as house size and number of rooms.

## Overview

House Price Prediction is a Machine Learning project developed using Python and Scikit-Learn. The project uses Linear Regression to predict house prices based on important features such as the number of rooms and house size. The objective is to understand the fundamentals of supervised machine learning and predictive analytics.

---

## Features

* Load and analyze housing dataset
* Data preprocessing using Pandas
* Train-Test Split
* Linear Regression Model Training
* House Price Prediction
* Model Evaluation using Mean Absolute Error (MAE)
* Data Visualization using Matplotlib
* Interactive user input for price prediction

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib

---

## Project Structure

```text
House-Price-Prediction/
│
├── house_price_prediction.py
├── house_data.csv
├── requirements.txt
├── README.md
└── report.txt
```

---

## Dataset

Sample Dataset Structure:

| Rooms | Size (sq ft) | Price   |
| ----- | ------------ | ------- |
| 2     | 800          | 2500000 |
| 3     | 1200         | 4000000 |
| 4     | 1500         | 5500000 |
| 5     | 2000         | 7500000 |

---

## Installation

Install required libraries:

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python house_price_prediction.py
```

---

## Workflow

1. Load housing dataset.
2. Select features and target variable.
3. Split data into training and testing sets.
4. Train the Linear Regression model.
5. Evaluate model performance.
6. Predict house prices using user input.
7. Visualize the relationship between house size and house price.

---

## Model Evaluation

The model is evaluated using:

* Mean Absolute Error (MAE)

A lower MAE indicates better prediction accuracy.

---

## Example Output

```text
Enter number of rooms: 3
Enter house size (sq ft): 1400

Predicted House Price: ₹4,800,000
```

---

## Learning Outcomes

* Understanding Supervised Machine Learning
* Working with Real-World Datasets
* Data Preprocessing
* Model Training and Evaluation
* Predictive Analytics
* Data Visualization

---

## Future Improvements

* Larger Housing Dataset
* Multiple Regression Features
* House Location Integration
* Advanced Machine Learning Algorithms
* Web-Based Prediction System

---

## Conclusion

This project demonstrates the implementation of Linear Regression for house price prediction. It provides practical experience in machine learning, data preprocessing, model evaluation, and predictive analytics using Python.
