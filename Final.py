import streamlit as st
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression


@st.cache
def trained_model():
    data = pd.read_csv("car_price.csv")
    data = data[["year", "mileage", "tax", "mpg", "price"]]
    x = data.dropna(subset=['price']).drop("price", axis=1)
    y = data.dropna(subset=['price'])['price']
    impute = SimpleImputer()
    transformed = impute.fit_transform(x)
    new_model = LinearRegression()
    new_model.fit(transformed, y)
    return new_model


modelTraining = st.container()
with modelTraining:
    st.title("Input to estimate the car's price")
    model = trained_model()

    left_column, right_column = st.columns(2)  # We need columns to add side by side
    left_column2, right_column2 = st.columns(2)  # These columns are one below the previous columns
    # Input with sliders
    year = left_column.slider("Give the Prod. year", min_value=1900, max_value=2023, step=1, value=2000)
    tax = right_column.slider("Give the tax", min_value=0, max_value=600, step=5, value=300)
    # Input with text box
    mileage = left_column2.number_input("Give the mileage", step=500.0, format="%.1f")
    mpg = right_column2.number_input("Give the Miles per Gallon", step=1.0, format="%.1f")

    predict_button = st.button("Show the prediction")  # 1
    prediction = st.container()
    if predict_button:  # 2
        prediction.write(model.predict([[year, mileage, tax, mpg]]))  # 3
    st.write("If you have the actual result, can you write it?")
    number = st.number_input("Actual result", step=10.0, format="%.2f")
    real_resultButton = st.container()
    if real_resultButton.button("I wrote the actual result"):
        st.write("The actual result is ", number)
        # Here you can save the actual result with the model's prediction for later comparison.

