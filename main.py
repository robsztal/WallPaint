import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from matplotlib.streamplot import Grid
from rooms import House


class MainPage(GridLayout):
    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)
        self.rooms = []
        self.init_main_page(None)

    def house_popup(self, instance):
        self.house_popup_instance = Popup(title="Add house")

        content = GridLayout(cols=1)
        content_cancel = Button(text='Cancel', size_hint_y=None, height=40)
        content_submit = Button(text='Submit')
        content_cancel.bind(on_press=self.house_popup_instance.dismiss)
        content_submit.bind(on_press=self.save_house_rooms)
        content.add_widget(Label(text="How many rooms?"))
        self.rooms_text = TextInput()
        content.add_widget(self.rooms_text)
        content.add_widget(content_cancel)
        content.add_widget(content_submit)
        self.house_popup_instance.content = content
        self.house_popup_instance.open()
        self.rooms_button.disabled = False
        return

    def save_house_rooms(self, instance):
        self.rooms_num = int(self.rooms_text.text)
        return self.house_popup_instance.dismiss()

    def init_main_page(self, instance):
        self.clear_widgets()
        self.rooms_num = 0
        self.cols = 2

        self.house_button = Button(text="Add house")
        self.house_button.bind(on_press=self.house_popup)
        self.add_widget(self.house_button)

        self.rooms_button = Button(text="Edit rooms", disabled=True)
        self.rooms_button.bind(on_press=self.move_to_house_page)
        self.add_widget(self.rooms_button)

    def move_to_house_page(self, instance):
        self.clear_widgets()

        self.house = House(self.rooms_num)
        self.cols = 2

        for i in range(self.rooms_num):
            new_button = Button(id=i, text=f"Room-{i+1}", on_press=self.room_popup)
            self.add_widget(new_button)
        
        self.add_widget(Button(text="Reset house", on_press=self.init_main_page))
        self.add_widget(Button(text="Reset rooms", on_press=self.move_to_house_page))

    def move_to_room_planning(self, instance):
        self.clear_widgets()
        for i in range(self.rooms_num):
            new_button = Button(text=f"{self.rooms[i]}", on_press=self.room_planner)
            self.add_widget(new_button)


    def room_popup(self, instance):
        self.room_popup_instance = Popup(title="Room edition")

        content = GridLayout(cols=2)
        content_cancel = Button(text='Cancel')
        content_submit = Button(text='Submit')
        content_cancel.bind(on_press=self.room_popup_instance.dismiss)
        content_submit.bind(on_press=lambda *args: self.save_rooms(self.room_name, *args))
        content.add_widget(content_cancel)
        content.add_widget(content_submit)

        content.add_widget(Label(text="Room name"))
        self.room_name = TextInput()
        content.add_widget(self.room_name)

        content.add_widget(Label(text="Walls symetrical?"))
        self.symetrical = CheckBox()
        content.add_widget(self.symetrical)

        content.add_widget(Label(text="How many walls?"))
        self.walls_num = TextInput()
        content.add_widget(self.walls_num)
        

        self.room_popup_instance.content = content
        self.room_popup_instance.open()
        return

    def save_rooms(self, instance):
        self.rooms.append(self.room_name.text)
        self.house.add_room(self.symetrical.active, int(self.walls_num.text), self.room_name.text)

    def room_planner(self, instance):
        pass
        # self.house.rooms[self.]

class WallPainter(App):
    def build(self):
        return MainPage()
    

WallPainter().run()