# Latin Study Quiz (Python + Raspberry Pi + Claude AI)

This project shows how to build your own Latin multiple choice study quiz using Python and a Raspberry Pi.  
All versions of the code inside this repo were generated using iterative prompts through Claude AI on a free plan.

[![Build a Latin Study Quiz with AI](play-Latin-study-ai-thumbnail.jpg)](https://youtu.be/d9G9p86aWAs)

## What This Project Does

This quiz tests Latin forms in a multiple choice format.  
As you progress through each version, you will see:

- clean GUI quiz interface
- score tracking over 5 questions
- context sentences instead of isolated forms
- explanations that mention cases and grammar usage
- English translations added to the feedback
- a 15-second countdown timer with color changes

This is a real example of “vibe coding” where you use AI to iterate your way into a better tool by giving targeted update prompts.

## Requirements

- Raspberry Pi (any recent version works)
- Python 3 installed
- Raspberry Pi OS Desktop
- Geany Programmer’s Editor (preinstalled on Raspberry Pi OS Desktop)
- Internet access to log in to Claude AI in your browser

## How to Run

1. Clone or download this repo to your Raspberry Pi  
2. Open the version you want to run in Geany (or your editor of choice)  
3. Save the file with a `.py` extension  
4. Click the paper plane run icon in Geany, or run it from a terminal using `python3 your_file_name.py`  

## Versions Inside This Repo

| Version File  | What Changed                                                                 |
|---------------|------------------------------------------------------------------------------|
| `v1`          | initial GUI quiz with 5 questions, score shown after the last question      |
| `v2`          | adds context sentences, explanations, and English translations in feedback  |
| `v3`          | adds a 15-second countdown timer with color changes and time-out handling   |

You can continue to build from any version.

---

## Ideas for Your Own Updates

This project is intended to be modified.  
Try these next:

- add more Latin forms (nouns, verbs, adjectives)
- change the tense or case focus (perfect, pluperfect, ablative, etc.)
- group questions by chapter from your Latin textbook
- randomize distractors based on other valid but incorrect forms
- switch the content to another language you are studying

---

## How the Code Was Generated

Every version came from a single starting prompt to Claude AI on a free account.

Then I asked for targeted upgrades over time:

- UI layout improvements
- scoring and feedback changes
- sentence context around each form
- English translations in the explanations
- countdown timer and time-out behavior

This shows how AI can be used to learn Python and Latin at the same time.

---

## 📚 Author

Created by **Caroline Dunn**  

- 🌐 <https://winningintech.com/>  
- 📺 <https://www.youtube.com/caroline>  
- 📘 *A Woman’s Guide to Winning in Tech*: <https://amzn.to/3YxHVO7>  

---

## License

MIT License — you can use, remix, and modify this code for your own study tools.

If you build your own version, please share it!
