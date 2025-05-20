import os
from dotenv import load_dotenv


load_dotenv()

def __convert_str_to_bool(value: str) -> bool:
    """Конвертирует строку из .env в class bool."""

    return value.lower() == 'true'


BASE_URL = os.getenv('BASE_URL', 'http://track.nordclan/login')
VALID_USERNAME = os.getenv('VALID_USERNAME')
VALID_PASSWORD = os.getenv('VALID_PASSWORD')

HEADLESS = __convert_str_to_bool(os.getenv('HEADLESS', 'False'))
