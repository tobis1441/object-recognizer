import pytest
import os


@pytest.fixture(autouse=True)
def configure_ifc_dir():
    if ('PYTHONPATH' not in os.environ) or (not os.environ['PYTHONPATH']):
        # Check if environment variable IFC_DIR is set
        current_dir = os.path.dirname(os.path.realpath(__file__))
        os.environ['PYTHONPATH'] = current_dir
