import sys
import os

from src.interfaz_login import LoginApp

# Agregar la carpeta src al path para importar módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))



if __name__ == "__main__":
    app = LoginApp()
    app.ejecutar()