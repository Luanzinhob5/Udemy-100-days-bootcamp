from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

def quiz_game():
    question_bank = []

    for question in question_data:
        question_text = question["text"]
        questions_answer = question["answer"]
        new_question = Question(q_text=question_text,q_answer=questions_answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()
    quiz.final()

quiz_game()






