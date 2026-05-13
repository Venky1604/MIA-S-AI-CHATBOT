from pathlib import Path
import zipfile, shutil

root = Path("/mnt/data/mias_beauty_chatbot_streamlit")
if root.exists():
    shutil.rmtree(root)
root.mkdir(parents=True, exist_ok=True)

app_py = r'''import streamlit as st

# ============================================================
# MIA'S HAIR & BEAUTY SUPPLY - STREAMLIT CHATBOT WEBSITE
# Version 1: Rule-based store assistant using store_knowledge.txt
# ============================================================

# ---------------- FEATURE 1: PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Mia's Beauty Supply Chatbot",
    page_icon="💄",
    layout="centered"
)

# ---------------- FEATURE 2: SIMPLE WEBSITE STYLE ----------------
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

# ---------------- FEATURE 3: LOAD STORE KNOWLEDGE ----------------
@st.cache_data
def load_store_knowledge():
    with open("store_knowledge.txt", "r", encoding="utf-8") as file:
        return file.read()

store_knowledge = load_store_knowledge()

# ---------------- FEATURE 4: HEADER ----------------
st.markdown("<div class='big-title'>💄 Mia's Beauty Supply Assistant</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='sub-title'>Ask about products, prices, store location, pickup, promotions, and return policy.</div>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='info-box'>
    Hi! I can help with general questions about Mia's Hair & Beauty Supply.
    For exact inventory, current price, or urgent help, please call the store.
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------- FEATURE 5: CHAT HISTORY ----------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! Welcome to Mia's Hair & Beauty Supply. How can I help you today?"
        }
    ]

# ---------------- FEATURE 6: HELPER FUNCTION ----------------
def contains_any(question, keywords):
    question = question.lower()
    return any(keyword in question for keyword in keywords)

# ---------------- FEATURE 7: CHATBOT ANSWER LOGIC ----------------
def answer_question(question):
    q = question.lower()

    if contains_any(q, ["address", "location", "where are you", "where is", "directions"]):
        return "Mia's Hair & Beauty Supply is located at 59 Albany Ave, Hartford, CT 06120."

    if contains_any(q, ["phone", "number", "call", "contact", "email"]):
        return "You can contact Mia's Hair & Beauty Supply by phone at 860-206-8732 or email miashairbeauty@gmail.com."

    if contains_any(q, ["hour", "hours", "open", "close", "closing", "timing", "time"]):
        return "I do not have confirmed store hours in my current knowledge file. Please call the store at 860-206-8732 to confirm today's hours."

    if contains_any(q, ["pickup", "pick up", "curbside", "order online"]):
        return "Yes, online ordering with free curbside pickup is available. Please place the order online or call the store for pickup questions."

    if contains_any(q, ["return", "refund", "exchange", "policy"]):
        return "For returns and refunds, items generally need to be unused and in original condition. Some items such as opened wigs, sale items, or personal beauty products may not be returnable. Please confirm with the store before purchasing."

    if contains_any(q, ["promotion", "promotions", "discount", "deal", "deals", "sale", "coupon"]):
        return "Mia's website lists sale sections such as special sale wigs, big sale wigs, bundle hair sale, and quick pickup items. Promotions may change, so please check the website or call the store for current deals."

    if contains_any(q, ["wig", "wigs", "lace wig", "half wig", "synthetic wig", "human wig"]):
        return "Yes, Mia's carries many wig options, including human lace wigs, regular human wigs, synthetic lace wigs, regular synthetic wigs, and half wigs. Availability, color, style, and price can change, so please call for exact inventory."

    if contains_any(q, ["braid", "braiding", "pre-stretched", "crochet", "loc"]):
        return "Yes, Mia's carries braiding hair including human braiding hair, pre-stretched braid, crochet braid, and related braid/twist/loc products. Colors and lengths may vary."

    if contains_any(q, ["weave", "bundle", "closure", "clip in", "extension", "extensions"]):
        return "Yes, Mia's carries weave and extension products including bundle hair, lace closures, human hair, synthetic hair, and clip-in extensions. Please call for exact availability."

    if contains_any(q, ["shampoo", "conditioner", "hair oil", "oil", "edge control", "gel", "relaxer", "perm", "treatment", "color"]):
        return "Yes, Mia's carries hair care items such as shampoo, conditioner, oils, styling products, hair color, treatments, relaxers, perms, edge control, and braid/twist/loc gel."

    if contains_any(q, ["flat iron", "curling iron", "dryer", "blow dryer", "clipper", "outliner", "tool", "tools"]):
        return "Yes, Mia's carries beauty tools including dryers, flat irons, curling irons, clippers, and outliners."

    if contains_any(q, ["lash", "lashes", "nail", "nails", "cosmetic", "makeup", "lip", "jewelry"]):
        return "Yes, Mia's carries lashes, nails, cosmetics, lip products, and jewelry. Specific brands and prices may vary."

    if contains_any(q, ["price", "cost", "how much", "$"]):
        if "wild growth" in q:
            return "Wild Growth Hair Oil is listed on the website at $8.99, but please confirm current pricing before purchase."
        if "rat tail" in q or "comb" in q:
            return "A Rat Tail Comb is listed on the website at $1.00, but please confirm current pricing before purchase."
        if "lip gloss" in q:
            return "Broadway Clear Lip Gloss is listed on the website at $1.29, but please confirm current pricing before purchase."
        if "x-pression" in q or "xpression" in q:
            return "X-PRESSION Pre-Stretched Braid 3X 52 inch is listed at $5.49, but prices may change."
        return "Prices vary by brand, size, color, and availability. Please check the website or call 860-206-8732 for the exact current price."

    if contains_any(q, ["do you have", "available", "in stock", "stock", "carry", "sell"]):
        return "Mia's carries many beauty supply categories including wigs, braids, weave, hair care, general beauty items, lashes, nails, cosmetics, dryers, irons, jewelry, clippers, and more. For exact item availability, please call 860-206-8732."

    return "I’m not fully sure about that yet. Please call Mia's Hair & Beauty Supply at 860-206-8732 or email miashairbeauty@gmail.com for the most accurate answer."

# ---------------- FEATURE 8: DISPLAY CHAT MESSAGES ----------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# ---------------- FEATURE 9: USER INPUT ----------------
user_question = st.chat_input("Ask about products, prices, returns, pickup, or store info...")

if user_question:
    st.session_state.messages.append({"role": "user", "content": user_question})

    with st.chat_message("user"):
        st.write(user_question)

    bot_answer = answer_question(user_question)

    st.session_state.messages.append({"role": "assistant", "content": bot_answer})

    with st.chat_message("assistant"):
        st.write(bot_answer)

# ---------------- FEATURE 10: SIDEBAR STORE INFO ----------------
with st.sidebar:
    st.header("Store Info")
    st.write("**Mia's Hair & Beauty Supply**")
    st.write("59 Albany Ave, Hartford, CT 06120")
    st.write("Phone: 860-206-8732")
    st.write("Email: miashairbeauty@gmail.com")
    st.divider()
    if st.button("Clear Chat"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hi! Welcome to Mia's Hair & Beauty Supply. How can I help you today?"
            }
        ]
        st.rerun()
(root / "app.py").write_text(app_py)
(root / "requirements.txt").write_text(requirements)
(root / "store_knowledge.txt").write_text(knowledge)
(root / "README.md").write_text(readme)

zip_path = Path("/mnt/data/mias_beauty_chatbot_streamlit.zip")
if zip_path.exists():
    zip_path.unlink()

with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for f in root.rglob("*"):
        z.write(f, f.relative_to(root))

print("Created:", zip_path)
print("Files:")
for f in root.iterdir(): 
    print("-", f.name)
