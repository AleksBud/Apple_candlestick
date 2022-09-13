import yfinance as yf
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

tickerData = yf.Ticker('AAPL')

tickerDf = tickerData.history(period='max')

trace1 = go.Bar(
    x=tickerDf.index,
    y=tickerDf['Volume'],
)

trace2 = go.Candlestick(
    x=tickerDf.index,
    low=tickerDf['Low'],
    high=tickerDf['High'],
    close=tickerDf['Close'],
    open=tickerDf['Open'],
    increasing_line_color='green',
    decreasing_line_color= 'red',
)

fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(trace1)
fig.add_trace(trace2, secondary_y=True)

fig.update_xaxes(rangebreaks = [{'bounds': ['sat', 'mon']}])

fig.update_layout(
    title='График котировок',
    height=600,
    width=800,
    showlegend=False
)

st.write("""
# Данные о котировках

## ![](https://s3-symbol-logo.tradingview.com/apple--big.svg) Apple Inc. 
NASDAQ: AAPL

*О компании*

Apple (МФА: [ˈæp(ə)l], в переводе с англ. — «яблоко») — американская корпорация, производитель персональных и планшетных компьютеров, аудиоплееров, смартфонов, программного обеспечения и цифрового контента. Apple Inc.
""")

st.plotly_chart(fig)
