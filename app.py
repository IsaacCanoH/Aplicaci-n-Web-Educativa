from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Ruta principal (inicio del sitio)
    # Renderiza index.html y envía el breadcrumb con "Inicio"
    return render_template(
        'index.html',
        breadcrumb=["Inicio"]
    )
    
@app.route('/sistema-ambiental')
def sistema():
    # Ruta para la sección del sistema de gestión ambiental
    # Renderiza sistema.html con el breadcrumb correspondiente
    return render_template(
        'sistema.html',
        breadcrumb=["Inicio", "Sistema de Gestión Ambiental"]
    )
    
@app.route('/futuro')
def futuro():
    # Ruta para la página sobre el futuro del planeta
    # Renderiza futuro.html y define el camino de navegación
    return render_template(
        'futuro.html',
        breadcrumb=["Inicio", "Futuro del Planeta"]
    )
    
@app.route('/tres-r')
def tres_r():
    # Ruta para la página de las 3 R (Reducir, Reutilizar, Reciclar)
    # Renderiza tres_r.html con su breadcrumb
    return render_template(
        'tres_r.html',
        breadcrumb=["Inicio", "Las 3 R"]
    )
    
if __name__ == '__main__':
    app.run(debug=True)
