
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QCheckBox, QLineEdit, QPushButton, QListWidgetItem, QListWidget
)
from PyQt5.QtCore import Qt

class ToDoList(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List")
        self.setGeometry(100, 100, 400, 500)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout() # 수직박스 레이아웃

        # 입력창과 추가 버튼
        input_layout = QHBoxLayout() # 수평 레이아웃

        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("할 일을 입력하세요")

        self.add_button = QPushButton("추가")
        self.add_button.clicked.connect(self.add_task)

        input_layout.addWidget(self.task_input)
        input_layout.addWidget(self.add_button)

        # To-do list를 위한 QListWidget
        self.todo_list = QListWidget()

        layout.addLayout(input_layout)
        layout.addWidget(self.todo_list)
        self.setLayout(layout)


    def add_task(self):
        task_text = self.task_input.text().strip() # 앞 뒤 공백제거
        if task_text:
            item = QListWidgetItem()
            checkbox = QCheckBox(task_text)
            checkbox.stateChanged.connect(self.toggle_task) # conntect 는 체크 상태가 바뀔때마다 자동으로 toggle_task() 함수 실행
                                                            # 즉, 한번 연결하면 이후 이벤트가 발생할 때 마다 자동으로 실행됨 (QT의 이벤트기반 시스템)
            self.todo_list.addItem(item) # 리스트에 item 추가
            self.todo_list.setItemWidget(item, checkbox)
            self.task_input.clear() # 입력차 비움

    def toggle_task(self, state):
        checkbox = self.sender() # 이벤트 발생 객체 반환
        font = checkbox.font() 
        font.setStrikeOut(state == Qt.Checked) # Qt.Checked = True or False / setStrikeOut = 줄긋기
        checkbox.setFont(font) # 글꼴 설정

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoList()
    window.show()
    sys.exit(app.exec_())
