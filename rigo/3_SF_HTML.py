from dash import Dash, html, dcc
import pandas as pd

df = pd.read_csv('projectos.csv', encoding='Latin1')
df['Percent complete'] = pd.to_numeric(df['Percent complete'], errors='coerce')

total_projects = len(df)
avg_completion = round(df['Percent complete'].mean(), 2)
active_projects = df[df['Active'] == 'VERDADERO'].shape[0]

Header_style = {
    'textAlign': 'center',
    'backgroundColor': '#EBF5FB', 
    'color': '#1A5276',             
    'padding': '10px',
    'borderRadius': '5px',
    'border': '1px solid #D6DBDF'
}

Metric_style = {
    'display': 'flex',
    'justify-content': 'center',
    'gap': '15px',
    'marginTop': '10px'
}

Card_style = {
    'backgroundColor': '#FBFCFC',  
    'border': '1px solid #D6DBDF',  
    'border-radius': '5px',
    'padding': '10px',
    'textAlign': 'center',
    'width': '180px'
}

P_style = {
    'fontSize': '14px',
    'color': '#424949',
    'textAlign': 'center',
    'margin': '5px'
}

#Creación de app en dash
app = Dash(__name__)

app.layout = html.Div([ 
    #Título
    html.H1('Dashboard de Proyectos - Nivel 1: HTML Básico', style=Header_style),
    #Subtítulo
    html.H2('Estadísticas Generales', style=Header_style),
    #Contenido de un párrafo
    html.P('Este es un dashboard simple usando solo componentes HTML de Dash', style=P_style),

    # Separador horizontal
    html.Hr(), 
    html.Div([
        html.H3('Métricas Clave:'),
        # Lista
        html.Ul([
            #Elementos de la lista
            html.Li('Total de proyectos: ' + str(total_projects)),
            html.Li('Proyectos activos: ' + str(active_projects)),
            html.Li('Completitud Promedio: ' + str(round(avg_completion, 2)) + '%')

        ])
    ]),
    html.Hr(), 
    #Métricas básicas
    html.Div([
        html.Div([
            html.H2(f"{total_projects}", style={'color': '#FF69B4'}),   
            html.P("Total de Proyectos", style=P_style)

        ], style=Card_style),

        html.Div([
            html.H2(f"{active_projects}", style={'color': '#FFC0CB'}),  
            html.P("Proyectos Activos", style=P_style)

        ], style=Card_style),

        html.Div([
            html.H2(f"{avg_completion}%", style={'color': '#1ABC9C'}),  
            html.P("Promedio de Completitud", style=P_style)

        ], style=Card_style)

    ], style=Metric_style),

    html.P("Dashboard creado con Dash", style=P_style)

], style={'padding': '20px', 'font-family': 'Arial, sans-serif', 'backgroundColor': '#F8F9F9'}) 
    


if __name__ == '__main__':
    app.run(debug=True, port=8052) #Para generar cambios en "tiempo real"
