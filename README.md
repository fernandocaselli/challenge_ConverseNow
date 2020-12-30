# ConverseNow Challenge
The purpose of this repository is share the code utilized to resolve ConverseNow D.E. Challenge

<b>Pasos en la creación de scripts</b>

1. Instalación de la base de datos NoSQL MongoDB sobre plataforma Windows 10 (podri ser sobre Linux tambien)
2. En el hipotetico caso donde se acabara de crear el dataset, y mediante alguna funcionalidad como la proporcionada por la herramienta cron en Linux o Tareas de Windows    10 corremos el script uploadDS.py, éste carga todo el datatset recien creado en la base de datos conversenow -> collection tabla1
3. Luego corremos el script restapi.py el cual levanta un demonio HTTP y de los cuales solo hacemos uso del verbo GET. La arquitectura de este script esta basada en el      framework MVC Flask y sirve como API para consultas a nuestra base de datos en MongoDB.
4. Para hacer consultas en MongoDB corremos el script connect.py en cual nos trae el primer registro encontrado donde el atributo accent sea mexicano.
