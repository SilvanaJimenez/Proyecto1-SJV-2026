"""
=====================================================================
PROYECTO 1 - APLICACION EN STREAMLIT
Especializacion en Python for Analytics
Modulo 1 - Python Fundamentals
=====================================================================
Ejecutar localmente con:   streamlit run app.py
=====================================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import os

# Librerias externas entregadas por el docente
import libreria_funciones_proyecto1 as lf
import libreria_clases_proyecto1 as lc


# =====================================================================
# >>> DATOS DEL ESTUDIANTE  ---  CAMBIA ESTOS VALORES POR LOS TUYOS <<<
# =====================================================================
NOMBRE_ESTUDIANTE = "Silvana Melissa Jiménez Vargas"
MODULO = "Modulo 1 - Python Fundamentals"
CURSO = "Especializacion en Python for Analytics"
ANIO = "2026"
AREA = "Operaciones / Produccion / TI"
DOCENTE = "Ing. Carlos Carrillo Villavicencio MSc. TIC"
LOGO = "Python_logo.png"   # debe coincidir EXACTO con el nombre del archivo de imagen


# =====================================================================
# CONFIGURACION GENERAL DE LA PAGINA
# =====================================================================
st.set_page_config(
    page_title="Proyecto 1 - Python Fundamentals",
    page_icon="🐍",
    layout="wide",
)


# =====================================================================
# INICIALIZACION DE session_state (conserva los datos entre recargas)
# =====================================================================
def inicializar_estado():
    # Ejercicio 1 -> lista de movimientos
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    # Ejercicio 2 -> arrays de NumPy
    if "arr_producto" not in st.session_state:
        st.session_state.arr_producto = np.array([], dtype=object)
        st.session_state.arr_categoria = np.array([], dtype=object)
        st.session_state.arr_precio = np.array([], dtype=float)
        st.session_state.arr_cantidad = np.array([], dtype=int)

    # Ejercicio 3 -> historico de resultados
    if "historico_funciones" not in st.session_state:
        st.session_state.historico_funciones = []

    # Ejercicio 4 -> registros CRUD
    if "equipos" not in st.session_state:
        st.session_state.equipos = []


inicializar_estado()


# =====================================================================
# MENU LATERAL DE NAVEGACION
# =====================================================================
st.sidebar.title("📊 Proyecto 1")
st.sidebar.markdown(f"**{NOMBRE_ESTUDIANTE}**")
st.sidebar.markdown("---")

seccion = st.sidebar.selectbox(
    "Selecciona una seccion:",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"],
)

st.sidebar.markdown("---")
st.sidebar.caption(f"{CURSO} · {ANIO}")


# =====================================================================
# 1. HOME
# =====================================================================
if seccion == "Home":

    col1, col2 = st.columns([1, 3])

    with col1:
        if os.path.exists(LOGO):
            st.image(LOGO, width=180)
        else:
            st.markdown("<div style='font-size:110px; text-align:center'>🐍</div>",
                        unsafe_allow_html=True)

    with col2:
        st.title("Proyecto Aplicado en Streamlit")
        st.subheader("Fundamentos de Programacion en Python")
        st.write(f"**Estudiante:** {NOMBRE_ESTUDIANTE}")
        st.write(f"**Modulo:** {MODULO}")
        st.write(f"**Curso:** {CURSO}")
        st.write(f"**Area de aplicacion:** {AREA}")
        st.write(f"**Docente:** {DOCENTE}")
        st.write(f"**Año:** {ANIO}")

    st.markdown("---")

    st.markdown("### 📝 Descripcion del proyecto")
    st.markdown(
        """
        Esta aplicacion interactiva integra los conceptos fundamentales revisados
        durante el **Modulo 1 - Python Fundamentals**: variables, estructuras de
        datos, control de flujo, funciones, programacion funcional y programacion
        orientada a objetos (POO).

        La app esta organizada en cuatro ejercicios, accesibles desde el menu lateral:

        1. **Ejercicio 1 - Flujo de caja con listas:** registro de movimientos
           financieros (ingresos y gastos) almacenados en una lista, con calculo
           automatico de totales y saldo final.
        2. **Ejercicio 2 - Registro con NumPy:** captura de productos mediante
           widgets, almacenamiento en arreglos de NumPy y visualizacion en un
           DataFrame de Pandas.
        3. **Ejercicio 3 - Funciones desde libreria externa:** conexion de widgets
           con funciones del archivo `libreria_funciones_proyecto1.py`, orientadas
           al area de operaciones y mantenimiento, con historico de resultados.
        4. **Ejercicio 4 - Clases con CRUD:** uso de la clase `EquipoMantenimiento`
           del archivo `libreria_clases_proyecto1.py` con operaciones de Crear,
           Leer, Actualizar y Eliminar.
        """
    )

    st.markdown("### 🛠️ Tecnologias utilizadas")
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.info("**Python 3**")
    c2.info("**Streamlit**")
    c3.info("**Pandas**")
    c4.info("**NumPy**")
    c5.info("**GitHub**")

    st.markdown("---")
    st.success("Usa el menu lateral izquierdo para navegar entre los ejercicios.")


# =====================================================================
# 2. EJERCICIO 1 - FLUJO DE CAJA CON LISTAS
# =====================================================================
elif seccion == "Ejercicio 1":

    st.title("Ejercicio 1 - Flujo de caja con listas")

    st.markdown(
        """
        En este ejercicio se registran **movimientos financieros** dentro de una
        **lista vacia**. Cada movimiento guarda un *concepto*, un *tipo de
        movimiento* (Ingreso o Gasto) y un *valor*.

        Al presionar el boton **Agregar movimiento**, el registro se añade a la
        lista y la aplicacion recalcula el total de ingresos, el total de gastos,
        el saldo final e indica si el flujo de caja esta **a favor** o **en contra**.
        """
    )

    st.markdown("---")
    st.subheader("Registrar movimiento")

    col1, col2, col3 = st.columns(3)

    with col1:
        concepto = st.text_input("Concepto:", placeholder="Ej: Venta de repuestos")
    with col2:
        tipo = st.selectbox("Tipo de movimiento:", ["Ingreso", "Gasto"])
    with col3:
        valor = st.number_input("Valor (S/):", min_value=0.0, step=10.0, format="%.2f")

    col_a, col_b = st.columns([1, 1])

    with col_a:
        if st.button("➕ Agregar movimiento", use_container_width=True):
            # Validacion de entradas antes de agregar
            if concepto.strip() == "":
                st.error("Debes ingresar un concepto.")
            elif valor <= 0:
                st.error("El valor debe ser mayor que cero.")
            else:
                st.session_state.movimientos.append(
                    {"Concepto": concepto.strip(), "Tipo": tipo, "Valor": float(valor)}
                )
                st.success(f"Movimiento '{concepto.strip()}' agregado correctamente.")

    with col_b:
        if st.button("🗑️ Limpiar todos los movimientos", use_container_width=True):
            st.session_state.movimientos = []
            st.warning("Se eliminaron todos los movimientos.")

    st.markdown("---")
    st.subheader("Movimientos registrados")

    if len(st.session_state.movimientos) == 0:
        st.info("Aun no hay movimientos registrados. Agrega el primero con el formulario de arriba.")
    else:
        df_mov = pd.DataFrame(st.session_state.movimientos)
        st.dataframe(df_mov, use_container_width=True)

        # ---- Calculos con control de flujo y listas ----
        total_ingresos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Ingreso")
        total_gastos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Gasto")
        saldo_final = total_ingresos - total_gastos

        st.markdown("### Resultado del flujo de caja")
        m1, m2, m3 = st.columns(3)
        m1.metric("Total ingresos", f"S/ {total_ingresos:,.2f}")
        m2.metric("Total gastos", f"S/ {total_gastos:,.2f}")
        m3.metric("Saldo final", f"S/ {saldo_final:,.2f}", delta=f"{saldo_final:,.2f}")

        if saldo_final > 0:
            st.success(f"✅ El flujo de caja esta A FAVOR con un saldo de S/ {saldo_final:,.2f}")
        elif saldo_final < 0:
            st.error(f"❌ El flujo de caja esta EN CONTRA con un deficit de S/ {abs(saldo_final):,.2f}")
        else:
            st.warning("⚖️ El flujo de caja esta EQUILIBRADO: los ingresos igualan a los gastos.")


# =====================================================================
# 3. EJERCICIO 2 - REGISTRO CON NUMPY, ARRAYS Y DATAFRAME
# =====================================================================
elif seccion == "Ejercicio 2":

    st.title("Ejercicio 2 - Registro con NumPy, arrays y DataFrame")

    st.markdown(
        """
        En este ejercicio se registran **productos** mediante widgets. Cada dato
        se almacena en un **arreglo de NumPy** independiente (`np.append`) y luego
        todos los arrays se combinan en un **DataFrame de Pandas** que se muestra
        actualizado en pantalla.

        El campo *total* se calcula de forma **vectorizada** con NumPy:
        `total = precio * cantidad`.
        """
    )

    st.markdown("---")
    st.subheader("Registrar producto")

    col1, col2 = st.columns(2)
    with col1:
        nombre_prod = st.text_input("Nombre del producto:", placeholder="Ej: Rodamiento 6205")
        categoria = st.selectbox(
            "Categoria:",
            ["Repuestos", "Insumos", "Herramientas", "Lubricantes", "Equipos de proteccion"],
        )
    with col2:
        precio = st.number_input("Precio unitario (S/):", min_value=0.0, step=1.0, format="%.2f")
        cantidad = st.number_input("Cantidad:", min_value=0, step=1)

    col_a, col_b = st.columns([1, 1])

    with col_a:
        if st.button("➕ Agregar registro", use_container_width=True):
            if nombre_prod.strip() == "":
                st.error("Debes ingresar el nombre del producto.")
            elif precio <= 0 or cantidad <= 0:
                st.error("El precio y la cantidad deben ser mayores que cero.")
            else:
                st.session_state.arr_producto = np.append(st.session_state.arr_producto, nombre_prod.strip())
                st.session_state.arr_categoria = np.append(st.session_state.arr_categoria, categoria)
                st.session_state.arr_precio = np.append(st.session_state.arr_precio, float(precio))
                st.session_state.arr_cantidad = np.append(st.session_state.arr_cantidad, int(cantidad))
                st.success(f"Producto '{nombre_prod.strip()}' agregado al array.")

    with col_b:
        if st.button("🗑️ Limpiar registros", use_container_width=True):
            st.session_state.arr_producto = np.array([], dtype=object)
            st.session_state.arr_categoria = np.array([], dtype=object)
            st.session_state.arr_precio = np.array([], dtype=float)
            st.session_state.arr_cantidad = np.array([], dtype=int)
            st.warning("Se eliminaron todos los registros.")

    st.markdown("---")
    st.subheader("Tabla de registros (DataFrame)")

    if st.session_state.arr_producto.size == 0:
        st.info("Aun no hay productos registrados.")
    else:
        # Operacion vectorizada con NumPy
        arr_total = st.session_state.arr_precio * st.session_state.arr_cantidad

        df_prod = pd.DataFrame(
            {
                "Producto": st.session_state.arr_producto,
                "Categoria": st.session_state.arr_categoria,
                "Precio": st.session_state.arr_precio,
                "Cantidad": st.session_state.arr_cantidad,
                "Total": arr_total,
            }
        )
        st.dataframe(df_prod, use_container_width=True)

        st.markdown("### Estadisticas calculadas con NumPy")
        e1, e2, e3, e4 = st.columns(4)
        e1.metric("Registros", int(st.session_state.arr_producto.size))
        e2.metric("Valor total", f"S/ {np.sum(arr_total):,.2f}")
        e3.metric("Precio promedio", f"S/ {np.mean(st.session_state.arr_precio):,.2f}")
        e4.metric("Precio maximo", f"S/ {np.max(st.session_state.arr_precio):,.2f}")

        st.markdown("### Valor total por categoria")
        st.bar_chart(df_prod.groupby("Categoria")["Total"].sum())


# =====================================================================
# 4. EJERCICIO 3 - FUNCIONES DESDE LIBRERIA EXTERNA
# =====================================================================
elif seccion == "Ejercicio 3":

    st.title("Ejercicio 3 - Uso de funciones desde una libreria externa")

    st.markdown(
        """
        Este ejercicio conecta widgets de Streamlit con funciones del archivo
        **`libreria_funciones_proyecto1.py`**. Las funciones seleccionadas
        corresponden al area de **Operaciones, Mantenimiento y TI**:

        - `calcular_oee()` - Eficiencia General de los Equipos (OEE)
        - `calcular_indicadores_mantenimiento()` - MTBF, MTTR y disponibilidad
        - `calcular_disponibilidad_sistema()` - disponibilidad de un sistema

        Cada ejecucion se guarda en un **historico** mostrado como DataFrame.
        """
    )

    st.markdown("---")

    funcion = st.selectbox(
        "Selecciona la funcion a ejecutar:",
        [
            "calcular_oee - Eficiencia General de los Equipos",
            "calcular_indicadores_mantenimiento - MTBF / MTTR",
            "calcular_disponibilidad_sistema - Disponibilidad",
        ],
    )

    st.subheader("Parametros de entrada")

    resultado = None
    etiqueta = ""

    # ---------- Funcion 1: OEE ----------
    if funcion.startswith("calcular_oee"):
        st.caption("OEE = Disponibilidad x Rendimiento x Calidad")
        c1, c2, c3 = st.columns(3)
        disponibilidad_pct = c1.number_input("Disponibilidad (%):", 0.0, 100.0, 90.0, 0.1)
        rendimiento_pct = c2.number_input("Rendimiento (%):", 0.0, 100.0, 95.0, 0.1)
        calidad_pct = c3.number_input("Calidad (%):", 0.0, 100.0, 99.0, 0.1)

        if st.button("▶️ Ejecutar funcion", use_container_width=True):
            try:
                resultado = lf.calcular_oee(disponibilidad_pct, rendimiento_pct, calidad_pct)
                etiqueta = "calcular_oee"
                st.success("Funcion ejecutada correctamente.")
                st.metric("OEE", f"{resultado['oee_pct']} %")
                oee = resultado["oee_pct"]
                if oee >= 85:
                    st.success("Clase mundial: el proceso opera a un nivel excelente.")
                elif oee >= 60:
                    st.warning("Nivel aceptable, con oportunidades de mejora.")
                else:
                    st.error("Nivel bajo: se recomienda revisar el proceso.")
                st.write(resultado)
            except ValueError as e:
                st.error(f"Error de validacion: {e}")

    # ---------- Funcion 2: Indicadores de mantenimiento ----------
    elif funcion.startswith("calcular_indicadores_mantenimiento"):
        st.caption("MTBF = horas de operacion / fallas   |   MTTR = horas de reparacion / fallas")
        c1, c2, c3 = st.columns(3)
        tiempo_operacion_h = c1.number_input("Tiempo de operacion (h):", 0.0, value=720.0, step=1.0)
        numero_fallas = c2.number_input("Numero de fallas:", 0, value=4, step=1)
        tiempo_reparacion_total_h = c3.number_input("Tiempo total de reparacion (h):", 0.0, value=12.0, step=0.5)

        if st.button("▶️ Ejecutar funcion", use_container_width=True):
            try:
                resultado = lf.calcular_indicadores_mantenimiento(
                    tiempo_operacion_h, numero_fallas, tiempo_reparacion_total_h
                )
                etiqueta = "calcular_indicadores_mantenimiento"
                st.success("Funcion ejecutada correctamente.")
                m1, m2, m3 = st.columns(3)
                m1.metric("MTBF", f"{resultado['mtbf_h']} h")
                m2.metric("MTTR", f"{resultado['mttr_h']} h")
                m3.metric("Disponibilidad", f"{resultado['disponibilidad_pct']} %")
                st.write(resultado)
            except ValueError as e:
                st.error(f"Error de validacion: {e}")

    # ---------- Funcion 3: Disponibilidad del sistema ----------
    else:
        st.caption("Disponibilidad = ((tiempo total - tiempo de caida) / tiempo total) x 100")
        c1, c2 = st.columns(2)
        tiempo_total_horas = c1.number_input("Tiempo total (h):", 0.0, value=730.0, step=1.0)
        tiempo_caida_horas = c2.number_input("Tiempo de caida (h):", 0.0, value=5.0, step=0.5)

        if st.button("▶️ Ejecutar funcion", use_container_width=True):
            try:
                resultado = lf.calcular_disponibilidad_sistema(tiempo_total_horas, tiempo_caida_horas)
                etiqueta = "calcular_disponibilidad_sistema"
                st.success("Funcion ejecutada correctamente.")
                st.metric("Disponibilidad del sistema", f"{resultado['disponibilidad_pct']} %")
                st.write(resultado)
            except ValueError as e:
                st.error(f"Error de validacion: {e}")

    # ---------- Guardar en el historico ----------
    if resultado is not None:
        registro = {"Funcion": etiqueta}
        registro.update({k: v for k, v in resultado.items()})
        st.session_state.historico_funciones.append(registro)

    st.markdown("---")
    st.subheader("Historico de resultados")

    if len(st.session_state.historico_funciones) == 0:
        st.info("Aun no se ha ejecutado ninguna funcion.")
    else:
        df_hist = pd.DataFrame(st.session_state.historico_funciones)
        st.dataframe(df_hist, use_container_width=True)
        if st.button("🗑️ Limpiar historico"):
            st.session_state.historico_funciones = []
            st.warning("Historico eliminado.")


# =====================================================================
# 5. EJERCICIO 4 - CLASES DESDE LIBRERIA EXTERNA CON CRUD
# =====================================================================
elif seccion == "Ejercicio 4":

    st.title("Ejercicio 4 - Clase EquipoMantenimiento con CRUD")

    st.markdown(
        """
        Este ejercicio utiliza la clase **`EquipoMantenimiento`** del archivo
        **`libreria_clases_proyecto1.py`**. Cada equipo registrado se convierte en
        un objeto de la clase, que calcula automaticamente **MTBF**, **MTTR** y
        **disponibilidad** mediante sus metodos.

        Se implementan las cuatro operaciones **CRUD**: Crear, Leer, Actualizar y Eliminar.
        """
    )

    st.markdown("---")

    tab_crear, tab_leer, tab_actualizar, tab_eliminar = st.tabs(
        ["➕ Crear", "📋 Leer", "✏️ Actualizar", "🗑️ Eliminar"]
    )

    # -------------------- CREAR --------------------
    with tab_crear:
        st.subheader("Crear nuevo equipo")

        nombre_equipo = st.text_input("Nombre del equipo:", placeholder="Ej: Compresor A-01", key="c_nombre")
        c1, c2, c3 = st.columns(3)
        horas_operacion = c1.number_input("Horas de operacion:", 0.0, value=720.0, step=1.0, key="c_horas")
        numero_fallas = c2.number_input("Numero de fallas:", 0, value=3, step=1, key="c_fallas")
        horas_reparacion = c3.number_input("Horas de reparacion:", 0.0, value=9.0, step=0.5, key="c_rep")

        if st.button("Guardar equipo", use_container_width=True):
            if nombre_equipo.strip() == "":
                st.error("Debes ingresar el nombre del equipo.")
            elif any(e["nombre_equipo"].lower() == nombre_equipo.strip().lower()
                     for e in st.session_state.equipos):
                st.error("Ya existe un equipo registrado con ese nombre.")
            else:
                try:
                    # Se instancia la clase para validar los datos ingresados
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
                    st.success(f"Equipo '{equipo.nombre_equipo}' creado correctamente.")
                    st.write(equipo.resumen())
                except ValueError as e:
                    st.error(f"Error de validacion: {e}")

    # -------------------- LEER --------------------
    with tab_leer:
        st.subheader("Equipos registrados")

        if len(st.session_state.equipos) == 0:
            st.info("Aun no hay equipos registrados. Crea el primero en la pestaña 'Crear'.")
        else:
            filas = []
            for datos in st.session_state.equipos:
                equipo = lc.EquipoMantenimiento(**datos)
                resumen = equipo.resumen()
                filas.append(
                    {
                        "Equipo": resumen["equipo"],
                        "Horas operacion": datos["horas_operacion"],
                        "Fallas": datos["numero_fallas"],
                        "Horas reparacion": datos["horas_reparacion"],
                        "MTBF (h)": resumen["mtbf_h"],
                        "MTTR (h)": resumen["mttr_h"],
                        "Disponibilidad (%)": resumen["disponibilidad_pct"],
                    }
                )

            df_equipos = pd.DataFrame(filas)
            st.dataframe(df_equipos, use_container_width=True)

            k1, k2, k3 = st.columns(3)
            k1.metric("Equipos registrados", len(df_equipos))
            k2.metric("Disponibilidad promedio", f"{df_equipos['Disponibilidad (%)'].mean():.2f} %")
            k3.metric("Total de fallas", int(df_equipos["Fallas"].sum()))

            st.markdown("#### Disponibilidad por equipo")
            st.bar_chart(df_equipos.set_index("Equipo")["Disponibilidad (%)"])

    # -------------------- ACTUALIZAR --------------------
    with tab_actualizar:
        st.subheader("Actualizar un equipo")

        if len(st.session_state.equipos) == 0:
            st.info("No hay equipos para actualizar.")
        else:
            nombres = [e["nombre_equipo"] for e in st.session_state.equipos]
            seleccionado = st.selectbox("Selecciona el equipo:", nombres, key="u_sel")
            indice = nombres.index(seleccionado)
            actual = st.session_state.equipos[indice]

            c1, c2, c3 = st.columns(3)
            n_horas = c1.number_input("Horas de operacion:", 0.0,
                                      value=float(actual["horas_operacion"]), step=1.0, key="u_horas")
            n_fallas = c2.number_input("Numero de fallas:", 0,
                                       value=int(actual["numero_fallas"]), step=1, key="u_fallas")
            n_rep = c3.number_input("Horas de reparacion:", 0.0,
                                    value=float(actual["horas_reparacion"]), step=0.5, key="u_rep")

            if st.button("Actualizar equipo", use_container_width=True):
                try:
                    equipo = lc.EquipoMantenimiento(seleccionado, n_horas, n_fallas, n_rep)
                    st.session_state.equipos[indice] = {
                        "nombre_equipo": seleccionado,
                        "horas_operacion": n_horas,
                        "numero_fallas": n_fallas,
                        "horas_reparacion": n_rep,
                    }
                    st.success(f"Equipo '{seleccionado}' actualizado correctamente.")
                    st.write(equipo.resumen())
                except ValueError as e:
                    st.error(f"Error de validacion: {e}")

    # -------------------- ELIMINAR --------------------
    with tab_eliminar:
        st.subheader("Eliminar un equipo")

        if len(st.session_state.equipos) == 0:
            st.info("No hay equipos para eliminar.")
        else:
            nombres = [e["nombre_equipo"] for e in st.session_state.equipos]
            a_eliminar = st.selectbox("Selecciona el equipo a eliminar:", nombres, key="d_sel")

            if st.button("Eliminar equipo", use_container_width=True):
                st.session_state.equipos = [
                    e for e in st.session_state.equipos if e["nombre_equipo"] != a_eliminar
                ]
                st.success(f"Equipo '{a_eliminar}' eliminado correctamente.")

            if st.button("Eliminar TODOS los equipos", use_container_width=True):
                st.session_state.equipos = []
                st.warning("Se eliminaron todos los equipos registrados.")
