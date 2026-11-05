
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

questions = [
    {
        'question': '1. What is Python?',
        'options': ['Programming Language', 'Browser', 'Database', 'Operating System'],
        'answer': 'Programming Language'
    },
    {
        'question': '2. Who developed Python?',
        'options': ['Google', 'Guido van Rossum', 'Microsoft', 'Apple'],
        'answer': 'Guido van Rossum'
    },
    {
        'question': '3. Which symbol is used for comments in Python?',
        'options': ['//', '#', '/*', '@'],
        'answer': '#'
    },
    {
        'question': '4. Which function displays output?',
        'options': ['input()', 'print()', 'show()', 'display()'],
        'answer': 'print()'
    },
    {
        'question': '5. Which data type stores True or False?',
        'options': ['String', 'Integer', 'Boolean', 'List'],
        'answer': 'Boolean'
    }
]


@login_required
def quiz_home(request):

    if request.method == 'POST':
        score = 0

        for i, q in enumerate(questions):
            selected = request.POST.get(f'q{i}')

            if selected == q['answer']:
                score += 1

        if score >= 4:
            message = "Excellent! You passed the quiz."
        elif score >= 2:
            message = "Good try! Keep practising."
        else:
            message = "Keep learning and try again!"

        return render(request, 'result.html', {
            'score': score,
            'total': len(questions),
            'message': message
        })

    return render(request, 'quiz.html', {
        'questions': questions
    })
