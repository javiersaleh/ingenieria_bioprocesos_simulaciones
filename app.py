from flask import Flask, render_template, request, send_file
from io import BytesIO
import base64
from bioreactor import Bioreactor
from visualization import PlotResults

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    # Obtener los datos del formulario
    initial_substrate = float(request.form['initial_substrate'])
    initial_biomass = float(request.form['initial_biomass'])
    mu_max = float(request.form['mu_max'])
    Ks = float(request.form['Ks'])
    Yxs = float(request.form['Yxs'])
    time = float(request.form['time'])
    dt = 0.1
    #dt = float(request.form['dt'])

    # Crear una instancia del bioreactor y simular
    reactor = Bioreactor(initial_substrate, initial_biomass, mu_max, Ks, Yxs)
    times, substrate_concentrations, biomass_concentrations = reactor.simulate(time, dt)
    
    # Generar la gráfica
    img = BytesIO()
    resultado = PlotResults(times, substrate_concentrations, biomass_concentrations)
    resultado.plot_results(img)

    img.seek(0)

    return send_file(img, mimetype='image/png')

app.run(debug = True)
