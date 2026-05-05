Python
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
