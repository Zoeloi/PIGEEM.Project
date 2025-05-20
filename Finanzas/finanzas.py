import customtkinter as ctk

class FinanzasFrame(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Finanzas y Contabilidad")
        self.geometry("600x400")
        
        ctk.CTkLabel(self, text="Módulo de Finanzas y Contabilidad", font=("Arial", 20)).pack(pady=20)
        
        # Botón para ver estados financieros
        btn_estados = ctk.CTkButton(self, text="Ver Estados Financieros", command=self.ver_estados)
        btn_estados.pack(pady=10)
        
        # Botón para generar reporte PDF
        btn_reporte = ctk.CTkButton(self, text="Generar Reporte PDF", command=self.generar_reporte)
        btn_reporte.pack(pady=10)
        
        # Botón para cerrar la ventana
        btn_cerrar = ctk.CTkButton(self, text="Cerrar", command=self.destroy)
        btn_cerrar.pack(pady=30)
    
    def ver_estados(self):
        # Aquí va la lógica para mostrar estados financieros
        ctk.CTkLabel(self, text="(Aquí se mostrarán los estados financieros)", font=("Arial", 14)).pack(pady=5)
    
    def generar_reporte(self):
        # Aquí va la lógica para generar el reporte PDF
        ctk.CTkLabel(self, text="(Reporte PDF generado)", font=("Arial", 14)).pack(pady=5)






     