#El codigo se debe ejecutar en online-python.com
import os
import sys

# Se crea la pipe
fd =os.pipe()

# Se crea el mensaje que va a enviar el padre
mensaje = "Soy el padre, le mando este mensaje a mi hijo"

# Se crea el nuevo proceso con fork
pid= os.fork()

# Se comprueba si estamos en el proceso padre o hijo
if pid < 0:
    # Si el pid es menor que 0, significa que ha ocurrido un error al crear el proceso.
    print("No se ha podido crear el proceso hijo")
    # Se sale del programa
    sys.exit(1)

elif pid==0:
    # Si el pid es 0, significa que estamos en el proceso hijo
    # El hijo lee el mensaje del padre
    buffer = os.read(fd[0], 80).decode("utf-8")
    # El hijo acaba de leer, se cierra la lectura
    os.close(fd[0])
    print("El hijo ha recibido el mensaje:", buffer)
    # El hijo modifica el mensaje del padre
    mensaje_modificado = buffer.upper()
    # El hijo escribe el mensaje modificado en el pipe
    os.write(fd[1], mensaje_modificado.encode("utf-8"))
    # El hijo acaba de escribir, se cierra la escritura
    os.close(fd[1])

else:
    # Estamos en el proceso padre
    # El padre escribe el mensaje en la pipe
    os.write(fd[1], mensaje.encode("utf-8"))
    # El padre cierra la escritura
    os.close(fd[1])
    # El padre espera a que el hijo acabe
    os.wait()
    # El padre debe leer la respuesta del hijo
    respuesta = os.read(fd[0], 80).decode("utf-8")
    # El padre acaba de leer, se cierra la lectura
    os.close(fd[0])
    print("El padre lee el mensaje que ha escrito el hijo:", respuesta)