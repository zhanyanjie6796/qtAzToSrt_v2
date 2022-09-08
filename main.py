from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFrame
import sys
from Ui_win import Ui_Form # 把win的類匯入讓這邊可以用
 
class MainFrame(QFrame, Ui_Form):
    #AzKey，AzRegion,全域變數。
    set_AzKey    = ""
    set_AzRegion = "" 
    
    def __init__(self, parent=None):
        super(MainFrame, self).__init__(parent) # 調用父類把子類對象轉為父類對象     
        # 調用介面
        self.setupUi(self) 
        
        # 信號         
        self.pushButton_importKeyRegion.clicked.connect(self.calculation_importKeyRegion) # 信號與槽連接
        self.pushButton_OpenFile.clicked.connect(self.calculation_OpenFile) # 信號與槽連接
        self.pushButton_Transcribe.clicked.connect(self.calculation_Transcribe) # 信號與槽連接
        self.pushButton.clicked.connect(self.calculation) # 信號與槽連接
        self.pushButton.setGeometry(QtCore.QRect(390, 400, 104, 0)) ##設定後面 0，0 讓 pushButton 按鈕消失。
        self.lineEdit.setGeometry(QtCore.QRect(20, 430, 481, 0))   ##設定後面 0 讓 lineEdit 文字方塊消失。
        
    # 自訂槽函數_匯入AzKey，AzRegion，目前暫時放程式裏面。
    def calculation_importKeyRegion(self):     
        #從 config.json 匯入 AzureSubscriptionKey 和 AzureServiceRegion        
        path = "config.json" 
        f = None
        try: 
            # 開啓檔案
            # f = open(path, 'r',encoding="utf-8") #都是英文的檔案可能不需要 utf-8
            f = open(path, 'r')
            self.textEdit.append("從 config.json 檔匯入 Key / Region \n")
            
            import json
            #json 的資料形式字串
            # strjson = '{"firstName": "Allen", "lastName":"Chen"}'
            strjson = f.read()
            #轉換json
            parsedJson = json.loads(strjson)
            # print(parsedJson['AzureSubscriptionKey']) 
            # print(parsedJson['AzureServiceRegion'])
            self.set_AzKey = parsedJson['AzureSubscriptionKey']
            self.set_AzRegion = parsedJson['AzureServiceRegion']
            f.close()            
        except IOError:
            print('ERROR: can not found ' + path)
            self.textEdit.append("匯入失敗\n")
            if f:
                f.close()
        finally:
            if f:
                f.close()
                
        self.lineEdit_AzKey.setText(self.set_AzKey) #全域變數 AzKey。
        self.lineEdit_AzRegion.setText(self.set_AzRegion) #全域變數 AzRegion。      
        
    # 自訂槽函數_開啓檔案
    def calculation_OpenFile(self): 
        #開啓檔案路徑與檔名。
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()
        #完整的路徑+檔名+副檔名
        file_path = filedialog.askopenfilename(parent=root, title='選擇檔案', filetypes=(("音頻檔案","*.wav"),("all files","*.*")))
        
        #路徑與檔名
        import os 
        file_path_path = os.path.split(file_path)[0]  # 路徑不含檔名。['/home/ubuntu/python', 'example.py']  的第二個欄位
        file_path_name = os.path.split(file_path)[1]  # 檔名包含副檔名
        file_path_name_left = os.path.splitext(file_path_name)[0] # 檔名【不】包含副檔名
       
        self.lineEdit_FilePath.setText(file_path) #顯示檔案路徑
        self.lineEdit_FileOutput.setText(file_path_path+"/"+file_path_name_left+".srt") #顯示輸出路徑
        
        # self.lineEdit.setText(file_path_path)
        # self.textEdit.append(file_path_name)
        # self.textEdit.append(file_path_name_left)

    # 自訂槽函數_轉換
    def calculation_Transcribe(self):          
        self.textEdit.append("轉換過程：")
        #執行轉換字幕的指令。
        cmd_str = "<now_path>captioning.exe --key <key> --region <region> --input <inputFile> --output <outputFile> --srt --recognizing --threshold 3 --profanity raw --phrases \"Contoso;Jessie;Rehaan\" --languages zh-TW"
        cmd_str = cmd_str.replace('<key>', self.lineEdit_AzKey.text()) #指令 <key>
        cmd_str = cmd_str.replace('<region>', self.lineEdit_AzRegion.text()) #指令 <region>

        #找出目前程式所在路徑
        import pathlib
        #print(str(pathlib.Path().absolute())+"\\")
        now_path = str(pathlib.Path().absolute())+"\\" #目前程式所在路徑
        # self.lineEdit.setText("程式所在路徑："+now_path)
        cmd_str = cmd_str.replace('<now_path>', now_path) #指令 <now_path>

        #輸入檔案的路徑 <inputFile>，和輸出檔案的路徑 <outputFile>        
        if self.lineEdit_FilePath.text() == "":#如果沒有【開啓檔案】，路徑是空的。
            self.textEdit.append("還沒【開啓檔案】\n")
            return
        self.textEdit.append("輸入檔案的路徑 <inputFile>")
        self.textEdit.append(self.lineEdit_FilePath.text()+"\n")
        cmd_str = cmd_str.replace('<inputFile>', self.lineEdit_FilePath.text()) #指令 <inputFile>
        
        self.textEdit.append("輸出檔案的路徑 <outputFile>")
        self.textEdit.append(self.lineEdit_FileOutput.text()+"\n")
        cmd_str = cmd_str.replace('<outputFile>', self.lineEdit_FileOutput.text()) #指令 <outputFile>

        #yanjie here home hh
        # self.textEdit.append(self.lineEdit_AzKey.text())
        # self.textEdit.append(self.lineEdit_AzRegion.text())
        self.textEdit.append("轉換指令如下：")        
        self.textEdit.append(cmd_str+"\n")
        
        #使用微軟的 Azure 開源碼 captioning.exe 進行字幕轉化
        import os    
        #os.system("Transcribe.bat")    
        #os.system(str(now_path)+"Transcribe.bat")
        # os.system("captioning.exe")
        os.system(cmd_str)
        self.textEdit.append("轉換完成") 



    # 自訂槽函數_測試 ansi to utf-8 , 去除"[zh-TW] "字串。
    def calculation(self):  
        #.setText方法讓文字顯示在lineEdit上
        #self.lineEdit.setText(self.lineEdit.text() +'彥杰\n') 
        self.textEdit.setText("")
        self.textEdit.append("開始轉換成【utf-8】格式的 srt 字幕檔案\n")
        
        #檔案格式整理:start ==========> ansi to utf-8 , 去除"[zh-TW] "字串。
        # path = '許院長開幕致詞.srt' 
        path = self.lineEdit_FileOutput.text() #輸出檔案的路徑 <outputFile>
        f = None
        try: 
            # 開啓檔案
            # f = open(path, 'r',encoding="utf-8") # 檔案是ansi不是utf-8
            f = open(path, 'r')
            fileText = f.read()
            # print(fileText)
            
            fileText_TranOutput = fileText.replace('[zh-TW] ', '') #字串'[zh-TW] '的地方取代為空白
            print(fileText_TranOutput)          
            f.close()
            
            f = open(path, 'w' , encoding="utf-8")
            f.write(fileText_TranOutput)
            f.close()
            self.textEdit.append("轉換完成\n")
            
            
        except IOError:
            print('ERROR: can not found ' + path)
            self.textEdit.append("轉換失敗\n")
            if f:
                f.close()
        finally:
            if f:
                f.close()       
        #檔案格式整理:end ==========>


#-------- main  主程式如下  --------------------------------          
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainFrame = MainFrame()
    mainFrame.show()
    sys.exit(app.exec_())         

