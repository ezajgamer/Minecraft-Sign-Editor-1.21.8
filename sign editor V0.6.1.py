import sys
import json
import datetime
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QComboBox, QCheckBox, QPushButton, QTextEdit, QColorDialog
)
from PySide6.QtGui import QColor, QPalette, Qt

# All sign types in Minecraft 1.21.8 including hanging signs
SIGN_TYPES = [
    'oak_sign','spruce_sign','birch_sign','jungle_sign','acacia_sign','dark_oak_sign',
    'mangrove_sign','cherry_sign','bamboo_sign','warped_sign','crimson_sign',
    'oak_wall_sign','spruce_wall_sign','birch_wall_sign','jungle_wall_sign','acacia_wall_sign',
    'dark_oak_wall_sign','mangrove_wall_sign','cherry_wall_sign','bamboo_wall_sign',
    'warped_wall_sign','crimson_wall_sign',
    'oak_hanging_sign','spruce_hanging_sign','birch_hanging_sign','jungle_hanging_sign','acacia_hanging_sign',
    'dark_oak_hanging_sign','mangrove_hanging_sign','cherry_hanging_sign','bamboo_hanging_sign',
    'warped_hanging_sign','crimson_hanging_sign'
]

# Facings for wall signs
FACINGS = ['north','east','south','west']

# Arrow indicators for standing and hanging sign rotation
ROT_ARROWS = ['↑','↗','→','↘','↓','↙','←','↖']
ARROW_TO_IDX = {arrow: idx*2 for idx, arrow in enumerate(ROT_ARROWS)}

def generate_command(sign_type, glow, lines, facing=None, rotation=None):
    messages = []
    for text, color, bold, italic in lines:
        part = {"text": text, "color": color}
        if bold: part['bold'] = True
        if italic: part['italic'] = True
        messages.append(part)
    sign_data = {"has_glowing_text": 1 if glow else 0, "messages": messages}
    be_tag = json.dumps(sign_data, separators=(',', ':'))
    if sign_type.endswith('_wall_sign'):
        prop = f'facing={facing}'
    else:
        idx = ARROW_TO_IDX.get(rotation, 0)
        prop = f'rotation={idx}'
    return f"/setblock ~ ~ ~ {sign_type}[{prop}]{{front_text:{be_tag}}} replace"

class SignEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("sign editor V0.6.1.py")
        self.resize(800, 680)
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        top_layout = QHBoxLayout()
        layout.addLayout(top_layout)

        top_layout.addWidget(QLabel("Sign Type:"))
        self.sign_type = QComboBox()
        self.sign_type.addItems(SIGN_TYPES)
        self.sign_type.currentTextChanged.connect(self.on_sign_type_change)
        top_layout.addWidget(self.sign_type)

        self.facing_label = QLabel("Facing:")
        top_layout.addWidget(self.facing_label)
        self.facing = QComboBox()
        self.facing.addItems(FACINGS)
        top_layout.addWidget(self.facing)

        self.rotation_label = QLabel("Rotation:")
        top_layout.addWidget(self.rotation_label)
        self.rotation = QComboBox()
        self.rotation.addItems(ROT_ARROWS)
        top_layout.addWidget(self.rotation)

        self.glow = QCheckBox("Glowing Text")
        top_layout.addWidget(self.glow)

        self.line_edits = []
        self.colors = ['#FFFFFF'] * 4
        for i in range(4):
            row = QHBoxLayout()
            layout.addLayout(row)
            row.addWidget(QLabel(f"Line {i+1}:"))
            text_edit = QLineEdit()
            text_edit.setPlaceholderText("Enter text...")
            row.addWidget(text_edit)
            color_btn = QPushButton("Pick Color")
            color_btn.clicked.connect(lambda _, idx=i: self.choose_color(idx))
            row.addWidget(color_btn)
            bold_cb = QCheckBox("Bold")
            row.addWidget(bold_cb)
            italic_cb = QCheckBox("Italic")
            row.addWidget(italic_cb)
            self.line_edits.append((text_edit, color_btn, bold_cb, italic_cb))

        btn_layout = QHBoxLayout()
        layout.addLayout(btn_layout)
        gen_btn = QPushButton("Generate Command")
        gen_btn.clicked.connect(self.on_generate)
        btn_layout.addWidget(gen_btn)
        copy_btn = QPushButton("Copy to Clipboard")
        copy_btn.clicked.connect(self.on_copy)
        btn_layout.addWidget(copy_btn)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        pal = self.output.palette()
        pal.setColor(QPalette.Base, QColor('#1e1e1e'))
        pal.setColor(QPalette.Text, QColor('lightgreen'))
        self.output.setPalette(pal)
        layout.addWidget(self.output)

        signature = QLabel("Ezaj Gamer")
        signature.setAlignment(Qt.AlignCenter)
        signature.setStyleSheet("color: white; font-style: italic;")
        layout.addWidget(signature)

        version_label = QLabel(f"Version 0.6.1 - {datetime.date.today().isoformat()}")
        version_label.setAlignment(Qt.AlignCenter)
        version_label.setStyleSheet("color: white;")
        layout.addWidget(version_label)

        self.on_sign_type_change(self.sign_type.currentText())

    def on_sign_type_change(self, sign_type):
        is_wall = sign_type.endswith('_wall_sign')
        self.facing_label.setVisible(is_wall)
        self.facing.setVisible(is_wall)
        self.rotation_label.setVisible(not is_wall)
        self.rotation.setVisible(not is_wall)

    def choose_color(self, index):
        color = QColorDialog.getColor(QColor(self.colors[index]), self)
        if color.isValid():
            self.colors[index] = color.name()
            self.line_edits[index][1].setStyleSheet(f"background-color: {self.colors[index]}; color: white;")

    def on_generate(self):
        lines = [(te.text(), self.colors[i], cbold.isChecked(), citalic.isChecked())
                 for i, (te, _, cbold, citalic) in enumerate(self.line_edits)]
        cmd = generate_command(
            self.sign_type.currentText(),
            self.glow.isChecked(),
            lines,
            facing=self.facing.currentText(),
            rotation=self.rotation.currentText()
        )
        self.output.setPlainText(cmd)

    def on_copy(self):
        QApplication.clipboard().setText(self.output.toPlainText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SignEditor()
    window.show()
    sys.exit(app.exec())
