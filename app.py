import streamlit as st
import random

# --- DATASET ---
# Add your top 100 verbs here using this structure
VERB_DATA = {
    "hablar": {
        "preterito perfecto simple": "hablé",
        "preterito imperfecto": "hablaba",
        "futuro": "hablaré",
        "condicional": "hablaría",
        "example": ("Yo hablé con mi madre ayer.", "I spoke with my mother yesterday.")
    },
    "tener": {
        "preterito perfecto simple": "tuve",
        "preterito imperfecto": "tenía",
        "futuro": "tendré",
        "condicional": "tendría",
        "example": ("Tendré un coche nuevo pronto.", "I will have a new car soon.")
    },
    "ir": {
        "preterito perfecto simple": "fui",
        "preterito imperfecto": "iba",
        "futuro": "iré",
        "condicional": "iría",
        "example": ("Nosotros íbamos al parque cada día.", "We used to go to the park every day.")
    },
    "hacer": {
        "preterito perfecto simple": "hice",
        "preterito imperfecto": "hacía",
        "futuro": "haré",
        "condicional": "haría",
        "example": ("Mañana haré la tarea.", "Tomorrow I will do the homework.")
    }
}

# --- SESSION STATE INITIALIZATION ---
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_verb' not in st.session_state:
    st.session_state.current_verb = random.choice(list(VERB_DATA.keys()))
if 'current_tense' not in st.session_state:
    st.session_state.current_tense = random.choice(["preterito perfecto simple", "preterito imperfecto", "futuro", "condicional"])
if 'feedback' not in st.session_state:
    st.session_state.feedback = ""

# --- APP LAYOUT ---
st.title("🇪🇸 Spanish Conjugation Master")
st.subheader("Master the top 100 verbs")

col1, col2 = st.columns(2)
with col1:
    st.metric("Score", st.session_state.score)
with col2:
    if st.button("New Verb"):
        st.session_state.current_verb = random.choice(list(VERB_DATA.keys()))
        st.session_state.current_tense = random.choice(["preterito perfecto simple", "preterito imperfecto", "futuro", "condicional"])
        st.session_state.feedback = ""
        st.rerun()

st.divider()

# Game Logic Display
verb = st.session_state.current_verb
tense = st.session_state.current_tense

st.write(f"Conjugate the verb: **{verb.upper()}**")
st.write(f"Tense: **{tense.title()}** (1st Person Singular - Yo)")

# User Input
with st.form(key='answer_form', clear_on_submit=True):
    user_guess = st.text_input("Enter conjugation:").strip().lower()
    submit = st.form_submit_id("Check Answer")

if submit:
    correct_ans = VERB_DATA[verb][tense]
    if user_guess == correct_ans:
        st.session_state.score += 1
        st.session_state.feedback = "correct"
        # Setup next verb for the next refresh
        st.session_state.last_verb = verb # store to show example
    else:
        st.session_state.feedback = "incorrect"
        st.session_state.last_correct = correct_ans

# --- FEEDBACK DISPLAY ---
if st.session_state.feedback == "correct":
    st.success(f"¡Excelente! +1 Point.")
    ex_es, ex_en = VERB_DATA[verb]["example"]
    st.info(f"**Example:** {ex_es}\n\n**Translation:** {ex_en}")
    
elif st.session_state.feedback == "incorrect":
    st.error(f"Not quite! The correct conjugation was: **{VERB_DATA[verb][tense]}**")

st.markdown("---")
st.caption("Tip: Don't forget your accents! (á, é, í, ó, ú)")
