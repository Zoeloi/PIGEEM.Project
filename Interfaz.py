import customtkinter as ctk

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuración básica de la ventana
        self.title("PIGEEM - Sistema de Gestión")
        self.geometry("800x600")
        ctk.set_appearance_mode("dark")  # Modo oscuro
        ctk.set_default_color_theme("blue")  # Tema azul
        
        # Crear el título principal
        self.title_label = ctk.CTkLabel(
            self, 
            text="PIGEEEM - Sistema de Gestión\nPlataforma Integral\n",
            text_color="white",
            fg_color="transparent",
            font=("Arial", 24, "bold")
        )
        self.title_label.pack(pady=20)
        
        # Crear los botones del menú
        self.create_menu_buttons()
        
    def create_menu_buttons(self):
        # Lista de opciones del menu
        menu_options = [
            "FINANZAS Y CONTABILIDAD",
            "INVENTARIO Y PEDIDOS",
            "GESTION DE CLIENTES Y EMPLEADOS",
            "PANEL GENERAL",
            "SALIR"
        ]
        
        # Crear un frame para contener los botones
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=20, padx=100, fill="both", expand=True)
        
        # Crear cada botón del menú
        for option in menu_options:
            button = ctk.CTkButton(
                button_frame,
                text=option,
                font=("Arial", 16),
                height=50,
                command=lambda opt=option: self.menu_action(opt)
            )
            button.pack(pady=10, fill="x")
    
    def menu_action(self, option):
        # Acciones al hacer clic en cada botón
        if option == "FINANZAS Y CONTABILIDAD":
            print("Abriendo módulo de Finanzas...")
            # Aquí iría el código para abrir tu módulo
        elif option == "INVENTARIO Y PEDIDOS":
            print("Abriendo módulo de Inventario...")
        elif option == "GESTION DE CLIENTES Y EMPLEADOS":
            print("Abriendo módulo de Clientes...")
        elif option == "PANEL GENERAL":
            print("Abriendo Panel General...")
        elif option == "SALIR":
            self.quit()
        
        print(f"Opción seleccionada: {option}")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
