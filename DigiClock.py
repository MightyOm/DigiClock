import sys
import winreg
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QSizeGrip, QMenu
from PyQt6.QtCore import Qt, QTimer, QTime
from PyQt6.QtGui import QFont, QFontDatabase, QPainter, QPen, QColor


def get_windows_accent_color():
    try:
        registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        key = winreg.OpenKey(registry, r'Software\Microsoft\Windows\DWM')
        value, _ = winreg.QueryValueEx(key, 'ColorizationColor')
        winreg.CloseKey(key)
        color_hex = f"{value:08x}"
        return f"#{color_hex[2:]}"
    except Exception:
        return "#00FF00"


class OutlinedLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text_color = QColor("white")
        self.border_width = 3
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)

    def set_text_color(self, qcolor):
        self.text_color = qcolor
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        text = self.text()
        rect = self.rect()
        painter.setFont(self.font())

        painter.setPen(QPen(Qt.GlobalColor.black, self.border_width))
        for dx in [-2, -1, 0, 1, 2]:
            for dy in [-2, -1, 0, 1, 2]:
                if dx != 0 or dy != 0:
                    painter.drawText(rect.adjusted(dx, dy, dx, dy), Qt.AlignmentFlag.AlignCenter, text)

        painter.setPen(QPen(self.text_color))
        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, text)


class DigiClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = OutlinedLabel(self)
        self.timer = QTimer(self)
        self.drag_position = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle("DigiClock")
        self.setMinimumSize(300, 100)
        self.resize(600, 200)

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

        vbox = QVBoxLayout()
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            my_font = QFont(font_family, 120)
        else:
            my_font = QFont("Arial", 120, QFont.Weight.Bold)
        self.time_label.setFont(my_font)

        self.grip = QSizeGrip(self)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)

        accent_color_hex = get_windows_accent_color()
        base_color = QColor(accent_color_hex)

        hue = base_color.hue()
        if hue == -1:
            hue = 240

        neon_color = QColor()
        neon_color.setHsv(hue, 255, 255)

        self.time_label.set_text_color(neon_color)


    def paintEvent(self, event):
        """Paints a nearly invisible background so Windows registers clicks anywhere on the widget."""
        painter = QPainter(self)
        # Alpha is 1 out of 255. Invisible to the human eye, solid to Windows.
        painter.fillRect(self.rect(), QColor(0, 0, 0, 1))


    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.drag_position is not None:
            self.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()


    def contextMenuEvent(self, event):
        context_menu = QMenu(self)


        context_menu.setStyleSheet("""
            QMenu { background-color: #222; color: white; border: 1px solid #444; }
            QMenu::item:selected { background-color: #444; }
        """)

        minimize_action = context_menu.addAction("Minimize")
        close_action = context_menu.addAction("Close")

        action = context_menu.exec(self.mapToGlobal(event.pos()))
        if action == close_action:
            self.close()
        elif action == minimize_action:
            self.showMinimized()


    def resizeEvent(self, event):

        width_based_size = int(self.width() * 0.18)
        height_based_size = int(self.height() * 0.7)


        new_size = max(15, min(width_based_size, height_based_size))

        font = self.time_label.font()
        font.setPointSize(new_size)
        self.time_label.setFont(font)

        self.grip.move(self.width() - self.grip.width(), self.height() - self.grip.height())
        super().resizeEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigiClock()
    clock.show()
    sys.exit(app.exec())