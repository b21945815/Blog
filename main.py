import streamlit as st
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression

Header1 = st.container()
Header2 = st.container()
Header3 = st.container()


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


with Header1:
    st.title("ML model for the price of cars")
    st.text("This project was made to set an example for people.")
with Header2:
    st.header("Section for inputs")
    inputProdYear, inputTax = st.columns(2)  # This way we can add side by side
    inputMileage, inputMPG = st.columns(2)  # These will be under the columns we made in number 2
    # I am adding 2 slider
    year = inputProdYear.slider("Give the Prod. year", min_value=1900, max_value=2023, step=1, value=2000)
    tax = inputTax.slider("Give the tax", min_value=0, max_value=600, step=5, value=300)
    # I am adding two number input box
    mileage = inputMileage.number_input("Give the mileage", step=500.0, format="%.1f")
    mpg = inputMPG.number_input("Give the Miles per Gallon", step=1.0, format="%.1f")
    # The inputs that were entered by using these sliders and number
with Header3:
    model = trained_model()
    st.header("Output")
    st.text("If you have the actual result, can you write it?")
    predict_button = st.button("Show the prediction")
    output = st.container()
    if predict_button:
        output.write(model.predict([[year, mileage, tax, mpg]]))  # Displaying the prediction
    # To get feedback
    st.write("If you have the actual result, can you write it?")
    number = st.number_input("Actual result", step=10.0, format="%.2f")
    getRealButton = st.container()
    if getRealButton.button("I wrote the actual result"):
        print("Here you can save the actual result with the model's prediction for later comparison")

