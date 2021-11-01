import PySimpleGUI as gui
import youtube_dl
from constants import ICON, VERSION, TITLE
gui.theme('BluePurple')

ELEMENTS = {
    'statusBar': 'statusBar',
    'title': '1.text.Title',
    'formInput': '1.form.Url',
    'formSubmit': '1.button.Submit',
    'reset': '1.button.Reset',
    'formSelect': '2.form.List'
}

TRANSLATIONS = {
    'title': 'Please enter Youtube URL',
    'formInputTooltip': 'Insert the URL here',
    'formSubmitText': 'OK',
    'reset': 'Clear',
    'loading': 'Fetching data...',
    'error': 'ERROR'
}

FONT_STYLES = {
    'default': 'Tahoma 11',
    'highlight': 'Tahoma 11 italic'
}


class YASE_UI():
    def __init__(self):
        self.LIST_VALUES = ['OPUS', 'OGG VORBIS', 'AAC (M4A/MP4)']
        self.LAYOUT = [
            [
                gui.Text(
                    text=TRANSLATIONS['title'],
                    key=ELEMENTS['title']
                )
            ],
            [
                gui.InputText(
                    key=ELEMENTS['formInput'],
                    tooltip=TRANSLATIONS['formInputTooltip'],
                    enable_events=True
                )
            ],
            [
                gui.Button(
                    button_text=TRANSLATIONS['formSubmitText'],
                    key=ELEMENTS['formSubmit'],
                    bind_return_key=True,
                    disabled=True
                ),
                gui.Button(
                    button_text=TRANSLATIONS['reset'],
                    key=ELEMENTS['reset']
                )
            ],
            [
                gui.Combo(
                    default_value=self.LIST_VALUES[0],
                    values=self.LIST_VALUES,
                    key=ELEMENTS['formSelect'],
                    visible=False
                )
            ],
            [
                gui.StatusBar(
                    text=VERSION,
                    key=ELEMENTS['statusBar'],
                    justification='right',
                    expand_x='true',
                    pad=(0, (100, 0)),
                    text_color='white'
                )
            ]
        ]

    class updateUI():
        def submit(self):
            self.window[ELEMENTS['statusBar']].update(
                value=TRANSLATIONS['loading']
            )
            self.window[ELEMENTS['title']].update(
                visible=False
            )
            self.window[ELEMENTS['formInput']].update(
                disabled=True
            )
            self.window[ELEMENTS['formSubmit']].update(
                visible=False
            )
            self.window[ELEMENTS['reset']].update(
                visible=False
            )

    def run(self):
        self.window = gui.Window(
            title=TITLE,
            layout=self.LAYOUT,
            finalize=True,
            icon=ICON,
            right_click_menu=['', ['Paste']],
            font=FONT_STYLES['default']
        )
        while True:
            event, value = self.window.read()

            if (event == ELEMENTS['formSubmit'] and value[ELEMENTS['formInput']]):
                self.updateUI().submit
                # youtube-dl data fetch
                try:
                    result = youtube_dl.YoutubeDL({
                        # 'format': 'bestaudio/best',
                        # 'format': '251',
                        'simulate': True,
                        'listformats': True,
                    }).extract_info(
                        value[ELEMENTS['formInput']]
                    )
                    self.window[ELEMENTS['formSelect']].update(
                        visible=True,
                        values=self.LIST_VALUES
                    )
                    self.window[ELEMENTS['statusBar']].update(
                        value=VERSION
                    )
                except:
                    self.window[ELEMENTS['statusBar']].update(
                        value=TRANSLATIONS['error'],
                        text_color='red',
                        font=FONT_STYLES['highlight']
                    )
                    self.window[ELEMENTS['reset']].update(
                        visible=True
                    )

            if value[ELEMENTS['formInput']]:
                self.window[ELEMENTS['formSubmit']].update(disabled=False)
            else:
                self.window[ELEMENTS['formSubmit']].update(disabled=True)

            if event == ELEMENTS['reset']:
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
