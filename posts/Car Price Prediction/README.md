## Car Prize Predection
### Introduction
This project focuses on predicting car prices using a linear regression model. The dataset contains various features such as horsepower, peak RPM, curb weight, and others that influence the price of a car. By analyzing these features and cleaning the data, we build a model that accurately estimates car prices. This project demonstrates the process of data cleaning, exploration, and the application of linear regression to make predictions based on real-world data.

### Setup and Importing Libraries
```{python}
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score ,mean_absolute_error
import matplotlib.pyplot as plt
import seaborn as sns
```
