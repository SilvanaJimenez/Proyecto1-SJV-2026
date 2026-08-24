
import os

import streamlit as st
import pandas as pd
import numpy as np

import libreria_funciones_proyecto1 as lf
import libreria_clases_proyecto1 as lc


# DATOS DE PANTALLA PRINCIPAL
NOMBRE_ESTUDIANTE = "Silvana Melissa Jiménez Vargas"
MODULO = "Módulo 1 - Python Fundamentals"
CURSO = "Especialización en Python for Analytics"
DOCENTE = "Ing. Carlos Carrillo Villavicencio MSc. TIC"
ANIO = "2026"
LOGO = "Python_logo.png"


st.set_page_config(page_title="Proyecto 1 - Python Fundamentals", layout="wide")


# VARIABLES
if "movimientos" not in st.session_state:
    st.session_state.movimientos = []

if "arr_producto" not in st.session_state:
    st.session_state.arr_producto = np.array([], dtype=object)
    st.session_state.arr_categoria = np.array([], dtype=object)
    st.session_state.arr_precio = np.array([], dtype=float)
    st.session_state.arr_cantidad = np.array([], dtype=int)

if "historico_funciones" not in st.session_state:
    st.session_state.historico_funciones = []

if "equipos" not in st.session_state:
    st.session_state.equipos = []


# MENU LATERAL
st.sidebar.title("Proyecto 1")
st.sidebar.write(NOMBRE_ESTUDIANTE)

seccion = st.sidebar.selectbox(
    "Selecciona una sección:",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"],
)


# HOME

if seccion == "Home":

    st.title("Proyecto Aplicado en Streamlit")
    st.subheader("Fundamentos de Programación en Python")

    st.write(f"Elaborado por: {NOMBRE_ESTUDIANTE}")

    if os.path.exists(LOGO):
        st.image(LOGO, width=320)

    st.write(f"**Módulo:** {MODULO}")
    st.write(f"**Curso:** {CURSO}")
    st.write(f"**Docente:** {DOCENTE}")
    st.write(f"**Año:** {ANIO}")

    st.markdown("---")

    st.subheader("Descripción del proyecto")
    st.markdown(
        """
        Aplicación interactiva que reúne los temas revisados en el Módulo 1:
        variables, estructuras de datos, control de flujo, funciones y
        programación orientada a objetos.

        Está dividida en cuatro ejercicios que se abren desde el menú lateral:

        1. Flujo de caja con listas.
        2. Registro de productos con arrays de NumPy y DataFrame.
        3. Funciones traídas desde una librería externa.
        4. Clase con operaciones CRUD.
        """
    )

    st.subheader("Tecnologías utilizadas")
    st.markdown(
        """
        - Python 3
        - Streamlit
        - Pandas
        - NumPy
        - GitHub y Streamlit Cloud
        """
    )


# EJERCICIO 1 - Flujo de caja con listas

elif seccion == "Ejercicio 1":

    st.title("Ejercicio 1 - Flujo de caja con listas")

    st.markdown(
        "Los movimientos se guardan en una lista. Para cada uno se registra el "
        "concepto, el tipo (ingreso o gasto) y el valor. Al final se calculan los "
        "totales y se indica si el flujo de caja está a favor o en contra."
    )

    st.subheader("Registrar movimiento")

    col1, col2, col3 = st.columns(3)
    concepto = col1.text_input("Concepto:")
    tipo = col2.selectbox("Tipo de movimiento:", ["Ingreso", "Gasto"])
    valor = col3.number_input("Valor (S/):", min_value=0.0, step=10.0, format="%.2f")

    col_a, col_b = st.columns(2)

    if col_a.button("Agregar movimiento", use_container_width=True):
        if concepto.strip() == "":
            st.error("Debes ingresar un concepto.")
        elif valor <= 0:
            st.error("El valor debe ser mayor que cero.")
        else:
            st.session_state.movimientos.append(
                {"Concepto": concepto.strip(), "Tipo": tipo, "Valor": float(valor)}
            )
            st.success("Movimiento agregado.")

    if col_b.button("Limpiar movimientos", use_container_width=True):
        st.session_state.movimientos = []

    st.markdown("---")
    st.subheader("Movimientos registrados")

    if len(st.session_state.movimientos) == 0:
        st.info("Todavía no hay movimientos registrados.")
    else:
        st.dataframe(pd.DataFrame(st.session_state.movimientos), use_container_width=True)

        total_ingresos = 0
        total_gastos = 0

        for movimiento in st.session_state.movimientos:
            if movimiento["Tipo"] == "Ingreso":
                total_ingresos = total_ingresos + movimiento["Valor"]
            else:
                total_gastos = total_gastos + movimiento["Valor"]

        saldo_final = total_ingresos - total_gastos

        col1, col2, col3 = st.columns(3)
        col1.metric("Total ingresos", f"S/ {total_ingresos:,.2f}")
        col2.metric("Total gastos", f"S/ {total_gastos:,.2f}")
        col3.metric("Saldo final", f"S/ {saldo_final:,.2f}")

        if saldo_final > 0:
            st.success(f"El flujo de caja está a favor con S/ {saldo_final:,.2f}")
        elif saldo_final < 0:
            st.error(f"El flujo de caja está en contra con S/ {abs(saldo_final):,.2f}")
        else:
            st.warning("Los ingresos son iguales a los gastos.")


