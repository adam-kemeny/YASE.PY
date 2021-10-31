import PySimpleGUI as gui
import youtube_dl
from constants import ICON, DESCRIPTION
gui.theme('BluePurple')


class YASE_UI():
    def __init__(self):
        self.LIST_VALUES = ['OPUS', 'OGG VORBIS', 'AAC (M4A/MP4)']
        self.LAYOUT = [
            [
                gui.Text('Please enter Youtube URL', key='1.text.Title')
            ],
            [
                gui.InputText(key='1.form.Url',
                              tooltip='Insert the URL here', enable_events=True)
            ],
            [
                gui.Button('OK', key='1.button.Submit',
                           bind_return_key=True, disabled=True),
                gui.Button(
                    'Clear', key='1.button.Reset', disabled=True),
            ],
            [
                gui.Combo(default_value=self.LIST_VALUES[0], values=self.LIST_VALUES, key='2.form.List',
                          visible=False)
            ],
            [
                gui.StatusBar(text=DESCRIPTION,
                              key='statusBar',
                              justification='right', expand_x='true',
                              pad=(0, (100, 0)))
            ]
        ]

    class updateUI():
        def submit(self):
            self.window['statusBar'].update(value='Fetching data...')
            self.window['1.text.Title'].update(visible=False)
            self.window['1.form.Url'].update(disabled=True)
            self.window['1.button.Submit'].update(visible=False)
            self.window['1.button.Reset'].update(visible=False)



    def run(self):
        self.window = gui.Window('YASE.PY', self.LAYOUT, finalize=True,
                                 icon=ICON, right_click_menu=['', ['Paste']])
        while True:
            event, value = self.window.read()

            if (event == '1.button.Submit' and value['1.form.Url']):
                # YASE_UI Operations
                self.updateUI().submit
                # youtube-dl data fetch
                try:
                    result = youtube_dl.YoutubeDL({
                        # 'format': 'bestaudio/best',
                        # 'format': '251',
                        'simulate': True,
                        'listformats': True,
                    }).extract_info(value['1.form.Url'])
                    self.window['2.form.List'].update(
                        visible=True, values=self.LIST_VALUES)
                    self.window['statusBar'].update(value=DESCRIPTION)
                except:
                    self.window['statusBar'].update(value='ERROR')
                    self.window['1.button.Reset'].update(visible=True)

            if value['1.form.Url']:
                self.window['1.button.Submit'].update(disabled=False)
                self.window['1.button.Reset'].update(disabled=False)
            else:
                self.window['1.button.Submit'].update(disabled=True)
                self.window['1.button.Reset'].update(disabled=True)

            if event == '1.button.Reset':
                self.window.close()
                self.reset()
                break

            if event == gui.WIN_CLOSED:
                self.window.close()
                break

    def reset(self):
        del self.LAYOUT
        self.__init__()
        self.run()


instance = YASE_UI().run()
