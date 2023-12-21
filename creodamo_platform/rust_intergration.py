import rust_bindings 

class RustIntegration:

    def __init__(self):
        self.rust = rust_bindings.RustAPI()

    def initialize(self):
        self.rust.initialize()

    def simulate_reaction(self, reactants):
        return self.rust.simulate(reactants) 

    def optimize_molecule(self, molecule):
        return self.rust.optimize(molecule)

    def analyze_properties(self, molecule):
        return self.rust.analyze(molecule)
