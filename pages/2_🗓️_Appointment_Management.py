import streamlit as st

@st.dialog("Medical History Summary")
def show_history():
    st.write("""Patient presented to her GP with complaints of intermittently occurring joint pain in her wrists and ankles. Further questioning revealed that she had been experiencing occasional morning stiffness and a tingling sensation in her extremities. She denied any headache or constitutional symptoms beyond mild fatigue. She stated that she had been tested for ANA and rheumatoid factor in the past and they were both negative. Additional inquiry revealed that the patient has a positive family history for rheumatoid arthritis. On physical exam, the patient expressed mild tenderness at both wrists. The rest of the exam was non-contributory. The GP was concerned about a potential autoimmune disease process and ordered an erythrocyte sedimentation rate (ESR) and an antinuclear antibody (ANA) test. The results are listed in table 1. The GP then referred the patient to rheumatology.""")

st.set_page_config(page_title="Appointment Management", page_icon="🗓️")
st.markdown("# Appointment Management")

upcoming_appt, missed_appt, open_appt = st.tabs(["Upcoming", "Missed", "Open"])

tile1 = upcoming_appt.container(height=125)
tile1.write("""Singapore University Hospital  \n10 Apr 2025 Thu 10:00am  \nTechnical Visit (Blood Test\Procedure\Others)  \nTower A, Clinic 6B, Level 6""")

tile2 = upcoming_appt.container(height=210)
tile2.write("""Singapore University Hospital  \n10 Apr 2025 Thu 12:00pm  \nRheumatology - Repeat Visit  \nDr Mary Tan  \nTower A, Clinic 6A, Level 6""")
if tile2.button("View history"):
    show_history()

tile3 = missed_appt.container(height=125)
tile3.write("""Kent Ridge Polyclinic  \n18 Feb 2025 Tue 2:30pm  \nTechnical Visit (Blood Test\Procedure\Others)  \nClinic 43, Level 4""")

open_appt.subheader("You have no open appointments")