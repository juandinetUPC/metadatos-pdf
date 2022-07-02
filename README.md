# Extraer metadados de un archivo PDF
## By: Juan Diego Cubillos Maestre
### [Github](https://github.com/juandinetUPC)
### [LinkedIn](https://linkedin.com/in/juan-diego-cubillos-630654195)

## En un entorno virtual usando Python3 , pip y la siguiente lista de dependencias (requirements.txt)
para exportar los requerimientos de la aplicación(sejecuta al final):
```pip freeze > requirements.txt```
- PyMuPDF==1.20.1


Si no está instalado, instalamos virtualenv

```powershell
pip install virtualenv
```

Para crear un ambiente virtual digitamos el siguiente comando:

```powershell
virtualenv -p python3 venv
```

para poner a funcionar el entorno virtual, se debe ejecutar:

```powershell
.\venv\Scripts\activate
```

Una vez iniciado el entorno virtual, se ejecuta el siguiente comando:

```powershell
pip install -r .\requirements.txt
```


Para usar se ejecuta el siguiente comando:

```powershell
python .\pdf.py
```

Y se selecciona el PDF del que se quiere extraer los metadatos.
