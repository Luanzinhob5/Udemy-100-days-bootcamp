import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterFace:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.true()
        self.false()
        self.score()
        self.text_image()
        self.get_next_question()
        self.window.mainloop()

    def true(self):
        self.true_img = tk.PhotoImage(file="/Users/berga/Documents/Programação atual/CursoUdemy/day34/quizzler_app/images/true.png")
        self.true_button = tk.Button(image=self.true_img, command=self.true_pressed,highlightthickness=0)
        self.true_button.grid(row=2,column=0)
    
    def false(self):
        self.false_img = tk.PhotoImage(file="/Users/berga/Documents/Programação atual/CursoUdemy/day34/quizzler_app/images/false.png")
        self.false_button = tk.Button(image=self.false_img, command=self.false_pressed,highlightthickness=0)
        self.false_button.grid(row=2,column=1)

    def score(self):
        self.score_label = tk.Label(text="Score: 0", bg=THEME_COLOR,fg="white", pady=20, padx=20, highlightthickness=0)
        self.score_label.grid(row=0,column=1)

    def text_image(self):
        self.canvas = tk.Canvas(width=300,height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="SOme QUestio text", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(row=1,column=0,columnspan=2,padx=20,pady=20)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

