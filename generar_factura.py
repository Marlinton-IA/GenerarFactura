# ========================================
# GENERADOR DE FACTURAS EN PDF
# Crea facturas automáticas con registro en Excel
# ========================================

import pandas as pd  # Para manejo de datos en Excel
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer  # Para crear PDF
from reportlab.lib import colors  # Para colores en tablas PDF
from reportlab.lib.pagesizes import letter  # Tamaño de página letter
from reportlab.lib.styles import getSampleStyleSheet  # Estilos predefinidos para PDF
import datetime  # Para obtener la fecha actual

# Nombre del archivo Excel donde se guardarán los registros de facturas
archivo = "facturas.xlsx"

# Leer datos existentes del archivo Excel
df = pd.read_excel(archivo)

# ========== GENERACIÓN DE CONSECUTIVO AUTOMÁTICO ==========
# Si el archivo está vacío, inicia en 1
# Si hay datos, obtiene el consecutivo máximo y suma 1
if len(df) == 0:
    consecutivo = 1
else:
    consecutivo = int(df["consecutivo"].max()) + 1

# ========== ENTRADA DE DATOS DEL USUARIO ==========
# Solicitar al usuario los datos de la factura
cliente = input("Cliente: ")
documento = input("Documento: ")
descripcion = input("Descripción: ")
cantidad = int(input("Cantidad: "))
valor_unitario = float(input("Valor unitario: "))

# Obtener la fecha actual del sistema
fecha = datetime.date.today()

# ========== GUARDAR EN EXCEL ==========
# Crear un diccionario con los datos de la nueva factura
nuevo = {
    "consecutivo": consecutivo,
    "fecha": fecha,
    "cliente": cliente,
    "documento": documento,
    "descripcion": descripcion,
    "cantidad": cantidad,
    "valor_unitario": valor_unitario
}

# Agregar la nueva fila al DataFrame y guardar en Excel
df = pd.concat([df, pd.DataFrame([nuevo])], ignore_index=True)
df.to_excel(archivo, index=False)

# ========== CREAR PDF ==========
# Calcular el total (cantidad × valor unitario)
total = cantidad * valor_unitario

# Crear documento PDF con nombre de factura numerado (Factura_FV-0001.pdf)
pdf = SimpleDocTemplate(f"Factura_FV-{consecutivo:04d}.pdf", pagesize=letter)

# Obtener estilos predefinidos para el PDF
styles = getSampleStyleSheet()

# Lista que contendrá todos los elementos del PDF
contenido = []

# ========== ENCABEZADO ==========
# Agregar nombre de la empresa
contenido.append(Paragraph("LA SEXTA PC IMPRESORAS", styles["Title"]))
# Agregar datos de la empresa
contenido.append(Paragraph("VALSEBSA S.A.S - NIT 901764039-3", styles["Normal"]))
contenido.append(Paragraph("Yumbo - Valle del Cauca", styles["Normal"]))
# Espacio en blanco
contenido.append(Spacer(1, 12))

# ========== NÚMERO Y FECHA DE FACTURA ==========
contenido.append(Paragraph(f"Factura No: FV-{consecutivo:04d}", styles["Normal"]))
contenido.append(Paragraph(f"Fecha: {fecha}", styles["Normal"]))
contenido.append(Spacer(1, 12))

# ========== TABLA CON DATOS ==========
# Crear tabla con información de la factura
tabla = Table([
    ["Cliente", cliente],
    ["Documento", documento],
    ["Descripción", descripcion],
    ["Cantidad", cantidad],
    ["Valor Unitario", f"${valor_unitario:,.0f}"],
    ["Total", f"${total:,.0f}"]
])

# Aplicar estilos a la tabla (bordes, colores)
tabla.setStyle(TableStyle([
    ("GRID", (0, 0), (-1, -1), 1, colors.black),  # Bordes en toda la tabla
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey)  # Fondo gris en encabezado
]))

# Agregar tabla al contenido del PDF
contenido.append(tabla)

# Generar el archivo PDF
pdf.build(contenido)

print(f"Factura FV-{consecutivo:04d} generada correctamente")
