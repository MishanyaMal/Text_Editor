import sys, os

from PyQt6.QtWidgets import (QApplication, QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog, QTextEdit, QListWidget)

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setCentralWidget(Text_Editor())

class Text_Editor(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Text Editor')

        self.setGeometry(500, 500, 500, 400)

        self.setMaximumSize(500, 400)
        self.setMinimumSize(500, 400)

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.main_layout = QVBoxLayout()
        self.layout.addLayout(self.main_layout)

        self.button_layout = QHBoxLayout()
        self.main_layout.addLayout(self.button_layout)

        self.open_button = QPushButton('Open')
        self.button_layout.addWidget(self.open_button)

        self.open_button.clicked.connect(self.open)

        self.save_button = QPushButton('Save')
        self.button_layout.addWidget(self.save_button)

        self.save_button.clicked.connect(self.save)

        self.close_button = QPushButton('Close')
        self.button_layout.addWidget(self.close_button)

        self.close_button.clicked.connect(self.close)

        self.text_area = QTextEdit()
        self.main_layout.addWidget(self.text_area)

        self.list_area = QListWidget()
        self.layout.addWidget(self.list_area)

        self.load_notes()
        self.list_area.itemDoubleClicked.connect(self.open_file)

    def open(self):

        filename, _ = QFileDialog.getOpenFileName(self, 'Открыть файл', '.', 'Текстовые файлы (*.txt)')

        if filename:
            with open(filename, 'r', encoding='utf-8') as file:
                text = file.read()

            self.text_area.setText(text)

    def save(self):
        note_text = self.text_area.toPlainText()

        filename, _ = QFileDialog.getSaveFileName(self, 'Сохранить файл', '.', 'Текстовые файлы (*.txt)')

        if filename:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(note_text)

    def close(self):
        sys.exit()

    def load_notes(self):
        self.text_area.clear()
        self.list_area.clear()

        notes_list = os.listdir('notes')
        for note in notes_list:
            self.list_area.addItem(note)


    def open_file(self, item):
        path = 'notes/' + item.text()

        with open(path, 'r', encoding='utf-8') as file:
            text = file.read()
            self.text_area.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec())