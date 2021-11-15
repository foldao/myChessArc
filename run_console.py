from src.Interfaces.Console.PygameInstance import PygameInstance
from src.Interfaces.Repositories.Cache.BoardStateRepoCache import BoardStateRepoCache

import os
os.environ["SDL_VIDEODRIVER"] = "x11"
PygameInstance(BoardStateRepoCache()).run()
