from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
            width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score = 0

        self.scoreboard = Label(text=f"Score: {self.score}", bg=THEME_COLOR, foreground="white")
        self.scoreboard.grid(row=0, column=1)

        self.true_image = PhotoImage(file="./images/true.png")
        self.false_image = PhotoImage(file="./images/false.png")

        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.check_if_true)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.check_if_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_the_answer(self, answer: bool):
        if self.quiz.check_answer(str(answer)):
            self.feedback(True)
            self.score += 1
            self.scoreboard.config(text=f"Score: {self.score}")
        else:
            self.feedback(False)

    def check_if_true(self):
        self.check_the_answer(True)

    def check_if_false(self):
        self.check_the_answer(False)

    def change_canvas_color(self, color):
        self.canvas.configure(bg=color)

    def feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
