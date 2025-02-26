# 📘 FICV1 - Práctica 2 

El repositorio contiene los problemas organizados en módulos de Python. Cada problema puede ejecutarse de manera independiente usando `py -m ProblemaX`. Además, cuenta con un módulo `utils/` que contiene funciones reutilizables.

- Estudiante: **Thomas Emanuel Bermúdez Mora ([Saturnxs](https://github.com/Saturnxs)).**
- Profesor: **Andrés Castro Nuñez**
- Curso: Fisíca I


## 🐍 1. Instalación de Python (omitir si ya tienes Python instalado)

1. Descarga la última versión de Python desde: [https://www.python.org/downloads/](https://www.python.org/downloads/) dando click en el botón Donwload Python 3.13.2.
2. ⚠️ Marca la opción **"Add Python to PATH"**. ⚠️
3. Instala Python con las opciones por defecto.
4. Verifica que Python está instalado correctamente ejecutando en una terminal:
   ```sh
   python --version
   ```
   o:
   ```sh
   py --version
   ```
---

## 📥 2. Descarga del Repositorio

### 🔹 Clonar con Git

Para obtener el código, clona este repositorio desde GitHub en una terminal y descargalo en una carpeta local:

```sh
C:\Users\emabm>cd Documentos
C:\Users\user\Documentos> git clone https://github.com/Saturnxs/FICV1-Practica-2.git
```
En caso de no tener git descargar el código en formato `.zip` desde GitHub y extraelo en una carpeta local.

### 🔹 Navegar al proyecto

Una vez descargado el repositorio navega desde la carpeta local a la carpeta raíz del proyecto:

```sh
C:\Users\user\Documentos> cd FICV1-Practica-2
C:\Users\emabm\Desktop\FICV1-Practica-2>
```

---
## ▶️ 3. Ejecutar los Problemas
Cada problema está en su propia carpeta y se ejecuta con el siguiente comando:

```sh
C:\Users\emabm\Desktop\FICV1-Practica-2> py -m Problema1
```
Los demás problemas se ejecutan de la misma manera, solo cambia el nombre del módulo:

```sh
py -m Problema1  # Ejecutar el problema 1
py -m Problema2  # Ejecutar el problema 2
py -m Problema4  # Ejecutar el problema 4
py -m Problema5  # Ejecutar el problema 5
```

---
## 📂 4. Estructura del Proyecto

```
FICV1-Practica-2/
│── __init__.py  
│── Problema1/
│   ├── __init__.py
│   ├── __main__.py 
│   ├── problema1.py
│   ├── Problema 1.pdf
│── Problema2/
│   ├── __init__.py
│   ├── __main__.py
│   ├── problema2.py
│   ├── Problema 2.pdf
│── Problema4/
│   ├── __init__.py
│   ├── __main__.py
│   ├── problema4.py
│   ├── Problema 4.pdf
│── Problema5/
│   ├── __init__.py
│   ├── __main__.py
│   ├── problema5.py
│   ├── Problema 5.pdf
│── utils/
│   ├── __init__.py
│   ├── conversiones.py
│   ├── formulas.py
```

