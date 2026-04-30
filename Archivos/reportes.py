from datetime import datetime

def generar_reporte(ventas, archivo="reporte_ventas.txt"):
    """Genera un reporte de ventas en formato de texto."""
    
    total = sum(v["monto"] for v in ventas)
    promedio = total / len(ventas) if ventas else 0
    
    with open(archivo, "w") as f:
        f.write("=" * 40 + "\n")
        f.write("   REPORTE DE VENTAS\n")
        f.write(f"   Fecha: {datetime.now().strftime('%Y-%m-%d')}\n")
        f.write("=" * 40 + "\n\n")
        
        for i, venta in enumerate(ventas, start=1):
            f.write(f"  {i}. {venta['producto']}: ${venta['monto']:.2f}\n")
        
        f.write("\n" + "-" * 40 + "\n")
        f.write(f"  Total: ${total:.2f}\n")
        f.write(f"  Promedio: ${promedio:.2f}\n")
        f.write(f"  Cantidad de ventas: {len(ventas)}\n")
        f.write("-" * 40 + "\n")
    
    print(f"Reporte generado: {archivo}")

# Datos de ejemplo
ventas_del_dia = [
    {"producto": "Teclado mecánico", "monto": 89.99},
    {"producto": "Mouse inalámbrico", "monto": 45.50},
    {"producto": "Monitor 27 pulgadas", "monto": 299.99},
]

generar_reporte(ventas_del_dia)