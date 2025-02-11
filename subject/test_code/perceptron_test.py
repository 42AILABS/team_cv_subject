def TEST_NAND(NAND):
    count = 4

    if (NAND(0, 0) != 1):
        print(f"(0, 0) is not 1 !!")
        count -= 1

    if (NAND(1, 0) != 1):
        print("(1, 0) is not 1 !!")
        count -= 1

    if (NAND(0, 1) != 1):
        print("(0, 1) is not 1 !!")
        count -= 1

    if (NAND(1, 1) != 0):
        print("(1, 1) is not 0 !!")
        count -= 1
    print(f'\nNAND GATE TOTAL SCORE : {count} / 4')
    print("="*30)

def TEST_OR(OR):
    count = 4

    if (OR(0, 0) != 0):
        print(f"(0, 0) is not 0 !!")
        count -= 1

    if (OR(1, 0) != 1):
        print("(1, 0) is not 1 !!")
        count -= 1

    if (OR(0, 1) != 1):
        print("(0, 1) is not 1 !!")
        count -= 1

    if (OR(1, 1) != 1):
        print("(1, 1) is not 1 !!")
        count -= 1
    print(f'\nOR GATE TOTAL SCORE : {count} / 4')
    print("="*30)

def TEST_OR(XOR):
    count = 4

    if (XOR(0, 0) != 0):
        print(f"(0, 0) is not 0 !!")
        count -= 1

    if (XOR(1, 0) != 1):
        print("(1, 0) is not 1 !!")
        count -= 1

    if (XOR(0, 1) != 1):
        print("(0, 1) is not 1 !!")
        count -= 1

    if (XOR(1, 1) != 0):
        print("(1, 1) is not 0 !!")
        count -= 1
    print(f'\nXOR GATE TOTAL SCORE : {count} / 4')
    print("="*30)


