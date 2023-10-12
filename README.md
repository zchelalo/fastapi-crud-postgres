# fastapi-crud-postgres
API REST hecha con FastAPI y PostgreSQL.  

## **Instalación:**  
Para probar la API debe tener instalado python y postgres, una vez con eso listo clone el proyecto:  
```bash  
git clone https://github.com/zchelalo/fastapi-crud-mongo.git  
```  
  
Despues de ello asegurese de estar dentro de la carpeta del proyecto y corra el siguiente comando:  
Para probar la API debe tener instalado python y postgres, una vez con eso listo clone el proyecto:  
```bash  
pip install -r requirements.txt 
```  
  
Es posible que si tiene mas de una versión de python falle y deba correr el siguiente comando en lugar del anterior:  
```bash  
pip3 install -r requirements.txt
``` 
  
Con los requerimientos instalados deberá crear una base de datos en postgres, para despues reemplazar el archivo *.env.example* con sus datos de usuario, y quitarle el *.example*, quedando un archivo parecido a esto:  
```bash  
DBNAME=fastapi_test
USER=postgres
PASSWORD=password
HOST=localhost
PORT=5432
``` 
  
Una vez hecho esto deberá correr el servidor con uvicorn a traves del siguiente comando:  
```bash  
uvicorn app:app
``` 
  
En caso de que quiera hacer un cambio y este se refleje automaticamente en el servidor deberá ejecutar el siguiente comando en lugar del anterior:  
```bash  
uvicorn app:app --reload
``` 
  
Con esto basta con probar la aplicación dirigiendose a cada endpoint con la URL *http://localhost:8000/* en la cual esta alojado nuestro servidor.  
  
## **Documentación:**  
Para poder ver la documentación a la vez que probar la API REST nos podremos dirigir a *http://localhost:8000/docs* una vez que nuestro servidor este activo.  
  
En esta ruta se podrán ver todos los endpoints de la API y podremos probar cada uno de ellos desde ahí mismo, siendo esto muy útil a la hora de testear.  
  
Se utiliza Swagger para documentar la API, de esta forma se ordenan los endpoints en bloques a la misma vez que se documenta su utilidad y funcionamiento.