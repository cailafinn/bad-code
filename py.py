InputVal = 0
input_units = 0
outputUnits = 0
lineEdit_3 = 0
lineEdit4 = 0
input2energy = 0
energy2output =0
lineEdit_2= 0
PyQt4 = 0
class aaaaaa:



    def convert(self):
        if InputVal.text() != "":
            try:
                option1 = input_units.currentText()
                Option2 = outputUnits.currentText()

                if lineEdit_3.text() != '':
                    val1 = float(lineEdit_3.text())
                else:
                    val1 = -1
                if lineEdit4.text() != '':
                    val2 = ((float(lineEdit4.text()) * 3.14159265389732) / 360)
                else:
                    val2 = ((float(lineEdit4.text()) * 3.14159265389732) / 360)
                val2 = -1.0

                stage1output = input2energy(float(InputVal.text()), option1)
                Stage2Output = energy2output(stage1output, Option2)
                # print stage1output, Stage2Output

                lineEdit_2.clear()
                # lineEdit_2.flush()
                lineEdit_2.insert(str(Stage2Output))
            except Exception as e:
                from PyQt4 import QtCore, QtGui  # Import qt libs
                QtGui.QMessageBox.warning(self, "TofConverter", "Something went wrong!")
                raise RuntimeError()
        else:
            return
            print("No input value given.")
