import PySimpleGUI as gui
gui.theme('BluePurple')

layout = [
    [
        gui.Text('Please enter Youtube URL', key='1.text.Title')
    ],
    [
        gui.InputText(key='1.form.Url',
                      right_click_menu=['', ['Paste']])
    ],
    [
        gui.Button('OK', key='1.button.Ok'),
        gui.Button(
            'Clear', key='1.button.Clear'),
    ],
    [
        gui.Text('test', key='ttt', visible=False)
    ]
]
window = gui.Window('YASE.PY', layout, margins=(220, 120))

while True:
    event, value = window.read()
    if (event == '1.button.Ok' and value['1.form.Url']):
        window['1.text.Title'].update(visible=False)
        window['1.form.Url'].update(disabled=True)
        window['1.button.Ok'].update(visible=False)
        window['1.button.Clear'].update(visible=False)
        window['ttt'].update(visible=True)
    if event == 'Clear':
        print('clear input field')
        window['1.form.Url'].update('')
    if event == 'Exit' or event == gui.WIN_CLOSED:
        break
window.close()
