from ..models.gamestate import GameState
import dearpygui.dearpygui as dpg


class HexGrid:
    def __init__(self, radius, spacing):
        self.radius = radius
        self.spacing = spacing

    def game_to_screen(self, game_pos):
        x, y = game_pos
        screen_x = x * self.spacing
        screen_y = y * self.spacing
        return screen_x, screen_y


class View:
    def __init__(self, game_state: GameState):
        self.game_state = game_state

        with dpg.window(label="Barbarian Quest", tag="main_window") as self.main_window:
            with dpg.group(horizontal=True):
                with dpg.child_window(width=200, height=600, tag="left_panel"):
                    with dpg.group(tag="stats_group") as self.stats_container:
                        self.days_text = dpg.add_text(f"Days: {game_state.days}")
                        self.food_text = dpg.add_text(f"Food: {game_state.food}")
                        self.gold_text = dpg.add_text(f"Gold: {game_state.gold}")
                        self.endurance_text = dpg.add_text(f"Endurance: {game_state.endurance}")

                    dpg.add_separator()

                    with dpg.group(tag="button_group") as self.button_container:
                        pass

                with dpg.child_window(width=600, height=600, tag="right_panel"):
                    with dpg.child_window(height=400, tag="map_window"):
                        self.map_canvas = dpg.add_drawlist(width=580, height=380)

                    with dpg.child_window(height=180, tag="info_window") as self.info_container:
                        self.info_text = dpg.add_text(
                            default_value="Welcome to Barbarian Quest!",
                            wrap=560
                        )

    def update_stats(self, game_state: GameState):
        dpg.set_value(self.days_text, f"Days: {game_state.days}")
        dpg.set_value(self.food_text, f"Food: {game_state.food}")
        dpg.set_value(self.gold_text, f"Gold: {game_state.gold}")
        dpg.set_value(self.endurance_text, f"Endurance: {game_state.endurance}")

    def update_info(self, text: str):
        current_text = dpg.get_value(self.info_text)
        new_text = current_text + "\n" + text
        dpg.set_value(self.info_text, new_text)