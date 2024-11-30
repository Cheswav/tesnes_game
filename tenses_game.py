import tkinter as tk
from tkinter import ttk, messagebox

# Define questions based on grammar topics from Chapter 1: Review of Tenses
grammar_questions = {
    "Present Simple": [
        ("She ___ (like) ice cream.", "likes"),
        ("They ___ (not/work) on Sundays.", "don't work"),
    ],
    "Past Simple": [
        ("He ___ (go) to the park yesterday.", "went"),
        ("They ___ (not/see) the movie last week.", "didn't see"),
    ],
    "Future Simple": [
        ("I ___ (travel) to Paris next month.", "will travel"),
        ("She ___ (not/attend) the meeting tomorrow.", "won't attend"),
    ],
}

class GrammarTrainerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Grammar Trainer")
        self.score = 0
        self.current_tense = None
        self.current_question = None
        self.current_answer = None

        # Welcome screen
        self.welcome_label = tk.Label(root, text="Welcome to the Grammar Trainer!", font=("Arial", 16))
        self.welcome_label.pack(pady=20)

        self.start_button = ttk.Button(root, text="Start", command=self.choose_tense)
        self.start_button.pack(pady=10)

    def choose_tense(self):
        # Clear welcome screen
        self.welcome_label.pack_forget()
        self.start_button.pack_forget()

        # Tense selection screen
        self.tense_label = tk.Label(self.root, text="Choose a tense to practice:", font=("Arial", 14))
        self.tense_label.pack(pady=20)

        self.tense_var = tk.StringVar()
        self.tense_combobox = ttk.Combobox(self.root, textvariable=self.tense_var, state="readonly")
        self.tense_combobox['values'] = list(grammar_questions.keys())
        self.tense_combobox.pack(pady=10)

        self.next_button = ttk.Button(self.root, text="Next", command=self.start_practice)
        self.next_button.pack(pady=10)

    def start_practice(self):
        self.current_tense = self.tense_var.get()
        if not self.current_tense:
            messagebox.showwarning("No selection", "Please select a tense to continue.")
            return

        # Clear tense selection screen
        self.tense_label.pack_forget()
        self.tense_combobox.pack_forget()
        self.next_button.pack_forget()

        self.display_question()

    def display_question(self):
        if not grammar_questions[self.current_tense]:
            messagebox.showinfo("Complete", f"You've completed all questions for {self.current_tense}!\nYour score: {self.score}")
            self.root.destroy()
            return

        self.current_question, self.current_answer = grammar_questions[self.current_tense].pop(0)

        self.question_label = tk.Label(self.root, text=self.current_question, font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.answer_entry = ttk.Entry(self.root)
        self.answer_entry.pack(pady=10)
        self.answer_entry.bind("<Return>", self.check_answer)

    def check_answer(self, event=None):
        user_answer = self.answer_entry.get().strip()
        if user_answer.lower() == self.current_answer.lower():
            self.score += 1
            messagebox.showinfo("Correct", "Great job!")
        else:
            messagebox.showerror("Incorrect", f"The correct answer was: {self.current_answer}")

        self.answer_entry.pack_forget()
        self.question_label.pack_forget()

        self.display_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = GrammarTrainerApp(root)
    root.mainloop()
