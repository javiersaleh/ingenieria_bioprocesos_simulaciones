from flask import Flask, render_template, request, jsonify
from io import BytesIO
import base64
from bioreactor import Bioreactor
from cla_cultivation import CLACultivation  # Importar la nueva clase
from visualization1 import PlotResults

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index3.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    cultivation_type = request.form['cultivation_type']
    initial_substrate = float(request.form['initial_substrate'])
    initial_biomass = float(request.form['initial_biomass'])
    mu_max = float(request.form['mu_max'])
    Ks = float(request.form['Ks'])
    Yxs = float(request.form['Yxs'])
    qp = float(request.form['qp'])
    Yps = float(request.form['Yps'])
    growth_associated = request.form['growth_associated']
    time = float(request.form['time'])
    dt = float(request.form['dt'])

    if cultivation_type == 'batch':
        reactor = Bioreactor(initial_substrate, initial_biomass, mu_max, Ks, Yxs, qp, Yps, growth_associated)
        times, substrate_concentrations, biomass_concentrations, mus, products = reactor.simulate(time, dt)
        volumes = None
        resultado = PlotResults(times, substrate_concentrations, biomass_concentrations, mus, volumes, products)
    elif cultivation_type == 'cla':
        feed_rate = float(request.form['feed_rate'])
        feed_concentration = float(request.form['feed_concentration'])
        initial_volume = float(request.form['initial_volume'])
        reactor = CLACultivation(initial_substrate, initial_biomass, mu_max, Ks, Yxs, qp, Yps, growth_associated, feed_rate, feed_concentration, initial_volume)
        times, substrate_concentrations, biomass_concentrations, mus, volumes, products, biomass = reactor.simulate(time, dt)
        resultado = PlotResults(times, substrate_concentrations, biomass_concentrations, mus, volumes, products, biomass)
    
    img = BytesIO()
    resultado.plot_concentrations(img)
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')
    
    # Para CLA, generar la gráfica de acumulación de biomasa
    if cultivation_type == 'cla':
        img_biomass = BytesIO()
        resultado.plot_biomass_accumulation(img_biomass)
        img_biomass.seek(0)
        img_biomass_base64 = base64.b64encode(img_biomass.getvalue()).decode('utf-8')
        return jsonify({'img_base64': img_base64, 'img_biomass_base64': img_biomass_base64})
    

    return jsonify({'img_base64': img_base64})

if __name__ == '__main__':
    app.run(debug=True)