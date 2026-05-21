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
# CLASE PÚBLICA: GestionParticipantes
# Encapsula todos los datos del participante y la lógica
# de negocio para el cálculo del costo total del taller.
# ============================================================
class GestionParticipantes:
    """
    Clase pública que modela un participante de la academia
    de música Melodías Perfectas.

    Atributos:
        identificacion  (str)  : Número de identificación del participante.
        nombre_completo (str)  : Nombre completo del participante.
        genero          (str)  : Género del participante (Masculino / Femenino).
        tecnica         (str)  : Técnica artística seleccionada.
        costo_por_clase (int)  : Costo en pesos por cada clase según técnica.
        numero_clases   (int)  : Cantidad de clases tomadas por el participante.
        fecha_registro  (str)  : Fecha de registro generada automáticamente.
    """

    def __init__(self,
                 identificacion: str,
                 nombre_completo: str,
                 genero: str,
                 tecnica: str,
                 costo_por_clase: int,
                 numero_clases: int,
                 fecha_registro: str):
        # Asignación correcta de todos los atributos en el constructor
        self.identificacion  = identificacion
        self.nombre_completo = nombre_completo
        self.genero          = genero
        self.tecnica         = tecnica
        self.costo_por_clase = costo_por_clase
        self.numero_clases   = numero_clases
        self.fecha_registro  = fecha_registro

    # ----------------------------------------------------------
    # MÉTODO: calcular_costo_total
    # Recibe: numero_clases (int), costo_por_clase (int)
    # Retorna: int  →  total = numero_clases × costo_por_clase
    # ----------------------------------------------------------
    def calcular_costo_total(self, numero_clases: int, costo_por_clase: int) -> int:
        """Calcula y retorna el costo total del taller."""
        return numero_clases * costo_por_clase

    # ----------------------------------------------------------
    # MÉTODO: obtener_reporte
    # Retorna: str  →  cadena con todos los datos del participante
    #                  más el costo total calculado.
    # ----------------------------------------------------------
    def obtener_reporte(self) -> str:
        """Genera y retorna un reporte completo del participante."""
        total = self.calcular_costo_total(self.numero_clases, self.costo_por_clase)
        reporte = (
            f"Nombre:          {self.nombre_completo}\n"
            f"ID:              {self.identificacion}\n"
            f"Género:          {self.genero}\n"
            f"Técnica:         {self.tecnica}\n"
            f"Clases:          {self.numero_clases}\n"
            f"Fecha Registro:  {self.fecha_registro}\n"
            f"Costo por clase: ${self.costo_por_clase:,}".replace(",", ".") + "\n"
            f"Total a pagar:   ${total:,}".replace(",", ".")
        )
        return reporte


# ============================================================
# TABLA DE PRECIOS POR TÉCNICA ARTÍSTICA
# ============================================================
PRECIOS = {
    "Dibujo":     70000,
    "Pintura":    85000,
    "Escritura": 100000,
    "Fotografía": 90000,
    "Grabado":    75000,
}


# ============================================================
# VENTANA 1: LOGIN
# ============================================================
class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f4f8")
        self._centrar(380, 220)
        self._construir_ui()

    def _centrar(self, w, h):
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        self.root.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}")

    def _construir_ui(self):
        frame = tk.Frame(self.root, bg="#f0f4f8", padx=20, pady=20)
        frame.pack(expand=True)

        tk.Label(frame, text="🎵 Gestión de Participantes",
                 font=("Arial", 13, "bold"), bg="#f0f4f8", fg="#1a3c5e").pack(pady=(0, 4))
        tk.Label(frame, text="Autor: Cristian Gabriel Moreno Rodriguez",
                 font=("Arial", 10), bg="#f0f4f8", fg="#555").pack(pady=(0, 14))

        tk.Label(frame, text="Contraseña:", font=("Arial", 11), bg="#f0f4f8").pack()
        self.entry_pass = tk.Entry(frame, show="*", font=("Arial", 11),
                                   width=22, relief="solid", bd=1)
        self.entry_pass.pack(pady=6)
        self.entry_pass.bind("<Return>", lambda e: self._ingresar())

        tk.Button(frame, text="  Ingresar  ", command=self._ingresar,
                  font=("Arial", 11, "bold"), bg="#1a3c5e", fg="white",
                  relief="flat", cursor="hand2", padx=10, pady=4).pack(pady=8)

    def _ingresar(self):
        if self.entry_pass.get() == "3971":
            self.root.withdraw()
            RegistroWindow(tk.Toplevel(self.root), self.root)
        else:
            messagebox.showerror("Acceso denegado", "Contraseña incorrecta. Intente de nuevo.")
            self.entry_pass.delete(0, tk.END)


