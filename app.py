import streamlit as st
import random

# --- DATASET ---
# (Abbreviated for clarity, follow this structure for all 50 verbs)
VERB_DATA = {
    "ser": {
        "english": "to be",
        "preterito perfecto simple": ["fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron"],
        "preterito imperfecto": ["era", "eras", "era", "éramos", "erais", "eran"],
        "futuro": ["seré", "serás", "será", "seremos", "seréis", "serán"],
        "condicional": ["sería", "serías", "sería", "seríamos", "seríais", "serían"],
        "example": ("Él fue mi profesor.", "He was my teacher.")
    },
    "estar": {
        "english": "to be",
        "preterito perfecto simple": ["estuve", "estuviste", "estuvo", "estuvimos", "estuvisteis", "estuvieron"],
        "preterito imperfecto": ["estaba", "estabas", "estaba", "estábamos", "estabais", "estaban"],
        "futuro": ["estaré", "estarás", "estará", "estaremos", "estaréis", "estarán"],
        "condicional": ["estaría", "estarías", "estaría", "estaríamos", "estaríais", "estarían"],
        "example": ("Estuve en la playa.", "We were at the beach.")
    },
    "tener": {
        "english": "to have",
        "preterito perfecto simple": ["tuve", "tuviste", "tuvo", "tuvimos", "tuvisteis", "tuvieron"],
        "preterito imperfecto": ["tenía", "tenías", "tenía", "teníamos", "teníais", "tenían"],
        "futuro": ["tendré", "tendrás", "tendrá", "tendremos", "tendréis", "tendrán"],
        "condicional": ["tendría", "tendrías", "tendría", "tendríamos", "tendríais", "tendrían"],
        "example": ("Tuve mucho trabajo ayer.", "I had a lot of work yesterday.")
    }
}

PRONOUNS = ["Yo", "Tú", "Él/Ella/Usted", "Nosotros", "Vosotros", "Ellos/Ellas/Ustedes"]

# --- INITIALIZE SESSION STATE ---
if 'game_started' not in st.session_state:
    st.session_state.game_started = False
if 'level' not in st.session_state:
    st.session_state.level = None
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_verb' not in st.session_state:
    st.session_state.current_verb = random.choice(list(VERB_DATA.keys()))
if 'current_tense' not in st.session_state:
    st.session_state.current_tense = random.choice(["preterito perfecto simple", "preterito imperfecto", "futuro", "condicional"])
if 'pronoun_idx' not in st.session_state:
    st.session_state.pronoun_idx = random.randint(0, 5)
if 'answered' not in st.session_state:
    st.session_state.answered = False

def next_question():
    st.session_state.current_verb = random.choice(list(VERB_DATA.keys()))
    st.session_state.current_tense = random.choice(["preterito perfecto simple", "preterito imperfecto", "futuro", "condicional"])
    st.session_state.pronoun_idx = random.randint(0, 5)
    st.session_state.answered = False

# --- UI LOGIC ---

# SCREEN 1: THE OPENING SCREEN
if not st.session_state.game_started:
    st.title("🏆 Spanish Verb Master")
    st.markdown("""
    Welcome! Choose your path to master the top 50 Spanish verbs.
    
    *   **Level 1**: Vocabulary – Guess the English translation of the infinitive.
    *   **Level 2**: Conjugation – Practice Preterite, Imperfect, Future, and Conditional.
    """)
    
    choice = st.selectbox("Select your level:", ["Level 1: Vocabulary", "Level 2: Conjugations"])
    
    if st.button("Start Game 🚀"):
        st.session_state.level = choice
        st.session_state.game_started = True
        st.rerun()

# SCREEN 2: THE ACTUAL GAME
else:
    st.sidebar.title("🎮 Game Info")
    st.sidebar.write(f"**Mode:** {st.session_state.level}")
    st.sidebar.metric("Current Score", st.session_state.score)
    
    if st.sidebar.button("Quit to Main Menu"):
        st.session_state.game_started = False
        st.session_state.score = 0
        st.rerun()

    verb = st.session_state.current_verb
    verb_info = VERB_DATA[verb]

    # LEVEL 1 UI
    if "Level 1" in st.session_state.level:
        st.header("Level 1: Translation")
        st.subheader(f"What does the verb **'{verb.upper()}'** mean?")
        
        with st.form("l1_form", clear_on_submit=True):
            ans = st.text_input("Answer in English:").strip().lower()
            submitted = st.form_submit_button("Check")
            
        if submitted:
            st.session_state.answered = True
            correct = verb_info["english"].lower()
            if ans in correct or correct in ans:
                st.success(f"¡Correcto! **{verb}** = **{verb_info['english']}**")
                st.session_state.score += 1
            else:
                st.error(f"Incorrecto. **{verb}** means **{verb_info['english']}**.")

    # LEVEL 2 UI
    else:
        st.header("Level 2: Conjugation")
        tense = st.session_state.current_tense
        pronoun = PRONOUNS[st.session_state.pronoun_idx]
        correct_ans = verb_info[tense][st.session_state.pronoun_idx]

        st.markdown(f"Verb: **{verb.upper()}**")
        st.markdown(f"Tense: **{tense.title()}** | Pronoun: **{pronoun}**")

        with st.form("l2_form", clear_on_submit=True):
            ans = st.text_input("Conjugation:").strip().lower()
            submitted = st.form_submit_button("Check")

        if submitted:
            st.session_state.answered = True
            if ans == correct_ans:
                st.success(f"¡Perfecto! La respuesta es **{correct_ans}**.")
                st.session_state.score += 1
                es, en = verb_info["example"]
                st.info(f"💡 {es} ({en})")
            else:
                st.error(f"No. The correct form for {pronoun} is **{correct_ans}**.")

    # NAVIGATION BUTTONS
    if st.session_state.answered:
        if st.button("Next Verb ➡️"):
            next_question()
            st.rerun()
