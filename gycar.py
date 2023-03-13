#!/bin/bash

# Crea el archivo de configuración externo y escribe las credenciales de usuario en él
echo "usuario = mi_usuario" > /ruta/hacia/credenciales.cfg
echo "contraseña = mi_contraseña_encriptada" >> /ruta/hacia/credenciales.cfg

# Modifica la configuración de autenticación en el archivo de configuración de GICAR para que use el archivo externo
sed -i 's/tipo = base_de_datos/tipo = archivo_externo/g' /ruta/hacia/archivo_de_configuracion_gicar.cfg
sed -i 's/usuario_bd = nombre_usuario/ruta_archivo = \/ruta\/hacia\/credenciales.cfg/g' /ruta/hacia/archivo_de_configuracion_gicar.cfg

# Reinicia el servidor de GICAR para que los cambios surtan efecto
systemctl restart gicar.service
