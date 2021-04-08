import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame({'x': [1, 2, 3],
                   'y': [4, 5, 6]})
x_max = st.slider('Max value of x', float(df['x'].max()))
st.title("My streamlit app")
st.markdown("""
Hey, you are cool
""")

df[df['x'] <= x_max]

st.markdown("""
Look at this shit
""")
a = st.slider('Amplitude', 0., 10.)
b = st.slider('Frequency', 0., 10.)
x = np.linspace(0,10, 500)
fig = plt.figure()
plt.plot(x, a * np.sin(x * b))
st.pyplot(fig)

uploaded_file = st.file_uploader("Drop file here")
if uploaded_file is not None:
    st.text(uploaded_file.getvalue().decode('utf-8'))
