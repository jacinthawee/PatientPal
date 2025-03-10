import streamlit as st
import streamlit_survey as ss

st.set_page_config(page_title="Post Consult", page_icon="💬")
st.markdown("# Post Consult")

feedback, pt_education = st.tabs(["Patient Experience Feedback", "Patient Education Materials"])

with feedback: 
    st.header("Generic Short Patient Experiences Questionnaire (GS-PEQ)")
    survey = ss.StreamlitSurvey()
    survey.radio("Did the clinicians talk to you in a way that was easy to understand?", options=["NA", "😞", "🙁", "😐", "🙂", "😀"], horizontal=True)
    st.text_input("Comments 1:")
    survey.radio("Do you have confidence in the clinicians' professional competence?", options=["NA", "😞", "🙁", "😐", "🙂", "😀"], horizontal=True)
    st.text_input("Comments 2:")
    survey.radio("Did you get sufficient information about your diagnosis/your afflictions?", options=["NA", "😞", "🙁", "😐", "🙂", "😀"], horizontal=True)
    st.text_input("Comments 3:")
    survey.radio("Did you perceive the treatment you received as suited to your situation?", options=["NA", "😞", "🙁", "😐", "🙂", "😀"], horizontal=True)
    st.text_input("Comments 4:")
    survey.radio("Were you involved in any decisions regarding your treatment?", options=["NA", "😞", "🙁", "😐", "🙂", "😀"], horizontal=True)
    st.text_input("Comments 5:")
    survey.radio("Did you perceive the institution's work as well organised?", options=["NA", "😞", "🙁", "😐", "🙂", "😀"], horizontal=True)
    st.text_input("Comments 6:")
    survey.radio("Did you have to wait before you were admitted for services at the institution?", options=["NA", "😞", "🙁", "😐", "🙂", "😀"], horizontal=True)
    st.text_input("Comments 7:")
    survey.radio("Overall, was the help and treatment you received at the institution satisfactory?", options=["NA", "😞", "🙁", "😐", "🙂", "😀"], horizontal=True)
    st.text_input("Comments 8:")
    survey.radio("Overall, what benefit have you had from the care at the institution?", options=["NA", "😞", "🙁", "😐", "🙂", "😀"], horizontal=True)
    st.text_input("Comments 9:")
    survey.radio("Do you believe that you were in any way given the wrong treatment (according to your own judgment)?", options=["NA", "😞", "🙁", "😐", "🙂", "😀"], horizontal=True)
    st.text_input("Comments 10:")
    st.button("Submit feedback")

with pt_education:
    st.markdown(
        """
        ### List of useful links
        ##### Taken in part from [ACE Educational Resources](https://www.ace-hta.gov.sg/Patients-And-Community/Educational-Resources)
        [Hormone therapy for advanced prostate cancer](https://www.ace-hta.gov.sg/docs/default-source/educational-resources/hormone-therapy-for-advanced-prostate-cancer.pdf?sfvrsn=43a3fde0_11)  \n
        [Combination eye drops for open-angle glaucoma](https://www.ace-hta.gov.sg/docs/default-source/educational-resources/combination-eye-drops-for-open-angle-glaucoma.pdf?sfvrsn=f3dfa9fb_1)  \n
        [What are cell, tissue, and gene therapies?](https://www.ace-hta.gov.sg/docs/default-source/educational-resources/what-are-cell-tissue-and-gene-therapies.pdf?sfvrsn=7f7c44fc_1)  \n
        [Oral treatments for type 2 diabetes](https://www.ace-hta.gov.sg/docs/default-source/educational-resources/oral-treatments-for-type-2-diabetes.pdf?sfvrsn=36f53a1d_11)  \n
        [Treatments for chronic lymphocytic leukaemia](https://www.ace-hta.gov.sg/docs/default-source/educational-resources/treatments-for-chronic-lymphocytic-leukaemia.pdf?sfvrsn=68210db4_7)  \n
        """)
