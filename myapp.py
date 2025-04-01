import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


df = pd.read_csv("supply_chain_data.csv")


st.set_page_config(page_title="Supply Chain Dashboard", layout="wide")
st.title("📦 Supply Chain Performance Dashboard")


st.sidebar.title("Navigation")
sections = ["Sales Overview", "Logistics & Shipping", "Quality Control", "Manufacturing & Profitability"]
section = st.sidebar.radio("Go to", sections)


st.sidebar.header("Key Metrics")
st.sidebar.metric("Total Revenue", f"${df['Revenue generated'].sum():,.2f}")
st.sidebar.metric("Total Products Sold", f"{df['Number of products sold'].sum():,}")
st.sidebar.metric("Average Order Quantity", f"{df['Order quantities'].mean():.2f}")
st.sidebar.metric("Average Shipping Cost", f"${df['Shipping costs'].mean():.2f}")
st.sidebar.metric("Most Used Shipping Carrier", df['Shipping carriers'].mode()[0])
st.sidebar.metric("Average Shipping Time", f"{df['Shipping times'].mean():.2f} days")
st.sidebar.metric("Overall Defect Rate", f"{df['Defect rates'].mean():.2f}%")
st.sidebar.metric("Pass Rate in Inspections",
                  f"{(df['Inspection results'].value_counts(normalize=True).get('Pass', 0) * 100):.2f}%")
st.sidebar.metric("Total Manufacturing Cost", f"${df['Manufacturing costs'].sum():,.2f}")
st.sidebar.metric("Average Lead Time", f"{df['Lead times'].mean():.2f} days")


# Sales Overview
if section == "Sales Overview":
    st.title("📊 Sales Overview")
    fig, ax = plt.subplots()
    revenue_group = df.groupby("Product type")["Revenue generated"].sum().reset_index()
    revenue = px.pie(revenue_group, values="Revenue generated", names="Product type",
                     title='Revenue Generated by each product')
    st.plotly_chart(revenue)

    loc = df.groupby("Location")["Revenue generated"].sum().reset_index()
    fig_loc = px.bar(loc, x="Location", y="Revenue generated", title="Revenue Generated by Different Locations",color="Location")
    st.plotly_chart(fig_loc)

    sales = df.groupby("Product type")["Number of products sold"].sum().reset_index()
    fig_sales = px.bar(sales, x="Product type", y="Number of products sold",
                 title="Sales by Product Type",
                 labels={"Product type": "Product Type", "Number of products sold": "Number of Products Sold"},
                 hover_data={"Number of products sold": True},
                 color="Product type")
    st.plotly_chart(fig_sales)

    fig_sku = px.bar(df, x="SKU", y="Order quantities", title="Order Quantity by SKU")
    st.plotly_chart(fig_sku)

# Logistics & Shipping
elif section == "Logistics & Shipping":
    st.title("🚛 Logistics & Shipping")
    shipping_revenue = df.groupby("Shipping carriers")["Revenue generated"].sum().reset_index()
    shipping_revenue_ = px.bar(shipping_revenue, x="Shipping carriers", y="Revenue generated",title="Revenue generated by shipping carrier",
                               color="Shipping carriers")
    st.plotly_chart(shipping_revenue_)

    fig_shipping = px.box(df, x="Shipping carriers", y="Shipping costs", title="Shipping Costs by Carrier",color="Shipping carriers")
    st.plotly_chart(fig_shipping)

    fig_transport = px.pie(df, names="Transportation modes", values="Costs",
                           title="Cost Distribution by Transportation Mode")
    st.plotly_chart(fig_transport)

    shipping_group = df.groupby("Shipping carriers")["Shipping times"].sum().reset_index()
    fig_times = px.bar(shipping_group, x="Shipping carriers", y="Shipping times", title="Shipping Times by Carrier",color="Shipping carriers")


    st.plotly_chart(fig_times)

# Quality Control
elif section == "Quality Control":
    st.title("🔍 Quality Control")
    defect = df.groupby("Product type")["Defect rates"].mean().reset_index()
    defect["Defect rates"] = defect["Defect rates"].round(2)
    defect_rate = px.pie(defect, values="Defect rates", names="Product type",
                         title='Average Defect Rate by Product Type')
    st.plotly_chart(defect_rate)

    defect_group = df.groupby("Transportation modes")["Defect rates"].mean().reset_index()
    defect_group=defect_group.sort_values(by="Defect rates",ascending=False)
    fig_defect_transport = px.bar(defect_group, x="Transportation modes", y="Defect rates",
                                  title="Average Defect Rates by Transportation Mode",color="Transportation modes")
    st.plotly_chart(fig_defect_transport)

    fig_lead_defect = px.scatter(df, x="Lead time", y="Defect rates", title="Lead Time vs. Defect Rates",color="Product type")
    st.plotly_chart(fig_lead_defect)

# Manufacturing & Profitability
elif section == "Manufacturing & Profitability":
    st.title("🏭 Manufacturing & Profitability")
    df["Profit"] = df["Revenue generated"] - df["Costs"]
    profit_group = df.groupby("Product type")["Profit"].sum().reset_index()
    profit = px.bar(profit_group, x="Product type", y="Profit", title="Profit by Product type", color="Product type")
    st.plotly_chart(profit)

    df["Profit Margin (%)"] = (df["Profit"] / df["Revenue generated"]) * 100
    profit_margin_group=df.groupby("Product type")["Profit Margin (%)"].mean().reset_index()
    fig_profit_margin = px.bar(
        profit_margin_group,
        x="Product type",
        y="Profit Margin (%)",
        title="Profit Margin by Product Type",
        color="Product type"
    )
    st.plotly_chart(fig_profit_margin)

    df['Price'] = df['Price'].round(2)
    manufact_rev = px.scatter(df, x="Manufacturing costs", y="Revenue generated",
                              title="Relationship between manufacturing cost and revenue generated",
                              size="Price", color="Product type", hover_data={'SKU'})
    st.plotly_chart(manufact_rev)

    price_group = df.groupby("Product type")["Price"].sum().reset_index()
    manufact_group = df.groupby("Product type")["Manufacturing costs"].sum().reset_index()
    comparison_df = pd.merge(price_group, manufact_group, on="Product type")
    comparison_df = comparison_df.melt(id_vars="Product type", var_name="Cost Type", value_name="Amount")
    fig_comp = px.bar(comparison_df, x="Product type", y="Amount", color="Cost Type",
                 title="Comparison of Manufacturing Cost and Price",
                 barmode="group")
    st.plotly_chart(fig_comp)

    lead_time_group = df.groupby("Product type")["Lead times"].mean().reset_index()
    lead_time = px.pie(lead_time_group, names="Product type", values="Lead times",
                       title="Average Lead Time by Product Type")
    st.plotly_chart(lead_time)

    top_skus = df.groupby("Product type").apply(lambda x: x.nlargest(5, "Profit")).reset_index(drop=True)
    top_skus = top_skus.sort_values(by="Profit", ascending=True)
    fig_top_skus = px.bar(
        top_skus,
        x="Profit",
        y="SKU",
        color="Product type",
        title="Top 5 Profitable SKUs in Each Product Type",
        orientation="h"
    )

    st.plotly_chart(fig_top_skus)

    fig_customer = px.histogram(df, x="Customer demographics", title="Customer Demographics Analysis",color="Customer demographics")
    st.plotly_chart(fig_customer)

st.sidebar.info("Select a section to view detailed analysis.")
