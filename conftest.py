import os.path

root_dir = os.path.dirname(os.path.abspath(__file__))

pytest_plugins = [
    "fixtures.data_provider",
]
