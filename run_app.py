from openai import OpenAI
import streamlit as st

openai_api_key = <your openai apy key>

def generate_quiz(topic, openai_api_key):
    prompt = (
        f"Generate 5 multiple choice questions on the topic: {topic}. "
        "For each question, provide 4 options labeled A, B, C, D and indicate the correct answer after \n"
    )
    client = OpenAI(api_key = openai_api_key)
    response = client.responses.create(
        model= "gpt-5",
        input= prompt)

    questions = response.output_text.strip().split("\n\n")

    # Display formatted output in Streamlit
    for q in questions:
        q = q.strip()
        st.markdown(q)
        st.markdown("-"*60)  # Divider line

    return 

def generate_flashcards(topic, openai_api_key):
    prompt = (
        f"Create 5 flashcards with question and answer pairs on the topic: {topic}.\n"
        "Format as:\nQ: question\nA: answer"
    )
    client = OpenAI(api_key = openai_api_key)
    response = client.responses.create(
    model= "gpt-5",
    input= prompt
    )

    cleaned_res = response.output_text.strip().split("\n\n")
    # Display formatted output in Streamlit
    for q in cleaned_res:
        qa = q.strip().split('?')
        st.markdown(qa[0] + ' ?')
        st.markdown(qa[1])
        st.markdown("-"*60)  # Divider line

    return 

def answer_question(question, openai_api_key):
    prompt = f"Answer the following student question clearly:\n{question}"
    client = OpenAI(api_key = openai_api_key)
    response = client.responses.create(
    model= "gpt-5",
    input= prompt
    )

    st.markdown(response.output_text.strip())

    return


# --- Streamlit UI ---

st.title("AI Study Buddy")

if "topic" not in st.session_state:
    st.session_state.topic = ""

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Select or input study topic
topic_input = st.text_input("Enter your study topic or subject:", st.session_state.topic)
if topic_input:
    st.session_state.topic = topic_input.strip()

st.markdown("---")

# User selects an action
action = st.radio(
    "Choose an action:",
    ("Ask a Question", "Generate Quiz", "Generate Flashcards"),
)

user_input = st.text_input("Type your question or press Enter to generate content:")

if st.button("Submit") or (user_input and st.session_state.last_action != action):
    st.session_state.last_action = action

    if action == "Generate Quiz":
        if not st.session_state.topic:
            st.warning("Please enter a study topic first!")
        else:
            with st.spinner("Generating quiz..."):
                quiz_text = generate_quiz(st.session_state.topic, openai_api_key)
                st.session_state.chat_history.append(("Study Buddy (Quiz)", quiz_text))

    elif action == "Generate Flashcards":
        if not st.session_state.topic:
            st.warning("Please enter a study topic first!")
        else:
            with st.spinner("Generating flashcards..."):
                flashcards_text = generate_flashcards(st.session_state.topic, openai_api_key)
                st.session_state.chat_history.append(("Study Buddy (Flashcards)", flashcards_text))

    elif action == "Ask a Question":
        if not user_input.strip():
            st.warning("Please enter a question!")
        else:
            with st.spinner("Answering your question..."):
                answer = answer_question(user_input, openai_api_key)
                st.session_state.chat_history.append(("You", user_input))
                st.session_state.chat_history.append(("Study Buddy", answer))

# Show chat history
st.markdown("### Chat History")
for speaker, text in st.session_state.chat_history:
    if speaker.startswith("You"):
        st.markdown(f"**You:** {text}")
    #else:
    #    st.markdown(f"**{speaker}:**\n{text}")
