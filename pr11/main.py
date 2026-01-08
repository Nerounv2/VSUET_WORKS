from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

from PyQt5 import QtCore, QtGui, QtWidgets

import requests
from pprint import pprint


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Основной вертикальный layout для окна
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)  # Отступы от краев
        self.verticalLayout.setSpacing(10)  # Расстояние между элементами
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Layout для поля ввода и метки
        self.inputLayout = QtWidgets.QHBoxLayout()
        self.inputLayout.setSpacing(10)
        self.inputLayout.setObjectName("inputLayout")
        
        # Метка для поля ввода
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setText("GitHub username:")
        self.inputLayout.addWidget(self.label)
        
        # Поле для ввода названия репозитория
        self.usernameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameInput.setObjectName("usernameInput")
        self.usernameInput.setPlaceholderText("Введите имя пользователя GitHub")
        self.inputLayout.addWidget(self.usernameInput)
        
        # Добавляем layout с полем ввода в основной verticalLayout
        self.verticalLayout.addLayout(self.inputLayout)
        
        # ListWidget будет растягиваться
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        
        # Горизонтальный layout для кнопок
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        # Кнопка "Вывести данные"
        self.pullButton = QtWidgets.QPushButton(self.centralwidget)
        self.pullButton.setMouseTracking(False)
        self.pullButton.setObjectName("pullButton")
        self.horizontalLayout.addWidget(self.pullButton)
        
        # Кнопка "Очистить поле"
        self.clearBurron = QtWidgets.QPushButton(self.centralwidget)
        self.clearBurron.setObjectName("clearBurron")
        self.horizontalLayout.addWidget(self.clearBurron)
        
        # Добавляем горизонтальный layout с кнопками в вертикальный
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pullButton.setText(_translate("MainWindow", "Вывести данные"))
        self.clearBurron.setText(_translate("MainWindow", "Очистить поле"))

    def pull_info(self, username):
        url = f"https://api.github.com/users/{username}"
        user_data = requests.get(url).json()

        info_dict = {
                        'company': user_data["company"],
                        'created_at': user_data["created_at"],
                        'email': user_data["email"],
                        'id': user_data["id"],
                        'name': user_data["name"],
                        'url': user_data["url"],
        }

        # Очищаем listWidget перед добавлением новых данных
        self.listWidget.clear()
        
        # Добавляем данные в listWidget
        for key, value in info_dict.items():
            self.listWidget.addItem(f"{key}: {value}")

        with open("pr11/pr11_result.txt", "w") as f:
            for key, value in info_dict.items():
                f.write(f"{key}: {value}\n")




class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Инициализация интерфейса
        
        # Подключаем кнопку к методу
        self.pullButton.clicked.connect(self.on_pull_button_clicked)
        # Подключаем кнопку очистки
        self.clearBurron.clicked.connect(self.on_clear_button_clicked)
        # Подключаем Enter в поле ввода к той же функции
        self.usernameInput.returnPressed.connect(self.on_pull_button_clicked)
    
    def on_pull_button_clicked(self):
        """Обработчик нажатия кнопки 'Вывести данные'"""
        username = self.usernameInput.text().strip()
        if username:
            self.pull_info(username)
        else:
            # Если поле пустое, показываем сообщение
            self.listWidget.clear()
            self.listWidget.addItem("Введите имя пользователя GitHub")
    
    def on_clear_button_clicked(self):
        """Обработчик нажатия кнопки 'Очистить поле'"""
        self.listWidget.clear()
        self.usernameInput.clear()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':

    username = "Automattic"
   
    
    main()


