import pandas as pd
from fpdf import FPDF

# Read CSV data
df = pd.read_csv("sales_data.csv")

# Compute total sales per product
df["Total Sale"] = df["Units Sold"] * df["Unit Price"]
total_sales = df["Total Sale"].sum()
top_product = df.groupby("Product")["Total Sale"].sum().idxmax()
average_sale = df["Total Sale"].mean()

# Initialize PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, "Sales Report", ln=True, align='C')

pdf.set_font("Arial", '', 12)
pdf.ln(10)
pdf.cell(200, 10, f"Total Sales: Rs. {total_sales:,.2f}", ln=True)
pdf.cell(200, 10, f"Top Selling Product: {top_product}", ln=True)
pdf.cell(200, 10, f"Average Sale Value: Rs. {average_sale:,.2f}", ln=True)

pdf.ln(10)
pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, "Detailed Sales Data", ln=True)
pdf.set_font("Arial", '', 10)

# Table Header
pdf.set_fill_color(200, 220, 255)
pdf.cell(30, 8, "Date", border=1, fill=True)
pdf.cell(40, 8, "Product", border=1, fill=True)
pdf.cell(30, 8, "Units", border=1, fill=True)
pdf.cell(30, 8, "Price", border=1, fill=True)
pdf.cell(40, 8, "Total Sale", border=1, ln=True, fill=True)

# Table Rows
for index, row in df.iterrows():
    pdf.cell(30, 8, row["Date"], border=1)
    pdf.cell(40, 8, row["Product"], border=1)
    pdf.cell(30, 8, str(row["Units Sold"]), border=1)
    pdf.cell(30, 8, f"Rs. {row['Unit Price']}", border=1)
    pdf.cell(40, 8, f"Rs. {row['Total Sale']}", border=1, ln=True)

# Save PDF
pdf.output("sample_report.pdf", 'F')
print("✅ PDF report generated as sample_report.pdf")
