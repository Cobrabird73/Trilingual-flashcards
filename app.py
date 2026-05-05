import streamlit as st
import random

# Initializing the top verbs with present, past, and future translations
# Note: I've started with a few examples. You can expand this list to 100.
verbs_data = [
    {
        "spanish": "Ser (Presente: Soy)",
        "english": "To be",
        "filipino": "Maging",
        "example_en": "I am a professional.",
        "example_ph": "Ako ay isang propesyonal."
    },
    {
        "spanish": "Haber (Pasado: Había)",
        "english": "To have",
        "filipino": "Mayroon",
        "example_en": "There was a meeting.",
        "example_ph": "Mayroong pagpupulong."
    },
    {
        "spanish": "Ir (Futuro: Iré)",
        "english": "To go",
        "filipino": "Pumunta",
        "example_en": "I will go to Spain.",
        "example_ph": "Pupunta ako sa Espanya."
    }
]

# Initialize Session States
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_card' not in st.session_state:
    st.session_state.current_card = random.choice(verbs_data)
if 'feedback' not in st.session_state:
    st.session_state.feedback = ""

def check_answer(user_input, correct_en, correct_ph):
    user_input = user_input.strip().lower()
    if user_input == correct_en.lower() or user_input == correct_ph.lower():
        st.session_state.score += 1
        st.session_state.feedback = "✅ Correct! +1 Point"
        st.session_state.current_card = random.choice(verbs_data)
    else:
        st.session_state.feedback = f"❌ Try again! (Hints on the back)"

# --- UI LAYOUT ---
st.title("🇪🇸 Spanish Verb Flashcards")
st.subheader(f"Score: {st.session_state.score}")

# Front of the Card
st.info(f"### Verb: {st.session_state.current_card['spanish']}")

# User Input
user_guess = st.text_input("Translate to English or Filipino:", key="input")

if st.button("Submit Answer"):
    check_answer(user_guess, st.session_state.current_card['english'], st.session_state.current_card['filipino'])
    st.rerun()

st.write(st.session_state.feedback)

# Back of the Card (Expander)
with st.expander("👀 See Back of Card (Translations & Examples)"):
    card = st.session_state.current_card
    st.write(f"English:")
    st.write(f"Filipino:")
    st.divider()
    st.write(f"*Example (EN):* {card['example_en']}")
    st.write(f"*Example (PH):* {card['example_ph']}")

if st.button("Skip / Next Card"):
    st.session_state.current_card = random.choice(verbs_data)
    st.session_state.feedback = ""
    st.rerun()
