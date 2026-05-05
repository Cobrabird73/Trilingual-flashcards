import streamlit as st
import random

# --- DATASET (Top 50 Verbs) ---
# Note: For brevity in this example, I've filled the full lists for the first few.
# In a real app, you would continue filling the lists [yo, tú, él, nos, vos, ellos] for all.
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
        "example": ("Estuvimos en la playa.", "We were at the beach.")
    },
    "tener": {
        "english": "to have",
        "preterito perfecto simple": ["tuve", "tuviste", "tuvo", "tuvimos", "tuvisteis", "tuvieron"],
        "preterito imperfecto": ["tenía", "tenías", "tenía", "teníamos", "teníais", "tenían"],
        "futuro": ["tendré", "tendrás", "tendrá", "tendremos", "tendréis", "tendrán"],
        "condicional": ["tendría", "tendrías", "tendría", "tendríamos", "tendríais", "tendrían"],
        "example": ("Tuve mucho trabajo ayer.", "I had a lot of work yesterday.")
    },
    "hacer": {
        "english": "to do / to make",
        "preterito perfecto simple": ["hice", "hiciste", "hizo", "hicimos", "hicisteis", "hicieron"],
        "preterito imperfecto": ["hacía", "hacías", "hacía", "hacíamos", "hacíais", "hacían"],
        "futuro": ["haré", "harás", "hará", "haremos", "haréis", "harán"],
        "condicional": ["haría", "harías", "haría", "haríamos", "haríais", "harían"],
        "example": ("Hice la cena para todos.", "I made dinner for everyone.")
    },
    "poder": {"english": "to be able to / can", "preterito perfecto simple": ["pude", "pudiste", "pudo", "pudimos", "pudisteis", "pudieron"], "preterito imperfecto": ["podía", "podías", "podía", "podíamos", "podíais", "podían"], "futuro": ["podré", "podrás", "podrá", "podremos", "podréis", "podrán"], "condicional": ["podría", "podrías", "podría", "podríamos", "podríais", "podrían"], "example": ("No pude ir.", "I couldn't go.")},
    "ir": {"english": "to go", "preterito perfecto simple": ["fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron"], "preterito imperfecto": ["iba", "ibas", "iba", "íbamos", "ibais", "iban"], "futuro": ["iré", "irás", "irá", "iremos", "iréis", "irán"], "condicional": ["iría", "irías", "iría", "iríamos", "iríais", "irían"], "example": ("Fui al mercado.", "I went to the market.")},
    # ... Add the remaining 44 verbs here following the same structure ...
}

# Mapping English for the remaining list
BASIC_LIST = ["haber", "querer", "deber", "necesitar", "decir", "saber", "conocer", "pensar", "creer", "entender", "comprender", "preguntar", "contestar", "llamar", "venir", "llegar", "salir", "entrar", "volver", "pasar", "llevar", "traer", "quedar", "dar", "ver", "mirar", "oir", "escuchar", "comer", "beber", "vivir", "trabajar", "escribir", "leer", "pagar", "comprar", "vender", "usar", "ayudar", "esperar", "buscar", "encontrar", "sentir"]

PRONOUNS = ["Yo", "Tú", "Él/Ella/Usted", "Nosotros", "Vosotros", "Ellos/Ellas/Ustedes"]

# --- APP CONFIG ---
st.set_page_config(page_title="Spanish Learning Lab", page_icon="🎓")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Settings")
level = st.sidebar.radio("Choose Learning Level:", ["Level 1: English Translation", "Level 2: Verb Conjugation"])

if 'score' not in st.session_state: st.session_state.score = 0
if 'current_verb' not in st.session_state: st.session_state.current_verb = random.choice(list(VERB_DATA.keys()))
if 'current_tense' not in st.session_state: st.session_state.current_tense = random.choice(["preterito perfecto simple", "preterito imperfecto", "futuro", "condicional"])
if 'pronoun_idx' not in st.session_state: st.session_state.pronoun_idx = random.randint(0, 5)
if 'answered' not in st.session_state: st.session_state.answered = False

def get_new_question():
    st.session_state.current_verb = random.choice(list(VERB_DATA.keys()))
    st.session_state.current_tense = random.choice(["preterito perfecto simple", "preterito imperfecto", "futuro", "condicional"])
    st.session_state.pronoun_idx = random.randint(0, 5)
    st.session_state.answered = False

# --- UI LOGIC ---
st.title("🇪🇸 Spanish Learning Lab")
st.sidebar.metric("Your Total Score", st.session_state.score)

verb = st.session_state.current_verb
verb_info = VERB_DATA[verb]

if level == "Level 1: English Translation":
    st.subheader("Translate the Infinitive")
    st.info(f"What does the verb **{verb.upper()}** mean in English?")
    
    with st.form("level1_form"):
        user_guess = st.text_input("Translation:").strip().lower()
        submit = st.form_submit_button("Submit")
        
    if submit:
        st.session_state.answered = True
        correct = verb_info["english"].lower()
        # Allows for partial match if multiple meanings (e.g., "to do / to make")
        if user_guess in correct or correct in user_guess:
            st.success(f"Correcto! **{verb}** = **{verb_info['english']}**")
            st.session_state.score += 1
        else:
            st.error(f"Not quite. **{verb}** means **{verb_info['english']}**")

else:
    st.subheader("Master the Conjugations")
    tense = st.session_state.current_tense
    pronoun = PRONOUNS[st.session_state.pronoun_idx]
    correct_ans = verb_info[tense][st.session_state.pronoun_idx]
    
    st.info(f"Conjugate **{verb.upper()}**")
    st.write(f"**Tense:** {tense.title()} | **Pronoun:** {pronoun}")
    
    with st.form("level2_form"):
        user_guess = st.text_input("Conjugation:").strip().lower()
        submit = st.form_submit_button("Submit")
        
    if submit:
        st.session_state.answered = True
        if user_guess == correct_ans:
            st.success(f"✨ ¡Correcto! La respuesta es **{correct_ans}**.")
            st.session_state.score += 1
            es, en = verb_info["example"]
            st.write(f"📖 *Example:* {es} ({en})")
        else:
            st.error(f"❌ Incorrecto. The correct form is **{correct_ans}**.")

# Next Button
if st.session_state.answered:
    if st.button("Next Question ➡️"):
        get_new_question()
        st.rerun()
