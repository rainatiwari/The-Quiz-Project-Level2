THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

SCORE = 0

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("QUIZLER!!!!")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Here is the question??",
                                                     font=("Ariel", 20, "italic"),
                                                     width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(text=f"Score: {SCORE}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Create [Unknown] Button
        cross_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=cross_image, highlightthickness=0, command=self.false_pressed)  # See next word. , command=next_card
        self.false_button.grid(row=2, column=0)

        # Create [Known] Button
        check_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=check_image, highlightthickness=0, command =self.true_pressed)  # Remove the known word from list. ,
        self.true_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.window.after(2000, self.get_next_question)