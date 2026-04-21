import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
import datetime

archivo = "facturas.xlsx"

df = pd.read_excel(archivo)

# Generar consecutivo automático
if len(df) == 0:
    consecutivo = 1
else:
    consecutivo = int(df["consecutivo"].max()) + 1

# Datos (puedes cambiarlos aquí o luego hacer input)
cliente = input("Cliente: ")
documento = input("Documento: ")
descripcion = input("Descripción: ")
cantidad = int(input("Cantidad: "))
valor_unitario = float(input("Valor unitario: "))

fecha = datetime.date.today()

# Guardar en Excel
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

# Crear PDF
total = cantidad * valor_unitario

pdf = SimpleDocTemplate(f"Factura_FV-{consecutivo:04d}.pdf", pagesize=letter)
styles = getSampleStyleSheet()

contenido = []

contenido.append(Paragraph("LA SEXTA PC IMPRESORAS", styles["Title"]))
contenido.append(Paragraph("VALSEBSA S.A.S - NIT 901764039-3", styles["Normal"]))
contenido.append(Paragraph("Yumbo - Valle del Cauca", styles["Normal"]))
contenido.append(Spacer(1,12))

contenido.append(Paragraph(f"Factura No: FV-{consecutivo:04d}", styles["Normal"]))
contenido.append(Paragraph(f"Fecha: {fecha}", styles["Normal"]))
contenido.append(Spacer(1,12))

tabla = Table([
    ["Cliente", cliente],
    ["Documento", documento],
    ["Descripción", descripcion],
    ["Cantidad", cantidad],
    ["Valor Unitario", f"${valor_unitario:,.0f}"],
    ["Total", f"${total:,.0f}"]
])

tabla.setStyle(TableStyle([
    ("GRID",(0,0),(-1,-1),1,colors.black),
    ("BACKGROUND",(0,0),(-1,0),colors.lightgrey)
]))

contenido.append(tabla)

pdf.build(contenido)

print(f"Factura FV-{consecutivo:04d} generada correctamente")
