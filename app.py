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
        "example": ("Estuvimos en la playa.", "We were at the beach.")
    },
    "haber": {
        "english": "to have (auxiliary)",
        "preterito perfecto simple": ["hube", "hubiste", "hubo", "hubimos", "hubisteis", "hubieron"],
        "preterito imperfecto": ["había", "habías", "había", "habíamos", "habíais", "habían"],
        "futuro": ["habré", "habrás", "habrá", "habremos", "habréis", "habrán"],
        "condicional": ["habría", "habrías", "habría", "habríamos", "habríais", "habrían"],
        "example": ("Había mucha gente.", "There were many people.")
    },
    "tener": {
        "english": "to have / to possess",
        "preterito perfecto simple": ["tuve", "tuviste", "tuvo", "tuvimos", "tuvisteis", "tuvieron"],
        "preterito imperfecto": ["tenía", "tenías", "tenía", "teníamos", "teníais", "tenían"],
        "futuro": ["tendré", "tendrás", "tendrá", "tendremos", "tendréis", "tendrán"],
        "condicional": ["tendría", "tendrías", "tendría", "tendríamos", "tendríais", "tendrían"],
        "example": ("Tuve un perro.", "I had a dog.")
    },
    "poder": {
        "english": "to be able to / can",
        "preterito perfecto simple": ["pude", "pudiste", "pudo", "pudimos", "pudisteis", "pudieron"],
        "preterito imperfecto": ["podía", "podías", "podía", "podíamos", "podíais", "podían"],
        "futuro": ["podré", "podrás", "podrá", "podremos", "podréis", "podrán"],
        "condicional": ["podría", "podrías", "podría", "podríamos", "podríais", "podrían"],
        "example": ("No pude dormir.", "I couldn't sleep.")
    },
    "hacer": {
        "english": "to do / to make",
        "preterito perfecto simple": ["hice", "hiciste", "hizo", "hicimos", "hicisteis", "hicieron"],
        "preterito imperfecto": ["hacía", "hacías", "hacía", "hacíamos", "hacíais", "hacían"],
        "futuro": ["haré", "harás", "hará", "haremos", "haréis", "harán"],
        "condicional": ["haría", "harías", "haría", "haríamos", "haríais", "harían"],
        "example": ("Hice la tarea.", "I did the homework.")
    },
    "decir": {
        "english": "to say / to tell",
        "preterito perfecto simple": ["dije", "dijiste", "dijo", "dijimos", "dijisteis", "dijeron"],
        "preterito imperfecto": ["decía", "decías", "decía", "decíamos", "decíais", "decían"],
        "futuro": ["diré", "dirás", "dirá", "diremos", "diréis", "dirán"],
        "condicional": ["diría", "dirías", "diría", "diríamos", "diríais", "dirían"],
        "example": ("Él me dijo la verdad.", "He told me the truth.")
    },
    "ir": {
        "english": "to go",
        "preterito perfecto simple": ["fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron"],
        "preterito imperfecto": ["iba", "ibas", "iba", "íbamos", "ibais", "iban"],
        "futuro": ["iré", "irás", "irá", "iremos", "iréis", "irán"],
        "condicional": ["iría", "irías", "iría", "iríamos", "iríais", "irían"],
        "example": ("Fui al cine.", "I went to the cinema.")
    },
    "ver": {
        "english": "to see",
        "preterito perfecto simple": ["vi", "viste", "vio", "vimos", "visteis", "vieron"],
        "preterito imperfecto": ["veía", "veías", "veía", "veíamos", "veíais", "veían"],
        "futuro": ["veré", "verás", "verá", "veremos", "veréis", "verán"],
        "condicional": ["vería", "verías", "vería", "veríamos", "veríais", "verían"],
        "example": ("Vi una película.", "I saw a movie.")
    },
    "dar": {
        "english": "to give",
        "preterito perfecto simple": ["di", "diste", "dio", "dimos", "disteis", "dieron"],
        "preterito imperfecto": ["daba", "dabas", "daba", "dábamos", "dabais", "daban"],
        "futuro": ["daré", "darás", "dará", "daremos", "daréis", "darán"],
        "condicional": ["daría", "darías", "daría", "daríamos", "daríais", "darían"],
        "example": ("Le di un regalo.", "I gave him/her a gift.")
    },
    "saber": {
        "english": "to know (facts)",
        "preterito perfecto simple": ["supe", "supiste", "supo", "supimos", "supisteis", "supieron"],
        "preterito imperfecto": ["sabía", "sabías", "sabía", "sabíamos", "sabíais", "sabían"],
        "futuro": ["sabré", "sabrás", "sabrá", "sabremos", "sabréis", "sabrán"],
        "condicional": ["sabría", "sabrías", "sabría", "sabríamos", "sabríais", "sabrían"],
        "example": ("No supe qué decir.", "I didn't know what to say.")
    },
    "querer": {
        "english": "to want / to love",
        "preterito perfecto simple": ["quise", "quisiste", "quiso", "quisimos", "quisisteis", "quisieron"],
        "preterito imperfecto": ["quería", "querías", "quería", "queríamos", "queríais", "querían"],
        "futuro": ["querré", "querrás", "querrá", "querremos", "querréis", "querrán"],
        "condicional": ["querría", "querrías", "querría", "querríamos", "querríais", "querrían"],
        "example": ("Quise salir temprano.", "I wanted to leave early.")
    },
    "llegar": {
        "english": "to arrive",
        "preterito perfecto simple": ["llegué", "llegaste", "llegó", "llegamos", "llegasteis", "llegaron"],
        "preterito imperfecto": ["llegaba", "llegabas", "llegaba", "llegábamos", "llegabais", "llegaban"],
        "futuro": ["llegaré", "llegarás", "llegará", "llegaremos", "llegaréis", "llegarán"],
        "condicional": ["llegaría", "llegarías", "llegaría", "llegaríamos", "llegaríais", "llegarían"],
        "example": ("Llegué a las ocho.", "I arrived at eight.")
    },
    "pasar": {
        "english": "to pass / to happen",
        "preterito perfecto simple": ["pasé", "pasaste", "pasó", "pasamos", "pasasteis", "pasaron"],
        "preterito imperfecto": ["pasaba", "pasabas", "pasaba", "pasábamos", "pasabais", "pasaban"],
        "futuro": ["pasaré", "pasarás", "pasará", "pasaremos", "pasaréis", "pasarán"],
        "condicional": ["pasaría", "pasarías", "pasaría", "pasaríamos", "pasaríais", "pasarían"],
        "example": ("¿Qué pasó?", "What happened?")
    },
    "deber": {
        "english": "to owe / must",
        "preterito perfecto simple": ["debí", "debiste", "debió", "debimos", "debisteis", "debieron"],
        "preterito imperfecto": ["debía", "debías", "debía", "debíamos", "debíais", "debían"],
        "futuro": ["deberé", "deberás", "deberá", "deberemos", "deberéis", "deberán"],
        "condicional": ["debería", "deberías", "debería", "deberíamos", "deberíais", "deberían"],
        "example": ("Debía estudiar más.", "I should have studied more.")
    },
    "poner": {
        "english": "to put",
        "preterito perfecto simple": ["puse", "pusiste", "puso", "pusimos", "pusisteis", "pusieron"],
        "preterito imperfecto": ["ponía", "ponías", "ponía", "poníamos", "poníais", "ponían"],
        "futuro": ["pondré", "pondrás", "pondrá", "pondremos", "pondréis", "pondrán"],
        "condicional": ["pondría", "pondrías", "pondría", "pondríamos", "pondríais", "pondrían"],
        "example": ("Puse el libro en la mesa.", "I put the book on the table.")
    },
    "parecer": {
        "english": "to seem",
        "preterito perfecto simple": ["parecí", "pareciste", "pareció", "parecimos", "parecisteis", "parecieron"],
        "preterito imperfecto": ["parecía", "parecías", "parecía", "parecíamos", "parecíais", "parecían"],
        "futuro": ["pareceré", "parecerás", "parecerá", "pareceremos", "pareceréis", "parecerán"],
        "condicional": ["parecería", "parecerías", "parecería", "pareceríamos", "pareceríais", "parecerían"],
        "example": ("Parecía cansado.", "He seemed tired.")
    },
    "quedar": {
        "english": "to stay / to remain",
        "preterito perfecto simple": ["quedé", "quedaste", "quedó", "quedamos", "quedasteis", "quedaron"],
        "preterito imperfecto": ["quedaba", "quedabas", "quedaba", "quedábamos", "quedabais", "quedaban"],
        "futuro": ["quedaré", "quedarás", "quedará", "quedaremos", "quedaréis", "quedarán"],
        "condicional": ["quedaría", "quedarías", "quedaría", "quedaríamos", "quedaríais", "quedarían"],
        "example": ("Me quedé en casa.", "I stayed at home.")
    },
    "creer": {
        "english": "to believe",
        "preterito perfecto simple": ["creí", "creíste", "creyó", "creímos", "creísteis", "creyeron"],
        "preterito imperfecto": ["creía", "creías", "creía", "creíamos", "creíais", "creían"],
        "futuro": ["creeré", "creerás", "creerá", "creeremos", "creeréis", "creerán"],
        "condicional": ["creería", "creerías", "creería", "creeríamos", "creeríais", "creerían"],
        "example": ("No lo creí.", "I didn't believe it.")
    },
    "hablar": {
        "english": "to speak / to talk",
        "preterito perfecto simple": ["hablé", "hablaste", "habló", "hablamos", "hablasteis", "hablaron"],
        "preterito imperfecto": ["hablaba", "hablabas", "hablaba", "hablábamos", "hablabais", "hablaban"],
        "futuro": ["hablaré", "hablarás", "hablará", "hablaremos", "hablaréis", "hablarán"],
        "condicional": ["hablaría", "hablarías", "hablaría", "hablaríamos", "hablaríais", "hablarían"],
        "example": ("Hablamos por teléfono.", "We talked on the phone.")
    },
    "llevar": {
        "english": "to carry / to take",
        "preterito perfecto simple": ["llevé", "llevaste", "llevó", "llevamos", "llevasteis", "llevaron"],
        "preterito imperfecto": ["llevaba", "llevabas", "llevaba", "llevábamos", "llevabais", "llevaban"],
        "futuro": ["llevaré", "llevarás", "llevará", "llevaremos", "llevaréis", "llevarán"],
        "condicional": ["llevaría", "llevarías", "llevaría", "llevaríamos", "llevaríais", "llevarían"],
        "example": ("Llevé las maletas.", "I carried the suitcases.")
    },
    "dejar": {
        "english": "to leave / to let",
        "preterito perfecto simple": ["dejé", "dejaste", "dejó", "dejamos", "dejasteis", "dejaron"],
        "preterito imperfecto": ["dejaba", "dejabas", "dejaba", "dejábamos", "dejabais", "dejaban"],
        "futuro": ["dejaré", "dejarás", "dejará", "dejaremos", "dejaréis", "dejarán"],
        "condicional": ["dejaría", "dejarías", "dejaría", "dejaríamos", "dejaríais", "dejarían"],
        "example": ("Dejé las llaves.", "I left the keys.")
    },
    "seguir": {
        "english": "to follow / to continue",
        "preterito perfecto simple": ["seguí", "seguiste", "siguió", "seguimos", "seguisteis", "siguieron"],
        "preterito imperfecto": ["seguía", "seguías", "seguía", "seguíamos", "seguíais", "seguían"],
        "futuro": ["seguiré", "seguirás", "seguirá", "seguiremos", "seguiréis", "seguirán"],
        "condicional": ["seguiría", "seguirías", "seguiría", "seguiríamos", "seguiríais", "seguirían"],
        "example": ("Seguí las instrucciones.", "I followed the instructions.")
    },
    "encontrar": {
        "english": "to find",
        "preterito perfecto simple": ["encontré", "encontraste", "encontró", "encontramos", "encontrasteis", "encontraron"],
        "preterito imperfecto": ["encontraba", "encontrabas", "encontraba", "encontrábamos", "encontrabais", "encontraban"],
        "futuro": ["encontraré", "encontrarás", "encontrará", "encontraremos", "encontraréis", "encontrarán"],
        "condicional": ["encontraría", "encontrarías", "encontraría", "encontraríamos", "encontraríais", "encontrarían"],
        "example": ("Encontré mi cartera.", "I found my wallet.")
    },
    "llamar": {
        "english": "to call",
        "preterito perfecto simple": ["llamé", "llamaste", "llamó", "llamamos", "llamasteis", "llamaron"],
        "preterito imperfecto": ["llamaba", "llamabas", "llamaba", "llamábamos", "llamabais", "llamaban"],
        "futuro": ["llamaré", "llamarás", "llamará", "llamaremos", "llamaréis", "llamarán"],
        "condicional": ["llamaría", "llamarías", "llamaría", "llamaríamos", "llamaríais", "llamarían"],
        "example": ("Te llamé ayer.", "I called you yesterday.")
    },
    "venir": {
        "english": "to come",
        "preterito perfecto simple": ["vine", "viniste", "vino", "vinimos", "vinisteis", "vinieron"],
        "preterito imperfecto": ["venía", "venías", "venía", "veníamos", "veníais", "venían"],
        "futuro": ["vendré", "vendrás", "vendrá", "vendremos", "vendréis", "vendrán"],
        "condicional": ["vendría", "vendrías", "vendría", "vendríamos", "vendríais", "vendrían"],
        "example": ("Él vino a la fiesta.", "He came to the party.")
    },
    "pensar": {
        "english": "to think",
        "preterito perfecto simple": ["pensé", "pensaste", "pensó", "pensamos", "pensasteis", "pensaron"],
        "preterito imperfecto": ["pensaba", "pensabas", "pensaba", "pensábamos", "pensabais", "pensaban"],
        "futuro": ["pensaré", "pensarás", "pensará", "pensaremos", "pensaréis", "pensarán"],
        "condicional": ["pensaría", "pensarías", "pensaría", "pensaríamos", "pensaríais", "pensarían"],
        "example": ("Pensé en ti.", "I thought of you.")
    },
    "salir": {
        "english": "to leave / to go out",
        "preterito perfecto simple": ["salí", "saliste", "salió", "salimos", "salisteis", "salieron"],
        "preterito imperfecto": ["salía", "salías", "salía", "salíamos", "salíais", "salían"],
        "futuro": ["saldré", "saldrás", "saldrá", "saldremos", "saldréis", "saldrán"],
        "condicional": ["saldría", "saldrías", "saldría", "saldríamos", "saldríais", "saldrían"],
        "example": ("Salí de casa a las nueve.", "I left the house at nine.")
    },
    "volver": {
        "english": "to return / to come back",
        "preterito perfecto simple": ["volví", "volviste", "volvió", "volvimos", "volvisteis", "volvieron"],
        "preterito imperfecto": ["volvía", "volvías", "volvía", "volvíamos", "volvíais", "volvían"],
        "futuro": ["volveré", "volverás", "volverá", "volveremos", "volveréis", "volverán"],
        "condicional": ["volvería", "volverías", "volvería", "volveríamos", "volveríais", "volverían"],
        "example": ("Volvieron muy tarde.", "They returned very late.")
    },
    "tomar": {
        "english": "to take / to drink",
        "preterito perfecto simple": ["tomé", "tomaste", "tomó", "tomamos", "tomasteis", "tomaron"],
        "preterito imperfecto": ["tomaba", "tomabas", "tomaba", "tomábamos", "tomabais", "tomaban"],
        "futuro": ["tomaré", "tomarás", "tomará", "tomaremos", "tomaréis", "tomarán"],
        "condicional": ["tomaría", "tomarías", "tomaría", "tomaríamos", "tomaríais", "tomarían"],
        "example": ("Tomé un café.", "I drank a coffee.")
    },
    "conocer": {
        "english": "to know (people/places)",
        "preterito perfecto simple": ["conocí", "conociste", "conoció", "conocimos", "conocisteis", "conocieron"],
        "preterito imperfecto": ["conocía", "conocías", "conocía", "conocíamos", "conocíais", "conocían"],
        "futuro": ["conoceré", "conocerás", "conocerá", "conoceremos", "conoceréis", "conocerán"],
        "condicional": ["conocería", "conocerías", "conocería", "conoceríamos", "conoceríais", "conocerían"],
        "example": ("Conocí a María ayer.", "I met Maria yesterday.")
    },
    "vivir": {
        "english": "to live",
        "preterito perfecto simple": ["viví", "viviste", "vivió", "vivimos", "vivisteis", "vivieron"],
        "preterito imperfecto": ["vivía", "vivías", "vivía", "vivíamos", "vivíais", "vivían"],
        "futuro": ["viviré", "vivirás", "vivirá", "viviremos", "viviréis", "vivirán"],
        "condicional": ["viviría", "vivirías", "viviría", "viviríamos", "viviríais", "vivirían"],
        "example": ("Viví en España.", "I lived in Spain.")
    },
    "sentir": {
        "english": "to feel",
        "preterito perfecto simple": ["sentí", "sentiste", "sintió", "sentimos", "sentisteis", "sintieron"],
        "preterito imperfecto": ["sentía", "sentías", "sentía", "sentíamos", "sentíais", "sentían"],
        "futuro": ["sentiré", "sentirás", "sentirá", "sentiremos", "sentiréis", "sentirán"],
        "condicional": ["sentiría", "sentirías", "sentiría", "sentiríamos", "sentiríais", "sentirían"],
        "example": ("Sentí mucho frío.", "I felt very cold.")
    },
    "mirar": {
        "english": "to look",
        "preterito perfecto simple": ["miré", "miraste", "miró", "miramos", "mirasteis", "miraron"],
        "preterito imperfecto": ["miraba", "mirabas", "miraba", "mirábamos", "mirabais", "miraban"],
        "futuro": ["miraré", "mirarás", "mirará", "miraremos", "miraréis", "mirarán"],
        "condicional": ["miraría", "mirarías", "miraría", "miraríamos", "miraríais", "mirarían"],
        "example": ("Miré por la ventana.", "I looked through the window.")
    },
    "trabajar": {
        "english": "to work",
        "preterito perfecto simple": ["trabajé", "trabajaste", "trabajó", "trabajamos", "trabajasteis", "trabajaron"],
        "preterito imperfecto": ["trabajaba", "trabajabas", "trabajaba", "trabajábamos", "trabajabais", "trabajaban"],
        "futuro": ["trabajaré", "trabajarás", "trabajará", "trabajaremos", "trabajaréis", "trabajarán"],
        "condicional": ["trabajaría", "trabajarías", "trabajaría", "trabajaríamos", "trabajaríais", "trabajarían"],
        "example": ("Trabajé todo el día.", "I worked all day.")
    },
    "esperar": {
        "english": "to wait / to hope",
        "preterito perfecto simple": ["esperé", "esperaste", "esperó", "esperamos", "esperasteis", "esperaron"],
        "preterito imperfecto": ["esperaba", "esperabas", "esperaba", "esperábamos", "esperabais", "esperaban"],
        "futuro": ["esperaré", "esperarás", "esperará", "esperaremos", "esperaréis", "esperarán"],
        "condicional": ["esperaría", "esperarías", "esperaría", "esperaríamos", "esperaríais", "esperarían"],
        "example": ("Esperé el autobús.", "I waited for the bus.")
    },
    "buscar": {
        "english": "to search / to look for",
        "preterito perfecto simple": ["busqué", "buscaste", "buscó", "buscamos", "buscasteis", "buscaron"],
        "preterito imperfecto": ["buscaba", "buscabas", "buscaba", "buscábamos", "buscabais", "buscaban"],
        "futuro": ["buscaré", "buscarás", "buscará", "buscaremos", "buscaréis", "buscarán"],
        "condicional": ["buscaría", "buscarías", "buscaría", "buscaríamos", "buscaríais", "buscarían"],
        "example": ("Busqué mis llaves.", "I looked for my keys.")
    },
    "escribir": {
        "english": "to write",
        "preterito perfecto simple": ["escribí", "escribiste", "escribió", "escribimos", "escribisteis", "escribieron"],
        "preterito imperfecto": ["escribía", "escribías", "escribía", "escribíamos", "escribíais", "escribían"],
        "futuro": ["escribiré", "escribirás", "escribirá", "escribiremos", "escribiréis", "escribirán"],
        "condicional": ["escribiría", "escribirías", "escribiría", "escribiríamos", "escribiríais", "escribirían"],
        "example": ("Escribí una carta.", "I wrote a letter.")
    },
    "entender": {
        "english": "to understand",
        "preterito perfecto simple": ["entendí", "entendiste", "entendió", "entendimos", "entendisteis", "entendieron"],
        "preterito imperfecto": ["entendía", "entendías", "entendía", "entendíamos", "entendíais", "entendían"],
        "futuro": ["entenderé", "entenderás", "entenderá", "entenderemos", "entenderéis", "entenderán"],
        "condicional": ["entendería", "entenderías", "entendería", "entenderíamos", "entenderíais", "entenderían"],
        "example": ("No entendí la pregunta.", "I didn't understand the question.")
    },
    "leer": {
        "english": "to read",
        "preterito perfecto simple": ["leí", "leíste", "leyó", "leímos", "leísteis", "leyeron"],
        "preterito imperfecto": ["leía", "leías", "leía", "leíamos", "leíais", "leían"],
        "futuro": ["leeré", "leerás", "leerá", "leeremos", "leeréis", "leerán"],
        "condicional": ["leería", "leerías", "leería", "leeríamos", "leeríais", "leerían"],
        "example": ("Leímos el periódico.", "We read the newspaper.")
    },
    "comer": {
        "english": "to eat",
        "preterito perfecto simple": ["comí", "comiste", "comió", "comimos", "comisteis", "comieron"],
        "preterito imperfecto": ["comía", "comías", "comía", "comíamos", "comíais", "comían"],
        "futuro": ["comeré", "comerás", "comerá", "comeremos", "comeréis", "comerán"],
        "condicional": ["comería", "comerías", "comería", "comeríamos", "comeríais", "comerían"],
        "example": ("Comí una manzana.", "I ate an apple.")
    },
    "beber": {
        "english": "to drink",
        "preterito perfecto simple": ["bebí", "bebiste", "bebió", "bebimos", "bebisteis", "bebieron"],
        "preterito imperfecto": ["bebía", "bebías", "bebía", "bebíamos", "bebíais", "bebían"],
        "futuro": ["beberé", "beberás", "beberá", "beberemos", "beberéis", "beberán"],
        "condicional": ["bebería", "beberías", "bebería", "beberíamos", "beberíais", "beberían"],
        "example": ("Bebí mucha agua.", "I drank a lot of water.")
    },
    "comprar": {
        "english": "to buy",
        "preterito perfecto simple": ["compré", "compraste", "compró", "compramos", "comprasteis", "compraron"],
        "preterito imperfecto": ["compraba", "comprabas", "compraba", "comprábamos", "comprabais", "compraban"],
        "futuro": ["compraré", "comprarás", "comprará", "compraremos", "compraréis", "comprarán"],
        "condicional": ["compraría", "comprarías", "compraría", "compraríamos", "compraríais", "compraría"],
        "example": ("Compré ropa nueva.", "I bought new clothes.")
    },
    "pagar": {
        "english": "to pay",
        "preterito perfecto simple": ["pagué", "pagaste", "pagó", "pagamos", "pagasteis", "pagaron"],
        "preterito imperfecto": ["pagaba", "pagabas", "pagaba", "pagábamos", "pagabais", "pagaban"],
        "futuro": ["pagaré", "pagarás", "pagará", "pagaremos", "pagaréis", "pagarán"],
        "condicional": ["pagaría", "pagarías", "pagaría", "pagaríamos", "pagaríais", "pagarían"],
        "example": ("Pagué la cuenta.", "I paid the bill.")
    },
    "ayudar": {
        "english": "to help",
        "preterito perfecto simple": ["ayudé", "ayudaste", "ayudó", "ayudamos", "ayudasteis", "ayudaron"],
        "preterito imperfecto": ["ayudaba", "ayudabas", "ayudaba", "ayudábamos", "ayudabais", "ayudaban"],
        "futuro": ["ayudaré", "ayudarás", "ayudará", "ayudaremos", "ayudaréis", "ayudarán"],
        "condicional": ["ayudaría", "ayudarías", "ayudaría", "ayudaríamos", "ayudaríais", "ayudarían"],
        "example": ("Ayudamos a mi abuelo.", "We helped my grandfather.")
    },
    "traer": {
        "english": "to bring",
        "preterito perfecto simple": ["traje", "trajiste", "trajo", "trajimos", "trajisteis", "trajeron"],
        "preterito imperfecto": ["traía", "traías", "traía", "traíamos", "traíais", "traían"],
        "futuro": ["traeré", "traerás", "traerá", "traeremos", "traeréis", "traerán"],
        "condicional": ["traería", "traerías", "traería", "traeríamos", "traeríais", "traerían"],
        "example": ("Traje comida.", "I brought food.")
    },
    "escuchar": {
        "english": "to listen",
        "preterito perfecto simple": ["escuché", "escuchaste", "escuchó", "escuchamos", "escuchasteis", "escucharon"],
        "preterito imperfecto": ["escuchaba", "escuchabas", "escuchaba", "escuchábamos", "escuchabais", "escuchaban"],
        "futuro": ["escucharé", "escucharás", "escuchará", "escucharemos", "escucharéis", "escucharán"],
        "condicional": ["escucharía", "escucharías", "escucharía", "escucharíamos", "escucharíais", "escucharía"],
        "example": ("Escuché música.", "I listened to music.")
    },
    "necesitar": {
        "english": "to need",
        "preterito perfecto simple": ["necesité", "necesitaste", "necesitó", "necesitamos", "necesitasteis", "necesitaron"],
        "preterito imperfecto": ["necesitaba", "necesitabas", "necesitaba", "necesitábamos", "necesitabais", "necesitaban"],
        "futuro": ["necesitaré", "necesitarás", "necesitará", "necesitaremos", "necesitaréis", "necesitarán"],
        "condicional": ["necesitaría", "necesitarías", "necesitaría", "necesitaríamos", "necesitaríais", "necesitarían"],
        "example": ("Necesité ayuda.", "I needed help.")
    },
    "entrar": {
        "english": "to enter",
        "preterito perfecto simple": ["entré", "entraste", "entró", "entramos", "entrasteis", "entraron"],
        "preterito imperfecto": ["entraba", "entrabas", "entraba", "entrábamos", "entrabais", "entraban"],
        "futuro": ["entraré", "entrarás", "entrará", "entraremos", "entraréis", "entrarán"],
        "condicional": ["entraría", "entrarías", "entraría", "entraríamos", "entraríais", "entrarían"],
        "example": ("Entramos en la sala.", "We entered the room.")
    },
    "usar": {
        "english": "to use",
        "preterito perfecto simple": ["usé", "usaste", "usó", "usamos", "usasteis", "usaron"],
        "preterito imperfecto": ["usaba", "usabas", "usaba", "usábamos", "usabais", "usaban"],
        "futuro": ["usaré", "usarás", "usará", "usaremos", "usaréis", "usarán"],
        "condicional": ["usaría", "usarías", "usaría", "usaríamos", "usaríais", "usarían"],
        "example": ("Usé tu computadora.", "I used your computer.")
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
