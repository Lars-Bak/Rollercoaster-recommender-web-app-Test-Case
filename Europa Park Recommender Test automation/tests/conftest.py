import pytest
import os
import sys

# Voeg de projectroot toe aan sys.path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT_DIR)

from app import app as flask_app


@pytest.fixture
def app():
    flask_app.config["TESTING"] = True
    return flask_app
