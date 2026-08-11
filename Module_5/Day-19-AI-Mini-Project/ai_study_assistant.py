# AI Study Assistant
# Codomax Digital Solutions Internship - Day 19
# Free Local Version - No API Required

print("=" * 50)
print("           AI STUDY ASSISTANT")
print("=" * 50)

knowledge_base = {
    "machine learning": {
        "keywords": ["machine learning", "ml"],
        "answer": (
            "Machine Learning is a branch of Artificial Intelligence "
            "that enables computers to learn patterns from data and "
            "make predictions or decisions without being explicitly "
            "programmed for every task."
        )
    },

    "supervised learning": {
        "keywords": ["supervised learning", "supervised"],
        "answer": (
            "Supervised Learning is a type of Machine Learning in which "
            "a model learns from labeled data. The model uses input data "
            "and known output values to learn patterns and make predictions. "
            "Examples include spam detection, house price prediction, "
            "and image classification."
        )
    },

    "python": {
        "keywords": ["python", "programming"],
        "answer": (
            "Python is a high-level programming language known for its "
            "simple syntax and readability. It is widely used in web "
            "development, data analysis, Artificial Intelligence, "
            "Machine Learning, and cybersecurity."
        )
    },

    "cybersecurity": {
        "keywords": ["cybersecurity", "cyber security", "security"],
        "answer": (
            "Cybersecurity is the practice of protecting computers, "
            "networks, applications, and data from unauthorized access, "
            "attacks, and other security threats."
        )
    },

    "phishing": {
        "keywords": ["phishing", "phishing attack"],
        "answer": (
            "Phishing is a social engineering technique in which an "
            "attacker attempts to trick users into revealing sensitive "
            "information such as passwords or financial details. "
            "Phishing commonly uses fraudulent emails, messages, or websites."
        )
    },

    "pandas": {
        "keywords": ["pandas"],
        "answer": (
            "Pandas is a Python library used for data manipulation and "
            "analysis. It provides useful data structures such as "
            "Series and DataFrame for working with structured datasets."
        )
    },

    "numpy": {
        "keywords": ["numpy"],
        "answer": (
            "NumPy is a Python library used for numerical computing. "
            "It provides arrays and mathematical functions that are "
            "useful for scientific computing and data analysis."
        )
    }
}


def find_answer(question):
    question = question.lower()

    for topic, data in knowledge_base.items():
        for keyword in data["keywords"]:
            if keyword in question:
                return topic, data["answer"]

    return None, None


while True:
    print("\n" + "-" * 50)

    topic = input("Enter topic: ").strip()

    if topic.lower() == "exit":
        print("\nThank you for using AI Study Assistant.")
        break

    question = input("Enter your question: ").strip()

    if question.lower() == "exit":
        print("\nThank you for using AI Study Assistant.")
        break

    topic_found, answer = find_answer(topic + " " + question)

    print("\nAI Study Assistant Response:")
    print("-" * 50)

    if answer:
        print(answer)
    else:
        print(
            "Sorry, I could not find a matching topic in my local "
            "knowledge base."
        )
        print(
            "Try asking about Python, Machine Learning, "
            "Supervised Learning, Pandas, NumPy, Cybersecurity, "
            "or Phishing."
        )

    print("-" * 50)