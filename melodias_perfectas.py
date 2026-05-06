"""
Curso Estructura de Datos 301305
Autor:Cristian Gabriel Moreno Rodriguez
Descripción: Aplicación de escritorio desarrollada en Python con interfaz
gráfica (Tkinter) para la academia de música "Melodías Perfectas"..
"""
import tkinter as tk
from tkinter import messagebox
from datetime import date


# ============================================================
# CLASE PÚBLICA: GestionParticipantes (abstracción)
# ============================================================
class GestionParticipantes:
    """Clase pública para almacenar y gestionar los datos del participante."""

    def __init__(self):
        self.identificacion = ""
        self.nombre_completo = ""
        self.genero = ""
        self.tecnica_artistica = ""
        self.costo_por_clase = 0
        self.numero_clases = 0
        self.fecha_registro = ""

    def calcular_costo_total(self, numero_clases: int, costo_por_clase: int) -> int:
        """Calcula el costo total del taller según el número de clases y el costo por clase."""
        return numero_clases * costo_por_clase


# ============================================================
# PRECIOS POR TÉCNICA ARTÍSTICA
# ============================================================
PRECIOS = {
    "Dibujo": 70000,
    "Pintura": 85000,
    "Escritura": 100000,
    "Fotografía": 90000,
    "Grabado": 75000,
}


# ============================================================
# VENTANA DE LOGIN
# ============================================================
class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.resizable(False, False)
        self.root.geometry("380x220")
        self.root.configure(bg="#f0f4f8")
        self._center_window(380, 220)
        self._build_ui()

    def _center_window(self, w, h):
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        x = (screen_w - w) // 2
        y = (screen_h - h) // 2
        self.root.geometry(f"{w}x{h}+{x}+{y}")

    def _build_ui(self): 
        frame = tk.Frame(self.root, bg="#f0f4f8", padx=20, pady=20)
        frame.pack(expand=True)

        tk.Label(frame, text="🎵 Gestión de Participantes",
                 font=("Arial", 13, "bold"), bg="#f0f4f8", fg="#1a3c5e").pack(pady=(0, 4))
        tk.Label(frame, text="Autor: Cristian Gabriel Moreno",
                 font=("Arial", 10), bg="#f0f4f8", fg="#555").pack(pady=(0, 14))

        tk.Label(frame, text="Contraseña:", font=("Arial", 11), bg="#f0f4f8").pack()
        self.password_entry = tk.Entry(frame, show="*", font=("Arial", 11),
                                       width=22, relief="solid", bd=1)
        self.password_entry.pack(pady=6)
        self.password_entry.bind("<Return>", lambda e: self._ingresar())

        tk.Button(frame, text="  Ingresar  ", command=self._ingresar,
                  font=("Arial", 11, "bold"), bg="#1a3c5e", fg="white",
                  relief="flat", cursor="hand2", padx=10, pady=4).pack(pady=8)

    def _ingresar(self):
        if self.password_entry.get() == "3971":
            self.root.withdraw()
            reg_win = tk.Toplevel(self.root)
            RegistroWindow(reg_win, self.root)
        else:
            messagebox.showerror("Acceso denegado", "Contraseña incorrecta. Intente de nuevo.")
            self.password_entry.delete(0, tk.END)