# EJERCICIO 2 - Registro con NumPy y DataFrame

elif seccion == "Ejercicio 2":

    st.title("Ejercicio 2 - Registro con NumPy, arrays y DataFrame")

    st.markdown(
        "Cada dato del producto se guarda en un array de NumPy distinto. El total "
        "se calcula multiplicando los arrays de precio y cantidad, y luego todos "
        "se unen en un DataFrame que se actualiza en pantalla."
    )

    st.subheader("Registrar producto")

    col1, col2 = st.columns(2)
    nombre_producto = col1.text_input("Nombre del producto:")
    categoria = col1.selectbox(
        "Categoría:",
        ["Repuestos", "Insumos", "Herramientas", "Lubricantes", "Equipos de protección"],
    )
    precio = col2.number_input("Precio unitario (S/):", min_value=0.0, step=1.0, format="%.2f")
    cantidad = col2.number_input("Cantidad:", min_value=0, step=1)

    col_a, col_b = st.columns(2)

    if col_a.button("Agregar registro", use_container_width=True):
        if nombre_producto.strip() == "":
            st.error("Debes ingresar el nombre del producto.")
        elif precio <= 0 or cantidad <= 0:
            st.error("El precio y la cantidad deben ser mayores que cero.")
        else:
            st.session_state.arr_producto = np.append(
                st.session_state.arr_producto, nombre_producto.strip()
            )
            st.session_state.arr_categoria = np.append(st.session_state.arr_categoria, categoria)
            st.session_state.arr_precio = np.append(st.session_state.arr_precio, float(precio))
            st.session_state.arr_cantidad = np.append(st.session_state.arr_cantidad, int(cantidad))
            st.success("Producto agregado.")

    if col_b.button("Limpiar registros", use_container_width=True):
        st.session_state.arr_producto = np.array([], dtype=object)
        st.session_state.arr_categoria = np.array([], dtype=object)
        st.session_state.arr_precio = np.array([], dtype=float)
        st.session_state.arr_cantidad = np.array([], dtype=int)

    st.markdown("---")
    st.subheader("Registros almacenados")

    if st.session_state.arr_producto.size == 0:
        st.info("Todavía no hay productos registrados.")
    else:
        arr_total = st.session_state.arr_precio * st.session_state.arr_cantidad

        df_productos = pd.DataFrame(
            {
                "Producto": st.session_state.arr_producto,
                "Categoría": st.session_state.arr_categoria,
                "Precio": st.session_state.arr_precio,
                "Cantidad": st.session_state.arr_cantidad,
                "Total": arr_total,
            }
        )

        st.dataframe(df_productos, use_container_width=True)

        col1, col2, col3 = st.columns(3)
        col1.metric("Registros", int(st.session_state.arr_producto.size))
        col2.metric("Valor total", f"S/ {np.sum(arr_total):,.2f}")
        col3.metric("Precio promedio", f"S/ {np.mean(st.session_state.arr_precio):,.2f}")


# EJERCICIO 3 - Funciones desde una librería externa

