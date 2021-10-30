import PySimpleGUI as gui
import youtube_dl
gui.theme('BluePurple')

# CONSTS
LIST_VALUES = ['OPUS', 'OGG VORBIS', 'AAC (M4A/MP4)']
DESCRIPTION = 'YASE.PY 0.1'
LAYOUT = [
    [
        gui.Text('Please enter Youtube URL', key='1.text.Title')
    ],
    [
        gui.InputText(key='1.form.Url',
                      right_click_menu=['', ['Paste']],
                      tooltip='Insert the URL here')
    ],
    [
        gui.Button('OK', key='1.button.Ok', bind_return_key=True),
        gui.Button(
            'Clear', key='1.button.Clear'),
    ],
    [
        gui.Combo(default_value=LIST_VALUES[0], values=LIST_VALUES, key='2.form.List',
                  visible=False)
    ],
    [
        gui.StatusBar(text=DESCRIPTION,
                      key='statusBar',
                      justification='right', expand_x='true',
                      #   size=(100),
                      pad=(0, (100, 0)))
    ]
]
window = gui.Window('YASE.PY', LAYOUT, finalize=True)

while True:
    event, value = window.read()

    if (event == '1.button.Ok' and value['1.form.Url']):
        # UI Operations
        window['statusBar'].update(value='Fetching data...')
        window['1.text.Title'].update(visible=False)
        window['1.form.Url'].update(disabled=True)
        window['1.button.Ok'].update(visible=False)
        window['1.button.Clear'].update(visible=False)
        # youtube-dl data fetch

        result = youtube_dl.YoutubeDL({
            # 'format': 'bestaudio/best',
            # 'format': '251',
            'simulate': True,
            'listformats': True,
        }).extract_info(value['1.form.Url'])
        window['2.form.List'].update(
            visible=True, values=LIST_VALUES)
        window['statusBar'].update(value=DESCRIPTION)

    if event == '1.button.Clear':
        print('clear input field')
        window['1.form.Url'].update('')

    if event == 'Exit' or event == gui.WIN_CLOSED:
        break
window.close()
