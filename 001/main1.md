ALGORITMO cajero_automatico
ENTRADA: saldo_inicial, lista de operaciones
SALIDA: saldo_final

INICIO
    saldo ← saldo_inicial
    
    PARA cada operacion EN lista HACER
        TIPO ← tipo de operacion
        MONTO ← monto de operacion
        
        SI TIPO = "deposito" ENTONCES
            saldo ← saldo + MONTO
            IMPRIMIR "Depósito de", MONTO, "exitoso"
            
        SI_NO SI TIPO = "retiro" ENTONCES
            SI MONTO <= saldo ENTONCES
                saldo ← saldo - MONTO
                IMPRIMIR "Retiro de", MONTO, "exitoso"
            SI_NO
                IMPRIMIR "Error: saldo insuficiente"
            FIN_SI
            
        SI_NO SI TIPO = "consulta" ENTONCES
            IMPRIMIR "Saldo actual:", saldo
            
        SI_NO
            IMPRIMIR "Error: operación desconocida"
        FIN_SI
    FIN_PARA
    
    IMPRIMIR "Saldo final:", saldo
FIN

saldo_inicial = $10,00
MONTO = $5,00
Tipo_operacion = "Retiro"

saldo_inicial <- $10,00 
retiro = $10,00 - $5,00
saldo_final = saldo_inicial - retiro
saldo final = $10,00 - $5,00