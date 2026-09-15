
#First block -- Import all the libraries
import pandas as pd
import plotly.express as px
import streamlit as st

#df for Data Frame
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

st.sidebar.title("Filters")

regioes = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

categorias = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

df = df[(df["Region"].isin(regioes)) & (df["Category"].isin(categorias))]
#Title and metrics for streamlit

st.title("📊 Sales Dashboard  - Superstore")

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${df['Sales'].sum():,.0f}")
col2.metric("Total Profit", f"${df['Profit'].sum():,.0f}")
col3.metric("Nº Orders", f"{df['Order ID'].nunique():,}")

col4, col5, col6 = st.columns(3)
col4.metric("AVG per order", f"${df.groupby('Order ID')['Sales'].sum().mean():,.0f}")
col5.metric("Best Selling Product ", df.groupby('Product Name')['Sales'].sum().idxmax())
col6.metric("Top Regions", df.groupby('Region')['Sales'].sum().idxmax())


#Graphic sales per category 
st.subheader("Sales per Category")
cat = df.groupby("Category")["Sales"].sum().reset_index()
fig1 = px.bar(cat, x="Category", y="Sales", color="Category",
              color_discrete_map={
                  "Furniture": "#1cdf6d",
                  "Office Supplies": "#d12411",
                  "Technology": "#e6920b"
              })
st.plotly_chart(fig1)


#Sales along time

st.subheader("Sales along Time")
df["Order Date"] = pd.to_datetime(df["Order Date"])
time = df.groupby("Order Date")["Sales"].sum().reset_index()
fig2 = px.line(time, x="Order Date", y="Sales", color_discrete_sequence=["#06aa4a"])
st.plotly_chart(fig2)

#Change Time Line

time = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum().reset_index()
time["Order Date"] = time["Order Date"].dt.to_timestamp()

#Top 10 Products

st.subheader("Top 10 Product per Orders")
top10 = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10).reset_index()
fig3 = px.bar(top10, x="Sales", y="Product Name", orientation="h",
              color="Sales", color_continuous_scale="Greens")
st.plotly_chart(fig3)

#Sales per region

st.subheader("Sales per Region")
region = df.groupby("Region")["Sales"].sum().reset_index()
fig4 = px.pie(region, values = "Sales",names = "Region", 
              color_discrete_sequence=["#17d366", "#c52a19", "#f3a11d", "#490eec"])
st.plotly_chart(fig4)

#Sales vs Profit 

st.subheader("Sales vs Profit")
fig5 = px.scatter(df, x="Sales", y="Profit", color="Category",
                  hover_data=["Product Name", "Region"],
                  color_discrete_map={
                      "Furniture": "#17d366",
                      "Office Supplies": "#c52a19",
                      "Technology": "#f3a11d"
                  })
st.plotly_chart(fig5)


