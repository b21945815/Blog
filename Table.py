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
    st.title("Car")
    data = pd.read_csv("car_price.csv")
    data = data[["year", "mileage", "tax", "mpg", "price"]]
    st.subheader("Prod. year distribution")
    year_graph = pd.DataFrame(data['year'].value_counts())
    st.bar_chart(year_graph)  # We place our chart in container named dataset
    st.write(data.head())  # We place our dataset's head in container named dataset below the graph

with modelTraining:
    st.title("Input to estimate the car's price")
    model = trained_model(data)

    left_column, right_column, extra = st.columns(3)  # We need columns to add side by side
    left_column2, right_column2 = st.columns(2)  # These columns are one below the previous columns
    # Input with sliders
    year = left_column.slider("Give the Prod. year", min_value=1900, max_value=2023, step=1, value=2000)
    tax = right_column.slider("Give the tax", min_value=0, max_value=600, step=5, value=300)
    # Input with text box
    # Values written in these sliders/number_input boxes are returned as values.
    mileage = left_column2.number_input("Give the mileage", step=500.0, format="%.1f")
    mpg = right_column2.number_input("Give the Miles per Gallon", step=1.0, format="%.1f")
    extra.selectbox("Just want to show this", options=[100, 200], index=1)






