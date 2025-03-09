import streamlit as st

st.set_page_config(page_title="Billing and Subsidies", page_icon="💳")
st.markdown("# Billing and Subsidies")

outstanding, paid = st.tabs(["Outstanding Bills", "Fully-paid Bills"])

tile1 = outstanding.container(height=155)
tile1.write("""Singapore University Hospital  \nVisited on 10 March 2025  \nAmount due: $46.80""")
tile1.button("Pay Now")

tile2 = paid.container(height=155)
tile2.write("""Singapore University Hospital  \nVisited on December 30 2024  \nBill Reference No.: 12345678A""")
tile2.button("Download Bill")