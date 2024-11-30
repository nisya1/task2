import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QSlider
from PyQt6.QtGui import QPainter, QColor
from PyQt6 import uic
import io
from random import randrange

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>340</x>
      <y>250</y>
      <width>131</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Кнопка</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class GoodMoodRising(QMainWindow):
    def __init__(self):
        super().__init__()
        self.size = 100
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.dopaint = False
        self.pushButton.clicked.connect(self.drawe)

    def drawe(self):
        self.dopaint = True
        self.update()

    def paintEvent(self, event):
        if self.dopaint:
            qp = QPainter()
            qp.begin(self)
            self.drawelipse(qp)
            qp.end()
        self.dopaint = False

    def drawelipse(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        qp.setPen(QColor(255, 255, 0))
        for _ in range(randrange(5, 20)):
            d = randrange(10, 100)
            qp.drawEllipse(randrange(10, 700), randrange(10, 500), d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GoodMoodRising()
    ex.show()
    sys.exit(app.exec())
