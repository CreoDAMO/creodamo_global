from typing import Dict
from dotenv import load_dotenv
import yaml
from modules import Module, ModuleRegistry

config: Dict
registry = ModuleRegistry()

def load_config() -> Dict:
  load_dotenv()
  return yaml.safe_load(open("config.yaml")) 

class ConfigurationManager:

  def __init__(self):
    global config
    config = load_config()

  def register(self, module: Module):
    registry.register(module)

  def get_config(self) -> Dict:
    return config

  def get_module(self, name: str) -> Module:
    return registry.get_module(name)
    
class CreoDAMO:

  def __init__(self, manager: ConfigurationManager):
    self.manager = manager
    self.config = manager.get_config()
    
def main():

  manager = ConfigurationManager()

  manager.register(CreoLangModule(manager))
  
  # register other modules

  damo = CreoDAMO(manager)
  
  damo.start()

if __name__ == "__main__":
  main()
