from stockfish import Stockfish
import dearpygui.dearpygui as dpg

stockfish = Stockfish(path="stockfish_15.1_win_x64_avx2/stockfish_15.1_win_x64_avx2/stockfish-windows-2022-x86-64-avx2.exe")
stockfish.set_position(["e2e4", "e7e6"])

print(stockfish.get_best_move())
dpg.create_context()

with dpg.window(tag="Primary Window"):
    dpg.add_text("Hello, world")
    dpg.add_button(label="press me")

dpg.create_viewport(title='chess by vitya', width=200, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()


# Start the event loop.
window = Window()
window.mainloop()