# ============================================================
# VENTANA 2: REGISTRO DE DATOS
# ============================================================
class RegistroWindow:
    def __init__(self, root, login_root):
        self.root        = root
        self.login_root  = login_root
        self.participante = None          # Se crea al guardar
        self.root.title("Registro de Participante")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f4f8")
        self._centrar(480, 450)
        self._construir_ui()
        self.root.protocol("WM_DELETE_WINDOW", self._salir)

    def _centrar(self, w, h):
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        self.root.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}")

    def _construir_ui(self):
        # Encabezado
        tk.Frame(self.root, bg="#1a3c5e", pady=10).pack(fill="x")
        tk.Label(self.root.winfo_children()[-1],
                 text="🎵 Registro de Participante",
                 font=("Arial", 13, "bold"), bg="#1a3c5e", fg="white").pack()

        form = tk.Frame(self.root, bg="#f0f4f8", padx=28, pady=16)
        form.pack(fill="both", expand=True)

        def etiqueta(texto, fila):
            tk.Label(form, text=texto, font=("Arial", 10, "bold"),
                     bg="#f0f4f8", anchor="w", width=20
                     ).grid(row=fila, column=0, sticky="w", pady=5)

        # Identificación
        etiqueta("Identificación:", 0)
        self.entry_id = tk.Entry(form, font=("Arial", 10), width=28, relief="solid", bd=1)
        self.entry_id.grid(row=0, column=1, sticky="w", pady=5)

        # Nombre completo
        etiqueta("Nombre Completo:", 1)
        self.entry_nombre = tk.Entry(form, font=("Arial", 10), width=28, relief="solid", bd=1)
        self.entry_nombre.grid(row=1, column=1, sticky="w", pady=5)

        # Género
        etiqueta("Género:", 2)
        self.var_genero = tk.StringVar(value="Masculino")
        gf = tk.Frame(form, bg="#f0f4f8")
        gf.grid(row=2, column=1, sticky="w")
        tk.Radiobutton(gf, text="Masculino", variable=self.var_genero,
                       value="Masculino", bg="#f0f4f8", font=("Arial", 10)).pack(side="left")
        tk.Radiobutton(gf, text="Femenino",  variable=self.var_genero,
                       value="Femenino",  bg="#f0f4f8", font=("Arial", 10)).pack(side="left", padx=10)

        # Técnica artística
        etiqueta("Técnica Artística:", 3)
        self.var_tecnica = tk.StringVar()
        om = tk.OptionMenu(form, self.var_tecnica, *PRECIOS.keys(),
                           command=self._actualizar_costo)
        om.config(font=("Arial", 10), width=20, relief="solid")
        om.grid(row=3, column=1, sticky="w", pady=5)

        # Costo por clase (deshabilitado — solo lectura)
        etiqueta("Costo por Clase ($):", 4)
        self.var_costo = tk.StringVar(value="0")
        tk.Entry(form, textvariable=self.var_costo, font=("Arial", 10),
                 width=28, relief="solid", bd=1, state="disabled",
                 disabledforeground="#333", disabledbackground="#e8e8e8"
                 ).grid(row=4, column=1, sticky="w", pady=5)

        # Número de clases
        etiqueta("Número de Clases:", 5)
        self.entry_clases = tk.Entry(form, font=("Arial", 10), width=28, relief="solid", bd=1)
        self.entry_clases.grid(row=5, column=1, sticky="w", pady=5)

        # Fecha de registro (automática, deshabilitada)
        etiqueta("Fecha de Registro:", 6)
        self.var_fecha = tk.StringVar(value=str(date.today()))
        tk.Entry(form, textvariable=self.var_fecha, font=("Arial", 10),
                 width=28, relief="solid", bd=1, state="disabled",
                 disabledforeground="#333", disabledbackground="#e8e8e8"
                 ).grid(row=6, column=1, sticky="w", pady=5)

        # Botones
        bf = tk.Frame(self.root, bg="#f0f4f8", pady=10)
        bf.pack()
        tk.Button(bf, text="💾 Guardar Registro",
                  command=self._guardar,
                  font=("Arial", 10, "bold"), bg="#2e7d32", fg="white",
                  relief="flat", cursor="hand2", padx=10, pady=6
                  ).grid(row=0, column=0, padx=6)
        tk.Button(bf, text="📊 Calcular / Mostrar Reporte",
                  command=self._mostrar_reporte,
                  font=("Arial", 10, "bold"), bg="#1565c0", fg="white",
                  relief="flat", cursor="hand2", padx=10, pady=6
                  ).grid(row=0, column=1, padx=6)
        tk.Button(bf, text="🚪 Salir",
                  command=self._salir,
                  font=("Arial", 10, "bold"), bg="#b71c1c", fg="white",
                  relief="flat", cursor="hand2", padx=10, pady=6
                  ).grid(row=0, column=2, padx=6)

    def _actualizar_costo(self, tecnica):
        """Actualiza automáticamente el costo por clase al seleccionar técnica."""
        self.var_costo.set(f"{PRECIOS.get(tecnica, 0):,}".replace(",", "."))

    def _validar_campos(self) -> bool:
        """Valida que todos los campos estén completos y sean correctos."""
        if not self.entry_id.get().strip():
            messagebox.showwarning("Campo vacío", "Ingrese la identificación.")
            return False
        if not self.entry_nombre.get().strip():
            messagebox.showwarning("Campo vacío", "Ingrese el nombre completo.")
            return False
        if not self.var_tecnica.get():
            messagebox.showwarning("Campo vacío", "Seleccione una técnica artística.")
            return False
        clases = self.entry_clases.get().strip()
        if not clases.isdigit() or int(clases) <= 0:
            messagebox.showwarning("Dato inválido",
                                   "El número de clases debe ser un número entero positivo.")
            return False
        return True

    def _guardar(self):
        """
        Guarda los datos del formulario instanciando correctamente
        la clase GestionParticipantes con todos sus atributos.
        """
        if not self._validar_campos():
            return

        # Instancia correcta de la clase con TODOS los parámetros del constructor
        self.participante = GestionParticipantes(
            identificacion  = self.entry_id.get().strip(),
            nombre_completo = self.entry_nombre.get().strip(),
            genero          = self.var_genero.get(),
            tecnica         = self.var_tecnica.get(),
            costo_por_clase = PRECIOS.get(self.var_tecnica.get(), 0),
            numero_clases   = int(self.entry_clases.get().strip()),
            fecha_registro  = self.var_fecha.get()
        )
        messagebox.showinfo("Guardado",
                            f"✅ Registro de '{self.participante.nombre_completo}' guardado correctamente.")

    def _mostrar_reporte(self):
        """
        Abre la ventana de reporte. Llama al método obtener_reporte()
        del objeto GestionParticipantes para mostrar todos los datos
        incluyendo el costo total calculado.
        """
        if self.participante is None:
            messagebox.showwarning("Sin datos",
                                   "Primero guarde el registro antes de ver el reporte.")
            return

        ReporteWindow(tk.Toplevel(self.root), self.participante)

    def _salir(self):
        if messagebox.askyesno("Salir", "¿Desea salir de la aplicación?"):
            self.login_root.destroy()


