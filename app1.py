from flask import Flask, render_template, request, jsonify
from io import BytesIO
import base64
from bioreactor import Bioreactor
from cla_cultivation import CLACultivation  # Importar la nueva clase
from visualization import PlotResults

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    cultivation_type = request.form['cultivation_type']
    initial_substrate = float(request.form['initial_substrate'])
    initial_biomass = float(request.form['initial_biomass'])
    mu_max = float(request.form['mu_max'])
    Ks = float(request.form['Ks'])
    Yxs = float(request.form['Yxs'])
    time = float(request.form['time'])
    dt = float(request.form['dt'])

    if cultivation_type == 'batch':
        reactor = Bioreactor(initial_substrate, initial_biomass, mu_max, Ks, Yxs)
        times, substrate_concentrations, biomass_concentrations, mus = reactor.simulate(time, dt)
        volumes = None
    elif cultivation_type == 'cla':
        feed_rate = float(request.form['feed_rate'])
        feed_concentration = float(request.form['feed_concentration'])
        initial_volume = float(request.form['initial_volume'])
        reactor = CLACultivation(initial_substrate, initial_biomass, mu_max, Ks, Yxs, feed_rate, feed_concentration, initial_volume)
        times, substrate_concentrations, biomass_concentrations, mus, volumes = reactor.simulate(time, dt)
    
    #times, substrate_concentrations, biomass_concentrations = reactor.simulate(time, dt)
    
    img = BytesIO()
    resultado = PlotResults(times, substrate_concentrations, biomass_concentrations, mus, volumes)
    resultado.plot_concentrations(img)
    #plot_results(times, substrate_concentrations, biomass_concentrations, img)
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')
    
    return jsonify({'img_base64': img_base64})

if __name__ == '__main__':
    app.run(debug=True)
