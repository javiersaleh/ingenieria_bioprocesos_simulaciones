import matplotlib.pyplot as plt

class PlotResults:
    def __init__(self, times, substrate_concentrations, biomass_concentrations, mus, volumes, products):
        self.times = times
        self.substrate_concentrations = substrate_concentrations
        self.biomass_concentrations = biomass_concentrations
        self.mus = mus
        self.volumes = volumes
        self.products = products
    
    def plot_concentrations(self, img):
        plt.figure()
        plt.plot(self.times, self.substrate_concentrations, color = 'darkorange', label = 'Sustrato', )
        plt.plot(self.times, self.biomass_concentrations, color = 'green',  label = 'Biomasa')
        plt.plot(self.times, self.products, color = 'dodgerblue', label = 'Producto')
        plt.xlabel('Tiempo (h)')
        plt.ylabel('Concentración (g/L)')
        plt.legend()
        plt.savefig(img, format='png')
        plt.close()
    
    def plot_biomass_accumulation(self, img):
        plt.figure()
        accumulated_biomass = [self.biomass_concentrations[i] * self.volumes[i] for i in range(len(self.biomass_concentrations))]
        plt.plot(self.times, accumulated_biomass, label='Acumulación de Biomasa (g)')
        plt.xlabel('Tiempo (h)')
        plt.ylabel('Biomasa Acumulada (g)')
        plt.legend()
        plt.savefig(img, format='png')
        plt.close()
