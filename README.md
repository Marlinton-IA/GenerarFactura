# GenerarFactura

Generador automático de facturas en PDF con interfaz gráfica y soporte para múltiples items.

## Descripción

Aplicación profesional para generar facturas en formato PDF con una interfaz visual intuitiva. Permite agregar múltiples items por factura (servicios, repuestos, licencias, etc.) con cálculo automático de totales.

## Características

✨ **Interfaz visual moderna** con Tkinter
✓ **Múltiples items por factura** - Agregue servicios, repuestos, licencias, etc.
✓ **Cálculo automático** - Subtotal y total en tiempo real
🔢 **Numeración consecutiva** de facturas
💾 **Base de datos en Excel** con todos los registros
📄 **PDF profesionales** con formato de empresa
🗑 **Gestión de items** - Agregar, eliminar y modificar items

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

### Instrucciones de uso

1. **Ingrese datos del cliente:**
   - Cliente: Nombre del cliente
   - Documento: Número de identificación

2. **Agregue items:**
   - Descripción: Descripción del servicio/producto (ej: "Mantenimiento", "Repuesto XYZ", "Licencia Software")
   - Cantidad: Cantidad de unidades
   - Valor: Precio unitario
   - Click en "+ Agregar Item"

3. **Gestione items:**
   - Vea todos los items en la tabla
   - Seleccione un item y use "🗑 Eliminar Item" para borrarlo
   - Use "🗑 Limpiar Todo" para borrar todos los items

4. **Genere la factura:**
   - Verifique que tenga al menos un item
   - Click en "✓ Generar Factura"
   - Se creará el PDF y se guardarán los datos en Excel

5. **Botones disponibles:**
   - **+ Agregar Item**: Agrega un item a la factura
   - **🗑 Eliminar Item**: Elimina el item seleccionado
   - **✓ Generar Factura**: Crea el PDF y guarda en Excel
   - **🗑 Limpiar Todo**: Borra todos los campos
   - **📊 Ver Facturas**: Abre el archivo Excel con registros

### Panel de información

El panel "Resumen" muestra en tiempo real:
- Cantidad de items en la factura
- Total general de la factura
- Próximo número de consecutivo

## Ejemplos de uso

### Ejemplo 1: Factura con servicios múltiples
```
Cliente: Empresa ABC
Documento: 123456789

Items:
- Mantenimiento preventivo (Cant: 1, Val: $500.000)
- Reparación de equipo (Cant: 1, Val: $250.000)
- Licencia Software (Cant: 2, Val: $100.000 c/u)

Total: $950.000
```

### Ejemplo 2: Factura con repuestos
```
Cliente: Tienda XYZ
Documento: 987654321

Items:
- Tóner Negro (Cant: 5, Val: $45.000)
- Cartuchos Color (Cant: 3, Val: $55.000)
- Papel Bond (Cant: 10 resmas, Val: $25.000)

Total: $520.000
```

## Archivos

- `generar_factura.py` - Aplicación principal con interfaz gráfica
- `requirements.txt` - Dependencias del proyecto
- `facturas.xlsx` - Base de datos de facturas (se crea automáticamente)
- `Factura_FV-XXXX.pdf` - Facturas generadas

## Estructura de datos

### Archivo Excel (facturas.xlsx)
Columnas:
- `consecutivo`: Número de factura (FV-XXXX)
- `fecha`: Fecha de generación
- `cliente`: Nombre del cliente
- `documento`: Documento del cliente
- `items`: Descripción de todos los items
- `total`: Total general de la factura

### PDF generado
Incluye:
- Encabezado de la empresa
- Número y fecha de factura
- Datos del cliente
- Tabla con todos los items (descripción, cantidad, valor unitario, subtotal)
- Total general

## Notas

- Los archivos PDF y XLSX generados se excluyen del repositorio (`.gitignore`)
- La numeración de facturas es consecutiva y automática
- Diseñado para VALSEBSA S.A.S (Yumbo, Valle del Cauca)
- Soporta múltiples idiomas y caracteres especiales
- Permite agregar, eliminar y modificar items antes de generar

## Versión

- **v3.0** - Soporte para múltiples items por factura
- **v2.0** - Interfaz gráfica con Tkinter
- **v1.0** - Versión línea de comandos