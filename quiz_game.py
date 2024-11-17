history_questions = [{
    "question": "\n1. Who killed Abel? ",
    "answers": ['\nA. Cain', 'B. Jacob', 'C. Satan', 'D. None of the above'],
    "answer": 'A'},
{
    "question": "\n2. Who parted the sea? ",
    "answers": ['\nA. Joseph', 'B. Michael', 'C. Jesus', 'D. Moses'],
    "answer": 'D'
}]

greatest_questions = [{
    "question": "\n1. Who is the greatest of all time? ",
    "answers": ['\nA. Nelson', 'B. Jasper', 'C. Ben', 'D. None of the above'],
    "answer": 'A'},
{
    "question": "\n2. Who invented the moonwalk? ",
    "answers": ['\nA. Michael Jackson', 'B. Michael Jordan', 'C. Michael Doughlas', 'D. Michael Keaton'],
    "answer": 'A'
}]

def run_quiz(questions):
    score = 0
    correct_answers = []
    wrong_answers = []
    for question in questions:
        print(question['question'])
        for x in question['answers']:
            print(x)
        a = input('\nWhat is your answer? ')
        if a.upper() == question['answer']:
            score += 1
            correct_answers.append(question['question'])
            print('You are correct.')
        else:
            print("You're incorrect.\n")
            wrong_answers.append((question['question'], question['answer']))
    print(f"\nYour final score was {score}\n")
    print('Answers you got right:')
    for x in correct_answers:
        print(f'{x}\n')
    print("Questions you got wrong:")
    for question, correct_answer in wrong_answers:
        print(f'{question} (Correct answer: {correct_answer})\n')

category = input('What category would you like to be asked: history or greatest? ')
if category == 'history':
    run_quiz(history_questions)
elif category == 'greatest':
    run_quiz(greatest_questions)
