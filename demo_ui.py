import dearpygui.dearpygui as dpg
from src.view.main_menu import MainMenu

dpg.create_context()

main_menu = MainMenu()

dpg.create_viewport(title='Barbarian Quest', width=850, height=650)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("main_menu_window", True)

dpg.start_dearpygui()
dpg.destroy_context()
