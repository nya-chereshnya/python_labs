from PyQt5 import uic
import re
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication
from entities import Player, TownHall, Keep, Castle, Building
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog, QAction, QMainWindow
from PyQt5.QtGui import QColor
from PyQt5 import QtWidgets

import json

position = 0

Form, Window = uic.loadUiType("gui.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


player = Player()


def color_row(item):
    for row in range(len(player.units)):
        if row == item.row():
            continue
        for col in range(4):
            form.tableWidget.item(row, col).setBackground(
                QColor(255, 255, 255))

    for col in range(4):
        form.tableWidget.item(item.row(), col).setBackground(
            QColor(230, 230, 230))


def deselected():
    form.tableWidget.clearSelection()
    form.pushButton.setEnabled(False)
    form.pushButton_2.setEnabled(False)
    form.pushButton_4.setEnabled(False)
    form.pushButton_6.setEnabled(False)
    form.lineEdit.setEnabled(False)
    form.lineEdit_2.setEnabled(False)
    form.lineEdit.clear()
    form.lineEdit_2.clear()


def selected(item):
    global position
    position = item.row()
    color_row(item)
    form.pushButton.setEnabled(True)
    form.pushButton_2.setEnabled(True)
    form.pushButton_4.setEnabled(True)
    form.pushButton_6.setEnabled(True)
    form.lineEdit.setEnabled(True)
    form.lineEdit_2.setEnabled(True)
    return item.row()


def validate_input(input_text):
    try:
        input_text = int(input_text)
        return input_text
    except ValueError:
        QMessageBox.warning(window, "Warning", "Invalid input")
        return 0


def update_table(table_data):
    data_len = len(table_data)
    form.tableWidget.setRowCount(data_len)
    for row in range(data_len):
        id = row
        form.tableWidget.setItem(row, 0, QTableWidgetItem(str(id)))
        class_name = str(type(table_data[id]))
        match = re.match(r"<class '.*\.(\w+)'>", class_name)
        if match:
            class_name = match.group(1)
        form.tableWidget.setItem(row, 1, QTableWidgetItem(class_name))
        form.tableWidget.setItem(
            row, 2, QTableWidgetItem(str(table_data[id].level)))
        form.tableWidget.setItem(
            row, 3, QTableWidgetItem(str(table_data[id].HP)))


def update_balance():
    form.label_2.setText(str(player.gold))


def add_gold():
    data = validate_input(form.lineEdit_3.text())
    player.get_gold(data)
    form.label_2.setText(str(player.gold))
    form.lineEdit_3.clear()


def add_unit():
    player.add_unit()
    update_table(player.units)
    print(serialize())


def delete_unit():
    player.delete_unit(position)
    update_table(player.units)
    deselected()


def deal_damage():
    damage = validate_input(form.lineEdit.text())
    player.deal_damage(position, damage)
    update_table(player.units)
    deselected()


def heal():
    HP = validate_input(form.lineEdit_2.text())
    player.heal(position, HP)
    update_table(player.units)
    deselected()


def upgrade():
    player.buy_improvement(position)
    update_balance()
    update_table(player.units)
    deselected()


class Data:
    def __init__(self, player_gold, units) -> None:
        self.objs_data = units + [player_gold]

    def get_objs_array(self):
        return self.objs_data


class PlayerGold:
    def __init__(self, gold) -> None:
        self.gold = gold


def serialize():
    obj = Data(PlayerGold(player.gold), player.units)
    return json.dumps(obj.__dict__, default=lambda o: o.__dict__, indent=4)


def deserialize(json_str):
    data = json_str
    objs_data = data["objs_data"]
    objs = []
    for obj_data in objs_data:
        if "_level" in obj_data:
            level = obj_data["_level"]
            if level == 1:
                obj = TownHall(obj_data["_current_health"], obj_data["_max_health"],
                               obj_data["_armor"], obj_data["_cost"], obj_data["_level"])
            elif level == 2:
                obj = Keep(obj_data["_current_health"], obj_data["_max_health"],
                           obj_data["_armor"], obj_data["_cost"], obj_data["_level"])
            elif level == 3:
                obj = Castle(obj_data["_current_health"], obj_data["_max_health"],
                             obj_data["_armor"], obj_data["_cost"], obj_data["_level"])
        elif "gold" in obj_data:
            obj = PlayerGold(obj_data["gold"])
        else:
            continue
        objs.append(obj)

    return objs


def save_file():
    serialized_objs = serialize()
    print("wserwef")
    name, _ = QFileDialog.getSaveFileName(window, 'Save File')
    file = open(name, 'w')
    file.write(serialized_objs)
    file.close()


def load_data():
    file_name, _ = QFileDialog.getOpenFileName(
        None, "Open Data", "", "JSON Files (*.json)")
    if file_name:
        with open(file_name, 'r') as file:
            data = json.load(file)
        data = deserialize(data)
        player.gold = data[-1].gold
        player.units = data[:-1]
        update_balance()
        update_table(player.units)
        return data


update_table(player.units)
form.pushButton.clicked.connect(deal_damage)
form.pushButton_2.clicked.connect(heal)
form.pushButton_3.clicked.connect(add_gold)
form.pushButton_4.clicked.connect(upgrade)
form.pushButton_5.clicked.connect(add_unit)
form.pushButton_6.clicked.connect(delete_unit)

form.actionSave.triggered.connect(save_file)
form.actionOpen.triggered.connect(load_data)

form.tableWidget.itemClicked.connect(selected)


app.exec_()
