correct = 0

questions = [{
    'tanong': "1. Who killed Michael Jackson? ",
    'answers': ['A: George Clooney', 'B: Michael Jackson'],
    'answer': 'B'
},
{
    'tanong': "2. Who is the greatest of all time? ",
    'answers': ['A: Nelson Espiritu', 'B: Lebron James'],
    'answer': 'A'
}
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(f"\n{question['tanong']}\n")
        for a in question['answers']:
            print(a)
        sagot = input('Anong sagot mo? ')
        if sagot.upper() == question['answer']:
            correct +=1
            print('Your answer is correct')
        else:
            print('Bobo ka')

run_quiz(questions)
