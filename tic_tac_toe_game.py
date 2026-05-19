import tkinter as tk
from tkinter import messagebox

# Function to check winner
def check_winner():
    global winner

    winning_combos = [
        [0,1,2], [3,4,5], [6,7,8],   # Rows
        [0,3,6], [1,4,7], [2,5,8],   # Columns
        [0,4,8], [2,4,6]             # Diagonals
    ]

    for combo in winning_combos:
        if (
            buttons[combo[0]]["text"] ==
            buttons[combo[1]]["text"] ==
            buttons[combo[2]]["text"] != ""
        ):
            # Highlight winning buttons
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")

            winner = True

            messagebox.showinfo(
                "Tic-Tac-Toe",
                f"Player {buttons[combo[0]]['text']} wins!"
            )

            return

    # Check draw
    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Tic-Tac-Toe", "It's a Draw!")
        winner = True


# Function when button is clicked
def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()

        if not winner:
            toggle_player()


# Switch player
def toggle_player():
    global current_player

    current_player = "O" if current_player == "X" else "X"

    label.config(text=f"Player {current_player}'s turn")


# Main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Variables
current_player = "X"
winner = False

# Create buttons
buttons = [
    tk.Button(
        root,
        text="",
        font=("Arial", 25),
        width=6,
        height=2,
        command=lambda i=i: button_click(i)
    )
    for i in range(9)
]

# Place buttons in grid
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

# Status label
label = tk.Label(
    root,
    text=f"Player {current_player}'s turn",
    font=("Arial", 16)
)

label.grid(row=3, column=0, columnspan=3)

# Run app
root.mainloop()