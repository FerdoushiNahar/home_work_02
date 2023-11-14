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

def function_C(m1, m2, o): # changed the variable 
    p = f"{m1} {o} {m2}"
    if o == '+': 
        a = m1 + m2    # modified the sign
    elif o == '-': 
        a = m1 - m2
    else: 
        a = m1 * m2
    return p, a
def math_quiz():
    s = 0
    t_q = 3 #corrected float into integer
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
            s += 1 # moddified the inrement variable
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")
    print(f"\nGame over! Your score is: {s}/{t_q}")
if __name__ == "__main__":
    math_quiz()
import unittest
from math_quiz import function_A, function_B, function_C


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # TODO
        pass

    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                ''' TODO add more test cases here '''
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                pass

if __name__ == "__main__":
    unittest.main()
