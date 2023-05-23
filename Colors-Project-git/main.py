import pyautogui
import tkinter as tk
from pynput import mouse

def get_pixel_color_hex():
    x, y = pyautogui.position()
    pixel_color = pyautogui.pixel(x, y)
    hex_color = '#{:02x}{:02x}{:02x}'.format(pixel_color[0], pixel_color[1], pixel_color[2])
    return hex_color

def update_color_label():
    if not color_locked:
        color_hex = get_pixel_color_hex()
        color_entry.delete(0, tk.END)
        color_entry.insert(0, color_hex)
        color_preview.config(bg=color_hex)

        r = int(color_hex[1:3], 16)
        g = int(color_hex[3:5], 16)
        b = int(color_hex[5:7], 16)
        r_entry.delete(0, tk.END)
        r_entry.insert(0, str(r))
        g_entry.delete(0, tk.END)
        g_entry.insert(0, str(g))
        b_entry.delete(0, tk.END)
        b_entry.insert(0, str(b))
        rgb_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        rgb_preview.config(bg=rgb_color)

    color_entry.after(100, update_color_label)

def on_mouse_press(x, y, button, pressed):
    global color_locked
    if button == mouse.Button.left and pressed:
        color_locked = True
        lock_label.config(text="Colore bloccato")

def on_color_entry_change(event):
    color_hex = color_entry.get()

    # Verifica se il valore inserito è un valore esadecimale valido
    if len(color_hex) == 7 and color_hex[0] == '#':
        try:
            r = int(color_hex[1:3], 16)
            g = int(color_hex[3:5], 16)
            b = int(color_hex[5:7], 16)

            r_entry.delete(0, tk.END)
            r_entry.insert(0, str(r))
            g_entry.delete(0, tk.END)
            g_entry.insert(0, str(g))
            b_entry.delete(0, tk.END)
            b_entry.insert(0, str(b))

            color_preview.config(bg=color_hex)
            rgb_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
            rgb_preview.config(bg=rgb_color)

        except ValueError:
            # Il valore esadecimale non è valido
            pass

    else:
        # Il valore inserito non è un valore esadecimale valido
        pass

def on_rgb_entry_change(event):
    try:
        r = int(r_entry.get())
        g = int(g_entry.get())
        b = int(b_entry.get())

        color_hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        color_entry.delete(0, tk.END)
        color_entry.insert(0, color_hex)
        color_preview.config(bg=color_hex)

        rgb_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        rgb_preview.config(bg=rgb_color)

    except ValueError:
        # Il valore RGB inserito non è valido
        pass

def toggle_color_lock():
    global color_locked
    color_locked = not color_locked
    if color_locked:
        lock_label.config(text="Colore bloccato")
    else:
        lock_label.config(text="")

# Creazione della GUI
window = tk.Tk()
window.title("Punto Colore")
window.geometry("400x300")

color_locked = False

color_entry = tk.Entry(window, font=("Arial", 12))
color_entry.pack(pady=5)
color_entry.bind('<KeyRelease>', on_color_entry_change)

# Aggiunta della preview del colore
color_preview = tk.Label(window, width=10, height=2, bg="#000000")
color_preview.pack(pady=5)

# Aggiunta dei valori RGB modificabili
r_label = tk.Label(window, text="R:", font=("Arial", 12))
r_label.pack()
r_entry = tk.Entry(window, font=("Arial", 12))
r_entry.pack()
r_entry.bind('<KeyRelease>', on_rgb_entry_change)

g_label = tk.Label(window, text="G:", font=("Arial", 12))
g_label.pack()
g_entry = tk.Entry(window, font=("Arial", 12))
g_entry.pack()
g_entry.bind('<KeyRelease>', on_rgb_entry_change)

b_label = tk.Label(window, text="B:", font=("Arial", 12))
b_label.pack()
b_entry = tk.Entry(window, font=("Arial", 12))
b_entry.pack()
b_entry.bind('<KeyRelease>', on_rgb_entry_change)

# Aggiunta della preview dei valori RGB
rgb_preview = tk.Label(window, width=10, height=2, bg="#000000")
rgb_preview.pack(pady=5)

unlock_button = tk.Button(window, text="Sblocca colore", font=("Arial", 12), command=toggle_color_lock)
unlock_button.pack(pady=10)

lock_label = tk.Label(window, text="", font=("Arial", 12))
lock_label.pack(pady=5)

update_color_label()

# Avvio dell'ascoltatore del mouse
mouse_listener = mouse.Listener(on_click=on_mouse_press)
mouse_listener.start()

window.mainloop()
