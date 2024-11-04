import subprocess
import asyncio
import time


# Función sincrona que ejecuta el bloc de notas
def funcionSincrona():
    try:
        inicio = time.time()
        print("Has elegido la funcion sincrona")
        subprocess.run(['notepad.exe'])
        print("El bloc de notas se ha ejecutado de manera sincrona")
        fin = time.time()
        print("Tiempo de ejecución de la función sincrona: " + str(fin - inicio) + " segundos")
    except subprocess.CalledProcessError as e:
        print(e.output)


# Función asincrona que ejecuta el Bloc de notas
async def funcionAsincrona():
    try:
        inicio = time.time()
        print("Has elegido la funcion asincrona")
        proceso = await asyncio.create_subprocess_exec('notepad.exe')
        #El mensaje se muestra aunque el bloc de notas sigue en ejecucion
        print("El bloc de notas se ha ejecutado de manera asincrona")
        # Esperar a que Notepad se cierre
        await proceso.wait()
        fin = time.time()
        print("Tiempo de ejecución de la función asincrona: " + str(fin - inicio) + " segundos")
    except subprocess.CalledProcessError as e:
        print(e.output)


# Función main que se ejecuta de manera asincrona
async def main():
    print("Pulsa 1 para ejecutar el bloc de notas de manera sincrona\nPulsa 2 para ejecutar el bloc de notas de manera asincrona")
    opcion = input()
    if opcion == "1":
        funcionSincrona()
    elif opcion == "2":
        await funcionAsincrona()
    else:
        print("Opción no válida")
# Se ejecuta el main
asyncio.run(main())
