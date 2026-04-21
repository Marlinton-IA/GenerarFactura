# GenerarFactura

Generador automático de facturas en PDF con interfaz gráfica y registro en Excel.

## Descripción

Este proyecto permite generar facturas en formato PDF de manera automática con una interfaz gráfica amigable. Las facturas incluyen:
- Numeración consecutiva automática
- Datos del cliente (nombre y documento)
- Descripción de productos/servicios
- Cantidad y valores
- Cálculo automático de totales
- Registro permanente en archivo Excel
- Interfaz gráfica con Tkinter

## Características

✨ **Interfaz visual intuitiva** con Tkinter
✓ **Validación de datos** en tiempo real
📊 **Cálculo automático** de subtotales
🔢 **Numeración consecutiva** de facturas
💾 **Base de datos en Excel** con todos los registros
📄 **Generación de PDF** profesionales

## Requisitos

- Python 3.7 o superior
- Las librerías indicadas en `requirements.txt`

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/Marlinton-IA/GenerarFactura.git
cd GenerarFactura
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Uso

Ejecutar la aplicación:
```bash
python generar_factura.py
```

### Interfaz Gráfica

1. **Ingrese los datos:**
   - Cliente: Nombre del cliente
   - Documento: Número de identificación
   - Descripción: Descripción del producto o servicio
   - Cantidad: Cantidad de unidades
   - Valor Unitario: Precio unitario

2. **Botones disponibles:**
   - **Generar Factura**: Crea el PDF y guarda los datos en Excel
   - **Limpiar**: Borra todos los campos
   - **Ver Facturas**: Abre el archivo Excel con todos los registros

3. **Información en tiempo real:**
   - Cantidad total ingresada
   - Subtotal calculado
   - Próximo número de factura

## Archivos

- `generar_factura.py` - Aplicación principal con interfaz gráfica
- `requirements.txt` - Dependencias del proyecto
- `facturas.xlsx` - Base de datos de facturas (se crea automáticamente)
- `Factura_FV-XXXX.pdf` - Facturas generadas

## Notas

- Los archivos PDF y XLSX generados se excluyen del repositorio (`.gitignore`)
- La numeración de facturas es consecutiva y se almacena en Excel
- Diseñado para VALSEBSA S.A.S (Yumbo, Valle del Cauca)
- La interfaz es responsiva y fácil de usar

## Versión

- **v2.0** - Interfaz gráfica con Tkinter
- **v1.0** - Versión línea de comandos