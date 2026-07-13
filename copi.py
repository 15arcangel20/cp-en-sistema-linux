#!/usr/bin/env python3

import os
import subprocess
import shutil
from pathlib import Path

# Directorios
DIRECTORIO_ORIGEN = "/home/arcangel/Escritorio/mio"
DIRECTORIO_DESTINO = "/home/arcangel/Escritorio/usb"

# Instala inotify-tools si no está instalado
try:
    import inotify_simple
except ImportError:
    print("Instalando inotify-simple...")
    subprocess.check_call(["pip", "install", "inotify-simple"])
    import inotify_simple

# Inicializa el monitor
inotify = inotify_simple.INotify()
watch_descriptor = inotify.add_watch(DIRECTORIO_ORIGEN, inotify_simple.flags.CREATE | inotify_simple.flags.ONLYDIR)

print(f"Monitoreando: {DIRECTORIO_ORIGEN}")

try:
    while True:
        # Espera eventos
        events = inotify.read(timeout=1000)
        
        for event in events:
            # Obtiene la ruta completa del archivo
            nuevo_archivo = os.path.join(DIRECTORIO_ORIGEN, event.name)
            
            try:
                # Copia el archivo
                if os.path.isfile(nuevo_archivo):
                    shutil.copy2(nuevo_archivo, DIRECTORIO_DESTINO)
                elif os.path.isdir(nuevo_archivo):
                    shutil.copytree(nuevo_archivo, os.path.join(DIRECTORIO_DESTINO, event.name))
                
                print(f"Archivo copiado: {nuevo_archivo}")
            
            except Exception as e:
                print(f"Error copiando {nuevo_archivo}: {e}")

except KeyboardInterrupt:
    print("\nMonitoreo detenido.")
finally:
    inotify.rm_watch(watch_descriptor)
