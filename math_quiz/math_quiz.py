import random
    """
     code_cleanup branch
    """

def function_A(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)

def function_B():
    return random.choice(['+', '-', '*'])

def function_C(m1, m2, o):
    p = f"{m1} {o} {m2}"
    if o == '+': 
        a = m1 + m2
    elif o == '-': 
        a = m1 - m2
    else: 
        a = m1 * m2
    return p, a

def math_quiz():
    s = 0
    t_q = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        m1 = function_A(1, 10)
        m2 = function_A(1, 5)
        o = function_B()

        PROBLEM,ANSWER = function_C(m1, m2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()

