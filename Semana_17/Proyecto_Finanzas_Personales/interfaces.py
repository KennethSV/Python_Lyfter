
import tkinter as tk
from tkinter import ttk, messagebox
from typing import List
from logica import GestorFinanzas

CABECERAS = ("Fecha", "Tipo", "Título", "Monto", "Categoría")

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Finanzas")
        self.geometry("800x420")
        self.minsize(700, 380)

        self.gestor = GestorFinanzas()

        # --- Tabla ---
        self.tree = ttk.Treeview(self, columns=CABECERAS, show="headings")
        for col in CABECERAS:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120 if col != "Título" else 200, anchor=tk.W)
        yscroll = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=yscroll.set)

        # --- Botones ---
        btn_frame = ttk.Frame(self)
        b_cat = ttk.Button(btn_frame, text="Agregar categoría", command=self._abrir_cat)
        b_gas = ttk.Button(btn_frame, text="Agregar gasto", command=lambda: self._abrir_mov("gasto"))
        b_ing = ttk.Button(btn_frame, text="Agregar ingreso", command=lambda: self._abrir_mov("ingreso"))
        b_cat.grid(row=0, column=0, padx=4, pady=6)
        b_gas.grid(row=0, column=1, padx=4, pady=6)
        b_ing.grid(row=0, column=2, padx=4, pady=6)

        # --- Balance ---
        bal_frame = ttk.Frame(self)
        ttk.Label(bal_frame, text="Balance:").pack(side=tk.LEFT)
        self.lbl_balance = ttk.Label(bal_frame, text="₡ 0.00")
        self.lbl_balance.pack(side=tk.LEFT, padx=(6,0))

        # Layout
        self.tree.grid(row=0, column=0, sticky="nsew")
        yscroll.grid(row=0, column=1, sticky="ns")
        btn_frame.grid(row=1, column=0, sticky="w")
        bal_frame.grid(row=1, column=0, sticky="e", padx=8)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._refrescar()

    # --- Ventanas ---
    def _abrir_cat(self):
        win = tk.Toplevel(self)
        win.title("Agregar categoría")
        win.transient(self)
        win.grab_set()

        ttk.Label(win, text="Nombre de la categoría:").grid(row=0, column=0, padx=8, pady=(8,2), sticky="w")
        entrada = ttk.Entry(win, width=30)
        entrada.grid(row=1, column=0, padx=8, pady=2, sticky="w")
        entrada.focus()

        def guardar():
            nombre = entrada.get().strip()
            try:
                self.gestor.agregar_categoria(nombre)
            except Exception as e:
                messagebox.showerror("Error", str(e), parent=win)
                return
            win.destroy()
            self._refrescar()

        ttk.Button(win, text="Guardar", command=guardar).grid(row=2, column=0, padx=8, pady=8, sticky="w")
        ttk.Button(win, text="Cancelar", command=win.destroy).grid(row=2, column=0, padx=8, pady=8, sticky="e")

    def _abrir_mov(self, tipo: str):
        categorias = self.gestor.listar_categorias()
        if not categorias:
            messagebox.showerror("Sin categorías", "No hay categorías disponibles. Agregue una primero.", parent=self)
            return

        win = tk.Toplevel(self)
        win.title(f"Agregar {tipo}")
        win.transient(self)
        win.grab_set()

        ttk.Label(win, text="Título:").grid(row=0, column=0, padx=8, pady=(8,2), sticky="w")
        e_titulo = ttk.Entry(win, width=35)
        e_titulo.grid(row=1, column=0, padx=8, pady=2, sticky="w")

        ttk.Label(win, text="Monto:").grid(row=2, column=0, padx=8, pady=(8,2), sticky="w")
        e_monto = ttk.Entry(win, width=15)
        e_monto.grid(row=3, column=0, padx=8, pady=2, sticky="w")

        ttk.Label(win, text="Categoría:").grid(row=4, column=0, padx=8, pady=(8,2), sticky="w")
        c_categoria = ttk.Combobox(win, values=categorias, state="readonly", width=20)
        c_categoria.grid(row=5, column=0, padx=8, pady=2, sticky="w")
        if categorias:
            c_categoria.current(0)

        def guardar():
            titulo = e_titulo.get().strip()
            monto_str = e_monto.get().strip()
            categoria = c_categoria.get().strip()
            try:
                if tipo == "gasto":
                    self.gestor.agregar_gasto(titulo, monto_str, categoria)
                else:
                    self.gestor.agregar_ingreso(titulo, monto_str, categoria)
            except Exception as e:
                messagebox.showerror("Error", str(e), parent=win)
                return
            win.destroy()
            self._refrescar()

        btns = ttk.Frame(win)
        ttk.Button(btns, text="Guardar", command=guardar).pack(side=tk.LEFT, padx=6, pady=8)
        ttk.Button(btns, text="Cancelar", command=win.destroy).pack(side=tk.LEFT, padx=6, pady=8)
        btns.grid(row=6, column=0, sticky="w")

        e_titulo.focus()

    # --- Refresco de vista ---
    def _refrescar(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for m in self.gestor.listar_movimientos():
            self.tree.insert("", tk.END, values=(m["fecha"], m["tipo"].title(), m["titulo"], f"{float(m['monto']):.2f}", m["categoria"]))

        bal = self.gestor.balance()
        self.lbl_balance.config(text=f"₡ {bal:.2f}")

def mostrar_ventana_principal():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    mostrar_ventana_principal()
