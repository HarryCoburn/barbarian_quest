import dearpygui.dearpygui as dpg

dpg.create_context()

# Store hex data
hexes = [
    {"game_pos": (5, 5), "screen_x": 100, "screen_y": 100, "radius": 30},
    {"game_pos": (6, 5), "screen_x": 200, "screen_y": 100, "radius": 30},
]

def hex_clicked(sender, app_data):
    mouse_pos = dpg.get_mouse_pos(local=True)
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    
    for hex_data in hexes:
        dx = mouse_x - hex_data["screen_x"]
        dy = mouse_y - hex_data["screen_y"]
        distance = (dx*dx + dy*dy) ** 0.5
        
        if distance <= hex_data["radius"]:
            print(f"Clicked hex at game position {hex_data['game_pos']}")
            break

with dpg.window(label="Barbarian Quest", tag="main"):
    with dpg.drawlist(width=800, height=600, tag="canvas") as canvas:
        # Draw hexes as circles
        for hex_data in hexes:
            dpg.draw_circle(
                center=(hex_data["screen_x"], hex_data["screen_y"]),
                radius=hex_data["radius"],
                color=(100, 200, 100),
                fill=(50, 100, 50)
            )
    
with dpg.item_handler_registry(tag="canvas_handler") as handler:
    dpg.add_item_clicked_handler(callback=hex_clicked)
dpg.bind_item_handler_registry("canvas", "canvas_handler") 

dpg.create_viewport(title='Barbarian Quest', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("main", True)
dpg.start_dearpygui()
dpg.destroy_context()

