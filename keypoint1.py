import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Python Learning Environment",
    page_icon="🐍",
    layout="centered"
)

# App Title and Description
st.title("🐍 Python Learning Environment")
st.write("Explore the 10 foundational pillars of Python and test your knowledge with the interactive quiz below.")

# 1. 10 Core Keypoints Dictionary
keypoints = {
    "1. Everything in Python is an Object": 
        "Functions, strings, integers, and even modules are objects. Each object has a unique ID, a type, and a value.",
    
    "2. Save Code in .py File": 
        "Python scripts are saved with a `.py` extension and can be executed via terminal/command prompt using `python filename.py`.",
    
    "3. Use Indentation to Define Code Blocks": 
        "Unlike other languages that use curly braces `{}`, Python relies on consistent whitespace (standard is 4 spaces) to define scopes like loops, functions, and conditionals.",
    
    "4. Dynamically Typed & Automatic Memory Management": 
        "You do not need to declare variable types explicitly; Python infers them at runtime. Memory allocation and deallocation (Garbage Collection) are handled automatically.",
    
    "5. Keywords & Functions": 
        "Keywords are reserved words (like `if`, `def`, `return`) that cannot be used as variable names. Functions are reusable blocks of code defined using `def`.",
    
    "6. Data Types & Variables": 
        "Variables act as containers for storing data values. Built-in core data types include integers (`int`), floats (`float`), strings (`str`), booleans (`bool`), and collections (`list`, `dict`, `tuple`).",
    
    "7. OOPs (Object-Oriented Programming)": 
        "Python fully supports OOP principles like Classes, Objects, Inheritance, Polymorphism, Encapsulation, and Abstraction to structure software robustly.",
        
    "8. Control Flow & Loops": 
        "Control execution paths using conditional statements (`if`, `elif`, `else`) and automate repetitive tasks using loops (`for` and `while`).",
        
    "9. Collections": 
        "Utilize built-in sequence structures to manage grouped data efficiently: mutable indexed sequences (`lists`), immutable sequences (`tuples`), unique items (`sets`), and key-value mapping (`dictionaries`).",
        
    "10. Features of Python": 
        "Python is highly popular due to its simple readability, vast standard library, open-source nature, cross-platform portability, and extensibility for data science, web development, and AI."
}

# Render Keypoints Section
st.subheader("💡 Core Learning Keypoints")
for title, description in keypoints.items():
    with st.expander(title, expanded=False):
        st.write(description)

st.markdown("---")

# 2. Interactive Quiz Section
st.subheader("🧠 Knowledge Check Quiz")

# Question definitions (Question text, options array, index of the correct option)
quiz_data = [
    {
        "question": "1. What does the statement 'Everything in Python is an object' mean?",
        "options": ["Only functions are objects.", "Data types, functions, and modules are treated as objects with properties.", "Python doesn't support primitive configurations.", "You must instantiate classes for every basic variable."],
        "correct_idx": 1
    },
    {
        "question": "2. How does Python define code blocks and scopes?",
        "options": ["Using curly braces {}", "Using semicolons ;", "Using consistent indentation / whitespace", "Using BEGIN and END tags"],
        "correct_idx": 2
    },
    {
        "question": "3. Which of the following is true about Python's variables?",
        "options": ["Variables must have types explicitly declared (e.g., int x).", "Python is dynamically typed; types are inferred at runtime.", "Python requires manual memory deallocation.", "Variable values cannot change once assigned."],
        "correct_idx": 1
    },
    {
        "question": "4. Which of these collection types is immutable?",
        "options": ["List", "Dictionary", "Set", "Tuple"],
        "correct_idx": 3
    }
]

# Track score dynamically
score = 0
user_answers = []

# Display each question using a radio component
for i, item in enumerate(quiz_data):
    user_choice = st.radio(
        label=item["question"],
        options=item["options"],
        index=None,  # Unselected by default
        key=f"q_{i}"
    )
    user_answers.append(user_choice)
    st.write("") # Margin spacing

# Submit logic
if st.button("Submit Quiz Answers", type="primary"):
    all_answered = True
    correct_count = 0
    
    # Process choices
    for i, item in enumerate(quiz_data):
        if user_answers[i] is None:
            all_answered = False
            break
        if user_answers[i] == item["options"][item["correct_idx"]]:
            correct_count += 1
            
    if not all_answered:
        st.warning("Please answer all questions before submitting!")
    else:
        # Results metrics Display
        if correct_count == len(quiz_data):
            st.success(f"🎉 Perfect Score! You got {correct_count} out of {len(quiz_data)} correct.")
        elif correct_count >= len(quiz_data) / 2:
            st.info(f"👍 Good effort! You got {correct_count} out of {len(quiz_data)} correct.")
        else:
            st.error(f"📚 Keep studying! You got {correct_count} out of {len(quiz_data)} correct. Review the keypoints above.")

# Footer
st.markdown("---")
st.caption("Python Learning Environment | Built with Streamlit")
