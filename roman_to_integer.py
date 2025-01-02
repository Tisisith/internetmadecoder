import tkinter as tk

def create_button(frame, text, command=None):
    button = tk.Button(frame, text=text, width=15, height=2, command=command)
    button.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
    return button

def display_reminder(reminder_text, grid_frame, button):
    for widget in grid_frame.winfo_children():
        widget.destroy()
    label = tk.Label(grid_frame, text=reminder_text, font=("Arial", 14), wraplength=300, justify="center")
    label.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    button.config(bg="red")  # Change button background to red to indicate it has been clicked

def main():
    # Create the main window
    root = tk.Tk()
    root.title("3x3 Grid Application")
    
    # Create a frame for the empty grid on the left
    left_frame = tk.Frame(root, width=300, height=400, bg="lightgray")
    left_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Create a frame to hold the grid of buttons on the right
    grid_frame = tk.Frame(root)
    grid_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Define button labels and their associated reminders
    buttons = [
        ("Report", "This is a reminder for Report."),
        ("Banking", "This is a reminder for Banking."),
        ("Emails", "This is a reminder for Emails."),
        ("Update", "This is a reminder for Update."),
        ("Text", "This is a reminder for Text."),
        ("Warranty+", "This is a reminder for Warranty+."),
        ("Recoveries", "This is a reminder for Recoveries."),
        ("PowerBI", "This is a reminder for PowerBI."),
        ("Notices", "This is a reminder for Notices.")
    ]

    # Add buttons to the grid and link them to display reminders
    button_objects = []
    for i, (label, reminder) in enumerate(buttons):
        row, col = divmod(i, 3)
        button = tk.Button(grid_frame, text=label, width=20, height=2)
        button.config(command=lambda b=button, r=reminder: display_reminder(r, left_frame, b))
        button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        button_objects.append(button)

    # Configure row and column weights for responsive resizing
    for i in range(3):
        grid_frame.rowconfigure(i, weight=1)
        grid_frame.columnconfigure(i, weight=1)

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()
