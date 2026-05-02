# 🧠 CALCULUS STUDY BOT v1.0
# Designed to test knowledge of core differentiation rules.

def run_quiz():
    questions = [
        {
            "question": "What is the Power Rule for d/dx of x^n?",
            "options": "A) nx^(n-1) | B) x^(n+1) | C) nx^n",
            "answer": "A"
        },
        {
            "question": "What is the Product Rule for (uv)?",
            "options": "A) u'v' | B) u'v + uv' | C) u'v - uv'",
            "answer": "B"
        },
        {
            "question": "What rule is used for a function inside another function: f(g(x))?",
            "options": "A) Quotient Rule | B) Power Rule | C) Chain Rule",
            "answer": "C"
        }
    ]

    score = 0
    print("✨ WELCOME TO THE CALCULUS STRENGTH TEST ✨")
    print("------------------------------------------")

    for i, q in enumerate(questions):
        print(f"\nQuestion {i+1}: {q['question']}")
        print(f"Options: {q['options']}")
        choice = input("Your Answer (A, B, or C): ").upper()

        if choice == q['answer']:
            print("✅ Correct! Keep it up.")
            score += 1
        else:
            print(f"❌ Not quite. The correct answer was {q['answer']}.")

    print("\n" + "="*30)
    print(f"QUIZ COMPLETE! Your Score: {score}/{len(questions)}")
    
    if score == 3:
        print("🏆 Calculus Master! You're ready for the final.")
    else:
        print("📖 Good effort! Review the Study Vault for a refresher.")
    print("="*30)

if __name__ == "__main__":
    run_quiz()
