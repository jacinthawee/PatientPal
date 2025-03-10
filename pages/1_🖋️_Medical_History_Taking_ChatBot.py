import streamlit as st
from openai import OpenAI
import time

st.set_page_config(page_title="Medical History Taking", page_icon="🖋️")
st.markdown("# Medical History Taking")
st.write(
    """
    This is your PatientPal! Start by simply typing "hi" in the message box.
    Disclaimer: this chatbot is powered by OpenAI API Assistants gpt-4o, so do not key in sensitive data such as your IC, phone number, email etc.
    """
)

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Create assistant with file search enabled
if "assistant_id" not in st.session_state:
    assistant = client.beta.assistants.create(
        name="PatientPal",
        instructions="""
        You are a friendly and patient doctor's assistant. Use your knowledge base to take a medical history from the user and find out what are their goals for today's doctor consult. Always start by introducing yourself and asking the user if they're comfortable with having their history taken before proceeding. Once you're done asking questions, provide a summary of all concerns and responses of the user in a concise medical history.
        Please start off the chat by saying: "Hi! I'm PatientPal, your friendly doctor's assistant. May I have your permission to take a simple medical history from you? You may respond with a 'yes' or 'no'"
        If the user responds with a "no" or declines to have their history taken in any way, do not probe further. Respond with "Understood, hope you have a nice day!".
        Do not ask for sensitive data such as full name, age, and gender.
        Some essential questions to ask are: "Have you seen a doctor or done any tests (eg X-ray, lab tests) for this problem previously? If so, what was the diagnosis?"
        Ask one question at a time, be mindful of giving the user time to think.
        After you have provided the summary of the user's medical history, please give a disclaimer "Please let me know if there's any error in the history I've taken. To the overseeing doctor, please check if all information is correct."
        """,
        tools=[{"type": "file_search"}],
        model="gpt-4o"
    )

    # Upload files and add them to a vector store
    vector_store = client.beta.vector_stores.create(name="How To Take A Medical History")
    file_paths = ["resources/taking_history.txt", "resources/JME-38-6-109.pdf", "resources/Using a Six-Domain Framework to Include Biopsychosocial Information in the Standard Medical History.pdf"]
    file_streams = [open(path, "rb") for path in file_paths]
    file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
        vector_store_id=vector_store.id, files=file_streams
    )

    # Update the assistant to use the vector store
    assistant = client.beta.assistants.update(
        assistant_id=assistant.id,
        tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
    )
    st.session_state.assistant_id = assistant.id

# Initialize thread
if "thread_id" not in st.session_state:
    thread = client.beta.threads.create()
    st.session_state.thread_id = thread.id

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "user":
            st.markdown(message["content"])
        else:
            st.markdown(message["content"].content[0].text.value)
    
# Accept user input
if prompt := st.chat_input():
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Add user message to existing thread
    client.beta.threads.messages.create(
        thread_id=st.session_state.thread_id,
        role="user",
        content=prompt
    )

    # Create a run 
    run = client.beta.threads.runs.create(
        thread_id=st.session_state.thread_id,
        assistant_id=st.session_state.assistant_id,
    )

    while run.status != "completed":
        time.sleep(1)
        run = client.beta.threads.runs.retrieve(
            thread_id=st.session_state.thread_id,
            run_id=run.id
        )
    
    # Retrieve messages from assistant
    all_messages = client.beta.threads.messages.list(
        thread_id=st.session_state.thread_id
    )

    # Display assistant response in chat message container
    assistant_messages_for_run = [
        message for message in all_messages
        if message.run_id == run.id and message.role == "assistant"
    ]
    for message in assistant_messages_for_run:
        st.session_state.messages.append({"role": "assistant", "content": message})
        with st.chat_message("assistant"):
            st.markdown(message.content[0].text.value)
