"""
Created on Tue Jan  1 13:41:18 2019

@author: Jamiu Ekundayo

References:    
1. http://www.pyqtgraph.org/documentation/qtcrashcourse.html
2. https://matplotlib.org/gallery/user_interfaces/embedding_in_qt_sgskip.html
3. https://sukhbinder.wordpress.com/2013/12/16/simple-pyqt-and-matplotlib-example-with-zoompan/
4. http://stackoverflow.com/questions/12459811/how-to-embed-matplotib-in-pyqt-for-dummies
5. https://stackoverflow.com/questions/42602713/how-to-set-a-window-icon-with-pyqt5
6. http://blog.rcnelson.com/building-a-matplotlib-gui-with-qt-designer-part-1/
7. https://stackoverflow.com/questions/43947318/plotting-matplotlib-figure-inside-qwidget-using-qt-designer-form-and-pyqt5
8. https://mplcursors.readthedocs.io/en/stable/
9. https://www.programcreek.com/python/example/104926/PyQt5.QtWidgets.QSizePolicy.Expanding
"""
import numpy as np
from math import *
from PyQt5 import QtWidgets, QtGui # (the example applies equally well to PySide)
#import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas, NavigationToolbar2QT as NavigationToolbar
import mplcursors   # for interactive selection of plot data. First install mplcursors with pip install mplcursors

## Always start by initializing Qt (only once per application)
app = QtWidgets.QApplication([])

## Define a top-level widget to hold everything
MainWindow = QtWidgets.QMainWindow()
MainWindow.setWindowTitle('FunctionPlotter')
MainWindow.setWindowIcon(QtGui.QIcon('my_icon.png'))
menubar = QtWidgets.QMenuBar(MainWindow)
MainWindow.setMenuBar(menubar)
file_menu = menubar.addMenu("&File")
save_action = QtWidgets.QAction("&Save_Plot_As", file_menu)
file_menu.addAction(save_action)
save_action.setShortcut('Ctrl+S')
save_action.setCheckable(True)

exit_action = QtWidgets.QAction("&Exit", file_menu)
file_menu.addAction(exit_action)
exit_action.setShortcut('Ctrl+Q')
exit_action.setCheckable(True)

help_menu = menubar.addMenu("&Help")
help_action = QtWidgets.QAction("help", help_menu)
help_menu.addAction(help_action)
help_action.setShortcut('F1')
help_action.setCheckable(True)

abt_menu = menubar.addMenu("A&bout")
abt_action = QtWidgets.QAction("about", abt_menu)
abt_menu.addAction(abt_action)
abt_action.setShortcut('F8')
abt_action.setCheckable(True)

w = QtWidgets.QWidget()

MainWindow.setCentralWidget(w)

## Create some widgets to be placed inside
plot_btn = QtWidgets.QPushButton('Plot Function')
font = QtGui.QFont()
font.setPointSize(9)
font.setBold(True)
font.setWeight(75)
plot_btn.setFont(font)
plot_btn.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

close_btn = QtWidgets.QPushButton('Close')
font = QtGui.QFont()
font.setPointSize(9)
font.setBold(True)
font.setWeight(75)
close_btn.setFont(font)
close_btn.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

func_label = QtWidgets.QLabel('Function, f(x)')
func_label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
func = QtWidgets.QLineEdit('x + 2*cos(4*x)')
func.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

minx_label = QtWidgets.QLabel('x_min')
minx_label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
minx = QtWidgets.QLineEdit('-5')
minx.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

maxx_label = QtWidgets.QLabel('x_max')
maxx_label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
maxx = QtWidgets.QLineEdit('5')
maxx.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

xstep_label = QtWidgets.QLabel('x_step')
xstep_label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
xstep = QtWidgets.QLineEdit('1')
xstep.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

plot_widget = Figure(dpi=100)
canvas = Canvas(plot_widget)

## Create a grid layout to manage the widgets size and position
layout = QtWidgets.QGridLayout()

w.setLayout(layout)

## Add widgets to the layout in their proper positions
layout.addWidget(func_label, 0, 0)   # button goes in upper-left
layout.addWidget(func, 0, 1)
layout.addWidget(minx_label,1, 0)
layout.addWidget(minx, 1, 1)
layout.addWidget(maxx_label, 2, 0)
layout.addWidget(maxx, 2, 1)
layout.addWidget(xstep_label, 3, 0)
layout.addWidget(xstep, 3, 1)
layout.addWidget(plot_btn, 11, 1)
layout.addWidget(close_btn, 12, 1)


layout.addWidget(canvas, 0, 2, 12, 8)  # plot goes on right side, spanning 12 rows & 8 columns

toolbar = NavigationToolbar(canvas, w)
toolbar.hide()

