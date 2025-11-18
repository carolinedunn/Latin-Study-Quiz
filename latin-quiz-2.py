import tkinter as tk
from tkinter import font
import random

class LatinQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Latin Forms Quiz")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        # Quiz data - now with context sentences and explanations
        self.all_questions = [
            {
                "question": "Complete the sentence: 'Video _____' (I see the girl)",
                "context": "Video _____ in foro.",
                "options": ["puellam", "puellae", "puella", "puellas"],
                "answer": "puellam",
                "explanation": "The correct answer is 'puellam' (accusative singular). In Latin, direct objects take the accusative case. 'Puella' (girl) becomes 'puellam' when it's the object being seen.",
                "translation": "I see the girl in the forum."
            },
            {
                "question": "Complete the sentence: 'Ego _____ Romam' (I love Rome)",
                "context": "Ego _____ Romam multum.",
                "options": ["amas", "amo", "amat", "amamus"],
                "answer": "amo",
                "explanation": "The correct answer is 'amo' (1st person singular present). 'Ego' means 'I', so we need the first person singular form of 'amare' (to love).",
                "translation": "I love Rome very much."
            },
            {
                "question": "Complete the sentence: 'Liber _____' (The book of the girls)",
                "context": "Liber _____ est magnus.",
                "options": ["mensarum", "puellarum", "puellas", "puellae"],
                "answer": "puellarum",
                "explanation": "The correct answer is 'puellarum' (genitive plural). The genitive case shows possession or 'of'. 'Puellarum' means 'of the girls'.",
                "translation": "The book of the girls is large."
            },
            {
                "question": "Complete the sentence: 'Pueri _____' (The boys love)",
                "context": "Pueri _____ ludos.",
                "options": ["amant", "amat", "amamus", "amatis"],
                "answer": "amant",
                "explanation": "The correct answer is 'amant' (3rd person plural present). 'Pueri' (boys) is plural, so we need the third person plural form of 'amare' (to love).",
                "translation": "The boys love games."
            },
            {
                "question": "Complete the sentence: 'Do librum _____' (I give a book to the girls)",
                "context": "Do librum _____.",
                "options": ["puellis", "puellas", "puellarum", "puellae"],
                "answer": "puellis",
                "explanation": "The correct answer is 'puellis' (dative plural). The dative case is used for indirect objects - to whom or for whom something is given.",
                "translation": "I give a book to the girls."
            },
            {
                "question": "Complete the sentence: 'Servus _____ laborat' (The slave of the master works)",
                "context": "Servus _____ diu laborat.",
                "options": ["domino", "domini", "dominum", "dominus"],
                "answer": "domini",
                "explanation": "The correct answer is 'domini' (genitive singular). The genitive case shows possession. 'Domini' means 'of the master'.",
                "translation": "The slave of the master works for a long time."
            },
            {
                "question": "Complete the sentence: 'Tu _____ multos amicos' (You have many friends)",
                "context": "Tu _____ multos amicos bonos.",
                "options": ["habes", "habet", "habeo", "habent"],
                "answer": "habes",
                "explanation": "The correct answer is 'habes' (2nd person singular present). 'Tu' means 'you', so we need the second person singular form of 'habere' (to have).",
                "translation": "You have many good friends."
            },
            {
                "question": "Complete the sentence: 'Cum _____ ambulo' (I walk with the king)",
                "context": "Cum _____ in via ambulo.",
                "options": ["rege", "regis", "regem", "rex"],
                "answer": "rege",
                "explanation": "The correct answer is 'rege' (ablative singular). The preposition 'cum' (with) requires the ablative case.",
                "translation": "I walk in the street with the king."
            },
            {
                "question": "Complete the sentence: '_____ sunt magna' (The temples are large)",
                "context": "_____ Romae sunt magna.",
                "options": ["templa", "templi", "templum", "templos"],
                "answer": "templa",
                "explanation": "The correct answer is 'templa' (nominative plural). 'Templum' is a neuter noun, and neuter plural nominative endings are '-a'. The subject of 'sunt' (are) takes the nominative case.",
                "translation": "The temples of Rome are large."
            },
            {
                "question": "Complete the sentence: 'Nos _____ Romani' (We are Romans)",
                "context": "Nos _____ Romani fortes.",
                "options": ["sumus", "sunt", "sum", "estis"],
                "answer": "sumus",
                "explanation": "The correct answer is 'sumus' (1st person plural present). 'Nos' means 'we', so we need the first person plural form of 'esse' (to be).",
                "translation": "We are strong Romans."
            }
        ]
        
        self.score = 0
        self.current_question = 0
        self.questions = []
        
        # Setup fonts
        self.title_font = font.Font(family="Arial", size=24, weight="bold")
        self.question_font = font.Font(family="Arial", size=18)
        self.button_font = font.Font(family="Arial", size=16)
        self.context_font = font.Font(family="Arial", size=16, slant="italic")
        
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
        
        info = tk.Label(self.root, text="Test your knowledge of Latin forms in context!\n\n5 Questions", 
                       font=self.question_font, bg="#f0f0f0", fg="#34495e")
        info.pack(pady=30)
        
        start_btn = tk.Button(self.root, text="Start Quiz", 
                             font=self.button_font, bg="#27ae60", fg="white",
                             command=self.show_question, width=20, height=2,
                             relief=tk.RAISED, bd=3, cursor="hand2")
        start_btn.pack(pady=20)
    
    def show_question(self):
        """Display current question with context"""
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
        question_label.pack(pady=20)
        
        # Context sentence
        context_text = self.questions[self.current_question]["context"]
        context_label = tk.Label(self.root, text=context_text, 
                                font=self.context_font, bg="#f0f0f0", 
                                fg="#7f8c8d", wraplength=700)
        context_label.pack(pady=10)
        
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
            btn.pack(pady=8)
    
    def check_answer(self, selected_option):
        """Check if the selected answer is correct and show explanation"""
        correct_answer = self.questions[self.current_question]["answer"]
        
        if selected_option == correct_answer:
            self.score += 1
            self.show_explanation(True, selected_option)
        else:
            self.show_explanation(False, selected_option)
    
    def show_explanation(self, is_correct, selected_option):
        """Show detailed explanation with translation"""
        self.clear_screen()
        
        # Result indicator
        if is_correct:
            result_text = "✓ Correct!"
            result_color = "#27ae60"
        else:
            result_text = "✗ Incorrect"
            result_color = "#e74c3c"
            
        result_label = tk.Label(self.root, text=result_text, 
                               font=("Arial", 28, "bold"), bg="#f0f0f0", 
                               fg=result_color)
        result_label.pack(pady=20)
        
        # Show what they selected if wrong
        if not is_correct:
            selected_label = tk.Label(self.root, 
                                     text=f"You selected: {selected_option}", 
                                     font=("Arial", 14), bg="#f0f0f0", 
                                     fg="#7f8c8d")
            selected_label.pack(pady=5)
        
        # Explanation
        explanation = self.questions[self.current_question]["explanation"]
        exp_label = tk.Label(self.root, text=explanation, 
                            font=("Arial", 15), bg="#f0f0f0", 
                            fg="#2c3e50", wraplength=700, justify="left")
        exp_label.pack(pady=20, padx=40)
        
        # Translation header
        trans_header = tk.Label(self.root, text="English Translation:", 
                               font=("Arial", 14, "bold"), bg="#f0f0f0", 
                               fg="#16a085")
        trans_header.pack(pady=(20, 5))
        
        # Translation
        translation = self.questions[self.current_question]["translation"]
        trans_label = tk.Label(self.root, text=f'"{translation}"', 
                              font=self.context_font, bg="#f0f0f0", 
                              fg="#16a085", wraplength=700)
        trans_label.pack(pady=5)
        
        # Continue button
        continue_btn = tk.Button(self.root, text="Continue →", 
                               font=self.button_font, bg="#3498db", fg="white",
                               command=self.next_question, width=20, height=2,
                               relief=tk.RAISED, bd=3, cursor="hand2")
        continue_btn.pack(pady=30)
    
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
