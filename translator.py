import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

# 1. Main Application Window Setup
root = tk.Tk()
root.title("CodeAlpha - Language Translation Tool")
root.geometry("600x450")
root.config(bg="#f0f2f5")

translator = Translator()

# 2. Translation Function
def translate_text():
    input_text = text_entry.get("1.0", tk.END).strip()
    source_lang = src_lang_combo.get()
    target_lang = dest_lang_combo.get()
    
    if not input_text:
        messagebox.showwarning("Warning", "Please enter some text to translate!")
        return
        
    try:
        # Get language codes (e.g., 'English' -> 'en')
        src_code = [k for k, v in LANGUAGES.items() if v.title() == source_lang][0]
        dest_code = [k for k, v in LANGUAGES.items() if v.title() == target_lang][0]
        
        # Perform translation
        translated = translator.translate(input_text, src=src_code, dest=dest_code)
        
        # Display output
        output_entry.config(state=tk.NORMAL)
        output_entry.delete("1.0", tk.END)
        output_entry.insert(tk.END, translated.text)
        output_entry.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {str(e)}")

# 3. Copy to Clipboard Function (Optional Feature)
def copy_text():
    translated_text = output_entry.get("1.0", tk.END).strip()
    if translated_text:
        root.clipboard_clear()
        root.clipboard_append(translated_text)
        messagebox.showinfo("Success", "Text copied to clipboard!")

# --- UI Design ---
# Title Label
title_label = tk.Label(root, text="Language Translation Tool", font=("Arial", 16, "bold"), bg="#f0f2f5", fg="#333")
title_label.pack(pady=10)

# Language Options (Dropdowns List)
lang_list = [v.title() for v in LANGUAGES.values()]

frame_langs = tk.Frame(root, bg="#f0f2f5")
frame_langs.pack(pady=5)

tk.Label(frame_langs, text="From:", bg="#f0f2f5", font=("Arial", 10)).grid(row=0, column=0, padx=5)
src_lang_combo = ttk.Combobox(frame_langs, values=lang_list, width=20, state="readonly")
src_lang_combo.grid(row=0, column=1, padx=5)
src_lang_combo.set("English")

tk.Label(frame_langs, text="To:", bg="#f0f2f5", font=("Arial", 10)).grid(row=0, column=2, padx=5)
dest_lang_combo = ttk.Combobox(frame_langs, values=lang_list, width=20, state="readonly")
dest_lang_combo.grid(row=0, column=3, padx=5)
dest_lang_combo.set("Urdu")

# Input Text Area
tk.Label(root, text="Enter Text:", bg="#f0f2f5", font=("Arial", 10, "bold")).pack(anchor="w", padx=30, pady=(10,0))
text_entry = tk.Text(root, height=5, width=65, font=("Arial", 10))
text_entry.pack(padx=30, pady=5)

# Buttons (Translate & Copy)
frame_buttons = tk.Frame(root, bg="#f0f2f5")
frame_buttons.pack(pady=10)

btn_translate = tk.Button(frame_buttons, text="Translate", command=translate_text, bg="#007bff", fg="white", font=("Arial", 11, "bold"), padx=15, pady=5)
btn_translate.grid(row=0, column=0, padx=10)

btn_copy = tk.Button(frame_buttons, text="Copy Output", command=copy_text, bg="#28a745", fg="white", font=("Arial", 11), padx=10, pady=5)
btn_copy.grid(row=0, column=1, padx=10)

# Output Text Area
tk.Label(root, text="Translated Text:", bg="#f0f2f5", font=("Arial", 10, "bold")).pack(anchor="w", padx=30, pady=(10,0))
output_entry = tk.Text(root, height=5, width=65, font=("Arial", 10), state=tk.DISABLED, bg="#e9ecef")
output_entry.pack(padx=30, pady=5)

root.mainloop()
