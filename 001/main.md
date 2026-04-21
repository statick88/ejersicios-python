ALGORITMO fizzbuzz
ENTRADA: ninguno
SALIDA: secuencia impresa

INICIO
    PARA i DESDE 1 HASTA 50 HACER
        SI i es divisible por 3 Y i es divisible por 5 ENTONCES
            IMPRIMIR "FizzBuzz"
        SI_NO SI i es divisible por 3 ENTONCES
            IMPRIMIR "Fizz"
        SI_NO SI i es divisible por 5 ENTONCES
            IMPRIMIR "Buzz"
        SI_NO
            IMPRIMIR i
        FIN_SI
        i = i + 1
    FIN_PARA
FIN

i = 1 --> 1
i = 2 --> 2
i = 3 --> "Fizz"
i = 4 --> 4
i = 5 --> "Buzz"
i = 6 --> "Fizz"

Lista = 1, 2, "Fizz", 4, "Buzz", ..., "Buzz"