elif seccion == "Ejercicio 3":

    st.title("Ejercicio 3 - Uso de funciones desde una librería externa")

    st.markdown(
        "Del archivo `libreria_funciones_proyecto1.py` se trabajó con el área de "
        "Productividad y Operaciones, que corresponde a mi campo laboral. El "
        "selector permite elegir entre las dos funciones de esa área y cada "
        "resultado se guarda en un histórico."
    )

    funcion = st.selectbox(
        "Selecciona la función:",
        [
            "calcular_productividad_laboral",
            "calcular_costo_unitario_total",
        ],
    )

    st.subheader("Parámetros")

    resultado = None

    if funcion == "calcular_productividad_laboral":
        col1, col2, col3 = st.columns(3)
        unidades_producidas = col1.number_input("Unidades producidas:", 0.0, value=1200.0, step=10.0)
        horas_trabajadas = col2.number_input("Horas trabajadas:", 0.0, value=160.0, step=1.0)
        numero_trabajadores = col3.number_input("Número de trabajadores:", 0, value=5, step=1)

        if st.button("Ejecutar", use_container_width=True):
            try:
                resultado = lf.calcular_productividad_laboral(
                    unidades_producidas, horas_trabajadas, numero_trabajadores
                )
                col1, col2 = st.columns(2)
                col1.metric("Productividad por hora", resultado["productividad_por_hora"])
                col2.metric("Productividad por trabajador", resultado["productividad_por_trabajador"])
            except ValueError as error:
                st.error(error)

    else:
        col1, col2 = st.columns(2)
        materiales = col1.number_input("Materiales (S/):", 0.0, value=8000.0, step=100.0)
        mano_obra = col2.number_input("Mano de obra (S/):", 0.0, value=5000.0, step=100.0)
        col3, col4 = st.columns(2)
        costos_indirectos = col3.number_input("Costos indirectos (S/):", 0.0, value=2000.0, step=100.0)
        unidades = col4.number_input("Unidades producidas:", 0.0, value=1200.0, step=10.0)

        if st.button("Ejecutar", use_container_width=True):
            try:
                resultado = lf.calcular_costo_unitario_total(
                    materiales, mano_obra, costos_indirectos, unidades
                )
                col1, col2 = st.columns(2)
                col1.metric("Costo total", f"S/ {resultado['costo_total']:,.2f}")
                col2.metric("Costo unitario", f"S/ {resultado['costo_unitario']:,.2f}")
            except ValueError as error:
                st.error(error)

    if resultado is not None:
        registro = {"Función": funcion}
        registro.update(resultado)
        st.session_state.historico_funciones.append(registro)

    st.markdown("---")
    st.subheader("Histórico de resultados")

    if len(st.session_state.historico_funciones) == 0:
        st.info("Todavía no se ha ejecutado ninguna función.")
    else:
        df_historico = pd.DataFrame(st.session_state.historico_funciones)
        st.dataframe(df_historico.fillna("-"), use_container_width=True)

        if st.button("Limpiar histórico"):
            st.session_state.historico_funciones = []


# EJERCICIO 4 - Clase con CRUD

