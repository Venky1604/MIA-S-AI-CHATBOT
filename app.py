import streamlit as st

st.set_page_config(
    page_title="Mia's Hair & Beauty Supply",
    page_icon="💄",
    layout="wide"
)

# =========================
# CSS STYLE
# =========================

st.markdown("""
<style>
body {
    background-color: #fff8fc;
}

.hero {
    background: linear-gradient(135deg, #7a1e4d, #c2185b, #f8bbd0);
    padding: 55px;
    border-radius: 25px;
    color: white;
    margin-bottom: 25px;
}

.hero-title {
    font-size: 46px;
    font-weight: 900;
}

.hero-subtitle {
    font-size: 20px;
    margin-top: 10px;
}

.card {
    background: white;
    padding: 24px;
    border-radius: 20px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    margin-bottom: 18px;
}

.chat-box {
    position: fixed;
    bottom: 25px;
    right: 25px;
    width: 360px;
    max-height: 610px;
    background: white;
    border-radius: 24px;
    box-shadow: 0 8px 28px rgba(0,0,0,0.25);
    padding: 18px;
    z-index: 9999;
    border: 3px solid #f8bbd0;
}

.bot-face {
    width: 78px;
    height: 68px;
    background: #fff1f7;
    border-radius: 45% 45% 50% 50%;
    margin: auto;
    border: 3px solid #c2185b;
    box-shadow: inset 0 -6px 0 rgba(194,24,91,0.12);
    position: relative;
}

.bot-face:before {
    content: "●   ●";
    color: #7a1e4d;
    font-size: 18px;
    position: absolute;
    top: 18px;
    left: 18px;
}

.bot-mouth {
    text-align: center;
    color: #7a1e4d;
    font-size: 20px;
    margin-top: -32px;
}

.bot-title {
    text-align: center;
    font-weight: 800;
    color: #7a1e4d;
    font-size: 20px;
    margin-top: 10px;
}

.bot-subtitle {
    text-align: center;
    color: #777;
    font-size: 13px;
    margin-bottom: 10px;
}

.chat-message {
    background: #fff1f7;
    padding: 10px;
    border-radius: 14px;
    margin-bottom: 8px;
    font-size: 14px;
}

.user-message {
    background: #f3f3f3;
    padding: 10px;
    border-radius: 14px;
    margin-bottom: 8px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# CHATBOT LOGIC
# =========================

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! I’m Mia’s Bot 💄 Ask me about products, prices, returns, pickup, or store info."
        }
    ]

def contains_any(text, words):
    text = text.lower()
    return any(word in text for word in words)

def answer_question(question):
    q = question.lower()

    if contains_any(q, ["address", "location", "where"]):
        return "Mia's Hair & Beauty Supply is located at 59 Albany Ave, Hartford, CT 06120."

    if contains_any(q, ["phone", "contact", "call", "email"]):
        return "You can call us at 860-206-8732 or email miashairbeauty@gmail.com."

    if contains_any(q, ["hour", "hours", "open", "close"]):
        return "Please call 860-206-8732 to confirm today's store hours."

    if contains_any(q, ["return", "refund", "exchange"]):
        return "Unused items may be eligible for return. Opened wigs, sale items, and personal beauty products may not be returnable."

    if contains_any(q, ["sale", "promotion", "discount", "deal"]):
        return "Mia's often has wig sales, bundle hair sales, and pickup promotions. Please check the website or call for current deals."

    if contains_any(q, ["wig", "wigs"]):
        return "Yes, Mia's carries many wig options including human hair wigs, lace wigs, synthetic wigs, and half wigs."

    if contains_any(q, ["braid", "braiding", "crochet"]):
        return "Yes, Mia's carries braiding hair, pre-stretched braid, crochet braid, and twist/loc products."

    if contains_any(q, ["shampoo", "conditioner", "oil", "edge control", "gel"]):
        return "Yes, Mia's carries hair care products like shampoo, conditioner, oils, gels, and edge control."

    if contains_any(q, ["price", "cost", "how much"]):
        return "Prices vary by product, brand, size, and availability. Please call the store for exact current pricing."

    return "I’m not fully sure about that yet. Please call Mia's Hair & Beauty Supply at 860-206-8732 for the most accurate answer."

# =========================
# MAIN WEBSITE
# =========================

st.markdown("""
<div class="hero">
    <div class="hero-title">Mia's Hair & Beauty Supply</div>
    <div class="hero-subtitle">
        Hartford’s beauty destination for wigs, braids, hair care, cosmetics, tools, lashes, nails, and more.
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>💇 Hair & Wigs</h3>
        <p>Human hair wigs, synthetic wigs, lace wigs, half wigs, braiding hair, crochet braid, and weave products.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>💄 Beauty Essentials</h3>
        <p>Hair care, cosmetics, lashes, nails, skin products, oils, edge control, gels, and styling products.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>🛍️ Pickup & Support</h3>
        <p>Free curbside pickup available. Call the store for product availability, current prices, and promotions.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <h3>📍 Visit Us</h3>
    <p><b>Address:</b> 59 Albany Ave, Hartford, CT 06120</p>
    <p><b>Phone:</b> 860-206-8732</p>
    <p><b>Email:</b> miashairbeauty@gmail.com</p>
</div>
""", unsafe_allow_html=True)

# =========================
# BOTTOM RIGHT CHATBOT
# =========================

st.markdown('<div class="chat-box">', unsafe_allow_html=True)

st.markdown("""
<div class="bot-face"></div>
<div class="bot-mouth">⌣</div>
<div class="bot-title">Mia's Bot</div>
<div class="bot-subtitle">Your cute beauty assistant</div>
""", unsafe_allow_html=True)

for message in st.session_state.messages[-4:]:
    if message["role"] == "assistant":
        st.markdown(
            f"<div class='chat-message'><b>Mia's Bot:</b><br>{message['content']}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div class='user-message'><b>You:</b><br>{message['content']}</div>",
            unsafe_allow_html=True
        )

user_question = st.text_input(
    "Ask Mia's Bot",
    placeholder="Ask about wigs, prices, returns...",
    label_visibility="collapsed"
)

if st.button("Send"):
    if user_question.strip():
        st.session_state.messages.append(
            {"role": "user", "content": user_question}
        )

        bot_reply = answer_question(user_question)

        st.session_state.messages.append(
            {"role": "assistant", "content": bot_reply}
        )

        st.rerun()

if st.button("Clear Chat"):
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! I’m Mia’s Bot 💄 Ask me about products, prices, returns, pickup, or store info."
        }
    ]
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)
