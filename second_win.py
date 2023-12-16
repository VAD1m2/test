from final_win import *


class Experiment():
   def __init__(self, age, test1, test2, test3):
       self.age = age
       self.t1 = test1
       self.t2 = test2
       self.t3 = test3


class TestWin(QWidget):
   def __init__(self):
       ''' окно, в котором проводится опрос '''
       super().__init__()


       # создаём и настраиваем графические элементы:
       self.initUI()


       #устанавливает связи между элементами
       self.connects()


       #устанавливает, как будет выглядеть окно (надпись, размер, место)
       self.set_appear()
      
       # старт:
       self.show()


   ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
   def set_appear(self):
       self.setWindowTitle(txt_title)
       self.resize(win_width, win_height)
       self.move(win_x, win_y)


   def initUI(self):
       ''' создаёт графические элементы '''
       self.btn_next = QPushButton(txt_sendresults, self)
       self.btn_test1 = QPushButton(txt_starttest1, self)
       self.btn_test2 = QPushButton(txt_starttest2, self)
       self.btn_test3 = QPushButton(txt_starttest3, self)