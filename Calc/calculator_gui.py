import tkinter as tk
import random
from styles import get_color_schemes, get_font_style
from calc import add, sub, mult, div

# Fetch color schemes and font
colors = get_color_schemes()
fonts = get_font_style()

def draw_bevel(canvas):
    # Draw the bevel 
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    canvas.create_rectangle(
        5, 5, width - 5, height - 5,
        outline=colors['bevel_outer'], width=3, tags="bevel"
    )
    canvas.create_rectangle(
        8, 8, width - 8, height - 8,
        outline=colors['bevel_inner'], width=2, tags="bevel"
    )

def create_sparkles_and_texts():
    canvas.delete("sparkle")
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    
    if width <= 20 or height <= 20:
        return

    # Create sparkle
    for _ in range(30):
        x = random.randint(10, width - 10)
        y = random.randint(10, height - 10)
        size = random.randint(5, 15)
        color = random.choice(colors['sparkle_colors'])
        shape = random.choice(['oval', 'star'])
        
        if shape == 'oval':
            canvas.create_oval(
                x, y, x + size, y + size,
                fill=color, outline='', tags="sparkle"
            )
        else:
            points = [x, y, x + size, y + size // 2, x + size // 2, y + size, x, y + size // 2, x - size // 2, y + size]
            canvas.create_polygon(points, fill=color, outline='', tags="sparkle")

    # Create uwu text elements
    for _ in range(10):  # Number of text elements (adjusted for visibility)
        x = random.randint(10, width - 50)
        y = random.randint(10, height - 20)
        text_color = random.choice(colors['uwu_colors'])
        canvas.create_text(x, y, text="uwu", fill=text_color, font=("Arial", 16), tags="sparkle")

def animate_sparkles_and_texts():
    create_sparkles_and_texts()
    root.after(250, animate_sparkles_and_texts)  # Repeat every 0.25 seconds

def calculate():
    operation = operation_var.get()
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
    except ValueError:
        label_result.config(text="Invawid input! Pwease entew numbews.")
        return
    
    if operation == 'Add':
        result = add(num1, num2)
    elif operation == 'Subtract':
        result = sub(num1, num2)
    elif operation == 'Multiply':
        result = mult(num1, num2)
    elif operation == 'Divide':
        result = div(num1, num2)
    else:
        result = "Invalid operation!"
    
    label_result.config(text=f"Result: {result}")

# Setup GUI
root = tk.Tk()
root.title("Pink Cawcuwatow")

# Configure the main window
root.geometry("400x300")
root.configure(bg=colors['window_bg'])

# Create a canvas for sparkles and bevel effect
canvas = tk.Canvas(root, width=400, height=300, bg=colors['window_bg'], bd=0, highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

# Draw bevel effect
draw_bevel(canvas)

# Create and animate sparkles and text
root.after(100, animate_sparkles_and_texts)  # Start animation after a short delay

# Create a frame for widgets
frame = tk.Frame(root, bg=colors['frame_bg'])
frame.place(relx=0.5, rely=0.5, anchor='center')  # Center the frame

# Create and place widgets
operation_var = tk.StringVar(value='Add')

tk.Radiobutton(frame, text="Add", variable=operation_var, value='Add', bg=colors['button_bg'], fg=colors['text_fg'], font=fonts['font'], relief='raised').pack(pady=5)
tk.Radiobutton(frame, text="Subtwact", variable=operation_var, value='Subtract', bg=colors['button_bg'], fg=colors['text_fg'], font=fonts['font'], relief='raised').pack(pady=5)
tk.Radiobutton(frame, text="Muwtipwy", variable=operation_var, value='Multiply', bg=colors['button_bg'], fg=colors['text_fg'], font=fonts['font'], relief='raised').pack(pady=5)
tk.Radiobutton(frame, text="Dwivide", variable=operation_var, value='Divide', bg=colors['button_bg'], fg=colors['text_fg'], font=fonts['font'], relief='raised').pack(pady=5)

entry1 = tk.Entry(frame, font=fonts['font'], width=15)
entry1.pack(pady=5)

entry2 = tk.Entry(frame, font=fonts['font'], width=15)
entry2.pack(pady=5)

tk.Button(frame, text="Cawcuwate", command=calculate, bg=colors['button_bg'], fg=colors['text_fg'], font=fonts['font'], relief='raised').pack(pady=10)

label_result = tk.Label(frame, text="Wesult wiww be shown hewe", bg=colors['frame_bg'], fg=colors['text_fg'], font=fonts['font'])
label_result.pack(pady=5)

# Start the main loop
root.mainloop()
