
class Bioreactor:
    def __init__(self, initial_substrate, initial_biomass, mu_max, Ks, Yxs, qp, Yps, growth_associated):
        self.substrate = initial_substrate
        self.biomass = initial_biomass
        self.mu_max = mu_max
        self.Ks = Ks
        self.Yxs = Yxs
        self.qp = qp
        self.Yps = Yps
        self.growth_associated = growth_associated
        self.product = 0  # Inicializar el producto
    
    def simulate(self, time, dt):
        times = [0]
        substrate_concentrations = [self.substrate]
        biomass_concentrations = [self.biomass]
        mus = [self.mu_max]
        products = [self.product]

        t = 0
        while t < time:
            mu = self.mu_max * (self.substrate / (self.Ks + self.substrate)) #Monod
            mus.append(mu)
            dS = -mu * self.biomass * dt / self.Yxs #Consumo sustrato
            dX = mu * self.biomass * dt #Crecimiento biomasa

            self.substrate += dS
            self.biomass += dX

            t += dt
            times.append(t)

            substrate_concentrations.append(self.substrate)
            biomass_concentrations.append(self.biomass)

            # Cálculo del producto
            if self.growth_associated == 'yes':
                product_rate = self.Yps / self.Yxs * mu * self.biomass  # Producto asociado al crecimiento
            else:
                product_rate = self.qp * self.substrate  # Producto no asociado al crecimiento

            self.product += product_rate * dt
            products.append(self.product)

        return times, substrate_concentrations, biomass_concentrations, mus, products
