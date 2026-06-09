from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

questions = [
    "What is AI?",
    "What is Python?",
    "What is Machine Learning?"
]

answers = [
    "AI is Artificial Intelligence.",
    "Python is a programming language.",
    "Machine Learning allows computers to learn from data."
]

vectorizer = TfidfVectorizer()

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    vectors = vectorizer.fit_transform(questions + [user])

    similarity = cosine_similarity(vectors[-1], vectors[:-1])

    index = similarity.argmax()

    print("Bot:", answers[index])