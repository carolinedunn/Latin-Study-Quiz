import tkinter as tk
from tkinter import font
import random

class LatinQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Latin Forms Quiz")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        # Quiz data - easily add more questions here
        self.all_questions = [
            {
                "question": "What is the accusative singular of 'puella' (girl)?",
                "options": ["puellam", "puellae", "puella", "puellas"],
                "answer": "puellam"
            },
            {
                "question": "Conjugate 'amare' (to love) in 1st person singular present:",
                "options": ["amas", "amo", "amat", "amamus"],
                "answer": "amo"
            },
            {
                "question": "What is the genitive plural of 'mensa' (table)?",
                "options": ["mensas", "mensarum", "mensis", "mensae"],
                "answer": "mensarum"
            },
            {
                "question": "Conjugate 'amare' in 3rd person plural present:",
                "options": ["amant", "amat", "amamus", "amatis"],
                "answer": "amant"
            },
            {
                "question": "What case is 'puellis'?",
                "options": ["Dative/Ablative plural", "Nominative plural", "Genitive plural", "Accusative singular"],
                "answer": "Dative/Ablative plural"
            },
            {
                "question": "What is the dative singular of 'dominus' (master)?",
                "options": ["domino", "domini", "dominum", "dominus"],
                "answer": "domino"
            },
            {
                "question": "Conjugate 'habere' (to have) in 2nd person singular present:",
                "options": ["habes", "habet", "habeo", "habent"],
                "answer": "habes"
            },
            {
                "question": "What is the ablative singular of 'rex' (king)?",
                "options": ["rege", "regis", "regem", "rex"],
                "answer": "rege"
            },
            {
                "question": "What is the nominative plural of 'templum' (temple)?",
                "options": ["templa", "templi", "templum", "templos"],
                "answer": "templa"
            },
            {
                "question": "Conjugate 'esse' (to be) in 1st person plural present:",
                "options": ["sumus", "sunt", "sum", "estis"],
                "answer": "sumus"
            }
        ]
        
        self.score = 0
        self.current_question = 0
        self.questions = []
        
        # Setup fonts
        self.title_font = font.Font(family="Arial", size=24, weight="bold")
        self.question_font = font.Font(family="Arial", size=18)
        self.button_font = font.Font(family="Arial", size=16)
        
        self.setup_quiz()
    
    def setup_quiz(self):
        """Initialize a new quiz with 5 random questions"""
        self.score = 0
        self.current_question = 0
        # Select 5 random questions
        self.questions = random.sample(self.all_questions, min(5, len(self.all_questions)))
        self.show_start_screen()
    
    def show_start_screen(self):
        """Display the start screen"""
        self.clear_screen()
        
        title = tk.Label(self.root, text="Latin Forms Quiz", 
                        font=self.title_font, bg="#f0f0f0", fg="#2c3e50")
        title.pack(pady=50)
        
        info = tk.Label(self.root, text="Test your knowledge of Latin forms!\n\n5 Questions", 
                       font=self.question_font, bg="#f0f0f0", fg="#34495e")
        info.pack(pady=30)
        
        start_btn = tk.Button(self.root, text="Start Quiz", 
                             font=self.button_font, bg="#27ae60", fg="white",
                             command=self.show_question, width=20, height=2,
                             relief=tk.RAISED, bd=3, cursor="hand2")
        start_btn.pack(pady=20)
    
    def show_question(self):
        """Display current question"""
        self.clear_screen()
        
        # Progress indicator
        progress = tk.Label(self.root, 
                          text=f"Question {self.current_question + 1} of 5 | Score: {self.score}",
                          font=("Arial", 14), bg="#f0f0f0", fg="#7f8c8d")
        progress.pack(pady=10)
        
        # Question text
        question_text = self.questions[self.current_question]["question"]
        question_label = tk.Label(self.root, text=question_text, 
                                 font=self.question_font, bg="#f0f0f0", 
                                 fg="#2c3e50", wraplength=700)
        question_label.pack(pady=40)
        
        # Randomize options
        options = self.questions[self.current_question]["options"].copy()
        random.shuffle(options)
        
        # Create answer buttons
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=20)
        
        for i, option in enumerate(options):
            btn = tk.Button(button_frame, text=option, 
                          font=self.button_font, bg="#3498db", fg="white",
                          command=lambda opt=option: self.check_answer(opt),
                          width=30, height=2, relief=tk.RAISED, bd=3,
                          cursor="hand2")
            btn.pack(pady=10)
    
    def check_answer(self, selected_option):
        """Check if the selected answer is correct"""
        correct_answer = self.questions[self.current_question]["answer"]
        
        if selected_option == correct_answer:
            self.score += 1
            self.show_feedback("Correct! ✓", "#27ae60")
        else:
            self.show_feedback(f"Incorrect. The answer was: {correct_answer}", "#e74c3c")
    
    def show_feedback(self, message, color):
        """Show feedback and move to next question"""
        self.clear_screen()
        
        feedback_label = tk.Label(self.root, text=message, 
                                 font=self.question_font, bg="#f0f0f0", 
                                 fg=color, wraplength=700)
        feedback_label.pack(pady=100)
        
        # Wait 2 seconds then show next question or results
        self.root.after(2000, self.next_question)
    
    def next_question(self):
        """Move to next question or show results"""
        self.current_question += 1
        
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.show_results()
    
    def show_results(self):
        """Display final results"""
        self.clear_screen()
        
        title = tk.Label(self.root, text="Quiz Complete!", 
                        font=self.title_font, bg="#f0f0f0", fg="#2c3e50")
        title.pack(pady=50)
        
        score_text = f"Your Score: {self.score} out of 5"
        percentage = (self.score / 5) * 100
        
        score_label = tk.Label(self.root, text=score_text, 
                              font=("Arial", 22), bg="#f0f0f0", fg="#34495e")
        score_label.pack(pady=20)
        
        percent_label = tk.Label(self.root, text=f"{percentage:.0f}%", 
                                font=("Arial", 20), bg="#f0f0f0", fg="#7f8c8d")
        percent_label.pack(pady=10)
        
        # Motivational message
        if percentage >= 80:
            message = "Excellent work! Optime!"
        elif percentage >= 60:
            message = "Good job! Keep practicing!"
        else:
            message = "Keep studying! Practice makes perfect!"
        
        msg_label = tk.Label(self.root, text=message, 
                           font=self.question_font, bg="#f0f0f0", fg="#16a085")
        msg_label.pack(pady=20)
        
        # Retry button
        retry_btn = tk.Button(self.root, text="Try Again", 
                            font=self.button_font, bg="#3498db", fg="white",
                            command=self.setup_quiz, width=20, height=2,
                            relief=tk.RAISED, bd=3, cursor="hand2")
        retry_btn.pack(pady=20)
        
        # Exit button
        exit_btn = tk.Button(self.root, text="Exit", 
                           font=self.button_font, bg="#95a5a6", fg="white",
                           command=self.root.quit, width=20, height=2,
                           relief=tk.RAISED, bd=3, cursor="hand2")
        exit_btn.pack(pady=10)
    
    def clear_screen(self):
        """Remove all widgets from screen"""
        for widget in self.root.winfo_children():
            widget.destroy()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = LatinQuizApp(root)
    root.mainloop()
