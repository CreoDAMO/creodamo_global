import logging
import sys
from modules.core import BlockchainCore
from modules.language import CreoLang
from modules.consensus import ProofOfCreo
from modules.web3 import Web3Interface
from modules.storage import IPFS
from modules.monitoring import EventMonitoring
from modules.contracts import SmartContract
from modules.governance import GovernanceSystem
from modules.security import SecurityManager

class CreoBlockchain:

    def __init__(self, config):
        self.core = BlockchainCore(config)
        self.lang = CreoLang(self.core)
        self.consensus = ProofOfCreo(self.core)
        self.web3 = Web3Interface(self.core)
        self.storage = IPFS(self.core)
        self.monitoring = EventMonitoring(self.core)
        self.contract = SmartContract(self.core)
        self.governance = GovernanceSystem(self.core)
        self.security_manager = SecurityManager(self.core)

    def execute_script(self, script: str) -> str:
        try:
            return self.lang.run(script)
        except Exception as e:
            logging.error(f"Error executing script: {e}")
            raise

    def validate_transactions(self) -> bool:
        try:
            return self.consensus.verify()
        except Exception as e:
            logging.error(f"Error validating transactions: {e}")
            raise

    def call_contract(self, name: str, func: str, args: list) -> str:
        try:
            return self.contract.invoke(name, func, args)
        except Exception as e:
            logging.error(f"Error calling contract function: {e}")
            raise

    def monitor_events(self):
        try:
            self.monitoring.start()
        except Exception as e:
            logging.error(f"Error monitoring events: {e}")
            raise

    def store_data(self, data: dict) -> str:
        try:
            return self.storage.put(data)
        except Exception as e:
            logging.error(f"Error storing data: {e}")
            raise

    def govern(self):
        try:
            self.governance.execute()
        except Exception as e:
            logging.error(f"Governance execution error: {e}")
            raise

    def enforce_security(self):
        try:
            self.security_manager.enforce_policies()
        except Exception as e:
            logging.error(f"Security enforcement error: {e}")
            raise

if __name__ == "__main__":
    config = "path/to/config"  # Replace with actual config path
    logging.basicConfig(level=logging.INFO)
    blockchain = CreoBlockchain(config)

    try:
        script_result = blockchain.execute_script("path/to/script.cl")
        logging.info(f"Script executed successfully: {script_result}")
        blockchain.validate_transactions()
        blockchain.call_contract("Contract1", "add", [1, 2])
        blockchain.monitor_events()
        blockchain.store_data({"key": "value"})
        blockchain.govern()
        blockchain.enforce_security()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)
