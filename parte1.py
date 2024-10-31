import psutil

#Se pide al usuario que introduzca procesos que se almacenan en la lista listaProcesos hasta que meta un 0
listaProcesos=[]
print("Escribe una lista de procesos para mostrar informacion sobre ellos, pulsa 0 para cerrar la lista: ")
procesosEntrada= "";

while(procesosEntrada!="0"):
    procesosEntrada=input()
    if procesosEntrada!="0":
        listaProcesos.append(procesosEntrada)

#Se pide al usuario que escriba la palabra clave para filtrar los procesos que ha escrito
print("Escibe una palabra clave para filtrar los procesos que se muestran: ")
palabraClave=input()

#Por cada elemento de la lista se comprueba si existe un proceso activo con el mismo nombre y que contenga la palabra clave
for recLista in listaProcesos:
    try:
        procesoEncontrado=False
        for proc in psutil.process_iter():
            #Solo se muestran los procesos que contengan la palabra clave
            if ((proc.name().lower().__contains__(palabraClave.lower())) & (recLista.lower()==proc.name().lower())) :
                #Cuando cumple los criterios, se almacena la informacion del proceso
                procesoEncontrado=True
                nombreProceso = proc.name()
                pidProceso= proc.pid
                memoria=proc.memory_info().rss/(1024 * 1024)

        #Si se ha encontrado el proceso que busca el usuario, se muestra su informacion
        if(procesoEncontrado==True):
            print("El proceso", nombreProceso, "está activo | PID:", pidProceso, "| Memoria:", memoria, "mb")
        else:
            print("El proceso", recLista, "no está activo")

    except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        print("Ha ocurrido un error al acceder al proceso")
