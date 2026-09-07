import pandas as pd
from docx import Document

docx_file_name = "Streamli_taskdocx.docx"
csv_file_name = "Customer_Purchase_Data.csv"

# Open the Word document
document = Document(docx_file_name)
table = document.tables[0]

# Read every row of the table
# Collect all the rows into a simple list first.
all_rows = []
 
for row in table.rows:
    # Each row has many cells (columns). Get the text from each cell.
    one_row = []
    for cell in row.cells:
        text = cell.text.strip()   # strip() removes extra spaces
        one_row.append(text)
    all_rows.append(one_row)

# Separate the header row from the data rows

header_row = all_rows[0]
 
# Everything after the first row is actual data.
data_rows = all_rows[1:]

# Put everything into a pandas table (DataFrame)
df = pd.DataFrame(data_rows, columns=header_row)
 
# Fix the number columns
number_columns = ["Age", "AnnualIncome", "SpendingScore", "Purchased"]
 
for column_name in number_columns:
    df[column_name] = pd.to_numeric(df[column_name])
 

# Save the table as a CSV file

df.to_csv(csv_file_name, index=False)
 