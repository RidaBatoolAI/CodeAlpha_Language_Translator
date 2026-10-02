import tkinter as tk
from tkinter import messagebox
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Dataset: FAQs (Questions and Answers)
faq_data = {
    "what is artificial intelligence?": "Artificial Intelligence (AI) is the simulation of human intelligence processes by machines, especially computer systems.",
    "what is machine learning?": "Machine Learning is a subset of AI that provides systems the ability to automatically learn and improve from experience without being explicitly programmed.",
    "how many tasks are required for this internship?": "According to CodeAlpha guidelines, you need to complete a minimum of 2 or 3 tasks to get your internship certificate.",
    "when is the submission deadline?": "The final submission deadline for this batch is October 15, 2026.",
    "hi hello hey": "Hello! I am your AI FAQ Assistant. How can I help you today?",
    "what is codealpha?": "CodeAlpha is an online platform providing internship opportunities to students to enhance their technical and practical skills."
}

questions = list(faq_data.keys())

# 2. Chatbot Logic Function
def get_bot_response():
    user_query = user_entry.get().strip().lower()
    
    if not user_query:
        return
        
    # Append user message to chat area
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, "You: " + user_entry.get() + "\n")
    
    # Process text matching using Cosine Similarity
    vectorizer = TfidfVectorizer()
    all_texts = questions + [user_query]
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    
    # Compare user query with all FAQ questions
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])[0]
    best_match_idx = similarity_scores.argmax()
    
    # If match score is decent, give answer, otherwise default response
    if similarity_scores[best_match_idx] > 0.3:
        bot_reply = faq_data[questions[best_match_idx]]
    else:
        bot_reply = "I'm sorry, I couldn't find a direct answer to that. Please ask about AI, Internships, or Deadlines!"
        
    # Append bot reply to chat area
    chat_area.insert(tk.END, "Bot: " + bot_reply + "\n\n")
    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END)
    
    # Clear input field
    user_entry.delete(0, tk.END)

# 3. Main GUI Window Setup
root = tk.Tk()
root.title("CodeAlpha - FAQ Chatbot")
root.geometry("450x500")
root.config(bg="#f4f6f9")

# Header Title
title_label = tk.Label(root, text="AI FAQ Chatbot", font=("Arial", 14, "bold"), bg="#007bff", fg="white", pady=10)
title_label.pack(fill=tk.X)

# Chat Display Area
chat_area = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED, font=("Arial", 10), bg="white", bd=2)
chat_area.pack(padx=15, pady=15, fill=tk.BOTH, expand=True)

# User Input Frame
input_frame = tk.Frame(root, bg="#f4f6f9")
input_frame.pack(fill=tk.X, padx=15, pady=(0, 15))

user_entry = tk.Entry(input_frame, font=("Arial", 11), bd=2)
user_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=4)
user_entry.bind("<Return>", lambda event: get_bot_response())

send_button = tk.Button(input_frame, text="Send", command=get_bot_response, bg="#28a745", fg="white", font=("Arial", 10, "bold"), padx=10)
send_button.pack(side=tk.RIGHT, padx=(5, 0))

# Pre-populate greeting message
chat_area.config(state=tk.NORMAL)
chat_area.insert(tk.END, "Bot: Hello! Ask me anything about your internship or AI.\n\n")
chat_area.config(state=tk.DISABLED)

root.mainloop()
