import subprocess
import win32clipboard
import time

p1 = subprocess.Popen('ftp', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

comandos = [b"verbose\n",             # Activa el modo detallado para mostrar más información.
            b"open test.rebex.net\n", # Abre una conexión FTP al servidor 'test.rebex.net'.
            b"demo\n",                # Usuario de prueba para la autenticación.
            b"password\n",            # Contraseña de prueba para la autenticación.
            b"ls\n",                  # Lista los archivos y directorios en el servidor remoto.
            b"get readme.txt\n"]      # Descarga el archivo 'readme.txt' desde el servidor.

# Iteramos sobre cada comando en la lista y lo enviamos al proceso FTP.
for cmd in comandos:
    p1.stdin.write(cmd)  # Escribimos el comando en la entrada estándar del proceso.

p1.communicate(timeout=5)[0]
print("Se ha descargado el archivo")
# Leemos el contenido del archivo y lo copiamos al portapapeles
try:
    with open("readme.txt", "r") as file:
        contenido= file.read()
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(contenido, win32clipboard.CF_UNICODETEXT)
        texto = win32clipboard.GetClipboardData()
        print(texto)
        win32clipboard.CloseClipboard()
    print("Se ha copiado el contenido del archivo al portapapeles")
except FileNotFoundError:
    print("No se ha encontrado el archivo")


#Comprobacion periodica del portapapeles, se va a comprobar 8 veces cada 3 segundos
contenidoActual = ""
for _ in range(8):
    time.sleep(3)
    win32clipboard.OpenClipboard()
    print("Se va a comprobar el contenido del portapapeles")
    nuevoContenido = win32clipboard.GetClipboardData()
    #Se inicializa el contenido
    if contenidoActual == "":
        contenidoActual = nuevoContenido
    #Si el portapapeles cambia, se notifica y se cambia el contenido a comprobar
    if contenidoActual != nuevoContenido:
        print("El contenido del portapapeles ha cambiado, ahora es: ")
        print(nuevoContenido)
        contenidoActual = nuevoContenido
    win32clipboard.CloseClipboard()
    #Cuando se cierra el portapapeles se avisa para que el usuario pueda cambiar el contenido del portapapeles
    print("Tienes dos segundos para cambiar el contenido\n")


