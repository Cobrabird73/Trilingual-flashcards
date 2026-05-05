import streamlit as st
import random

# --- DATASET STRUCTURE ---
# "Verb": { "Tense": [yo, tú, él, nosotros, vosotros, ellos], "example": (ES, EN) }
VERB_DATA = {
    "hablar": {
        "preterito perfecto simple": ["hablé", "hablaste", "habló", "hablamos", "hablasteis", "hablaron"],
        "preterito imperfecto": ["hablaba", "hablabas", "hablaba", "hablábamos", "hablabais", "hablaban"],
        "futuro": ["hablaré", "hablarás", "hablará", "hablaremos", "hablaréis", "hablarán"],
        "condicional": ["hablaría", "hablarías", "hablaría", "hablaríamos", "hablaríais", "hablarían"],
        "example": ("Ayer hablamos por teléfono.", "Yesterday we spoke on the phone.")
    },
    "ser": {
        "preterito perfecto simple": ["fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron"],
        "preterito imperfecto": ["era", "eras", "era", "éramos", "erais", "eran"],
        "futuro": ["seré", "serás", "será", "seremos", "seréis", "serán"],
        "condicional": ["sería", "serías", "sería", "seríamos", "seríais", "serían"],
        "example": ("Ellos fueron mejores amigos.", "They were best friends.")
    },
    "ir": {
        "preterito perfecto simple": ["fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron"],
        "preterito imperfecto": ["iba", "ibas", "iba", "íbamos", "ibais", "iban"],
        "futuro": ["iré", "irás", "irá", "iremos", "iréis", "irán"],
        "condicional": ["iría", "irías", "iría", "iríamos", "iríais", "irían"],
        "example": ("¿Ibas a la playa de niño?", "Did you used to go to the beach as a child?")
    },
    "tener": {
        "preterito perfecto simple": ["tuve", "tuviste", "tuvo", "tuvimos", "tuvisteis", "tuvieron"],
        "preterito imperfecto": ["tenía", "tenías", "tenía", "teníamos", "teníais", "tenían"],
        "futuro": ["tendré", "tendrás", "tendrá", "tendremos", "tendréis", "tendrán"],
        "condicional": ["tendría", "tendrías", "tendría", "tendríamos", "tendríais", "tendrían"],
        "example": ("Tendremos una fiesta mañana.", "We will have a party tomorrow.")
    }
    # Add more verbs here...
}

PRONOUNS = ["Yo", "Tú", "Él/Ella/Usted", "Nosotros", "Vosotros", "Ellos/Ellas/Ustedes"]

# --- SESSION STATE ---
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_verb' not in st.session_state:
    st.session_state.current_verb = random.choice(list(VERB_DATA.keys()))
if 'current_tense' not in st.session_state:
    st.session_state.current_tense = random.choice(["preterito perfecto simple", "preterito imperfecto", "futuro", "condicional"])
if 'pronoun_index' not in st.session_state:
    st.session_state.pronoun_index = random.randint(0, 5)
if 'answered' not in st.session_state:
    st.session_state.answered = False

def next_question():
    st.session_state.current_verb = random.choice(list(VERB_DATA.keys()))
    st.session_state.current_tense = random.choice(["preterito perfecto simple", "preterito imperfecto", "futuro", "condicional"])
    st.session_state.pronoun_index = random.randint(0, 5)
    st.session_state.answered = False

# --- UI SETUP ---
st.title("🇪🇸 Conjugation Master Pro")
st.sidebar.metric("Score", st.session_state.score)

verb = st.session_state.current_verb
tense = st.session_state.current_tense
pronoun = PRONOUNS[st.session_state.pronoun_index]
correct_ans = VERB_DATA[verb][tense][st.session_state.pronoun_index]

# Main Display
st.markdown(f"### Verb: `{verb.upper()}`")
st.markdown(f"**Tense:** {tense.title()}")
st.markdown(f"**Pronoun:** {pronoun}")

# Form
with st.form(key='game_form', clear_on_submit=True):
    user_input = st.text_input("Conjugation:").strip().lower()
    submit = st.form_submit_button("Submit")

if submit:
    st.session_state.answered = True
    if user_input == correct_ans:
        st.session_state.score += 1
        st.success(f"¡Correcto! **{correct_ans}** is right.")
        es, en = VERB_DATA[verb]["example"]
        st.info(f"💡 {es} ({en})")
    else:
        st.error(f"Incorrecto. The correct form for {pronoun} was **{correct_ans}**.")

if st.session_state.answered:
    if st.button("Next Question ➡️"):
        next_question()
        st.rerun()

st.divider()
st.caption("Common shortcuts: á (Alt+0225), é (Alt+0233), í (Alt+0237), ó (Alt+0243), ú (Alt+0250), ñ (Alt+0241)")
