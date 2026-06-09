from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Create translator object
translator = Translator()

# Function to translate text
def translate_text():
    try:
        translated = translator.translate(
            input_text.get("1.0", END),
            src=source_lang.get(),
            dest=target_lang.get()
        )
        output_text.delete("1.0", END)
        output_text.insert(END, translated.text)
    except Exception as e:
        output_text.delete("1.0", END)
        output_text.insert(END, f"Error: {e}")

# Main window
root = Tk()
root.title("Language Translation Tool")
root.geometry("700x500")

# Language lists
languages = list(LANGUAGES.keys())

# Source language
Label(root, text="Source Language").pack()
source_lang = ttk.Combobox(root, values=languages)
source_lang.set("en")
source_lang.pack()

# Target language
Label(root, text="Target Language").pack()
target_lang = ttk.Combobox(root, values=languages)
target_lang.set("hi")
target_lang.pack()

# Input text
Label(root, text="Enter Text").pack()
input_text = Text(root, height=8, width=70)
input_text.pack()

# Translate button
Button(root, text="Translate", command=translate_text).pack(pady=10)

# Output text
Label(root, text="Translated Text").pack()
output_text = Text(root, height=8, width=70)
output_text.pack()

root.mainloop()