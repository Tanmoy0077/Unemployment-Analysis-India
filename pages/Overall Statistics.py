import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.read_csv('Unemployment in India.csv', parse_dates=['Date'], dayfirst=True)
st.header("Overall statistics of all states")
with st.sidebar.form("get vals"):
    date = st.selectbox("Select the date", options=df['Date'].dt.date.unique())
    submitted = st.form_submit_button("Proceed")

    

if submitted:
    left, mid, right = st.tabs(['Estimated Unemployment Rate','Estimated Employed','Estimated Labour Participation Rate (%)'])
    temp = df[df.Date.dt.date == date]
    # Left
    fig = px.bar(temp, x='Estimated Unemployment Rate (%)', y='Region', color='Area', barmode='group', color_discrete_sequence=['#e82c48','#e3f51b'], title=f"Estimated Unemployment Rate (%) on {date}")
    left.plotly_chart(fig)

    fig = px.histogram(df, x='Estimated Unemployment Rate (%)', color='Area', color_discrete_sequence=['#d45f5f','#5f69d4'], title="Distribution of Estimated Unemployment Rate (%)")
    left.plotly_chart(fig)

    # Mid
    fig = px.bar(temp, x='Estimated Employed', y='Region', color='Area', barmode='group', color_discrete_sequence=['#e82c48','#e3f51b'],title=f"Estimated Employed on {date}")
    mid.plotly_chart(fig)

    fig = px.histogram(df, x='Estimated Employed', color='Area', color_discrete_sequence=['#d45f5f','#5f69d4'], title="Distribution of Estimated Employed")
    mid.plotly_chart(fig)

    # Right
    fig = px.bar(temp, x='Estimated Labour Participation Rate (%)', y='Region', color='Area', barmode='group', color_discrete_sequence=['#e82c48','#e3f51b'],title=f"Estimated Labour Participation Rate (%) on {date}")
    right.plotly_chart(fig)

    fig = px.histogram(df, x='Estimated Labour Participation Rate (%)', color='Area', color_discrete_sequence=['#d45f5f','#5f69d4'], title="Distribution of Estimated Labour Participation Rate (%)")
    right.plotly_chart(fig)
