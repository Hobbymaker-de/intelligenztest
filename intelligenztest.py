from PyQt6.QtWidgets import QLabel, QPushButton, QWidget, QApplication, QMessageBox
from PyQt6.QtCore import QEvent, Qt
import sys


class MeinWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        original_stdout = sys.stdout
        # Umleite die Standardausgabe in ein Dummy-Objekt (z. B. ein leeres TextIO)
        sys.stdout = open('NUL', 'w')
        self.setGeometry(500, 500, 250, 150)
        self.setWindowTitle("Intelligenztest")
        # Blende die Minimieren- und Maximieren-Schaltflächen aus
        self.setWindowFlag(Qt.WindowType.WindowMinimizeButtonHint, False)
        self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)
        # Erstelle ein Label
        self.label = QLabel('Bist Du doof?', self)
        self.label.setGeometry(30, 10, 100, 30)
        #self.label.setVisible(True)  # Starte mit dem Label ausgeblendet
        self.counter = 0
        #Nein-Button
        self.button_nein = QPushButton('Nein', self)
        self.button_nein.installEventFilter(self)
        # Setze die ursprüngliche Größe und Position des Buttons
        self.button_nein.setGeometry(10, 60, 50, 30)
        #Ja-Button
        self.button_ja = QPushButton('Ja!', self)
        self.button_ja.installEventFilter(self)
        # Setze die ursprüngliche Größe und Position des Buttons
        self.button_ja.setGeometry(80, 60, 50, 30)
        self.button_ja.pressed.connect(self.einsicht_vorhanden)
            
    def einsicht_vorhanden(self):
        msg = QMessageBox()
        msg.setText('Einsicht ist der erste Schritt zur Erkenntnis!')
        msg.exec()
        app.exit()

    def eventFilter(self, source, event):
        
        if event.type() == QEvent.Type.HoverEnter:
            self.counter += 1
            #print(str(self.counter), 'Die Maus ist über dem Button!')
            if self.counter %2 == 0:
                # Verschiebe den Button um 150 Pixel nach links
                self.button_nein.setGeometry(10, 60, 50, 30)
            else:
                # Verschiebe den Button um 150 Pixel nach rechts
                self.button_nein.setGeometry(150, 60, 50, 30)
       
        return super().eventFilter(source, event)
    
if __name__ == '__main__':
    app = QApplication([])
    widget = MeinWidget()
    widget.show()
    app.exec()
