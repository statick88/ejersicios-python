from datetime import datetime

def registrar_log(mensaje, archivo_log="sistema.log"):
    """Registra un mensaje con fecha y hora en el archivo de logs."""
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(archivo_log, "a") as f:
        f.write(f"[{fecha}] {mensaje}\n")
    print(f"Log registrado: {mensaje}")

# Uso del sistema de logs
registrar_log("Sistema iniciado")
registrar_log("Usuario conectado: ana")
registrar_log("Error en módulo de pagos")