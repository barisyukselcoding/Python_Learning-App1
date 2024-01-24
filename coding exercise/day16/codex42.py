"""
Write a script that generates the GUI that converts feet and inches into metres.

"""

import PySimpleGUI as Sg

label1 = Sg.Text("Enter feet:")
input1 = Sg.Input()

label2 = Sg.Text("Enter inches:")
input2 = Sg.Input()
convert_button = Sg.Button("Convert")

window = Sg.Window("File Compressor",
                   layout=[[label1, input1],
                           [label2, input2],
                           [convert_button]])

window.read()
window.close()
