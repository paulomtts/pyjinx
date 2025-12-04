from pyjinhx import BaseComponent
from tests.ui.button_list import ButtonList


class Container(BaseComponent):
    id: str
    name: str
    button_lists: list[ButtonList]