home_btn = QtWidgets.QPushButton('Home')
pan_btn = QtWidgets.QPushButton('Pan')
zoom_btn = QtWidgets.QPushButton('Zoom')
save_btn = QtWidgets.QPushButton('Save_Plot_As')
config_btn = QtWidgets.QPushButton('Configure')
edit_btn = QtWidgets.QPushButton('Edit')

export_btn = QtWidgets.QPushButton('Export Plot_data')

layout.addWidget(home_btn, 12, 2, 1, 1)
layout.addWidget(pan_btn, 12, 3, 1, 1)
layout.addWidget(zoom_btn, 12, 4, 1, 1)
layout.addWidget(save_btn, 12, 5, 1, 1)
layout.addWidget(config_btn, 12, 6, 1, 1)
layout.addWidget(edit_btn, 12, 7, 1, 1)
layout.addWidget(export_btn, 12, 8, 1, 1)


def home():
    toolbar.home()
def zoom():
    toolbar.zoom()
def pan():
    toolbar.pan()
def save():
    toolbar.save_figure()
def config_plot():
    toolbar.configure_subplots()
def edit_plot():
    toolbar.edit_parameters()

def evaluate():

    f_txt = func.text()
    xmin = float(minx.text())
    xmax = float(maxx.text())
    xsteps = float(xstep.text())
    
    if xmax <= xmin: 
        raise ValueError('xmax must be greater than xmin')
    elif xsteps <= 0 or xsteps > xmax:
        raise ValueError('step cannot be 0 or > xmax')

    else:

        xlist = np.arange(xmin, xmax, xsteps)

    ylist = []
    for x in xlist:
        y = eval(f_txt)
        ylist.append(y)
    return(f_txt, xmin, xmax, xsteps, xlist, ylist)
    
def plot_function():    
    data = evaluate()    
    f_txt = data[0]; xlist = data[-2]; ylist = data[-1];     
    ax = plot_widget.add_subplot(111)
    ax.clear()
    graph = ax.plot(xlist,ylist, "bo-")    
    ax.set_title('The graph of '+f_txt, fontsize=12, fontweight='bold')
    ax.set_xlabel('x-axis', fontsize=10, fontweight='bold')
    ax.set_ylabel(f_txt, fontsize=10, fontweight='bold')
    ax.grid()
    mplcursors.cursor(graph)
    #plt.ax.set_xlim(xmin-xsteps, xmax+xsteps)      
    canvas.draw() 
    

def save_data():
    data1 = evaluate()
    xlist = data1[-2]
    ylist = data1[-1]
    
    with open("plot_data.txt", "w") as file:
        file.writelines("x  y\n")
        for ind in range(len(xlist)):
            file.writelines(str("%.4f" %xlist[ind]) + "  " + str("%.4f" %ylist[ind]) +"\n")
        file.close()
    
def quit_func(event=None):
    MainWindow.close()

def help_msg():
    msg_widget = QtWidgets.QMessageBox()
    msg_widget.setWindowIcon(QtGui.QIcon('my_icon.png'))
    msg_widget.setText("Valid operators are:")
    msg_widget.setInformativeText("+ (addition) \n- (subtraction) \n* (multiplication) \n/ (division) \n** (exponent) \n \nClick on show details button below for examples")
    msg_widget.setWindowTitle("Function Plotter Help")
    msg_widget.setDetailedText("Ex.1.   x**2 \nEx.2. x*sin(x) \nEx.3. (x + sin(x))/cos(2*x)")
    msg_widget.setStandardButtons(msg_widget.Ok | msg_widget.Cancel)	
    msg_widget.exec_()

def abt_msg():
    abt_widget = QtWidgets.QMessageBox()
    abt_widget.setWindowIcon(QtGui.QIcon('my_icon.png'))
    abt_widget.setText("FunctionPlotter version 1.0\nCreated, developed & maintained by Jamiu Ekundayo\nLicenced under the terms and conditions of the MIT licence\nCopyright ©\nEmail: function_plotter@gmail.com\n\nThanks")
    abt_widget.setWindowTitle("About Function Plotter")
    abt_widget.setStandardButtons(abt_widget.Ok | abt_widget.Cancel)	
    abt_widget.exec_()


save_action.triggered.connect(save)
exit_action.triggered.connect(quit_func)
help_action.triggered.connect(help_msg)
abt_action.triggered.connect(abt_msg)

home_btn.clicked.connect(home)
pan_btn.clicked.connect(pan)
zoom_btn.clicked.connect(zoom)
save_btn.clicked.connect(save)
config_btn.clicked.connect(config_plot)
edit_btn.clicked.connect(edit_plot)
export_btn.clicked.connect(save_data)

plot_btn.clicked.connect(plot_function)

close_btn.clicked.connect(quit_func)


#func.textChanged.connect(plot_function)
#minx.textChanged.connect(plot_function)
#maxx.textChanged.connect(plot_function)
#xstep.textChanged.connect(plot_function)

## Display the widget as a new window
MainWindow.show()

## Start the Qt event loop
app.exec_()