# ============================================================
# VENTANA 3: REPORTE
# ============================================================
class ReporteWindow:
    def __init__(self, root, participante: GestionParticipantes):
        self.root         = root
        self.participante = participante
        self.root.title("Reporte")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f4f8")
        self._centrar(400, 360)
        self._construir_ui()

    def _centrar(self, w, h):
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        self.root.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}")

    def _construir_ui(self):
        frame = tk.Frame(self.root, bg="#e3f2fd", bd=2,
                         relief="solid", padx=24, pady=20)
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        tk.Label(frame, text="ℹ️  Reporte del Participante",
                 font=("Arial", 12, "bold"), bg="#e3f2fd", fg="#1a3c5e"
                 ).pack(pady=(0, 14))

        # Calcula el total usando el método de la clase
        total = self.participante.calcular_costo_total(
            self.participante.numero_clases,
            self.participante.costo_por_clase
        )

        # Datos a mostrar
        datos = [
            ("Nombre",          self.participante.nombre_completo),
            ("ID",              self.participante.identificacion),
            ("Género",          self.participante.genero),
            ("Técnica",         self.participante.tecnica),
            ("Clases",          str(self.participante.numero_clases)),
            ("Fecha Registro",  self.participante.fecha_registro),
            ("Costo por clase", f"${self.participante.costo_por_clase:,}".replace(",", ".")),
            ("Total a pagar",   f"${total:,}".replace(",", ".")),
        ]

        for etiqueta, valor in datos:
            fila = tk.Frame(frame, bg="#e3f2fd")
            fila.pack(fill="x", pady=3)
            tk.Label(fila, text=f"{etiqueta}:", font=("Arial", 10, "bold"),
                     bg="#e3f2fd", width=16, anchor="w").pack(side="left")
            tk.Label(fila, text=valor, font=("Arial", 10),
                     bg="#e3f2fd", anchor="w").pack(side="left")

        tk.Button(self.root, text="  Aceptar  ", command=self.root.destroy,
                  font=("Arial", 11, "bold"), bg="#1a3c5e", fg="white",
                  relief="flat", cursor="hand2", pady=6).pack(pady=10)


# ============================================================
# PUNTO DE ENTRADA
# ============================================================
if __name__ == "__main__":
    root = tk.Tk()
    LoginWindow(root)
    root.mainloop()
