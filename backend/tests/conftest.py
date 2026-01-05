import os
import sys
from dotenv import load_dotenv

# Add the backend directory to pythonpath so 'app' module can be found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Load environment variables from .env.test immediately upon import
env_test_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env.test")
if os.path.exists(env_test_path):
    load_dotenv(env_test_path, override=True)
