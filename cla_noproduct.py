class CLACultivation:
    def __init__(self, initial_substrate, initial_biomass, mu_max, Ks, Yxs, feed_rate, feed_concentration, initial_volume):
        self.substrate = initial_substrate
        self.biomass = initial_biomass
        self.mu_max = mu_max
        self.Ks = Ks
        self.Yxs = Yxs
        self.feed_rate = feed_rate
        self.feed_concentration = feed_concentration
        self.volume = initial_volume

    def simulate(self, time, dt):
        times = [0]
        biomass = [self.biomass * self.volume]
        substrate_concentrations = [self.substrate]
        biomass_concentrations = [self.biomass]
        mus = [self.mu_max]
        volumes = [self.volume]

        t = 0
        while t < time:
            if self.substrate <= 0:
                break
            t += dt
            times.append(t)

            #Balance volumen
            dV = self.feed_rate * dt
            self.volume += dV
            volumes.append(self.volume)

            #Balance biomasa (pasos previos)
            Dilution = self.feed_rate / self.volume #tasa dilucion
            mu = self.mu_max * (self.substrate / (self.Ks + self.substrate)) #Monod
            mus.append(mu)
            #balance biomasa
            dX = (mu - Dilution) * self.biomass * dt
            self.biomass += dX
            biomass_concentrations.append(self.biomass)

            #biomasa acumulada
            biomass.append(self.biomass * self.volume)

            #Balance sustrato
            dS = (Dilution * (self.feed_concentration - self.substrate) - mu / self.Yxs * self.biomass) * dt
            self.substrate += dS
            substrate_concentrations.append(self.substrate)

        return times, substrate_concentrations, biomass_concentrations, mus, volumes, biomass