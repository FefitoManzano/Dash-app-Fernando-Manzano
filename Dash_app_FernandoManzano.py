from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
from datetime import datetime

nombre_archivo = 'CsvGF.xlsx'
df_tabla1 = pd.read_excel(nombre_archivo, sheet_name='Hoja 3')
df_tabla2 = pd.read_excel(nombre_archivo, sheet_name='Hoja 4')
df_tabla3 = pd.read_excel(nombre_archivo, sheet_name='Hoja 5')
df_tabla4 = pd.read_excel(nombre_archivo, sheet_name='Hoja 6')
df_grupal = pd.read_excel(nombre_archivo, sheet_name='opciones')
df_grupal2 = pd.read_excel(nombre_archivo, sheet_name='Hoja 2')
df_alt = pd.read_excel(nombre_archivo, sheet_name='H2')

# Obtener la lista de columnas disponibles
columnas_disponibles = df_grupal.columns[1:]
columnas_disponibles2 = df_grupal2.columns[1:]

# Inicializar la aplicación
app = Dash(__name__)

# Diseño de la aplicación
app.layout = html.Div([
    html.P("Hito 3", style={'fontSize': 20, 'fontWeight': 'bold'}),
    html.P("Gestión Financiera", style={'fontSize': 18, 'fontWeight': 'bold'}),
    html.P("Grupo 7: Energía", style={'fontSize': 18, 'fontWeight': 'bold'}),
    html.P("", style={'fontSize': 18, 'fontWeight': 'bold'}),
    html.P("Integrantes:", style={'fontSize': 13, 'fontWeight': 'bold'}),
    html.P("Juan Ayala - Benjamín Ruiz Tagle - Fernando Manzano", style={'fontSize': 13 }),
    html.P("Profesor:", style={'fontSize': 13, 'fontWeight': 'bold'}),
    html.P("Sebastián Cea", style={'fontSize': 13}),
    html.P("", style={'fontSize': 13}),
    html.P("Sebastián Cea", style={'fontSize': 13}),
    html.P(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"),
    html.Div(children=''),
            dcc.Checklist(
                id='column-selector',
                options=[{'label': col, 'value': col} for col in columnas_disponibles],
                value=columnas_disponibles.tolist()
            ),         
    # Tabs para distintos capítulos
    dcc.Tabs(id='tabs', value='definicion', children=[
        dcc.Tab(label='Definición', value='definicion'),
        dcc.Tab(label='Deuda, Emisiones y Derivados', value='deuda_emisiones_derivados'),
        dcc.Tab(label='Asignacion de Activos', value='asignacion_activos'),
        dcc.Tab(label='Modelo Binomial Jarrow-Rudd', value='modelo_binomial'),
        dcc.Tab(label='Resultados y Comparación', value='resultados_comparacion'),
        dcc.Tab(label='Caso Grupal', value='caso'),
    ]),

    # Output para mostrar contenido de cada capítulo
    html.Div(id='capitulo-content')
])

# Callback para actualizar el histograma según las selecciones del usuario
@app.callback(
            Output('histograma', 'figure'),
            [Input('column-selector', 'value')]
        )
def actualizar_histograma_caso(columnas_seleccionadas):
  if not columnas_seleccionadas:
                return px.histogram(df_grupal, x='Variable', y='Política actual', histfunc='sum')
  fig = px.histogram(df_grupal, x='Variable', y=columnas_seleccionadas, histfunc='sum')
  return fig

# Callback para actualizar el contenido de cada pestaña
@app.callback(
    Output('capitulo-content', 'children'),
    [Input('tabs', 'value')]
)
def actualizar_contenido_capitulo(selected_tab):
    # Puedes trabajar en cada capítulo aquí y devolver el contenido correspondiente
    if selected_tab == 'definicion':
        contenido_definicion = html.Div([
            html.P("Enel Chile S.A se propone alcanzar la neutralidad de carbono en 2040, 10 años antes que muchos países. La empresa, con metas de sostenibilidad en varios países, destaca por su liderazgo en innovación y alianzas para transformar el sector energético. Comparada con su competencia, Enel Chile S.A está avanzada en sostenibilidad, con un activo ENIC valorado en promedio en 4."),
            html.P("La adopción de energías renovables es esencial para reducir la dependencia de recursos no renovables y disminuir las emisiones de gases de efecto invernadero. Según la AIE, se espera que las renovables representen el 44% del suministro eléctrico global para 2040, lideradas por tecnologías eólicas y fotovoltaicas."),
            html.Img(
                src="https://www.enel.cl/content/dam/enel-cl/sostenibilidad/informes-de-sostenibilidad/informe-interactivo/2020/cambio-climatico/grafico-capacidad-generacion.jpg"),
            html.P("La industria de la energía renovable ha experimentado un crecimiento significativo, con costos en disminución desde 2010. Se proyecta que el 95% del crecimiento en capacidad de generación de energía provenga de renovables para 2026, indicando un crecimiento exponencial gracias a avances tecnológicos."),
            html.P("Variables económicas de contexto importantes que pueden afectar a empresas como Enel, en su rentabilidad y operación, en el sector de la energía son, por ejemplo: precio de la electricidad, costo de los combustibles o recursos energéticos, política energética, demanda de energía, política monetaria, tendencias en energías renovables y eventos climáticos extremos."),
            # Agregar la tabla proporcionada
            dash_table.DataTable(data=df_tabla1.to_dict('records'), page_size=6),
            html.Img(
                src="https://www.enel.com/content/dam/enel-com/immagini/master-azienda_2400x1160/storie_2400x1160/zero-emissions-day-2022_2400x1160.jpg",
                alt="Diferencia Porcentual", style={'width': '900px', 'height': '600px'}),

        ])
        return contenido_definicion
    elif selected_tab == 'deuda_emisiones_derivados':
        contenido_deuda_emisiones_derivados = html.Div([
            html.P("Enel Chile realiza inversiones en diversos sectores, como infraestructura de generación, red de distribución y transmisión, adquisición de empresas y activos, inversiones en energías renovables, y utiliza instrumentos financieros."),
            html.P("La estructura de capital de la empresa incluye 69.166.557.220 acciones sin valor nominal específico. En julio de 2020, Enel SpA aumentó su participación al 64,93% mediante la adquisición de acciones ordinarias y American Depositary Shares (ADS)."),
            html.P("En junio de 2018, Enel Chile emitió bonos por US $1.000 millones con un cupón de tasa de interés del 4,875% anual en dólares."),
            html.P("El proceso de emisión de acciones incluye evaluación de necesidades, selección de asesores, documentación legal y regulatoria, registro y aprobación regulatoria, mercado de capitales, oferta pública, liquidación y asignación."),
            html.P("Enel Chile utiliza derivados para gestionar riesgos, clasificándolos en coberturas de flujos de caja, coberturas de valor razonable y derivados no cobertura, según su política de gestión de riesgos."),
            html.Img(src="https://www.dogsofthedow.com/wp-content/uploads/charts/enic-stock-price-1yr.png?123681", alt="Formulas modelo"),

        ])
        return contenido_deuda_emisiones_derivados
    elif selected_tab == 'asignacion_activos':
        contenido_asignacion_activos = html.Div([
            html.P("Para poder asignar el porcentaje que se le dará a los activos en el portafolio es necesario tener en consideración algunos factores, a modo de entender y desarrollar un análisis claro."),
            html.P("Los tres activos del portafolio se encuentran definidos y con sus respectivos datos en la siguiente tabla:"),
            # Agregar la tabla proporcionada df_tabla2
            dash_table.DataTable(data=df_tabla2.to_dict('records'), page_size=6),
            html.Hr(),  # Línea horizontal para separar contenido
            html.P("Análisis Activos"),
            html.P("En el análisis de activos, Cencosud Shopping lidera en capitalización de mercado. Aunque los tres activos son relativamente seguros, el Banco de Chile es el menos riesgoso. Todos muestran un Ratio Sharpe negativo en los últimos tres meses."),
            html.P("Debido al alto Beta y bajo rendimiento, Enel tiene la menor asignación. Banco de Chile y Cencosud Shopping reciben el mismo porcentaje para mantener la estabilidad en el portafolio."),
            html.P("En un contexto de incertidumbre global, los activos energéticos son percibidos como más riesgosos. Cencosud Shopping destaca por su aumento del 99,6% en utilidades y una rentabilidad anual del 35%, obteniendo una mayor asignación en el portafolio."),
            # Agregar la tabla proporcionada df_tabla3
            dash_table.DataTable(data=df_tabla3.to_dict('records'), page_size=6),
        ])
        return contenido_asignacion_activos

    elif selected_tab == 'modelo_binomial':
        contenido_modelo_binomial = html.Div([
            html.P("Movimiento hacia arriba del Árbol Binomial"),
            html.P("Con probabilidades fijas, todos los inputs que describen el movimiento de precios, como la volatilidad σ, la tasa de interés libre de riesgo “r” y el rendimiento “q”, se reflejan en el tamaño de los movimientos hacia arriba y hacia abajo."),
            html.P("Donde Δt es la duración de un paso en años, calculada como el tiempo de vencimiento de la opción t dividido por el número de pasos del modelo n."),
            html.P("Los multiplicadores de movimiento hacia arriba y hacia abajo, denotados como u y d, se utilizan para generar el árbol de precios subyacentes, partiendo del precio subyacente actual S y llegando a la fecha de vencimiento de la opción."),
            html.P("Desde cada nodo en el árbol, el precio puede subir (S · u) o bajar (S · d) hacia uno de los dos nodos en el siguiente paso."),
            html.P("Los precios subyacentes en la fecha de vencimiento (el último paso en el árbol) se utilizan para calcular los pagos de la opción en la fecha de vencimiento, que constituyen el último paso en el árbol de precios de la opción."),
            html.P("Luego, el resto del árbol de precios de la opción se calcula hacia atrás, llegando finalmente a su primer nodo, que es el precio actual de la opción."),
            html.Img(src="data:image/png;base64,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", alt="Formulas modelo"),

        ])
        return contenido_modelo_binomial
    elif selected_tab == 'resultados_comparacion':
        contenido_resultados_comparacion = html.Div([
            html.P("Para analizar ambos modelos, los parámetros obtenidos se sacan directamente en tiempo real desde Yahoo Finance usando la librería yfinance."),
            html.P("El precio de la opción de compra (call) calculado con el modelo de Black-Scholes es de aproximadamente 0.5222, mientras que el modelo de Jarrow-Rudd da un precio de aproximadamente 0.5222."),
            html.P("La diferencia entre los dos precios es mínima (0.0000237107), lo que indica una cercanía sustancial entre los valores calculados por ambos modelos en este caso."),
            html.P("Esta pequeña discrepancia puede atribuirse a las diferencias en las suposiciones y métodos de cálculo específicos de cada modelo. En general, la similitud en los resultados sugiere que ambos modelos son consistentes en la valoración de la opción en esta situación particular."),
            html.P("Como siempre, es crucial considerar las condiciones específicas del activo subyacente, las características del mercado y las suposiciones de cada modelo al interpretar los resultados y tomar decisiones de inversión."),
            # Agregar la tabla proporcionada df_tabla4
            dash_table.DataTable(data=df_tabla4.to_dict('records'), page_size=6),
            html.P("Para realizar una comparación entre los dos modelos se realizaron varios cálculos usando diversos tickers y graficando la diferencia porcentual entre sus resultados."),
            html.P("Podemos apreciar que la diferencia porcentual no supera el valor absoluto de 0.2%. Esto es un porcentaje bastante pequeño y muestra que ambos modelos, a pesar de ser muy distintos en su manera de calcular las opciones, son consistentes en sus resultados."),
            # Leer la imagen y convertirla a base64
            html.Img(src="https://i.pinimg.com/originals/2b/9c/df/2b9cdf5fdc0d0715fe8180aec401c059.png", alt="Diferencia Porcentual"),

        ])
        return contenido_resultados_comparacion
    elif selected_tab == 'caso':
        contenido_caso = html.Div([
            html.Div(children=''),
            html.Div(children='Tabla'),
            dash_table.DataTable(data=df_grupal.to_dict('records'), page_size=12),
            dash_table.DataTable(data=df_grupal2.to_dict('records'), page_size=12),
            html.Div(children='Solucion'),
            dash_table.DataTable(data=df_alt.to_dict('records'), page_size=5),
            dcc.Graph(id='histograma', figure=px.histogram(df_grupal, x='Variable', y='Política actual', histfunc='sum')),
            dcc.Checklist(
                id='column-selector',
                options=[{'label': col, 'value': col} for col in columnas_disponibles],
                value=columnas_disponibles.tolist()
            ),
            html.P("Andrew Preston, tesorero, evalúa opciones para modificar la política de crédito actual de 30 días neto, considerando tres alternativas: relajar la decisión de otorgar crédito, extender el periodo a 45 días neto, o combinar ambas. Cada opción aumentaría las ventas, pero con el inconveniente de mayores tasas de incumplimiento y costos administrativos."),
            html.P("Considerando costos variables de producción del 45% de las ventas y una tasa de interés del 6%, la empresa debe elegir la política de crédito con el mayor Valor Presente Neto (VPN) positivo. Sin embargo, se destaca que la afirmación sobre la opción 3, con tasas de incumplimiento y costos administrativos menores que la opción 2, es incorrecta. La viabilidad de la opción 3 depende de implementar mejoras en la evaluación de riesgos y la automatización del proceso."),
            html.P("En resumen, la empresa debe realizar un análisis de costo-beneficio para determinar la opción más adecuada. La eficiencia y solvencia de Braam Industries se comparan con Enel, siendo esta última potencialmente una mejor opción de inversión si su VPN es mayor."),

        ])

        @app.callback(
            Output('histograma', 'figure'),
            [Input('column-selector', 'value')]
        )
        def actualizar_histograma_caso(columnas_seleccionadas):
            if not columnas_seleccionadas:
                return px.histogram(df_grupal, x='Variable', y='Política actual', histfunc='sum')
            fig = px.histogram(df_grupal, x='Variable', y=columnas_seleccionadas, histfunc='sum')
            return fig

        return contenido_caso
    else:
        return html.Div("Selecciona un capítulo")

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=False)



