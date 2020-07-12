from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager

Window.size = (300, 500)

navigation_helper = """
ScreenManager:
    LoginScreen:
    MenuScreen:
    RegisterScreen1:
    RegisterScreen2:


<LoginScreen>:
    name: 'Login'
    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            title: 'Demo App'
            elevation: 5

        Screen:
            MDCard:
                title: 'Login'
                orientation: "vertical"
                padding: "15dp"
                size_hint: [0.8, 0.45]
                pos_hint: {"center_x": .5, "center_y": .6}
                size: "280dp", "180dp"
                
                MDTextField:
                    hint_text: "Username"

                MDTextField:
                    hint_text: "Password"

                Widget:

                MDRoundFlatButton:
                    text: "Login"
                    pos_hint: {"center_x": .5}
                    on_release:
                        root.manager.current = 'Menu'
                        root.manager.transition.direction = "left"
        

<MenuScreen>:
    name: 'Menu'

    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            title: 'Demo App'
            elevation: 5

        Screen:
            MDCard:
                title: 'Login'
                orientation: "vertical"
                padding: "10dp"
                size_hint: [0.8, 0.7]
                pos_hint: {"center_x": .5, "center_y": .5}
                size: "280dp", "180dp"

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            MDTextButton:
                                text: 'Add a Student'
                                font_size: "18sp"
                                pos_hint: {'center_x': 0.58, 'center_y': 0.5}
                                text_color: 0, 0, 1, 1
                                on_release: 
                                    root.manager.current = 'Register1'
                                    root.manager.transition.direction = "left"
                                    
                            IconLeftWidget:
                                icon: 'face-profile'
                                user_font_size: "30sp"

                        OneLineIconListItem:
                            MDTextButton:
                                text: "Mark Attendance"
                                font_size: "18sp"
                                pos_hint: {'center_x': 0.64, 'center_y': 0.5}
                                on_release:
                                    
                            IconLeftWidget:
                                icon: 'checkbox-marked-outline'
                                user_font_size: "30sp"

        MDIconButton:
            icon: "keyboard-return"
            user_font_size: "30sp"
            pos_hint: {"center_x": 0.15, "center_y": 0.2}
            on_release:
                root.manager.current = 'Login'
                root.manager.transition.direction = "right"


<RegisterScreen1>:
    name: 'Register1'

    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            title: 'Demo App'
            elevation: 5

        Screen:
            MDCard:
                title: 'Login'
                orientation: "vertical"
                padding: "10dp"
                size_hint: [0.85, 0.8]
                pos_hint: {"center_x": .5, "center_y": .6}
                size: "280dp", "180dp"

                Screen:
                    BoxLayout:
                        orientation: 'vertical'
                        ScrollView:
                            MDList:
                                MDTextField:
                                    hint_text: "First Name"

                                MDTextField:
                                    hint_text: "Middle Name"

                                MDTextField:
                                    hint_text: "Last Name"

                                MDTextField:
                                    hint_text: "D.O.B."

                                MDTextField:
                                    hint_text: "Gender"

                                MDTextField:
                                    hint_text: "Mobile"

                                MDTextField:
                                    hint_text: "Email"
            MDRaisedButton:
                text: "Next"
                pos_hint: {"center_x": 0.78, "center_y": .12}
                on_release:
                    root.manager.current = 'Register2'
                    root.manager.transition.direction = "left"
            MDRaisedButton:
                text: "Back"
                pos_hint: {"center_x": 0.22, "center_y": .12}
                on_release:
                    root.manager.current = 'Menu'
                    root.manager.transition.direction = "right"                           


<RegisterScreen2>
    name: 'Register2'

    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            title: 'Demo App'
            elevation: 5

        Screen:
            MDCard:
                title: 'Login'
                orientation: "vertical"
                padding: "10dp"
                size_hint: [0.85, 0.6]
                pos_hint: {"center_x": .5, "center_y": .6}
                size: "280dp", "180dp"

                Screen:
                    BoxLayout:
                        orientation: 'vertical'
                        ScrollView:
                            MDList:
                                MDTextField:
                                    hint_text: "PRN"

                                MDTextField:
                                    hint_text: "Roll No."

                                MDTextField:
                                    hint_text: "Course"

                                MDTextField:
                                    hint_text: "Semester"

            MDRoundFlatButton:
                text: "Register"
                pos_hint: {"center_x": .5, "center_y": 0.2}
                on_release:
        
        MDIconButton:
            icon: "keyboard-return"
            user_font_size: "30sp"
            pos_hint: {"center_x": 0.12, "center_y": 0.2}
            on_release:
                root.manager.current = 'Register1'
                root.manager.transition.direction = "right"
                                
"""


class LoginScreen(Screen):
    pass


class MenuScreen(Screen):
    pass


class RegisterScreen1(Screen):
    pass


class RegisterScreen2(Screen):
    pass


sm = ScreenManager()
sm.add_widget(LoginScreen(name='Login'))
sm.add_widget(MenuScreen(name='Menu'))
sm.add_widget(RegisterScreen1(name='Register1'))
sm.add_widget(RegisterScreen1(name='Register2'))


class DemoApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Demo Page"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        self.sm = ScreenManager()
        super().__init__(**kwargs)

    def build(self):
        screen = Builder.load_string(navigation_helper)
        return screen


DemoApp().run()