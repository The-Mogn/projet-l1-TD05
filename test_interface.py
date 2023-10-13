import tkinter as tk
from traitementdetexte import sentence_in_common, text, rewrite_text, get_text

def submit():
    user_input1 = entry1.get()
    user_input2 = entry2.get()
    is_common = sentence_in_common(user_input1, user_input2)
    if is_common == True :
        result_label.config(text=f"There is a sentence in common")
    else :
        result_label.config(text=f"There is no sentence in common")    

def treat_text() :
    user_input = entry_path.get()
    
    my_text = text(get_text(user_input))
    rewrite_text(user_input, my_text.treat_text())
    result_treat_label.config(text="Treated text !")

# Create the main window
window = tk.Tk()
window.geometry("800x600")
window.title("String Input Interface")

label = tk.Label(window, text="Compare 2 sentences : ")
label.grid(row=0, column=1)

label1 = tk.Label(window, text="Enter sentence 1 : ")
label1.grid(row=1, column=0)

label2 = tk.Label(window, text="Enter sentence 2 : ")
label2.grid(row=2, column=0)

# Create an entry widget for user input
entry1 = tk.Entry(window)
entry1.grid(row=1, column=1)


entry2 = tk.Entry(window)
entry2.grid(row=2, column=1)

# Create a button to submit the input
submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.grid(row=3, column=1)

# Create a label to display the result
result_label = tk.Label(window, text="")
result_label.grid(row=4, column=1)



main_label2 = tk.Label(window, text="Treat your text in txt file")
main_label2.grid(row=6, column=1)

label_path = tk.Label(window, text="Enter the name of your file")
label_path.grid(row=7, column=0)

entry_path = tk.Entry(window)
entry_path.grid(row=7, column=1)

treat_button = tk.Button(window, text="Treat", command=treat_text)
treat_button.grid(row=8, column=1)

result_treat_label = tk.Label(window, text="")
result_treat_label.grid(row=9, column=1)


# Start the main event loop
window.mainloop()
