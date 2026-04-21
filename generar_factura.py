# ========================================
# GENERADOR DE FACTURAS EN PDF - VERSIÓN GUI
# Interfaz gráfica con Tkinter para generar facturas
# ========================================

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd  # Para manejo de datos en Excel
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
import datetime
import os

# Nombre del archivo Excel donde se guardarán los registros de facturas
archivo = "facturas.xlsx"

# Crear archivo Excel vacío si no existe
if not os.path.exists(archivo):
    df = pd.DataFrame(columns=["consecutivo", "fecha", "cliente", "documento", "descripcion", "cantidad", "valor_unitario"])
    df.to_excel(archivo, index=False)


class GeneradorFacturasApp:
    """Aplicación GUI para generar facturas"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Facturas - VALSEBSA S.A.S")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        
        # Colores
        self.color_primario = "#2c3e50"
        self.color_secundario = "#3498db"
        self.color_exito = "#27ae60"
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        """Crea los widgets de la interfaz"""
        
        # ========== ENCABEZADO ==========
        frame_encabezado = tk.Frame(self.root, bg=self.color_primario)
        frame_encabezado.pack(fill=tk.X, padx=0, pady=0)
        
        tk.Label(
            frame_encabezado,
            text="GENERADOR DE FACTURAS",
            font=("Arial", 18, "bold"),
            bg=self.color_primario,
            fg="white"
        ).pack(pady=15)
        
        tk.Label(
            frame_encabezado,
            text="VALSEBSA S.A.S - NIT 901764039-3",
            font=("Arial", 10),
            bg=self.color_primario,
            fg="#ecf0f1"
        ).pack()
        
        # ========== FRAME PRINCIPAL ==========
        frame_principal = ttk.Frame(self.root, padding="20")
        frame_principal.pack(fill=tk.BOTH, expand=True)
        
        # ========== CLIENTE ==========
        ttk.Label(frame_principal, text="Cliente:", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w", pady=10)
        self.entry_cliente = ttk.Entry(frame_principal, width=35, font=("Arial", 10))
        self.entry_cliente.grid(row=0, column=1, padx=10, pady=10)
        
        # ========== DOCUMENTO ==========
        ttk.Label(frame_principal, text="Documento:", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w", pady=10)
        self.entry_documento = ttk.Entry(frame_principal, width=35, font=("Arial", 10))
        self.entry_documento.grid(row=1, column=1, padx=10, pady=10)
        
        # ========== DESCRIPCIÓN ==========
        ttk.Label(frame_principal, text="Descripción:", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w", pady=10)
        self.entry_descripcion = ttk.Entry(frame_principal, width=35, font=("Arial", 10))
        self.entry_descripcion.grid(row=2, column=1, padx=10, pady=10)
        
        # ========== CANTIDAD ==========
        ttk.Label(frame_principal, text="Cantidad:", font=("Arial", 10, "bold")).grid(row=3, column=0, sticky="w", pady=10)
        self.entry_cantidad = ttk.Entry(frame_principal, width=35, font=("Arial", 10))
        self.entry_cantidad.grid(row=3, column=1, padx=10, pady=10)
        
        # ========== VALOR UNITARIO ==========
        ttk.Label(frame_principal, text="Valor Unitario ($):", font=("Arial", 10, "bold")).grid(row=4, column=0, sticky="w", pady=10)
        self.entry_valor = ttk.Entry(frame_principal, width=35, font=("Arial", 10))
        self.entry_valor.grid(row=4, column=1, padx=10, pady=10)
        
        # ========== INFORMACIÓN DINÁMICA ==========
        frame_info = ttk.LabelFrame(frame_principal, text="Información", padding="10")
        frame_info.grid(row=5, column=0, columnspan=2, sticky="ew", pady=20)
        
        ttk.Label(frame_info, text="Cantidad:", font=("Arial", 9)).grid(row=0, column=0, sticky="w")
        self.label_cantidad_total = ttk.Label(frame_info, text="0", font=("Arial", 9, "bold"), foreground=self.color_secundario)
        self.label_cantidad_total.grid(row=0, column=1, sticky="w", padx=20)
        
        ttk.Label(frame_info, text="Subtotal:", font=("Arial", 9)).grid(row=0, column=2, sticky="w")
        self.label_subtotal = ttk.Label(frame_info, text="$0", font=("Arial", 9, "bold"), foreground=self.color_secundario)
        self.label_subtotal.grid(row=0, column=3, sticky="w", padx=20)
        
        ttk.Label(frame_info, text="Próximo Consecutivo:", font=("Arial", 9)).grid(row=1, column=0, sticky="w", pady=5)
        self.label_consecutivo = ttk.Label(frame_info, text=self.obtener_consecutivo(), font=("Arial", 9, "bold"), foreground=self.color_exito)
        self.label_consecutivo.grid(row=1, column=1, sticky="w", padx=20)
        
        # Bindings para actualizar información
        self.entry_cantidad.bind("<KeyRelease>", lambda e: self.actualizar_totales())
        self.entry_valor.bind("<KeyRelease>", lambda e: self.actualizar_totales())
        
        # ========== BOTONES ==========
        frame_botones = ttk.Frame(frame_principal)
        frame_botones.grid(row=6, column=0, columnspan=2, sticky="ew", pady=20)
        
        boton_generar = tk.Button(
            frame_botones,
            text="✓ Generar Factura",
            command=self.generar_factura,
            bg=self.color_exito,
            fg="white",
            font=("Arial", 11, "bold"),
            padx=20,
            pady=10,
            cursor="hand2"
        )
        boton_generar.pack(side=tk.LEFT, padx=5)
        
        boton_limpiar = tk.Button(
            frame_botones,
            text="🗑 Limpiar",
            command=self.limpiar_campos,
            bg="#95a5a6",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=20,
            pady=10,
            cursor="hand2"
        )
        boton_limpiar.pack(side=tk.LEFT, padx=5)
        
        boton_ver_facturas = tk.Button(
            frame_botones,
            text="📊 Ver Facturas",
            command=self.ver_facturas,
            bg=self.color_secundario,
            fg="white",
            font=("Arial", 11, "bold"),
            padx=20,
            pady=10,
            cursor="hand2"
        )
        boton_ver_facturas.pack(side=tk.LEFT, padx=5)
    
    def obtener_consecutivo(self):
        """Obtiene el próximo consecutivo de factura"""
        try:
            df = pd.read_excel(archivo)
            if len(df) == 0:
                return "FV-0001"
            else:
                siguiente = int(df["consecutivo"].max()) + 1
                return f"FV-{siguiente:04d}"
        except:
            return "FV-0001"
    
    def actualizar_totales(self):
        """Actualiza los totales mostrados en la interfaz"""
        try:
            cantidad = int(self.entry_cantidad.get()) if self.entry_cantidad.get() else 0
            valor = float(self.entry_valor.get()) if self.entry_valor.get() else 0
            total = cantidad * valor
            
            self.label_cantidad_total.config(text=str(cantidad))
            self.label_subtotal.config(text=f"${total:,.0f}")
        except ValueError:
            pass
    
    def limpiar_campos(self):
        """Limpia todos los campos de entrada"""
        self.entry_cliente.delete(0, tk.END)
        self.entry_documento.delete(0, tk.END)
        self.entry_descripcion.delete(0, tk.END)
        self.entry_cantidad.delete(0, tk.END)
        self.entry_valor.delete(0, tk.END)
        self.label_cantidad_total.config(text="0")
        self.label_subtotal.config(text="$0")
        self.label_consecutivo.config(text=self.obtener_consecutivo())
        self.entry_cliente.focus()
    
    def validar_campos(self):
        """Valida que todos los campos estén completos y sean correctos"""
        if not self.entry_cliente.get():
            messagebox.showerror("Error", "Ingrese el nombre del cliente")
            return False
        
        if not self.entry_documento.get():
            messagebox.showerror("Error", "Ingrese el documento del cliente")
            return False
        
        if not self.entry_descripcion.get():
            messagebox.showerror("Error", "Ingrese la descripción del producto/servicio")
            return False
        
        try:
            cantidad = int(self.entry_cantidad.get())
            if cantidad <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número positivo")
            return False
        
        try:
            valor = float(self.entry_valor.get())
            if valor <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "El valor unitario debe ser un número positivo")
            return False
        
        return True
    
    def generar_factura(self):
        """Genera la factura en PDF y guarda los datos en Excel"""
        if not self.validar_campos():
            return
        
        try:
            # ========== LECTURA DE DATOS ==========
            df = pd.read_excel(archivo)
            cliente = self.entry_cliente.get()
            documento = self.entry_documento.get()
            descripcion = self.entry_descripcion.get()
            cantidad = int(self.entry_cantidad.get())
            valor_unitario = float(self.entry_valor.get())
            fecha = datetime.date.today()
            
            # ========== GENERAR CONSECUTIVO ==========
            if len(df) == 0:
                consecutivo = 1
            else:
                consecutivo = int(df["consecutivo"].max()) + 1
            
            # ========== GUARDAR EN EXCEL ==========
            nuevo = {
                "consecutivo": consecutivo,
                "fecha": fecha,
                "cliente": cliente,
                "documento": documento,
                "descripcion": descripcion,
                "cantidad": cantidad,
                "valor_unitario": valor_unitario
            }
            
            df = pd.concat([df, pd.DataFrame([nuevo])], ignore_index=True)
            df.to_excel(archivo, index=False)
            
            # ========== CREAR PDF ==========
            total = cantidad * valor_unitario
            pdf_path = f"Factura_FV-{consecutivo:04d}.pdf"
            pdf = SimpleDocTemplate(pdf_path, pagesize=letter)
            styles = getSampleStyleSheet()
            
            contenido = []
            
            # Encabezado
            contenido.append(Paragraph("LA SEXTA PC IMPRESORAS", styles["Title"]))
            contenido.append(Paragraph("VALSEBSA S.A.S - NIT 901764039-3", styles["Normal"]))
            contenido.append(Paragraph("Yumbo - Valle del Cauca", styles["Normal"]))
            contenido.append(Spacer(1, 12))
            
            # Número y fecha
            contenido.append(Paragraph(f"Factura No: FV-{consecutivo:04d}", styles["Normal"]))
            contenido.append(Paragraph(f"Fecha: {fecha}", styles["Normal"]))
            contenido.append(Spacer(1, 12))
            
            # Tabla
            tabla = Table([
                ["Cliente", cliente],
                ["Documento", documento],
                ["Descripción", descripcion],
                ["Cantidad", str(cantidad)],
                ["Valor Unitario", f"${valor_unitario:,.0f}"],
                ["Total", f"${total:,.0f}"]
            ])
            
            tabla.setStyle(TableStyle([
                ("GRID", (0, 0), (-1, -1), 1, colors.black),
                ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey)
            ]))
            
            contenido.append(tabla)
            pdf.build(contenido)
            
            # ========== MENSAJE DE ÉXITO ==========
            messagebox.showinfo(
                "¡Éxito!",
                f"Factura FV-{consecutivo:04d} generada correctamente\n\nGuardada como: {pdf_path}"
            )
            
            self.limpiar_campos()
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al generar la factura: {str(e)}")
    
    def ver_facturas(self):
        """Abre el archivo de facturas en Excel"""
        try:
            if os.path.exists(archivo):
                os.startfile(archivo)
            else:
                messagebox.showinfo("Información", "Aún no hay facturas generadas")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el archivo: {str(e)}")


# ========== EJECUTAR APLICACIÓN ==========
if __name__ == "__main__":
    root = tk.Tk()
    app = GeneradorFacturasApp(root)
    root.mainloop()
