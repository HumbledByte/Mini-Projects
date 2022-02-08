from Question import Question

question_prompts = [
    "What color is the sky?\n(a) Blue\n(b) Red\n(c) Green\n\n",
    "What color is an apple?\n(a) Blue\n(b) Green\n(c) Red\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct!")

run_test(questions)