# ============================================================
# VENTANA DE REGISTRO
# ============================================================
class RegistroWindow:
    def __init__(self, root, login_root):
        self.root = root
        self.login_root = login_root
        self.participante = GestionParticipantes()
        self.root.title("Registro de Participante")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f4f8")
        self._center_window(460, 430)
        self._build_ui()
        self.root.protocol("WM_DELETE_WINDOW", self._salir)

    def _center_window(self, w, h):
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        x = (screen_w - w) // 2
        y = (screen_h - h) // 2
        self.root.geometry(f"{w}x{h}+{x}+{y}")

    def _build_ui(self):
        header = tk.Frame(self.root, bg="#1a3c5e", pady=10)
        header.pack(fill="x")
        tk.Label(header, text="🎵 Registro de Participante",
                 font=("Arial", 13, "bold"), bg="#1a3c5e", fg="white").pack()

        form = tk.Frame(self.root, bg="#f0f4f8", padx=28, pady=16)
        form.pack(fill="both", expand=True)

        def field(label_text, row):
            tk.Label(form, text=label_text, font=("Arial", 10, "bold"),
                     bg="#f0f4f8", anchor="w", width=20).grid(row=row, column=0, sticky="w", pady=5)

        # Identificación
        field("Identificación:", 0)
        self.id_entry = tk.Entry(form, font=("Arial", 10), width=28, relief="solid", bd=1)
        self.id_entry.grid(row=0, column=1, sticky="w", pady=5)

        # Nombre completo
        field("Nombre Completo:", 1)
        self.nombre_entry = tk.Entry(form, font=("Arial", 10), width=28, relief="solid", bd=1)
        self.nombre_entry.grid(row=1, column=1, sticky="w", pady=5)

        # Género
        field("Género:", 2)
        genero_frame = tk.Frame(form, bg="#f0f4f8")
        genero_frame.grid(row=2, column=1, sticky="w")
        self.genero_var = tk.StringVar(value="Masculino")
        tk.Radiobutton(genero_frame, text="Masculino", variable=self.genero_var,
                       value="Masculino", bg="#f0f4f8", font=("Arial", 10)).pack(side="left")
        tk.Radiobutton(genero_frame, text="Femenino", variable=self.genero_var,
                       value="Femenino", bg="#f0f4f8", font=("Arial", 10)).pack(side="left", padx=10)

        # Técnica artística
        field("Técnica Artística:", 3)
        self.tecnica_var = tk.StringVar()
        opciones = list(PRECIOS.keys())
        self.tecnica_combo = tk.OptionMenu(form, self.tecnica_var, *opciones,
                                           command=self._actualizar_costo)
        self.tecnica_combo.config(font=("Arial", 10), width=20, relief="solid")
        self.tecnica_combo.grid(row=3, column=1, sticky="w", pady=5)

        # Costo por clase
        field("Costo por Clase ($):", 4)
        self.costo_var = tk.StringVar(value="0")
        costo_entry = tk.Entry(form, textvariable=self.costo_var, font=("Arial", 10),
                               width=28, relief="solid", bd=1, state="disabled",
                               disabledforeground="#333", disabledbackground="#e8e8e8")
        costo_entry.grid(row=4, column=1, sticky="w", pady=5)

        # Número de clases
        field("Número de Clases:", 5)
        self.clases_entry = tk.Entry(form, font=("Arial", 10), width=28, relief="solid", bd=1)
        self.clases_entry.grid(row=5, column=1, sticky="w", pady=5)

        # Fecha de registro
        field("Fecha de Registro:", 6)
        self.fecha_var = tk.StringVar(value=str(date.today()))
        fecha_entry = tk.Entry(form, textvariable=self.fecha_var, font=("Arial", 10),
                               width=28, relief="solid", bd=1, state="disabled",
                               disabledforeground="#333", disabledbackground="#e8e8e8")
        fecha_entry.grid(row=6, column=1, sticky="w", pady=5)

        # Botones
        btn_frame = tk.Frame(self.root, bg="#f0f4f8", pady=10)
        btn_frame.pack()

        tk.Button(btn_frame, text="💾 Guardar Registro", command=self._guardar,
                  font=("Arial", 10, "bold"), bg="#2e7d32", fg="white",
                  relief="flat", cursor="hand2", padx=10, pady=6).grid(row=0, column=0, padx=6)

        tk.Button(btn_frame, text="📊 Calcular / Mostrar Reporte", command=self._mostrar_reporte,
                  font=("Arial", 10, "bold"), bg="#1565c0", fg="white",
                  relief="flat", cursor="hand2", padx=10, pady=6).grid(row=0, column=1, padx=6)

        tk.Button(btn_frame, text="🚪 Salir", command=self._salir,
                  font=("Arial", 10, "bold"), bg="#b71c1c", fg="white",
                  relief="flat", cursor="hand2", padx=10, pady=6).grid(row=0, column=2, padx=6)

    def _actualizar_costo(self, tecnica):
        precio = PRECIOS.get(tecnica, 0)
        self.costo_var.set(f"{precio:,}".replace(",", "."))

    def _guardar(self):
        identificacion = self.id_entry.get().strip()
        nombre = self.nombre_entry.get().strip()
        tecnica = self.tecnica_var.get()
        clases_str = self.clases_entry.get().strip()

        if not identificacion or not nombre or not tecnica or not clases_str:
            messagebox.showwarning("Campos incompletos", "Por favor complete todos los campos.")
            return
        if not clases_str.isdigit() or int(clases_str) <= 0:
            messagebox.showwarning("Dato inválido", "El número de clases debe ser un número entero positivo.")
            return

        self.participante.identificacion = identificacion
        self.participante.nombre_completo = nombre
        self.participante.genero = self.genero_var.get()
        self.participante.tecnica_artistica = tecnica
        self.participante.costo_por_clase = PRECIOS.get(tecnica, 0)
        self.participante.numero_clases = int(clases_str)
        self.participante.fecha_registro = self.fecha_var.get()

        messagebox.showinfo("Guardado", f"✅ Registro de '{nombre}' guardado correctamente.")

    def _mostrar_reporte(self):
        if not self.participante.nombre_completo:
            messagebox.showwarning("Sin datos", "Primero guarde el registro antes de ver el reporte.")
            return

        total = self.participante.calcular_costo_total(
            self.participante.numero_clases,
            self.participante.costo_por_clase
        )

        reporte_win = tk.Toplevel(self.root)
        reporte_win.title("Reporte")
        reporte_win.resizable(False, False)
        reporte_win.configure(bg="#f0f4f8")
        reporte_win.geometry("380x340")
        screen_w = reporte_win.winfo_screenwidth()
        screen_h = reporte_win.winfo_screenheight()
        reporte_win.geometry(f"380x340+{(screen_w-380)//2}+{(screen_h-340)//2}")

        frame = tk.Frame(reporte_win, bg="#e3f2fd", bd=2, relief="solid", padx=20, pady=20)
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        tk.Label(frame, text="ℹ️  Reporte del Participante",
                 font=("Arial", 12, "bold"), bg="#e3f2fd", fg="#1a3c5e").pack(pady=(0, 12))

        datos = [
            ("Nombre", self.participante.nombre_completo),
            ("ID", self.participante.identificacion),
            ("Género", self.participante.genero),
            ("Técnica", self.participante.tecnica_artistica),
            ("Clases", str(self.participante.numero_clases)),
            ("Fecha Registro", self.participante.fecha_registro),
            ("Costo por clase", f"${self.participante.costo_por_clase:,}".replace(",", ".")),
            ("Total a pagar", f"${total:,}".replace(",", ".")),
        ]

        for etiqueta, valor in datos:
            row = tk.Frame(frame, bg="#e3f2fd")
            row.pack(fill="x", pady=2)
            tk.Label(row, text=f"{etiqueta}:", font=("Arial", 10, "bold"),
                     bg="#e3f2fd", width=16, anchor="w").pack(side="left")
            tk.Label(row, text=valor, font=("Arial", 10),
                     bg="#e3f2fd", anchor="w").pack(side="left")

        tk.Button(reporte_win, text="  Aceptar  ", command=reporte_win.destroy,
                  font=("Arial", 11, "bold"), bg="#1a3c5e", fg="white",
                  relief="flat", cursor="hand2", pady=6).pack(pady=10)

    def _salir(self):
        if messagebox.askyesno("Salir", "¿Desea salir de la aplicación?"):
            self.login_root.destroy()


# ============================================================
# PUNTO DE ENTRADA
# ============================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()
