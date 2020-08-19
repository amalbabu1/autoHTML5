# automatic html creater using PySimpleGui
import webbrowser
import PySimpleGUI as sg
import codecs
import htmllib


def gen(title, body, headsize, color):
    f = codecs.open("htmlge\index.html", "w", "utf-8")
    print(title, body)
    htmlgen = htmllib.head(title)
    htmlgen += htmllib.body(body, headsize, color)
    f.write(htmlgen)
    f.close()


heading_size = ['h1', 'h2', 'h3', 'h4', 'h5']
heading_color = ['blue', 'green', 'red']
sg.theme('DarkBlack1')
layout = [[sg.Text("html Generator")],
          [sg.Text("title"), sg.InputText(key='title')],
          [sg.Text("Body"), sg.InputText(key='body')],
          [sg.Listbox(values=heading_size, size=(5, 1),
                      key='headsize', enable_events=True), sg.Listbox(values=heading_color, size=(7, 1),
                                                                      key='color', enable_events=True)],
          [sg.Button("Generate")], [sg.Button("Render")]]

window = sg.Window("HTMLGEN", layout)

while True:
    event, values = window.read()
    if event == "Generate":
        gen(values['title'], values['body'],
            values['headsize'][0], values['color'][0])
    if event == "Render":
        webbrowser.open("htmlge\index.html")
        break

    if event == sg.WIN_CLOSED:
        break
window.close()
