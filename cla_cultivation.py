class CLACultivation:
    def __init__(self, initial_substrate, initial_biomass, mu_max, Ks, Yxs, qp, Yps, growth_associated, feed_rate, feed_concentration, initial_volume):
        self.substrate = initial_substrate
        self.biomass = initial_biomass
        self.mu_max = mu_max
        self.Ks = Ks
        self.Yxs = Yxs
        self.qp = qp
        self.Yps = Yps
        self.growth_associated = growth_associated
        self.product = 0  # Inicializar el producto
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
        products = [self.product]

        t = 0
        while t < time:
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

            biomass.append(self.biomass * self.volume)

            #Balance sustrato
            dS = (Dilution * (self.feed_concentration - self.substrate) - (mu / self.Yxs + self.qp / self.Yps) * self.biomass) * dt
            self.substrate += dS
            substrate_concentrations.append(self.substrate)

            #Balance producto
            if self.growth_associated == 'yes':
                product_rate = self.Yps / self.Yxs * mu # Producto asociado al crecimiento
            else:
                product_rate = self.qp # Producto no asociado al crecimiento

            self.product += (product_rate * self.biomass - Dilution * self.product) * dt
            products.append(self.product)

        return times, substrate_concentrations, biomass_concentrations, mus, volumes, products, biomass
