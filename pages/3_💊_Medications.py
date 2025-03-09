import streamlit as st

st.set_page_config(page_title="Medications", page_icon="💊")
st.markdown("# Medications")

current_prescription, refills = st.tabs(["Prescription List", "Refills"])

tile1 = current_prescription.container(height=135)
tile1.write("""Colecalciferol Tablet  \nTake 1,000 UNIT every morning for 364 days.  \nPrescribed 12 October 2024  \nApproved by Dr Jerry Ma  \nL2 Outpatient Pharmacy""")

tile2 = current_prescription.container(height=135)
tile2.write("""Omega-3 Fish Oil (HI-OMEGA 88) Capsule  \nTake 1 capsule once a day for 364 days.  \nPrescribed 12 October 2024  \nApproved by Dr Jerry Ma  \nL2 Outpatient Pharmacy""")

tile3 = current_prescription.container(height=135)
tile3.write("""Metamethasone (Valerate) 0.025% Cream (15g)  \nApply 1 application to affected area 2 times a day for 120 days.  \nPrescribed 31 March 2023  \nApproved by Dr Mary Tan  \nL2 Outpatient Pharmacy""")

tile4 = refills.container(height=135)
tile4.write("""Metamethasone (Valerate) 0.025% Cream (15g)  \nApply 1 application to affected area 2 times a day for 120 days.  \nRefilled 20 November 2023  \nApproved by Dr Mary Tan  \nL2 Outpatient Pharmacy""")