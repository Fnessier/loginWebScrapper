# Login Webscrapper

**Descripción :**

Breve script de logeo en plataforma de reservas de conocido consulado internacional.
El proyecto intenta automatizar el logeo e intento de reserva en busqueda de posibles turnos fortuitos.
De todas maneras, resulta adaptable para diferentes plataformas para uso personal como posbile testeo de calidad con manejo de errores.
Gracias por revisar mi repositorio, si tienen cualquier duda o contribucion no dudes en contactarme

https://www.linkedin.com/in/francisco-nessier/


**Tabla de contenidos:**

* **Instalación**
* **Uso**
* **Licencia**

## Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone [se quitó una URL no válida]

correr el archivo install.bat para instalar las dependencias en el entorno virtual loginEnv que generara automaticamente.

##  Uso

El archivo de logeo es facilmente configurable en tanto se modifique el URL de pagina de ingreso y posteriormente se identifique el ID de los campos a completar con las credenciales de acceso.
Cambiar las credenciales dentro de scriptLogin.py por la credenciales de usuario.
En caso de preferir que el navegador no se abra en la pantalla cambiar la linea comentada en #Inicializar Navegador

Guardar cambios y correr el archivo logincmd.bat desde la carpeta de proyecto.

El archivo automatizacion.log se genera automaticamente y guardo todos los eventos del programa.

##  Licencia

Este proyecto está licenciado bajo la licencia MIT. Para más detalles, consulta el archivo LICENSE.