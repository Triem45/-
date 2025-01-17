import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from GlobalVariable import global_obj,refresh_frequency
from GenUsers import total_size
from Main import SetWndIcon
class Ui_UserLoginWnd(object):
    def __init__(self):
        self.location = -1
        self.time_num = -1
        self.if_like = 0
        self.if_comment = 0
        self.if_share = 0

    def setupUi(self, UserLoginWnd):
        UserLoginWnd.setObjectName("UserLoginWnd")
        UserLoginWnd.resize(961, 794)
        SetWndIcon(UserLoginWnd) 
        self.listToPlay = QtWidgets.QListWidget(UserLoginWnd)
        self.listToPlay.setGeometry(QtCore.QRect(100, 260, 321, 451))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.listToPlay.setFont(font)
        self.listToPlay.setObjectName("listToPlay")
        self.label = QtWidgets.QLabel(UserLoginWnd)
        self.label.setGeometry(QtCore.QRect(130, 20, 221, 41))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(UserLoginWnd)
        self.textEdit.setGeometry(QtCore.QRect(360, 20, 221, 41))
        self.textEdit.setObjectName("textEdit")
        self.listHistory = QtWidgets.QListWidget(UserLoginWnd)
        self.listHistory.setGeometry(QtCore.QRect(530, 260, 301, 451))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.listHistory.setFont(font)
        self.listHistory.setObjectName("listHistory")
        self.label_2 = QtWidgets.QLabel(UserLoginWnd)
        self.label_2.setGeometry(QtCore.QRect(630, 210, 131, 51))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(UserLoginWnd)
        self.label_3.setGeometry(QtCore.QRect(170, 210, 161, 51))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Query = QtWidgets.QPushButton(UserLoginWnd)
        self.Query.setGeometry(QtCore.QRect(630, 20, 141, 41))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(18)
        self.Query.setFont(font)
        self.Query.setObjectName("Query")
        self.Share = QtWidgets.QPushButton(UserLoginWnd)
        self.Share.setGeometry(QtCore.QRect(670, 170, 141, 41))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(20)
        self.Share.setFont(font)
        self.Share.setObjectName("Share")
        self.Comment = QtWidgets.QPushButton(UserLoginWnd)
        self.Comment.setGeometry(QtCore.QRect(400, 170, 141, 41))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(20)
        self.Comment.setFont(font)
        self.Comment.setObjectName("Comment")
        self.Praise = QtWidgets.QPushButton(UserLoginWnd)
        self.Praise.setGeometry(QtCore.QRect(160, 170, 141, 41))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(20)
        self.Praise.setFont(font)
        self.Praise.setObjectName("Praise")
        self.lineEdit = QtWidgets.QLineEdit(UserLoginWnd)
        self.lineEdit.setGeometry(QtCore.QRect(280, 110, 401, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.Query_2 = QtWidgets.QPushButton(UserLoginWnd)
        self.Query_2.setGeometry(QtCore.QRect(700, 110, 141, 41))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(14)
        self.Query_2.setFont(font)
        self.Query_2.setObjectName("Query_2")
        self.label_4 = QtWidgets.QLabel(UserLoginWnd)
        self.label_4.setGeometry(QtCore.QRect(410, 60, 151, 51))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_bg = QtWidgets.QLabel(UserLoginWnd)
        self.label_bg.setGeometry(QtCore.QRect(0, 0, UserLoginWnd.width(), UserLoginWnd.height()))  # 设置背景图片大小为窗口大小
        self.label_bg.setPixmap(QtGui.QPixmap(r'C:\Users\27879\Desktop\SVRemmendation\xuexiao.jpg').scaled(UserLoginWnd.width(), UserLoginWnd.height()))  # 使用scaled方法将图片缩放到窗口大小
        opacity_effect = QtWidgets.QGraphicsOpacityEffect()
        opacity_effect.setOpacity(0.5)  # 设置透明度，值范围为0（完全透明）到1（完全不透明）
        self.label_bg.setGraphicsEffect(opacity_effect)

        self.label_bg.setAlignment(QtCore.Qt.AlignCenter)  # 设置对齐方式为居中
        self.label_bg.setObjectName("label_bg")
        # 将背景图片放置在窗口中心，不需要再手动计算位置
        self.label_bg.move(0, 0)

        # 将背景图片置于底层
        self.label_bg.lower()


        self.retranslateUi(UserLoginWnd)
        self.Query.clicked.connect(self.get_in_user) # type: ignore
        self.Praise.clicked.connect(self.like) # type: ignore
        self.Comment.clicked.connect(self.comment) # type: ignore
        self.Share.clicked.connect(self.share) # type: ignore
        self.Query_2.clicked.connect(self.clicked_play)
        QtCore.QMetaObject.connectSlotsByName(UserLoginWnd)

    def retranslateUi(self, UserLoginWnd):
        _translate = QtCore.QCoreApplication.translate
        UserLoginWnd.setWindowTitle(_translate("UserLoginWnd", "用户登陆"))
        self.label.setText(_translate("UserLoginWnd", "请输入用户 uid："))
        self.label_2.setText(_translate("UserLoginWnd", "历史记录"))
        self.label_3.setText(_translate("UserLoginWnd", "待播放视频"))
        self.Query.setText(_translate("UserLoginWnd", "登录用户"))
        self.Share.setText(_translate("UserLoginWnd", "分享"))
        self.Comment.setText(_translate("UserLoginWnd", "评论"))
        self.Praise.setText(_translate("UserLoginWnd", "点赞"))
        self.Query_2.setText(_translate("UserLoginWnd", "下一个视频"))
        self.label_4.setText(_translate("UserLoginWnd", "当前播放"))

    def like(self):
        self.if_like = 1
    def comment(self):
        self.if_comment = 1
    def share(self):
        self.if_share = 1

    def get_in_user(self):
        self.time_num = -1
        self.listToPlay.clear()
        self.listHistory.clear()
        self.lineEdit.clear()#进行初始化

        uid = self.textEdit.toPlainText()
        if total_size < int(uid):
            # QtWidgets.QMessageBox.warning(self,'警告', '用户不存在，请重新输入')
            self.textEdit.clear()
        else:
            self.location = int(uid)-1
            #QtWidgets.QMessageBox.information(self,'通知', '登录用户成功')

    def clicked_play(self):
        if self.time_num == -1:
            global_obj.GlobalUserList[self.location].HelpRefreshWeight()

            for item in global_obj.GlobalUserList[self.location].temp_play_list:

                for i in global_obj.GlobalVideoList:
                    if item[0] == i.uid:
                        index = global_obj.GlobalVideoList.index(i)
                        name = global_obj.GlobalVideoList[index].name
                        category = global_obj.GlobalVideoList[index].category##获得视频的名字和分类
                        break
                self.listToPlay.addItem(str(item[0])+str(name)+str(category))
            self.time_num = self.time_num + 1

        else:
            text_listToPlay = self.listToPlay.item(0)
            first_item_text = text_listToPlay.text()
            self.lineEdit.setText(first_item_text)
            first_letter = first_item_text[0] ###获取video编号 便于后续点赞等操作

            global_obj.GlobalUserList[self.location].history_list.append(int(first_letter))###插入用户观看的历史数据 便于更新权重计算

            for j in global_obj.GlobalVideoList:
                if int(first_letter) == j.uid:
                    index = global_obj.GlobalVideoList.index(j)
                    global_obj.GlobalVideoList[index].user_watch(self.location,self.if_like,self.if_comment,self.if_share)

            item_del = self.listToPlay.takeItem(0)
            del item_del

            if self.time_num >=1:
                self.listHistory.addItem(self.lineEdit.text())
            self.time_num = self.time_num + 1

            if self.time_num == refresh_frequency:
                self.listHistory.clear()
                self.time_num = -1
                #QtWidgets.QMessageBox.warning(self,'提醒', '权重已完成更新，请重新浏览视频')
                return
            weight=(1,2,3)
            score=weight[0]*self.if_like+weight[1]* self.if_comment+weight[2]*self.if_share
            if self.listToPlay:
               global_obj.add_videoscore(self.location,first_letter,score)
        self.if_like = 0
        self.if_comment = 0
        self.if_share = 0  #对每一个视频的点击后点赞等进行初始化

class UserLoginWndLogic:
    def __init__(self):
        self.location = -1
        self.time_num = -1
        self.if_like = 0
        self.if_comment = 0
        self.if_share = 0
        self.listToPlay = []

    def get_in_user(self, uid):
        self.time_num = -1
        self.if_like = 0
        self.if_comment = 0
        self.if_share = 0

        if total_size >= int(uid):
                self.location = int(uid) - 1
        else:
            raise ValueError(f"Invalid user ID: {uid} exceeds total user count")
    def like(self):
        self.if_like = 1

    def comment(self):
        self.if_comment = 1

    def share(self):
        self.if_share = 1

    def clicked_play(self):
        if self.time_num == -1: 
            global_obj.GlobalUserList[self.location].HelpRefreshWeight()
            temp_play_list = global_obj.GlobalUserList[self.location].temp_play_list
            for item in temp_play_list:
                video_uid = item[0]
                name = None
                category = None
                for i in global_obj.GlobalVideoList:
                    if video_uid == i.uid:
                        name = i.name
                        category = i.category
                        break
                self.listToPlay.append(f"{item[0]}{name}{category}")
            self.time_num = self.time_num + 1

        else:
            if self.listToPlay:
                first_item_text = self.listToPlay.pop(0)
                first_letter = first_item_text[0]
            else: print("hhhhh")  # 或其他可能引发的异常
            global_obj.GlobalUserList[self.location].history_list.append(int(first_letter))
            for j in global_obj.GlobalVideoList:
                if int(first_letter) == j.uid:
                    index = global_obj.GlobalVideoList.index(j)
                    global_obj.GlobalVideoList[index].user_watch(self.location, self.if_like, self.if_comment, self.if_share)
            self.time_num = self.time_num + 1
            if self.time_num == refresh_frequency:
                self.time_num = -1
            weight=(1,2,3)
            score=weight[0]*self.if_like+weight[1]* self.if_comment+weight[2]*self.if_share
            if self.listToPlay:
               global_obj.add_videoscore(self.location,first_letter,score)
        self.if_like = 0
        self.if_comment = 0
        self.if_share = 0  #对每一个视频的点击后点赞等进行初始化
                
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_UserLoginWnd()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
   