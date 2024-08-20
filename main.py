from bioreactor import Bioreactor
from visualization import PlotResults

def main():
    initial_substrate = 10  # g/L
    initial_biomass = 1  # g/L
    mu_max = 0.4  # 1/h
    Ks = 0.1  # g/L
    Yxs = 0.5  # g biomass / g substrate
    time = 5  # h
    dt = 0.1  # h

    reactor = Bioreactor(initial_substrate, initial_biomass, mu_max, Ks, Yxs)
    times, substrate_concentrations, biomass_concentrations = reactor.simulate(time, dt)
    
    resultado = PlotResults(times, substrate_concentrations, biomass_concentrations)
    resultado.plot_results(None)

main()
