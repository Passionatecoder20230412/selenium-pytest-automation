import os
from datetime import datetime


class Config:
    # ===============================
    # Project base directory
    # ===============================
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # ===============================
    # Directories
    # ===============================
    LOGS_DIR = os.path.join(BASE_DIR, "output", "logs")
    REPORTS_DIR = os.path.join(BASE_DIR, "output", "reports")
    SCREENSHOTS_DIR = os.path.join(BASE_DIR, "output", "screenshots")

    # ===============================
    # URLs
    # ===============================
    BASE_URL = "https://automationexercise.com"

    # ===============================
    # Browser configuration
    # ===============================
    BROWSER = os.getenv("BROWSER", "chrome")
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    IMPLICIT_WAIT = 30
    EXPLICIT_WAIT = 30

    # ===============================
    # Test data
    # ===============================
    TEST_DATA_PATH = os.path.join(BASE_DIR, "test_data")

    # ===============================
    # Logging
    # ===============================
    LOG_LEVEL = "INFO"
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

    # ===============================
    # Utilities
    # ===============================
    @staticmethod
    def get_timestamp():
        return datetime.now().strftime("%Y%m%d_%H%M%S")

    @classmethod
    def setup_directories(cls):
        for directory in [cls.LOGS_DIR, cls.REPORTS_DIR, cls.SCREENSHOTS_DIR]:
            os.makedirs(directory, exist_ok=True)
