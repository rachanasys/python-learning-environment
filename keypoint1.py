import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Python Learning Environment",
    page_icon="🐍",
    layout="centered"
)

# App Title and Description
st.title("🐍 Python Learning Environment")
st.write("Explore these 10 foundational pillars of Python programming.")

# Complete dictionary of your 10 keypoints
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

# Displaying keypoints interactively
for title, description in keypoints.items():
    with st.expander(title, expanded=False):
        st.write(description)

# Footer
st.markdown("---")
st.caption("Congratulations on setting up your 10 Python Core Keypoints!")