elif seccion == "Ejercicio 4":

    st.title("Ejercicio 4 - Clase EquipoMantenimiento con CRUD")

    st.markdown(
        "Del archivo `libreria_clases_proyecto1.py` se eligió la clase "
        "`EquipoMantenimiento`. Cada equipo registrado se convierte en un objeto "
        "de esa clase, que calcula el MTBF, el MTTR y la disponibilidad. Las "
        "pestañas corresponden a las operaciones crear, leer, actualizar y eliminar."
    )

    tab_crear, tab_leer, tab_actualizar, tab_eliminar = st.tabs(
        ["Crear", "Leer", "Actualizar", "Eliminar"]
    )

    with tab_crear:
        st.subheader("Registrar equipo")

        nombre_equipo = st.text_input("Nombre del equipo:", key="crear_nombre")
        col1, col2, col3 = st.columns(3)
        horas_operacion = col1.number_input("Horas de operación:", 0.0, value=720.0, step=1.0, key="crear_horas")
        numero_fallas = col2.number_input("Número de fallas:", 0, value=3, step=1, key="crear_fallas")
        horas_reparacion = col3.number_input("Horas de reparación:", 0.0, value=9.0, step=0.5, key="crear_reparacion")

        if st.button("Guardar", use_container_width=True):
            nombres_registrados = [e["nombre_equipo"] for e in st.session_state.equipos]

            if nombre_equipo.strip() == "":
                st.error("Debes ingresar el nombre del equipo.")
            elif nombre_equipo.strip() in nombres_registrados:
                st.error("Ya existe un equipo con ese nombre.")
            else:
                try:
                    equipo = lc.EquipoMantenimiento(
                        nombre_equipo.strip(), horas_operacion, numero_fallas, horas_reparacion
                    )
                    st.session_state.equipos.append(
                        {
                            "nombre_equipo": equipo.nombre_equipo,
                            "horas_operacion": equipo.horas_operacion,
                            "numero_fallas": equipo.numero_fallas,
                            "horas_reparacion": equipo.horas_reparacion,
                        }
                    )
                    st.success("Equipo registrado.")
                except ValueError as error:
                    st.error(error)

    with tab_leer:
        st.subheader("Equipos registrados")

        if len(st.session_state.equipos) == 0:
            st.info("Todavía no hay equipos registrados.")
        else:
            filas = []

            for datos in st.session_state.equipos:
                equipo = lc.EquipoMantenimiento(**datos)
                resumen = equipo.resumen()
                filas.append(
                    {
                        "Equipo": resumen["equipo"],
                        "Horas operación": datos["horas_operacion"],
                        "Fallas": datos["numero_fallas"],
                        "Horas reparación": datos["horas_reparacion"],
                        "MTBF (h)": resumen["mtbf_h"],
                        "MTTR (h)": resumen["mttr_h"],
                        "Disponibilidad (%)": resumen["disponibilidad_pct"],
                    }
                )

            st.dataframe(pd.DataFrame(filas), use_container_width=True)

    with tab_actualizar:
        st.subheader("Actualizar equipo")

        if len(st.session_state.equipos) == 0:
            st.info("No hay equipos para actualizar.")
        else:
            nombres = [e["nombre_equipo"] for e in st.session_state.equipos]
            seleccionado = st.selectbox("Equipo:", nombres, key="actualizar_sel")
            posicion = nombres.index(seleccionado)
            datos_actuales = st.session_state.equipos[posicion]

            col1, col2, col3 = st.columns(3)
            nuevas_horas = col1.number_input(
                "Horas de operación:", 0.0,
                value=float(datos_actuales["horas_operacion"]), step=1.0, key="actualizar_horas",
            )
            nuevas_fallas = col2.number_input(
                "Número de fallas:", 0,
                value=int(datos_actuales["numero_fallas"]), step=1, key="actualizar_fallas",
            )
            nuevas_reparaciones = col3.number_input(
                "Horas de reparación:", 0.0,
                value=float(datos_actuales["horas_reparacion"]), step=0.5, key="actualizar_reparacion",
            )

            if st.button("Actualizar", use_container_width=True):
                try:
                    lc.EquipoMantenimiento(
                        seleccionado, nuevas_horas, nuevas_fallas, nuevas_reparaciones
                    )
                    st.session_state.equipos[posicion] = {
                        "nombre_equipo": seleccionado,
                        "horas_operacion": nuevas_horas,
                        "numero_fallas": nuevas_fallas,
                        "horas_reparacion": nuevas_reparaciones,
                    }
                    st.success("Equipo actualizado.")
                except ValueError as error:
                    st.error(error)

    with tab_eliminar:
        st.subheader("Eliminar equipo")

        if len(st.session_state.equipos) == 0:
            st.info("No hay equipos para eliminar.")
        else:
            nombres = [e["nombre_equipo"] for e in st.session_state.equipos]
            a_eliminar = st.selectbox("Equipo:", nombres, key="eliminar_sel")

            if st.button("Eliminar", use_container_width=True):
                nuevos = []
                for equipo in st.session_state.equipos:
                    if equipo["nombre_equipo"] != a_eliminar:
                        nuevos.append(equipo)
                st.session_state.equipos = nuevos
                st.success("Equipo eliminado.")
