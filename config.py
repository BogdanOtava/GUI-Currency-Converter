import pathlib

ROOT = pathlib.Path(__file__).parent

# Replaces the icon of the app
IMAGE = ROOT.joinpath("window_icon.ico")

# Type and Size of the font used within the interface
FONT_TYPE = "franklin gothic medium"
FONT_SIZE = 10

# Changes the source of the data
DATA_SOURCE = "imf"