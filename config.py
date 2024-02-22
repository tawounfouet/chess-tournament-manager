import sys
import os


# ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the root directory of the project
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)


class Config:
    """Configuration class for the application"""

    
    
    # Tournament DB configuration
    TOURNAMENT_DB_FILE = os.path.join(ROOT_DIR, 'data/tournaments.json')

    # Logging configuration
    LOGGING_LEVEL = 'INFO'
