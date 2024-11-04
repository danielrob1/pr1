import psutil

# Se pide al usuario que introduzca procesos que se almacenan en la lista listaProcesos hasta que meta un 0
listaProcesos = []
listaProcesosEncontrados = []
print("Escribe una lista de procesos para mostrar información sobre ellos, pulsa 0 para cerrar la lista: ")
procesosEntrada = ""

while procesosEntrada != "0":
    procesosEntrada = input()
    if procesosEntrada != "0":
        listaProcesos.append(procesosEntrada)

# Por cada elemento de la lista se comprueba si existe un proceso activo con el mismo nombre
try:
    for recLista in listaProcesos:
        procesoEncontrado = False
        for proc in psutil.process_iter():
            if recLista.lower() == proc.name().lower():
                # Cuando cumple los criterios, se almacena la información del proceso
                procesoEncontrado = True
                nombreProceso = proc.name()
                pidProceso = proc.pid
                memoria = proc.memory_info().rss / (1024 * 1024)
                listaProcesosEncontrados.append(proc)

        # Si se ha encontrado el proceso que busca el usuario, se muestra su información
        if procesoEncontrado:
            print("El proceso", nombreProceso, "está activo | PID:", pidProceso, "| Memoria:", memoria, "MB")
        else:
            print("El proceso", recLista, "no está activo")
    procesoEncontrado=False

    # Se pide al usuario que escriba la palabra clave para filtrar los procesos que se muestran
    print("Escribe una palabra clave para filtrar los procesos que se muestran: ")
    palabraClave = input()
    for proc in listaProcesosEncontrados:
        if palabraClave.lower() in proc.name().lower():
            # Cuando cumple los criterios, se muestra la información del proceso
            nombreProceso = proc.name()
            pidProceso = proc.pid
            memoria = proc.memory_info().rss / (1024 * 1024)
            print("El proceso", nombreProceso, "contiene la palabra clave | PID:", pidProceso, "| Memoria:", memoria,
                  "MB")

    print("Escribe el nombre de un proceso para terminarlo: ")
    terminar=input()
    procesoTerminado=False
    for proc in psutil.process_iter():
        if(terminar.lower() == proc.name().lower()):
            procesoTerminado=True
            print("Se va a terminar el proceso ", proc.name(), "con PID:", proc.pid)
            proc.terminate()
    if(procesoTerminado==False):
        print("No se ha encontrado el proceso")

except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
    print("Ha ocurrido un error al acceder al proceso")
