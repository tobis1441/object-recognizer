from main.main import run
import os


def test_application_start():
    print("Current directory: ")
    print(os.path.join(os.path.dirname(__file__)))
    run()
