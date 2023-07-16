from tkinter import *
from data import question_data
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg="#375362", pady=20, padx=20)

        self.score_label = Label(text=f"Score: 0", bg="#375362", font=("Arial", 20, "italic"), fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(bg="white", height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125, text="Some question text.", fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_image = PhotoImage(file="true.png")
        wrong_image = PhotoImage(file="false.png")

        self.right_button = Button(image=right_image, command=self.true_pressed)
        self.right_button.grid(row=2, column=0)

        self.left_button = Button(image=wrong_image, command=self.false_pressed)
        self.left_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()
    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached end of the quiz.")
            self.canvas.config(bg="white")
            self.right_button.config(state="disabled")
            self.left_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

