import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Python Learning Environment",
    page_icon="🐍",
    layout="centered"
)

# App Title
st.title("🐍 Python Learning Environment")
st.write("Review the 10 core pillars of Python and test your understanding with the 10-question comprehensive quiz.")

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

# 2. Interactive 10-Question Quiz Section
st.subheader("🧠 10-Question Comprehensive Quiz")

quiz_data = [
    {
        "question": "1. What does the concept 'Everything in Python is an object' imply?",
        "options": ["Only instances of custom classes are objects.", "Data types, functions, and modules are treated as objects with identity and type.", "Python does not support primitive operations.", "Variables are raw pointers to hardware addresses."],
        "correct_idx": 1
    },
    {
        "question": "2. What standard file extension is used to save executable Python source code scripts?",
        "options": [".pt", ".pycode", ".py", ".pyp"],
        "correct_idx": 2
    },
    {
        "question": "3. How does Python distinctly handle structural blocks like loops or function definitions?",
        "options": ["Using curly braces {}", "Using consistent indentation / whitespace", "Using explicit 'end' statement keywords", "Using semicolons ;"],
        "correct_idx": 1
    },
    {
        "question": "4. Which system handles memory allocation and lifecycle cleanups automatically in Python?",
        "options": ["Manual calloc pointers", "The garbage collector & reference counting", "Operating system kernel interrupts", "Destructor calls using the 'free' keyword"],
        "correct_idx": 1
    },
    {
        "question": "5. Which keyword is exclusively used to initialize a new function block in Python?",
        "options": ["func", "function", "def", "lambda_start"],
        "correct_idx": 2
    },
    {
        "question": "6. What kind of value behavior happens when assigning a dynamic value to a raw Python variable?",
        "options": ["You must declare structural types beforehand.", "Python strictly checks memory sizes statically.", "Python infers the type automatically at runtime.", "Variables cannot shift assignments to alternative types."],
        "correct_idx": 2
    },
    {
        "question": "7. Which of these is a core cornerstone principle of Object-Oriented Programming (OOP) supported in Python?",
        "options": ["Inheritance", "Pointers", "Manual Compilation", "Linear Structuring"],
        "correct_idx": 0
    },
    {
        "question": "8. Which looping block structure is ideally used when iterating through an explicit sequence of items?",
        "options": ["while loop", "for loop", "do-while loop", "repeat-until loop"],
        "correct_idx": 1
    },
    {
        "question": "9. Which built-in Python collection sequence structure is completely immutable?",
        "options": ["List", "Dictionary", "Tuple", "Set"],
        "correct_idx": 2
    },
    {
        "question": "10. Which aspect best highlights a key architectural feature of Python?",
        "options": ["High language syntax complexity", "Simple human-readable syntax and cross-platform portability", "Absence of external standard libraries", "Hardware-dependent execution constraints"],
        "correct_idx": 1
    }
]

# Track score dynamically
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
    st.write("") 

# Submit logic
if st.button("Submit Complete Quiz", type="primary"):
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
        st.warning("Please answer all 10 questions before submitting!")
    else:
        # Results metrics Display
        if correct_count == len(quiz_data):
            st.success(f"🎉 Perfect Score! You got {correct_count} out of 10 correct!")
        elif correct_count >= 7:
            st.info(f"👍 Good work! You got {correct_count} out of 10 correct.")
        else:
            st.error(f"📚 Score: {correct_count}/10. Keep studying the core keypoints listed above!")
