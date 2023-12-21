from pyo3 import builtin
import rust_api as rust

class RustAPI:
   def __init__(self):
      self.rust = rust

   def initialize(self):
      self.rust.initialize()

   def simulate(self, reactants):
      return self.rust.simulate(reactants)

   def optimize(self, molecule):
      return self.rust.optimize(molecule)

   def analyze(self, molecule):   
      return self.rust.analyze(molecule)
