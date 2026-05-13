import streamlit as st

# ============================================================
# MIA'S HAIR & BEAUTY SUPPLY CHATBOT
# ============================================================

st.set_page_config(
    page_title="Mia's Beauty Supply Chatbot",
    page_icon="💄",
    layout="centered"
)

# ---------------- WEBSITE STYLE ----------------

st.markdown("""
<style>
.big-title {
    font-size: 38px;
    font-weight: 800;
    color: #7A1E4D;
}

.sub-title {
    font-size: 17px;
    color: #666666;
    margin-bottom: 20px;
}

.info-box {
    background-color: #fff1f7;
    padding: 18px;
    border-radius: 14px;
    border-left: 6px solid #c2185b;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown(
    "<div class='big-title'>💄 Mia's Beauty Supply Assistant</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Ask about products, prices, returns, pickup, promotions, and store information.</div>",
    unsafe_allow_html=True
)

# ---------------- INTRO MESSAGE ----------------

st.markdown(
    """
    <div class='info-box'>
    Hi! I can help answer general questions about Mia's Hair & Beauty Supply.
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------- CHAT HISTORY ----------------

if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! Welcome to Mia's Hair & Beauty Supply. How can I help you today?"
        }
    ]

# ---------------- HELPER FUNCTION ----------------

def contains_any(question, keywords):

    question = question.lower()

    return any(keyword in question for keyword in keywords)

# ---------------- CHATBOT RESPONSE LOGIC ----------------

def answer_question(question):

    q = question.lower()

    if contains_any(q, ["address", "location", "where"]):

        return "Mia's Hair & Beauty Supply is located at 59 Albany Ave, Hartford, CT 06120."

    if contains_any(q, ["phone", "contact", "call", "email"]):

        return "You can call Mia's Hair & Beauty Supply at 860-206-8732 or email miashairbeauty@gmail.com."

    if contains_any(q, ["hour", "hours", "open", "close"]):

        return "Please call the store at 860-206-8732 to confirm today's store hours."

    if contains_any(q, ["return", "refund", "exchange"]):

        return "Unused items may be eligible for return. Opened wigs, sale items, and personal beauty products may not be returnable."

    if contains_any(q, ["promotion", "sale", "discount", "deal"]):

        return "Mia's frequently has promotions and wig sales. Please check the website or call the store for current deals."

    if contains_any(q, ["wig", "wigs"]):

        return "Yes, Mia's carries many wig options including human hair wigs and synthetic wigs."

    if contains_any(q, ["braid", "braiding"]):

        return "Yes, Mia's carries braiding hair and crochet braid products."

    if contains_any(q, ["price", "cost", "how much"]):

        return "Prices vary depending on brand and availability. Please contact the store for current pricing."

    return "I’m not fully sure about that yet. Please call Mia's Hair & Beauty Supply at 860-206-8732 for more details."

# ---------------- DISPLAY CHAT ----------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])

# ---------------- USER INPUT ----------------

user_question = st.chat_input(
    "Ask a question..."
)

if user_question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    with st.chat_message("user"):

        st.write(user_question)

    bot_answer = answer_question(user_question)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": bot_answer
        }
    )

    with st.chat_message("assistant"):

        st.write(bot_answer)

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.header("Store Information")

    st.write("📍 59 Albany Ave, Hartford, CT 06120")

    st.write("📞 860-206-8732")

    st.write("✉️ miashairbeauty@gmail.com")
