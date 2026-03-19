import sys
import os
import re
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QLabel, QLineEdit, QMessageBox
)
from PyQt6.QtGui import QIcon


def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class XMLSumAppV23(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sumador de ISR - V2.3")
        self.setGeometry(100, 100, 500, 200)

        icon_path = resource_path(os.path.join("Resources", "cfdi_sat_icon.ico"))
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        self.layout = QVBoxLayout()

        self.label = QLabel("Pega aquí la ruta de la carpeta con archivos XML:")
        self.layout.addWidget(self.label)

        self.path_input = QLineEdit()
        self.layout.addWidget(self.path_input)

        self.button = QPushButton("Procesar Archivos")
        self.button.clicked.connect(self.process_folder)
        self.layout.addWidget(self.button)

        self.result_label = QLabel("")
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def process_folder(self):
        folder_path = self.path_input.text().strip()

        if not os.path.isdir(folder_path):
            QMessageBox.critical(self, "Error", "La ruta ingresada no es válida.")
            return

        total, archivos_sin_dato, archivos_totales = self.sum_isr_importe(folder_path)
        self.result_label.setText(f"Suma total de ISR: {total:.2f}")

        if archivos_sin_dato:
            mensaje = (
                f"{len(archivos_sin_dato)} de {archivos_totales} archivos no contienen 'Concepto=\"ISR\" Importe=\"...\"':\n" +
                "\n".join(archivos_sin_dato)
            )
            print(mensaje)
            QMessageBox.warning(self, "Faltantes", mensaje)
        else:
            QMessageBox.information(self, "Completado", f"Todos los {archivos_totales} archivos contienen ISR con Importe. ✅")

    def sum_isr_importe(self, folder_path):
        total = 0.0
        sin_valor = []
        archivos_xml = [f for f in os.listdir(folder_path) if f.endswith(".xml")]

        # Regex: Concepto="ISR" seguido inmediatamente de Importe="número"
        pattern = re.compile(r'Concepto="ISR"\s+Importe="([\d.]+)"')

        for file_name in archivos_xml:
            file_path = os.path.join(folder_path, file_name)
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    match = pattern.search(content)
                    if match:
                        value = float(match.group(1))
                        total += value
                    else:
                        sin_valor.append(file_name)
            except Exception as e:
                print(f"Error leyendo {file_name}: {e}")
                sin_valor.append(file_name)

        return total, sin_valor, len(archivos_xml)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = XMLSumAppV23()
    window.show()
    sys.exit(app.exec())
