# Proyecto_EDA

## Modo de ejecutar el proyecto 

1. Descargamos el proyeto y lo descomprimimos
2. Abrimos VS code, seleccionamos la carpeta descargada pero tenemos volver a dar doble click y abrir **Proyecto_EDA**

<img width="655" height="459" alt="image" src="https://github.com/user-attachments/assets/df787ce0-d920-4bcd-a6f1-146b14e0db4a" />

3. Para ejecutar el proyecto como un paquete, en la parte izquierda y seleccionar ejecucion y depuracion.

<img width="307" height="294" alt="image" src="https://github.com/user-attachments/assets/4b3fb2eb-7f33-4ed9-bea7-0018e6d30efe" />

4. Damos click en *cree un archivo launch.json* y seleccionamos python debugger, y archivo de python.

<img width="502" height="261" alt="image" src="https://github.com/user-attachments/assets/1777b330-48b2-4140-aa9b-66e2a308426d" 
  
<img width="695" height="226" alt="image" src="https://github.com/user-attachments/assets/48dc11bb-90ab-4787-b12a-ac1b95f0b5c5" />

5. En este archivo tenemos que ingresar el siguiente codigo en en launch.json:
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Proyecto_EDA",
            "type": "debugpy",
            "request": "launch",
            "module": "Presentacion.Principal",
            "cwd": "${workspaceFolder}",
            "console": "integratedTerminal",
            "env": {
                "PYTHONPATH": "${workspaceFolder}"
            }
        }
    ]
}

<img width="638" height="292" alt="image" src="https://github.com/user-attachments/assets/8a47708f-9f4b-4ee9-a889-618086b6419f" />

6. Y ya podriamos ejecutar dando clic en esta en el triangulo verde.
<img width="549" height="274" alt="image" src="https://github.com/user-attachments/assets/29c0b745-975b-4f92-b266-794a35b8c253" />

7. Ejecucion sin problemas
<img width="980" height="632" alt="image" src="https://github.com/user-attachments/assets/25db8357-a285-46f2-b926-3c9c9d2161dc" />

   
La manera de ejecutar el programa debe ser desde el apartado de depuración. Dado que el programa funciona con paquetes es necesario realizarlo de esa manera. Al hacerlo mediante depuracion en la terminal se podra observar. Se realizó el proyecto en el programa "Visual Studio Code". 
