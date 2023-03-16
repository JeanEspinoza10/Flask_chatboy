from pathlib import Path
from os import listdir
from importlib import import_module

path_parent = Path('./app/plantillas')

for module in listdir(path_parent):
    if 'messages' in module:
        import_module(
            f'app.plantillas.{module[:-3]}'
        )
