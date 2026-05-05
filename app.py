import random

# A dictionary containing the verb data. 
# Format: "Infinitivo": { Tense: Conjugation, "example": (Spanish, English) }
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
    # Add more verbs here to reach the top 100
}

def play_game():
    score = 0
    verbs = list(VERB_DATA.keys())
    random.shuffle(verbs)

    print("--- ¡Bienvenido al Juego de Conjugación! ---")
    print("Type the correct conjugation for the given tense.")
    print("Type 'exit' at any time to quit.\n")

    for verb in verbs:
        tenses = ["preterito perfecto simple", "preterito imperfecto", "futuro", "condicional"]
        target_tense = random.choice(tenses)
        correct_answer = VERB_DATA[verb][target_tense]
        
        print(f"Verb: {verb.upper()}")
        user_input = input(f"Conjugate for '{target_tense}' (1st person singular - Yo): ").strip().lower()

        if user_input == 'exit':
            break

        if user_input == correct_answer:
            score += 1
            spanish_ex, english_ex = VERB_DATA[verb]["example"]
            print(f"✅ ¡Correcto! +1 point.")
            print(f"Example: {spanish_ex}")
            print(f"Translation: {english_ex}\n")
        else:
            print(f"❌ Incorrecto. The correct form was: '{correct_answer}'\n")

    print(f"--- Game Over ---")
    print(f"Your final score: {score}")

if __name__ == "__main__":
    play_game()
