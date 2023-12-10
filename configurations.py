# configurations.py

from dynaconf import Dynaconf
from ai_ml import AIConfigAnalyzer
from iot import IoTConfigHandler
from plugin_store import PluginStore
from cloud_services import CloudConfigManager
from blockchain_logger import BlockchainLogger
from ansible_manager import AnsibleManager
from notification_system import NotificationSystem
from dynamic_config_loader import DynamicConfigLoader
from chaos_engine import ChaosEngine

load_dotenv()

class AppConfig:

    def __init__(self):
        self.settings = Dynaconf(
            environments=True,
            load_dotenv=True,
            settings_files=['settings.yaml', '.secrets.yaml']
        )
        self.ai_analyzer = AIConfigAnalyzer()
        self.iot_handler = IoTConfigHandler()
        self.plugin_store = PluginStore()
        self.cloud_manager = CloudConfigManager()
        self.blockchain_logger = BlockchainLogger()
        self.ansible_manager = AnsibleManager()
        self.notification_system = NotificationSystem()
        self.dynamic_config_loader = DynamicConfigLoader()
        self.chaos_engine = ChaosEngine()

    def get_setting(self, key):
        return self.settings.get(key)
