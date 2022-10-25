# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 15:33:43 2022
Edited by Yiğit Leblebicier on Sun Oct 23 04:02:13 2022

@authors: Sinan Uğuz, Yiğit Leblebicier
"""

# =============================================================================
# Y = w1x1 + w2x2 + w3x3 + w4x4 + w5x5 + w6x6
# Girdi değerleri (x1,x2,x3,x4,x5,x6)=(args..)
# Bu denklemi maksimize eden parametreleri (ağırlıkları) bulmaya çalışıyoruz. 
# Pozitif giriş, olası en büyük pozitif sayı ile çarpılacak ve 
# negatif sayı, mümkün olan en küçük negatif sayı ile çarpılacaktır.
# GA, pozitif girdilerle pozitif ağırlıkları ve negatif girdilerle 
# negatif ağırlıkları kullanmanın daha iyi olduğunu bilmelidir.
# =============================================================================
from numpy import float64
import GA
from re import findall
def genetic_algorithm(ui):
    if ui.spinBox_sol_per_pop.value() > 0 and ui.lineEdit_inputs.text() != '' and ui.spinBox_gen_num.value() > 0 and ui.spinBox_parent_num.value() > 0:
        ui.plainTextEdit_output.clear()
        ui.pushButton.setEnabled(False)
        equation_inputs = [float64(input) for input in findall(r"[-+]?(?:\d*\.\d+|\d+)", ui.lineEdit_inputs.text())]
        num_weights = len(equation_inputs)  #Ağırlıkların sayısı,

        #Bir sonraki adım, başlangıç ​​popülasyonunu tanımlamaktır. 
        import numpy
        sol_per_pop = ui.spinBox_sol_per_pop.value()  #Popülasyon başına çözüm sayısı
        pop_size = (sol_per_pop,num_weights) #Herbiri num_weights adet genden oluşan sol_per_pop kadar kromozom

        #Başlangıç popülasyonunun numpy.random.uniform ile random oluşturulması
        new_population = numpy.random.uniform(low= -1 * ui.spinBox_low.value(), high=ui.spinBox_high.value(), size=pop_size)
        #print(new_population)

        num_generations = ui.spinBox_gen_num.value()
        num_parents_mating = ui.spinBox_parent_num.value()  #eşleşme havuzundaki birey sayısı
        console_output = str()
        max_gen = ([], [])
        table_data = list()
        for generation in range(num_generations):
            has_error = False
            try:
                max_gen[1].append(generation)
                console_output += "Generation : " + str(generation) + "\n"
                # Popülasyondaki her kromozom için uygunluk değerini hesapla
                fitness = GA.cal_pop_fitness(equation_inputs, new_population)
                #eşleşme havuzundaki en iyi bireylerin seçimi
                parents = GA.select_mating_pool(new_population, fitness, num_parents_mating)
                
                #Çaprazlama ile yeni birey üretimi
                offspring_crossover = GA.crossover(parents,
                                                offspring_size=(pop_size[0]-parents.shape[0], num_weights))
                #Mutasyon uygulanması
                offspring_mutation = GA.mutation(offspring_crossover)
                
                #Yeni popülasyon oluşturulması
                new_population[0:parents.shape[0], :] = parents
                new_population[parents.shape[0]:, :] = offspring_mutation
                
                #Geçerli iterasyondaki en iyi sonuç
                best_result = numpy.max(numpy.sum(new_population*equation_inputs, axis=1))
                max_gen[0].append(best_result)
                console_output += "Best result : " + str(best_result)+ "\n"
                del best_result
                #Tüm nesilleri bitirmeyi yineledikten sonra en iyi çözümü elde etmek için 
                #İlk olarak, son nesildeki her bir çözüm için uygunluk hesaplanır.
                fitness = GA.cal_pop_fitness(equation_inputs, new_population)
                
                #Ardından, bu çözümün en iyi uygunluğa karşılık gelen indeksini döndürün.
                best_match_idx = numpy.where(fitness == numpy.max(fitness))
                table_data.extend(new_population[best_match_idx, :][0][0])
                console_output += "Best solution : " + str(new_population[best_match_idx, :][0][0]) + "\n"
                table_data.extend(fitness[best_match_idx])
                console_output += "Best solution fitness : " + str(fitness[best_match_idx]) + "\n" + "----------------------------------------------" + "\n"
                ui.progressBar.setValue(int(((generation + 1)/num_generations)*100))
            except Exception as ex:
                ui.plainTextEdit_output.setPlainText('EXCEPTION : ' + str(ex))
                has_error = True
                break
        if not has_error:
            ui.plainTextEdit_output.setPlainText(console_output)
            ui.graphWidget.clear()
            ui.graphWidget.plot(max_gen[1], max_gen[0], pen='g', symbol='x',
                         symbolPen='g', symbolBrush=0.2, name='green')
            ui.graphWidget.showGrid(x=True, y=True, alpha=0.4)

            ui.tableWidget.setColumnCount(num_weights + 1)
            ui.tableWidget.setRowCount(len(max_gen[0]))
            horizontal_labels = ['Gene-' + str(index) for index in range(num_weights)]
            horizontal_labels.append('Maximum')
            ui.tableWidget.setHorizontalHeaderLabels(horizontal_labels)
            del horizontal_labels
            ui.tableWidget.setVerticalHeaderLabels(['Generation-' + str(row) for row in range(len(max_gen[0]))])

            table_data = [table_data[i:i+(num_weights + 1)] for i in range(0, len(table_data),(num_weights + 1))]

            from PyQt5.QtWidgets import QTableWidgetItem
            from PyQt5.QtGui import QColor
            for i in range(len(max_gen[0])):
                for j in range((num_weights + 1)) :
                        ui.tableWidget.setItem(i, j, QTableWidgetItem(str(table_data[i][j])))
                        if i > 0 and ui.tableWidget.item(i - 1, j).text() != ui.tableWidget.item(i, j).text():
                                #ui.tableWidget.item(i - 1, j).setBackground(QColor(100, 255, 100))
                                ui.tableWidget.item(i, j).setBackground(QColor(52, 97, 35))

            ui.tableWidget.resizeColumnsToContents()
            ui.tableWidget.resizeRowsToContents()
            ui.tableWidget.scrollToBottom()
    else:
        ui.plainTextEdit_output.setPlainText("INPUT ERROR!")
    ui.plainTextEdit_output.verticalScrollBar().setValue(ui.plainTextEdit_output.verticalScrollBar().maximum())
    ui.pushButton.setEnabled(True)

def write_results(ui):
    if (ui.plainTextEdit_output.toPlainText() != '' and ui.plainTextEdit_output.toPlainText() != 'INPUT ERROR!' and
    ui.plainTextEdit_output.toPlainText() != 'Error : There is no data!' and ui.plainTextEdit_output.toPlainText() != None):
        from uuid import uuid1
        with open(str(uuid1())+'.txt', 'w') as file:
            file.write(ui.plainTextEdit_output.toPlainText())
    else:
        ui.plainTextEdit_output.setPlainText('Error : There is no data!')

def prevent_negative_dimension(ui):
    ui.spinBox_parent_num.setMaximum(ui.spinBox_sol_per_pop.value())

def write_excel(ui):
    if ui.tableWidget.rowCount() > 0:
        from xlsxwriter import Workbook
        from uuid import uuid1
        excel_file = Workbook(str(uuid1())+ '.xlsx')
        worksheet = excel_file.add_worksheet(name= 'GaGui - Table')
        for row in range(ui.tableWidget.rowCount()):
            for column in range(ui.tableWidget.columnCount()):
                if row == 0:
                    worksheet.write(row, column, ui.tableWidget.horizontalHeaderItem(column).text())
                worksheet.write(row + 1, column, ui.tableWidget.item(row, column).text())
        excel_file.close()
    else:
        ui.plainTextEdit_output.setPlainText('Error : There is no data!')