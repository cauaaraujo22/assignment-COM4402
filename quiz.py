import random


def rio_bank():
    # Each item: (question_text, [4 options], correct_option_text)
    return [
        ("Rio de Janeiro is the capital of which Brazilian state?",
         ["São Paulo", "Rio de Janeiro", "Minas Gerais", "Bahia"], "Rio de Janeiro"),

        ("Which statue stands on top of Corcovado Mountain in Rio?",
         ["Christ the Redeemer", "The Thinker", "Statue of Liberty", "David"], "Christ the Redeemer"),

        ("Which mountain is famous for the cable car ride in Rio?",
         ["Sugarloaf (Pão de Açúcar)", "Pico da Neblina", "Mount Everest", "Serra do Mar"], "Sugarloaf (Pão de Açúcar)"),

        ("Which large football stadium is in Rio and hosted major matches?",
         ["Maracanã", "Mineirão", "Morumbi", "Arena da Baixada"], "Maracanã"),

        ("Which bay is closely associated with Rio and the Sugarloaf area?",
         ["Guanabara Bay", "Hudson Bay", "Bay of Bengal", "Ha Long Bay"], "Guanabara Bay"),

        ("Which neighbourhood is known for the Selarón Steps (Escadaria Selarón)?",
         ["Lapa", "Tijuca", "Barra da Tijuca", "Irajá"], "Lapa"),

        ("Which beach is most commonly linked with the iconic wave-pattern promenade in Rio?",
         ["Copacabana", "Ipanema", "Leblon", "Flamengo"], "Copacabana"),

        ("Which beach name is associated with the song 'The Girl from Ipanema'?",
         ["Ipanema", "Copacabana", "Barra da Tijuca", "Recreio"], "Ipanema"),

        ("What is the name of the famous aqueduct arches often photographed in Rio nightlife area?",
         ["Arcos da Lapa", "Ponte Rio-Niterói", "Arcos do Maracanã", "Arcos de Copacabana"], "Arcos da Lapa"),

        ("Which huge urban forest is located within the city of Rio?",
         ["Tijuca Forest", "Amazon Rainforest", "Atlantic Forest (entirely)", "Pantanal"], "Tijuca Forest"),

        ("Which neighbourhood is widely known for its bohemian vibe, hills, and old trams in Rio?",
         ["Santa Teresa", "Urca", "Bangu", "Campo Grande"], "Santa Teresa"),

        ("Where do Rio’s samba school performances happen during Carnival?",
         ["Sambadrome (Sapucaí)", "Maracanã", "Copacabana Fort", "Sugarloaf Arena"], "Sambadrome (Sapucaí)"),

        ("Which neighbourhood is right next to Sugarloaf Mountain and has Praia Vermelha nearby?",
         ["Urca", "Centro", "Madureira", "Bonsucesso"], "Urca"),

        ("Which viewpoint in Rio is known for a panoramic city view and is often visited at sunrise/sunset?",
         ["Mirante Dona Marta", "Mirante do Amazonas", "Mirante do Mar", "Mirante Paulista"], "Mirante Dona Marta"),

        ("Which famous attraction in Rio is a large botanical garden with many tropical plants?",
         ["Jardim Botânico", "Jardim das Tulipas", "Jardim Central de Salvador", "Jardim do Planalto"],
         "Jardim Botânico"),
    ]


def pick_quiz_set(bank, how_many):
    return random.sample(bank, how_many)


def read_name():
    text = input("Enter your name (press Enter for 'Player'): ").strip()
    return text if text else "Player"


def choose_feedback_mode():
    while True:
        raw = input("Feedback mode: (A) after each question, (B) only at the end: ").strip().upper()
        if raw in ("A", "B"):
            return raw  # "A" = instant, "B" = end only
        print("Please type A or B.")


def read_how_many(max_q):
    while True:
        raw = input(f"How many questions do you want? (1-{max_q}): ").strip()
        if raw.isdigit():
            n = int(raw)
            if 1 <= n <= max_q:
                return n
        print("Invalid number. Try again.")


def shuffle_choices(options, correct_text):
    shuffled = options[:]  # copy
    random.shuffle(shuffled)
    correct_index = shuffled.index(correct_text)
    correct_letter = "ABCD"[correct_index]
    return shuffled, correct_letter


def read_abcd():
    while True:
        raw = input("Your answer (A/B/C/D): ").strip().upper()
        if raw in ("A", "B", "C", "D"):
            return raw
        print("Invalid input. Please enter A, B, C, or D.")


def ask_question(number, q_text, opts, ans_text, instant_feedback):
    print("\n" + "=" * 60)
    print(f"Q{number}. {q_text}\n")

    shown, correct_letter = shuffle_choices(opts, ans_text)

    for i, opt in enumerate(shown):
        print(f"  { 'ABCD'[i] }) {opt}")

    chosen = read_abcd()
    is_right = (chosen == correct_letter)

    if instant_feedback:
        if is_right:
            print("✅ Correct!")
        else:
            correct_text = shown["ABCD".index(correct_letter)]
            print(f"❌ Incorrect. Correct answer: {correct_letter}) {correct_text}")

    return is_right, chosen, correct_letter, shown

  
def run_session(question_set, instant_feedback):
    score = 0
    wrong_log = []

    for idx, (q_text, opts, ans_text) in enumerate(question_set, start=1):
        ok, chosen, correct, shown = ask_question(idx, q_text, opts, ans_text, instant_feedback)
        if ok:
            score += 1
        else:
            wrong_log.append({
                "n": idx,
                "q": q_text,
                "shown": shown,
                "chosen": chosen,
                "correct": correct
            })

    return score, wrong_log


def show_summary(player, score, total):
    pct = (score / total) * 100
    print("\n" + "-" * 60)
    print(f"Finished! {player}, you scored {score}/{total} ({pct:.2f}%).")
    print("-" * 60)


def review_mistakes(wrong_log):
    if not wrong_log:
        print("\nNo wrong answers to review. Great job!")
        return

    print("\nReview of incorrect answers:")
    for item in wrong_log:
        print("\n" + "-" * 60)
        print(f"Q{item['n']}. {item['q']}")
        for i, opt in enumerate(item["shown"]):
            letter = "ABCD"[i]
            tag = ""
            if letter == item["correct"]:
                tag = "  <-- correct"
            if letter == item["chosen"]:
                tag = (tag + " / your choice").strip() if tag else "  <-- your choice"
            print(f"  {letter}) {opt}{tag}")


def play_again():
    while True:
        raw = input("\nPlay again? (Y/N): ").strip().upper()
        if raw in ("Y", "N"):
            return raw == "Y"
        print("Please type Y or N.")


def main():
    print("Welcome to the Rio de Janeiro Multiple-Choice Quiz!")

    bank = rio_bank()

    while True:
        player = read_name()
        mode = choose_feedback_mode()
        instant = (mode == "A")

        count = read_how_many(len(bank))
        chosen_questions = pick_quiz_set(bank, count)

        score, wrong_log = run_session(chosen_questions, instant)
        show_summary(player, score, count)

        if not instant:
            want_review = input("Would you like to review incorrect answers? (Y/N): ").strip().upper()
            if want_review == "Y":
                review_mistakes(wrong_log)

        if not play_again():
            print("Thanks for playing — goodbye!")
            break


main()