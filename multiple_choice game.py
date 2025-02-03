class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "WHich organization hosts UCL? \n(a) UEFA\n(b) FIFA\n(c) CAF\n\n",
    "Which team has the most UCL trophies? \n(a) Chelsea\n(b) Bayern Munich \n(c) Real Madrid\n\n",
    "Who holds the record for the most goals in football? \n(a) Pele\n(b) Messi\n(c) Cristiano Ronaldo\n\n",
    "Which player has the most trophies in football history? \n(a) Modric\n(b) Iniesta\n(c) Messi\n\n",
    "Who is the GOAT in football? \n(a) George Best\n(b) Cristiano Ronaldo\n(c) Lionel Messi\n\n",
    "Which player has the most ballon d'ors?\n(a) Lionel Messi\n(b) Cristiano Ronaldo\n(c) Ronaldinho Gaucho\n\n",
    "Most golden boots in Europe belongs to?\n(a) Ibrahimovic\n(b) Cristiano Ronaldo\n(c) Lionel Messi\n\n",
    "Which country has the most World Cups? \n(a) England\n(b) Germany\n(c) Brazil\n\n",
    "Which player is known as El Pistolero? \n(a) Luis Saurez\n(b) Robert Lewandoski\n(c) Cristiano Ronaldo\n\n",
    "What's the name of FC Bayern Munich's home staduim? \n(a) Camp Nou\n(b) Anfield\n(c) Allians Arena\n\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "c"),
    Question(question_prompts[3], "c"),
    Question(question_prompts[4], "b"),
    Question(question_prompts[5], "a"),
    Question(question_prompts[6], "c"),
    Question(question_prompts[7], "c"),
    Question(question_prompts[8], "a"),
    Question(question_prompts[9], "c"),
]

def run_test(questions):
    scores = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer:
            scores += 1
    return scores

final_score = run_test(questions)
print("Congratulations!!")
print("You got " + str(final_score) + "/" + str(len(questions)) + " correct")
