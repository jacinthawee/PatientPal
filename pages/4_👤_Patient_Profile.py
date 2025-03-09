import streamlit as st

st.set_page_config(page_title="Patient Profile", page_icon="👤")
st.markdown("# Patient Profile")

particulars, dependents_caregivers = st.tabs(["My Particulars", "My Dependents and Caregivers"])

particulars.write("""NRIC/FIN: SXXXX123A  \nName: Jane Lee  \nSex: Female  \nDOB: 1 Jan 1980  \nNationality: Singapore Citizen  \nRegistered Address: Blk 456 Merlion Ave #07-890  \nEmail: jane.lee@gmail.com  \nTelephone: 8123 4567""")
particulars.button("Retrieve info with SingPass")

tile1 = dependents_caregivers.container(height=150)
tile1.write("""Dependent 1  \nRelationship: Son  \nNRIC/FIN: TXXXX456B  \nName: Eric Ang  \nSex: Male  \nDOB: 2 Feb 2008  \nNationality: Singapore Citizen  \nRegistered Address: Same as user""")

tile2 = dependents_caregivers.container(height=150)
tile2.write("""Dependent 2  \nRelationship: Daughter  \nNRIC/FIN: TXXXX789C  \nName: Mabel Ang  \nSex: Female  \nDOB: 3 March 2010  \nNationality: Singapore Citizen  \nRegistered Address: Same as user""")