import tkinter as tk

def evaluate_expression():
    """Evaluate the expression and display the result"""
    expression = entry.get()
    try:
        result = eval(expression)
        output.config(text="Result: " + str(result))
    except Exception as e:
        output.config(text="Error: " + str(e))

# Create the main window
window = tk.Tk()
window.title("Expression Calculator")

# Create an input entry field
entry = tk.Entry(window, width=30)
entry.pack()

# Create a button to evaluate the expression
evaluate_button = tk.Button(window, text="Evaluate", command=evaluate_expression)
evaluate_button.pack()

# Create a label to display the result or error message
output = tk.Label(window, text="")
output.pack()

# Start the main event loop
window.mainloop()
