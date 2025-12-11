import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.window(label="Barbarian Quest", tag="main"):
    dpg.add_text("Click a hex to move")
    # We'll add hex drawing here

dpg.create_viewport(title='Barbarian Quest', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("main", True)
dpg.start_dearpygui()
dpg.destroy_context()

