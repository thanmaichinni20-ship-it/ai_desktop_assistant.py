from tkinter import Tk, LabelFrame, Label, Text, Entry, Button, END, CENTER, SOLID
from PIL import Image, ImageTk
import speech_to_text
import Action

# Theme colors
BG_COLOR = "#6F8FAF"
BUTTON_COLOR = "#356696"
WINDOW_WIDTH = 550
WINDOW_HEIGHT = 675

# Initialize root window
root = Tk()
root.title("AI Assistant")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.resizable(False, False)
root.config(bg=BG_COLOR)

# GUI widgets
text_display = None
ask_button = None
send_button = None
delete_button = None
entry_field = None


def ask():
    """Handle voice input and get bot response"""
    user_input = speech_to_text.speech_to_text()
    bot_response = Action.Action(user_input)
    
    text_display.insert(END, f'You: {user_input}\n')
    if bot_response:
        text_display.insert(END, f"Bot: {str(bot_response)}\n")
    text_display.insert(END, '-' * 40 + '\n')
    text_display.see(END)  # Auto-scroll to latest message
    if bot_response == "ok mam":
        root.destroy()


def send():
    """Handle send button - process text input"""
    user_input = entry_field.get().strip()
    if not user_input:
        return
    
    bot_response = Action.Action(user_input)
    
    text_display.insert(END, f'You: {user_input}\n')
    if bot_response:
        text_display.insert(END, f"Bot: {str(bot_response)}\n")
    text_display.insert(END, '-' * 40 + '\n')
    text_display.see(END)  # Auto-scroll to latest message
    
    entry_field.delete(0, END)  # Clear input field
    
    if bot_response == "ok mam":
        root.destroy()


def delete_text():
    """Handle delete button - clear text display"""
    text_display.delete(1.0, END)


def create_widgets():
    """Create and arrange all UI widgets"""
    global text_display, ask_button, send_button, delete_button, entry_field
    
    # Top frame
    frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
    frame.config(bg=BG_COLOR)
    frame.grid(row=0, column=1, padx=55, pady=10)
    
    # Title label
    title_label = Label(frame, text="AI Assistant", font=("comic sans ms", 14, "bold"), 
                       bg=BUTTON_COLOR, bd=0)
    title_label.grid(row=0, column=0, padx=20, pady=10)
    
    # Image label
    img = ImageTk.PhotoImage(Image.open("assistant.png"))
    image_label = Label(frame, image=img)
    image_label.image = img  # Keep a reference
    image_label.grid(row=1, column=0, pady=20)
    
    # Text display
    text_display = Text(root, font=('courier 10 bold'), bg=BUTTON_COLOR)
    text_display.place(x=100, y=375, width=375, height=100)
    
    # Entry field
    entry_field = Entry(root, justify=CENTER)
    entry_field.place(x=100, y=500, width=350, height=30)
    
    # Buttons
    ask_button = Button(root, text="Ask", bg=BUTTON_COLOR, pady=16, padx=40, 
                       borderwidth=3, relief=SOLID, command=ask)
    ask_button.place(x=70, y=575)
    
    send_button = Button(root, text="Send", bg=BUTTON_COLOR, pady=16, padx=40, 
                        borderwidth=3, relief=SOLID, command=send)
    send_button.place(x=400, y=575)
    
    delete_button = Button(root, text="Delete", bg=BUTTON_COLOR, pady=16, padx=40, 
                          borderwidth=3, relief=SOLID, command=delete_text)
    delete_button.place(x=225, y=575)


if __name__ == "__main__":
    create_widgets()
    root.mainloop()