# 📦 Supply Chain Performance Dashboard

## 📌 Overview
This **Streamlit web app** provides key insights into **sales, logistics, quality control, and manufacturing profitability** through interactive visualizations and KPIs.

## 🚀 Features
- **Sales Analysis**: Revenue & sales by product type and location.
- **Logistics & Shipping**: Carrier revenue, shipping costs, and transportation mode analysis.
- **Quality Control**: Defect rates by product type & transportation mode.
- **Profitability**: Profit, cost vs. price comparison, and profit margin.
- **Customer Demographics**: Insights based on gender distribution.

## 📊 Key Insights
- **Mumbai & Kolkata** lead in revenue, while **Delhi** shows potential for growth.
- **Skincare** dominates sales (**41.8%** revenue), followed by **Haircare** and **Cosmetics**.
- **Carrier B** generates the most revenue and offers the fastest shipping times.
- **Road transport** incurs the highest cost (**30.3%**) and defect rates (**2.62%**), while **Air transport** has the lowest defects (**1.82%**).
- **Cosmetics** have the highest **profit margin (88.24%)**, but **Skincare** is the most profitable overall (**$219.39K**).
- **Lead times** are consistent across product types, with **Skincare** taking the longest (**16.7 days**).
- **Customer demographics** show a high percentage of **unknown gender**, followed by **female customers**.

## 📊 Key Metrics (KPIs)
- **Total Revenue & Profit** 
- **Total Products Sold & Order Quantity** 
- **Shipping Costs & On-Time Delivery Rate** 
- **Defect Rate & Inspection Pass Rate** 
- **Profit Margin by Product Type (%)**
- **Average Lead Time** 

## 🛠️ Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/GitHub158Kujan/suppy_chain_analysis.git
   cd supply-chain-dashboard
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the dashboard:
   ```bash
   streamlit run app.py
   ```

## 📁 Dataset
Ensure `supply_chain_data.csv` is in the project directory. Key columns:
- `Product type`, `Revenue generated`, `Profit`, `Shipping costs`
- `Order quantities`, `Lead times`, `Defect rates`, `Manufacturing costs`
- `Customer Demographics`

## 📌 Contributing
Contributions are welcome! Feel free to add new features or optimize the code. 🚀

## 📄 License
This project is open-source under the **MIT License**.

---
Made with ❤️ by [Kujan]


