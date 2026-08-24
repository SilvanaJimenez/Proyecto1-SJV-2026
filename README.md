# Proyecto 1 - Aplicación en Streamlit

Especialización en Python for Analytics
Módulo 1 - Python Fundamentals

Estudiante: Silvana Melissa Jiménez Vargas
Año: 2026

Aplicación interactiva que reúne los temas revisados en el Módulo 1: variables,
estructuras de datos, control de flujo, funciones y programación orientada a objetos.

## Enlaces

- Repositorio: https://github.com/SilvanaJimenez/Proyecto1-SJV-2026
- Aplicación publicada: https://proyecto1-sjv-2026.streamlit.app

## Secciones

La navegación se hace desde el menú lateral con `st.sidebar.selectbox()`.

- **Home**: presentación del proyecto, datos del estudiante y tecnologías utilizadas.
- **Ejercicio 1**: flujo de caja con listas. Registra movimientos de ingreso y gasto,
  calcula los totales y el saldo final, e indica si el flujo está a favor o en contra.
- **Ejercicio 2**: registro de productos en arrays de NumPy, que luego se convierten
  en un DataFrame de Pandas actualizado en pantalla.
- **Ejercicio 3**: uso de funciones del archivo `libreria_funciones_proyecto1.py`.
  Se trabajó con el área de Productividad y Operaciones, con las funciones
  `calcular_productividad_laboral()` y `calcular_costo_unitario_total()`, y un
  histórico de resultados.
- **Ejercicio 4**: uso de la clase `EquipoMantenimiento` del archivo
  `libreria_clases_proyecto1.py`, con las operaciones CRUD (crear, leer,
  actualizar y eliminar).

## Archivos

- `app.py` - aplicación principal
- `libreria_funciones_proyecto1.py` - librería de funciones
- `libreria_clases_proyecto1.py` - librería de clases
- `requirements.txt` - dependencias
- `Python_logo.png` - imagen usada en la sección Home

## Ejecución local

```
pip install -r requirements.txt
streamlit run app.py
```

## Tecnologías

Python 3, Streamlit, Pandas, NumPy, GitHub y Streamlit Cloud.
