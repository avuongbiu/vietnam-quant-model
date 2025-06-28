import streamlit as st
import pandas as pd

st.title("Mô Hình Giao Dịch Định Lượng Tích Hợp Cảm Xúc")

# Hiển thị dữ liệu giá cổ phiếu
df = pd.read_csv("data/stock_prices/cafef_VNM.csv")
st.line_chart(df['Giá đóng cửa'])

# Hiển thị tín hiệu mua/bán
st.bar_chart(df['buy_signal'])