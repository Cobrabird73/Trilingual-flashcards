import streamlit as st
import random

# --- DATASET ---
# Expand this list to reach the top 100
VERB_DATA = {
    "hablar": {
        "preterito perfecto simple": "hablé", "preterito imperfecto": "hablaba",
        "futuro": "hablaré", "condicional": "hablaría",
        "example": ("Yo hablé con mi madre ayer.", "I spoke with my mother yesterday.")
    },
    "tener": {
        "preterito perfecto simple": "tuve", "preterito imperfecto": "tenía",
        "futuro": "tendré", "condicional": "tendría",
        "example": ("Tendré un coche nuevo pronto.", "I will have a new car soon.")
    },
    "ir": {
        "preterito perfecto simple": "fui", "preterito imperfecto": "iba",
        "futuro": "iré", "condicional": "iría",
        "example": ("Nosotros íbamos al parque cada día.", "We used to go to the park every day.")
    },
    "ser": {
        "preterito perfecto simple": "fui", "preterito imperfecto": "era",
        "futuro": "seré", "condicional": "sería",
        "example": ("Yo era muy tímido de niño.", "I was very shy as a child.")
    },
    "estar": {
        "preterito perfecto simple": "estuve", "preterito imperfecto": "estaba",
        "futuro": "estaré", "condicional": "estaría",
        "example": ("Estuve en Madrid el verano pasado.", "I was in Madrid last summer.")
    },
    "poder": {
        "preterito perfecto simple": "pude", "preterito imperfecto": "podía",
        "futuro": "podré", "condicional": "podría",
        "example": ("No pude terminar el libro.", "I couldn't finish the book.")
    }
}

# --- SESSION STATE ---
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_verb' not in st.session_state:
    st.session_state.current_verb = random.choice(list(VERB_DATA.keys()))
if 'current_tense' not in st.session_state:
    st.session_state.current_tense = random.choice(["preterito perfecto simple", "preterito imperfecto", "futuro", "condicional"])
if 'answered' not in st.session_state:
    st.session_state.answered = False
if 'last_result' not in st.session_state:
    st.session_state.last_result = None

def next_question():
    st.session_state.current_verb = random.choice(list(VERB_DATA.keys()))
    st.session_state.current_tense = random.choice(["preterito perfecto simple", "preterito imperfecto", "futuro", "condicional"])
    st.session_state.answered = False
    st.session_state.last_result = None

# --- UI ---
st.set_page_config(page_title="Spanish Verb Master", page_icon="🇪🇸")
st.title("🇪🇸 Spanish Conjugation Master")

st.sidebar.metric("Total Score", st.session_state.score)
if st.sidebar.button("Reset Game"):
    st.session_state.score = 0
    next_question()
    st.rerun()

verb = st.session_state.current_verb
tense = st.session_state.current_tense
correct_ans = VERB_DATA[verb][tense]

st.info(f"Conjugate **{verb.upper()}** in the **{tense.upper()}**")
st.write("*Note: Use the 1st person singular (Yo) form.*")

# --- THE FORM ---
with st.form(key='conjugation_form'):
    user_guess = st.text_input("Your Answer:", placeholder="e.g. hablé").strip().lower()
    submit_button = st.form_submit_button(label='Submit Answer')

if submit_button and not st.session_state.answered:
    st.session_state.answered = True
    if user_guess == correct_ans:
        st.session_state.score += 1
        st.session_state.last_result = "correct"
    else:
        st.session_state.last_result = "incorrect"

# --- FEEDBACK & NEXT STEPS ---
if st.session_state.answered:
    if st.session_state.last_result == "correct":
        st.success(f"✨ ¡Correcto! La respuesta es **{correct_ans}**.")
        es, en = VERB_DATA[verb]["example"]
        st.write(f"📖 *{es}* ({en})")
    else:
        st.error(f"❌ Incorrecto. La forma correcta es **{correct_ans}**.")
    
    if st.button("Next Verb ➡️"):
        next_question()
        st.rerun()

st.divider()
st.caption("Common accents: á, é, í, ó, ú")
