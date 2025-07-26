import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from app.main import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5001)
