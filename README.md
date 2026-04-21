# GenerarFactura

Generador automático de facturas en PDF con registro en Excel.

## Descripción

Este proyecto permite generar facturas en formato PDF de manera automática. Las facturas incluyen:
- Numeración consecutiva automática
- Datos del cliente (nombre y documento)
- Descripción de productos/servicios
- Cantidad y valores
- Total calculado automáticamente
- Registro permanente en archivo Excel

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

Ejecutar el script:
```bash
python generar_factura.py
```

El programa solicitará los siguientes datos:
- **Cliente**: Nombre del cliente
- **Documento**: Número de identificación del cliente
- **Descripción**: Descripción del producto o servicio
- **Cantidad**: Cantidad de unidades
- **Valor unitario**: Precio unitario del producto/servicio

Después de ingresar los datos:
- Se guardará el registro en `facturas.xlsx`
- Se generará un PDF con la factura numerada automáticamente

## Archivos

- `generar_factura.py` - Script principal
- `requirements.txt` - Dependencias del proyecto
- `facturas.xlsx` - Base de datos de facturas (se crea automáticamente)

## Notas

- Los archivos PDF y XLSX generados se excluyen del repositorio (`gitignore`)
- La numeración de facturas es consecutiva y se almacena en Excel
- Diseñado para VALSEBSA S.A.S (Yumbo, Valle del Cauca)