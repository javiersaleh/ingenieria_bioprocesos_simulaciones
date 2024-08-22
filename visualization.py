import matplotlib.pyplot as plt

class PlotResults:
    def __init__(self, times, substrate_concentrations, biomass_concentrations, mus, volumes, biomass):
        self.times = times
        self.substrate_concentrations = substrate_concentrations
        self.biomass_concentrations = biomass_concentrations
        self.mus = mus
        self.volumes = volumes
        self.biomass = biomass
    
    def plot_concentrations(self, img):
        plt.figure()
        plt.plot(self.times, self.substrate_concentrations, color = 'darkorange', label = 'Sustrato', )
        plt.plot(self.times, self.biomass_concentrations, color = 'green',  label = 'Biomasa')
        plt.xlabel('Tiempo (h)')
        plt.ylabel('Concentración (g/L)')
        plt.legend()
        plt.savefig(img, format='png')
        plt.close()
    
    def plot_biomass_accumulation(self, img):
        plt.figure()
        plt.plot(self.times, self.biomass, color = 'green', label='Acumulación de Biomasa (g)')
        plt.xlabel('Tiempo (h)')
        plt.ylabel('Biomasa Acumulada (g)')
        plt.legend()
        plt.savefig(img, format='png')
        plt.close()
