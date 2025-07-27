fragen = [
    "Wie heißt du?",
    "Wie alt bist du?",
    "In welcher Stadt wohnst du?",
    "Was ist deine Lieblingsfarbe?",
    "Welches ist dein Lieblingsessen?",
    "Was ist dein Hobby?",
    "Welches Tier magst du am liebsten?",
    "Welcher ist dein Lieblingsfilm?",
    "Welche Musik hörst du gerne?",
    "Was ist dein Traumreiseziel?"
]

for i, frage in enumerate(fragen, start=1):
    antwort = input(f"Frage {i}/10: {frage} ")
    print(f"Du hast geantwortet: {antwort}\n")
