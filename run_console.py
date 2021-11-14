from src.Interfaces.Console.PygameInstance import PygameInstance
import os
os.environ["SDL_VIDEODRIVER"] = "x11"
PygameInstance().run()
