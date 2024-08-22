class Bioreactor:
    def __init__(self, initial_substrate, initial_biomass, mu_max, Ks, Yxs):
        self.substrate = initial_substrate
        self.biomass = initial_biomass
        self.mu_max = mu_max
        self.Ks = Ks
        self.Yxs = Yxs
    
    def simulate(self, time, dt):
        times = [0]
        substrate_concentrations = [self.substrate]
        biomass_concentrations = [self.biomass]
        mus = [self.mu_max]

        t = 0
        while t < time:
            if self.substrate <= 0:
                break
            mu = self.mu_max * (self.substrate / (self.Ks + self.substrate)) #Monod
            mus.append(mu)
            dS = - mu / self.Yxs * self.biomass * dt #Consumo sustrato
            dX = mu * self.biomass * dt #Crecimiento biomasa

            self.substrate += dS
            self.biomass += dX

            t += dt
            times.append(t)

            substrate_concentrations.append(self.substrate)
            biomass_concentrations.append(self.biomass)

        return times, substrate_concentrations, biomass_concentrations, mus