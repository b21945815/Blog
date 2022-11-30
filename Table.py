import streamlit as st
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression


def trained_model(main_data):
    x = main_data.dropna(subset=['price']).drop("price", axis=1)
    y = main_data.dropna(subset=['price'])['price']
    impute = SimpleImputer()
    transformed = impute.fit_transform(x)
    new_model = LinearRegression()
    new_model.fit(transformed, y)
    return new_model


dataset = st.container()
modelTraining = st.container()

with dataset:
    data = pd.read_csv("car_price.csv")
    data = data[["year", "mileage", "tax", "mpg", "price"]]
    st.write(data.head())  # 1

with modelTraining:
    st.title("Input to estimate the car's price")
    model = trained_model(data)  # This is returning the trained model

    left_column, right_column = st.columns(2)  # 2
    left_column2, right_column2 = st.columns(2)  # 3
    year = left_column.slider("Give the Prod. year", min_value=1900, max_value=2023, step=1, value=2000)  # 4
    tax = right_column.slider("Give the tax", min_value=0, max_value=600, step=5, value=300)  # 4
    mileage = left_column2.number_input("Give the mileage", step=500.0, format="%.1f")  # 5
    mpg = right_column2.number_input("Give the Miles per Gallon", step=1.0, format="%.1f")  # 5
    # 6






