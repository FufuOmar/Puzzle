from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
sentence0 = And(AKnight, AKnave)
knowledge0 = And(
    Not(And(AKnight, AKnave)),
    Or(AKnight, AKnave),
    Implication(AKnight, sentence0),
    Implication(AKnight, Not(sentence0))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
sentence1 = And(AKnave, BKnave)
knowledge1 = And(
    Not(And(BKnight, BKnave)),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),
    Or(AKnight, AKnave),
    Implication(AKnight, sentence1),
    Implication(AKnave, Not(sentence1)),
    Implication(sentence1, BKnave),
    Implication(Not(sentence1), BKnight)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
sentence2 = Or(And(AKnight, BKnight), And(AKnave, BKnave))
sentence3 = Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))
knowledge2 = And(
    Not(And(BKnight, BKnave)),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),
    Or(AKnight, AKnave),
    Implication(AKnight, sentence2),
    Implication(sentence2, BKnight),
    Implication(BKnight, sentence3),
    Implication(sentence3, AKnave)
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Not(And(BKnight, BKnave)),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),
    Or(AKnight, AKnave),
    Not(And(CKnight, CKnave)),
    Or(CKnight, CKnave),
    # A's statement (tautology, doesn't give direct constraints)
    Implication(AKnight, Or(AKnight, AKnave)),
    Implication(AKnave, Not(Or(AKnight, AKnave))),

    # B's statements
    Or(
        Implication(BKnight, Or(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave)))),
        Implication(BKnave, Not(Or(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave)))))
    ),

    # B says "C is a knave."
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),

    # C says "A is a knight."
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
