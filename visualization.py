import matplotlib.pyplot as plt

class PlotResults:
    def __init__(self, times, substrate_concentrations, biomass_concentrations, mus, volumes):
        self.times = times
        self.substrate_concentrations = substrate_concentrations
        self.biomass_concentrations = biomass_concentrations
        self.mus = mus
        self.volumes = volumes
    
    def plot_concentrations(self, img):
        plt.figure()
        plt.plot(self.times, self.substrate_concentrations, label = 'Sustrato')
        plt.plot(self.times, self.biomass_concentrations, label = 'Biomasa')
        plt.xlabel('Tiempo (h)')
        plt.ylabel('Concentración (g/L)')
        plt.legend()
        plt.savefig(img, format='png')
        plt.close()
    
    def plot_mu(self, img):
        plt.figure()
        plt.plot(self.times, self.mus, label='μ (Specific Growth Rate)')
        plt.xlabel('Time')
        plt.ylabel('μ')
        #plt.title('Specific Growth Rate Over Time')
        plt.savefig(img, format='png')
        plt.close()
    
    def plot_volume(self, img):
        plt.figure()
        plt.plot(self.times, self.volumes, label='Volume')
        plt.xlabel('Time')
        plt.ylabel('Volume')
        #plt.title('Volume Over Time')
        plt.savefig(img, format='png')
        plt.close()
