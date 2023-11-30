import gspread
import streamlit as st
import json
# Load service account credentials from Streamlit secrets

key_dict = json.loads(st.secrets["textkey"])

gc = gspread.service_account_from_dict(key_dict)

# Open the desired worksheet
sheet = gc.open("Equiptment Tracker").worksheet("Monitoring")
# Function to get all available items
def get_all_items(sheet):
    items = sheet.col_values(2)[1:]  # Assuming the items are in column B, starting from row 2
    return [item for item in items if item]

# Function to get row data for a selected item
def get_row_data(sheet, item):
    values = sheet.col_values(2)  # Assuming the items are in column B
    row_index = values.index(item) + 1  # Adding 2 to convert to 2 - based index
    row_data = sheet.row_values(row_index)
    return row_data, row_index

# Streamlit app
def main():
    st.title("Equipment Tracker App")

    # Get all available items
    all_items = get_all_items(sheet)

    # Select an item using dropdown
    selected_item = st.selectbox("Select an item:", all_items)

    # Display row data for the selected item
    row_data, row_index = get_row_data(sheet, selected_item)
    st.write(f"Information for {selected_item}:", row_data)

    # Input boxes for updating the row
    qty_req = st.number_input("Update Qty Req:", value=float(row_data[3]))
    qty_avail = st.number_input("Update Qty Avail:", value=float(row_data[4]))
    remarks = st.text_input("Update Remarks:", value=row_data[5])
    battery_level = st.text_input("Update Battery Level:", value=row_data[6])
    condemned_status = st.text_input("Update Condemned Status:", value=row_data[7])

    # Update the specific columns in the Google Sheet
    if st.button("Update Row"):
        # Assuming the columns for update are from D to H (QTY REQ to CONDEMNED STATUS)
        update_range = f"D{row_index}:H{row_index}"
        update_values = [qty_req, qty_avail, remarks, battery_level, condemned_status]
        sheet.update(update_range, [update_values])

        st.success("Row updated successfully!")

if __name__ == "__main__":
    main()
