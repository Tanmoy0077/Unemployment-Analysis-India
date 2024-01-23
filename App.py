import pandas as pd
import streamlit as st
import plotly.express as px

def plot_line(data, x, y, color, cmap, pos):
    pos.subheader(f"{y} during 2019 - 2020")
    g = px.line(data, x=x, y=y, color=color, markers=True,color_discrete_sequence=cmap)
    pos.plotly_chart(g)

def plot_area(data, x, y, color, cmap, pos):
    pos.subheader(f"Area plot of {y}")
    g = px.area(data, x=x, y=y, color=color,color_discrete_sequence=cmap)
    pos.plotly_chart(g)


def plot_hist(data, x,color, cmap, pos):
    pos.subheader(f"Distribution of {x}")
    g = px.histogram(data, x=x, color=color, color_discrete_sequence=cmap)
    pos.plotly_chart(g)

def plot_box(data, x, color, cmap, pos):
    pos.subheader(f"Box Plot of {x}")
    g = px.box(data, x=x, color=color, color_discrete_sequence=cmap)
    pos.plotly_chart(g)

def plot_all(data, d, pos):
    plot_line(data, "Date", d, "Area", ['#fad902','#5e026e'], pos)
    plot_area(data,'Date', d, 'Area', ['#24bf74','#214c9c'], pos)
    plot_hist(data, d, 'Area', ['#d45f5f','#5f69d4'], pos)
    plot_box(data, d,'Area', ['#06ba15','#064eba'], pos)

st.set_page_config(page_title="Unemployment Rates in India")
df = pd.read_csv('Unemployment in India.csv', parse_dates=['Date'], dayfirst=True)
st.title("Unemployment Rates in India :flag-in:")

with st.sidebar.form("Get Input"):
    state = st.selectbox(label="Select the state", options=df['Region'].unique())
    submitted = st.form_submit_button("Proceed")

if not submitted:
    st.markdown('''### About the visualization :bar_chart:''')
    st.markdown('''- All the visualizations in this app are based on this [dataset](https://www.kaggle.com/datasets/gokulrajkmv/unemployment-in-india) :balloon:''')
    st.image('India.jpg', caption="India")


if submitted:
    temp = df[df['Region'] == state]
    st.header(f"Analysis on {state}")
    with st.expander("View Descriptive statistics"):
        st.dataframe(temp.drop(['Date'], axis=1).describe().style.highlight_max(axis=0))

    left, mid, right = st.tabs(['Estimated Unemployment Rate','Estimated Employed','Estimated Labour Participation Rate (%)'])

    plot_all(temp, "Estimated Unemployment Rate (%)", left)

    plot_all(temp, "Estimated Employed", mid)
    
    plot_all(temp, "Estimated Labour Participation Rate (%)", right)

    
