import tkinter as tk
from tkinter import messagebox

class StackVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador Gráfico de una Pila (Stack)")
        self.root.geometry("500x600")
        self.root.config(bg="#f4f6f9")

        self.stack = []
        self.max_size = 8  

        title_label = tk.Label(root, text="Visualizador de Pila (LIFO)", font=("Arial", 16, "bold"), bg="#f4f6f9", fg="#333")
        title_label.pack(pady=10)

        control_frame = tk.Frame(root, bg="#f4f6f9")
        control_frame.pack(pady=10)

        tk.Label(control_frame, text="Valor:", font=("Arial", 11), bg="#f4f6f9").grid(row=0, column=0, padx=5)
        
        self.entry_val = tk.Entry(control_frame, font=("Arial", 11), width=10)
        self.entry_val.grid(row=0, column=1, padx=5)
        self.entry_val.bind("<Return>", lambda event: self.push()) 

        btn_push = tk.Button(control_frame, text="Push", command=self.push, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), width=8)
        btn_push.grid(row=0, column=2, padx=5)

        btn_pop = tk.Button(control_frame, text="Pop", command=self.pop, bg="#f44336", fg="white", font=("Arial", 10, "bold"), width=8)
        btn_pop.grid(row=0, column=3, padx=5)

        btn_peek = tk.Button(control_frame, text="Peek", command=self.peek, bg="#ff9800", fg="white", font=("Arial", 10, "bold"), width=8)
        btn_peek.grid(row=0, column=4, padx=5)

        self.canvas_width = 300
        self.canvas_height = 420
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="white", highlightthickness=1, highlightbackground="#ccc")
        self.canvas.pack(pady=10)

        self.status_label = tk.Label(root, text="Pila vacía. Capacidad: 0/8", font=("Arial", 11, "italic"), bg="#f4f6f9", fg="#555")
        self.status_label.pack(pady=5)

        self.draw_stack()

    def push(self):
        val = self.entry_val.get().strip()
        if not val:
            messagebox.showwarning("Advertencia", "Por favor ingresa un valor válido.")
            return
        if len(self.stack) >= self.max_size:
            messagebox.showerror("Error", "¡Desbordamiento de pila (Overflow)! Capacidad máxima alcanzada.")
            return
        
        self.stack.append(val)
        self.entry_val.delete(0, tk.END)
        self.draw_stack()
        self.update_status(f"Elemento '{val}' agregado (Push).")

    def pop(self):
        if not self.stack:
            messagebox.showerror("Error", "¡Subdesbordamiento de pila (Underflow)! La pila está vacía.")
            return
        
        val = self.stack.pop()
        self.draw_stack()
        self.update_status(f"Elemento '{val}' eliminado (Pop).")

    def peek(self):
        if not self.stack:
            messagebox.showinfo("Peek", "La pila está vacía.")
            return
        val = self.stack[-1]
        messagebox.showinfo("Peek", f"El elemento actual en el tope es: {val}")

    def update_status(self, action_msg):
        if self.stack:
            tope = self.stack[-1]
            self.status_label.config(text=f"{action_msg} | Total: {len(self.stack)}/{self.max_size} | Tope: {tope}")
        else:
            self.status_label.config(text=f"{action_msg} | Pila vacía.")

    def draw_stack(self):
        self.canvas.delete("all")
        
        box_width = 160
        box_height = 40
        start_x = (self.canvas_width - box_width) / 2
        start_y = self.canvas_height - 35 - box_height

        for i, val in enumerate(self.stack):
            y1 = start_y - (i * (box_height + 5))
            y2 = y1 + box_height
            x1 = start_x
            x2 = start_x + box_width

           
            if i == len(self.stack) - 1:
                color = "#4CAF50"  
            else:
                color = "#2196F3"  

            self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="#1976D2", width=2)
            self.canvas.create_text(x1 + box_width/2, y1 + box_height/2, text=str(val), font=("Arial", 12, "bold"), fill="white")
            
            if i == len(self.stack) - 1:
                self.canvas.create_text(x2 + 35, y1 + box_height/2, text="<-- Tope", font=("Arial", 10, "bold"), fill="#d32f2f")

        base_y = start_y + box_height + 5
        self.canvas.create_line(start_x - 15, base_y, start_x + box_width + 15, base_y, fill="#333", width=4)

root = tk.Tk()
app = StackVisualizer(root)
root.mainloop() 