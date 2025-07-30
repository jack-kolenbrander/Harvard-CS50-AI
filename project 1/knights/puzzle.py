from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # TODO
    # Define that each is either a Knight or a Knave
    And(Or(AKnight,AKnave),Not(And(AKnight,AKnave))),
    #define puzzle logic, if its a Knight then statement is true, if Knave then statement is false
    Implication(AKnight,And(AKnight,AKnave)),
    Implication(AKnave,Not(And(AKnight,AKnave))),
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # TODO
    # Define that each is either a Knight or a Knave
    And(Or(AKnight,AKnave),Not(And(AKnight,AKnave))),
    And(Or(BKnight,BKnave),Not(And(BKnight,BKnave))),
    #A says we are both knaves
    Implication(AKnight,And(AKnave,BKnave)),
    Implication(AKnave,Not(And(AKnave,BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # TODO
    # Define that each is either a Knight or a Knave
    And(Or(AKnight,AKnave),Not(And(AKnight,AKnave))),
    And(Or(BKnight,BKnave),Not(And(BKnight,BKnave))),
    # Define A, either both knights or both knaves
    Implication(AKnight,Or(And(AKnight,BKnight),And(AKnave,BKnave))),
    Implication(AKnave,Not(Or(And(AKnight,BKnight),And(AKnave,BKnave)))),
    #Define B, that they are not the same
    Implication(BKnight,Or(And(AKnight,BKnave),And(AKnave,BKnight))),
    Implication(BKnave,Not(Or(And(AKnight,BKnave),And(AKnave,BKnight)))),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
    # Define that each is either a Knight or a Knave
    And(Or(AKnight,AKnave),Not(And(AKnight,AKnave))),
    And(Or(BKnight,BKnave),Not(And(BKnight,BKnave))),
    And(Or(CKnight,CKnave),Not(And(CKnight,CKnave))),
    #A's statement is unknown so no knowledge required to add
    #Define B's Statements - A said I am a knave
    Implication(BKnight,Implication(AKnight,AKnave)),
    Implication(BKnight,Implication(AKnave,AKnight)),
    #Implication(BKnave,Not(Implication(AKnight,AKnave))),
    #C is a knave
    Implication(BKnight,CKnave),
    Implication(BKnave,CKnight),
    #Define C's statement - A is a knight
    Implication(CKnight,AKnight),
    Implication(CKnave,AKnave),
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
