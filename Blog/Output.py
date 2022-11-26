import streamlit as st
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression


@st.cache
def trained_model():
    data = pd.read_csv("Blog\1.csv")
    data = data[["potassium", "chloride", "pco2", "po2", "hemoglobin"]]
    x = data.dropna(subset=['hemoglobin']).drop("hemoglobin", axis=1)
    y = data.dropna(subset=['hemoglobin'])['hemoglobin']
    impute = SimpleImputer()
    transformed = impute.fit_transform(x)
    new_model = LinearRegression()
    new_model.fit(transformed, y)
    return new_model


#  Changing the background color

modelTraining = st.container()
with modelTraining:
    st.title("Input to estimate the hemoglobin ratio on people who do not have sepsis")
    model = trained_model()

    left_column, right_column = st.columns(2)  # We need columns to add side by side
    left_column2, right_column2 = st.columns(2)  # These columns are one below the previous columns
    # Input with sliders
    potassium = left_column.slider("Give the potassium", min_value=0.0, max_value=10.0, step=0.1, value=5.0)
    chloride = right_column.slider("Give the chloride", min_value=50.0, max_value=150.0, step=1.0, value=70.0)
    # Input with text box

    pco2 = left_column2.number_input("Give the PCO2", step=0.1, format="%.1f")
    co2 = right_column2.number_input("Give the CO2", step=0.1, format="%.1f")

    predict_button = st.button("Show the prediction")
    prediction = st.container()
    if predict_button:
        prediction.write(model.predict([[potassium, chloride, pco2, co2]]))
    st.write("If you have the actual result, can you write it?")
    number = st.number_input("Actual result", step=0.1, format="%.2f")
    real_resultButton = st.container()
    if real_resultButton.button("I wrote the actual result"):
        st.write("The actual result is ", number)
        # Here you can save the actual result with the model's prediction for later comparison.

st.markdown(
      """<style>.main {background-color: #FDE2E2;}</style>""",
      unsafe_allow_html=True
)
