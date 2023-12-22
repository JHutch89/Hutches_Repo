# calculator_app.py

import streamlit as st
import math

def main():
    st.title("JH89 Calculator")

    num1 = st.number_input("Enter first number:")

    operation = st.radio("Select operation:", (
        "Add", "Subtract", "Multiply", "Divide",
        "Square Root", "Power", "Logarithm", "Trigonometry"
    ))

    # Checking if operation require two inputs
    requires_second_number = operation not in ["Square Root", "Logarithm"]

    # Display the second number input conditionally
    if requires_second_number:
        num2 = st.number_input("Enter second number:")

    result = 0

    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Cannot divide by zero!")
    elif operation == "Square Root":
        result = math.sqrt(num1)
    elif operation == "Power":
        result = num1 ** num2
    elif operation == "Logarithm":
        result = math.log(num1, num2) if num1 > 0 and num2 > 0 else "Invalid input for logarithm"
    elif operation == "Trigonometry":
        angle = st.number_input("Enter angle in degrees:")
        if st.checkbox("Use radians instead of degrees"):
            angle = math.radians(angle)

        trig_function = st.radio("Select trigonometric function:", ("Sine", "Cosine", "Tangent"))

        if trig_function == "Sine":
            result = math.sin(angle)
        elif trig_function == "Cosine":
            result = math.cos(angle)
        elif trig_function == "Tangent":
            result = math.tan(angle)

    st.success(f"Result: {result}")

    # Display bullet points
    st.write("Additional Information:")
    st.write("- Bullet Point 1")
    st.write("- Bullet Point 2")
    st.write("- Bullet Point 3")

if __name__ == "__main__":
    main()
