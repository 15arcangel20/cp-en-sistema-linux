#!/bin/bash

# Directorio a monitorear
DIRECTORIO_ORIGEN="/home/arcangel/Escritorio/mio"
# Directorio de destino
DIRECTORIO_DESTINO="/home/arcangel/Escritorio/usb"
# Monitorea el directorio por nuevos archivos
inotifywait -m -r -e create --format '%w%f' "$DIRECTORIO_ORIGEN" | while read NUEVO_ARCHIVO
do
    # Copia el nuevo archivo al directorio de destino
    sudo cp -r "$NUEVO_ARCHIVO" "$DIRECTORIO_DESTINO"
    echo "Archivo copiado: $NUEVO_ARCHIVO"
done
