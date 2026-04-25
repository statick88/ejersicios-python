# Procesar solo archivos con extensión .txt
archivos = ["datos.txt", "imagen.png", "notas.txt", "script.py", "reporte.txt"]

for archivo in archivos:
    if not archivo.endswith(".txt"):
        print(f"⏭️ Saltando {archivo} (no es .txt)")
        continue
    
    # Solo llegamos aquí si el archivo es .txt
    print(f"📄 Procesando {archivo}...")
    # Aquí iría la lógica de procesamiento