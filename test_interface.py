import tkinter as tk

def submit():
    user_input = entry.get()
    result_label.config(text=f"You entered: {user_input}")

# Create the main window
window = tk.Tk()
window.title("String Input Interface")

# Create an entry widget for user input
entry = tk.Entry(window)
entry.pack()

# Create a button to submit the input
submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack()

# Create a label to display the result
result_label = tk.Label(window, text="")
result_label.pack()

# Start the main event loop
window.mainloop()
