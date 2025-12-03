import pytest
from jinja2 import Environment, FileSystemLoader
from pyjinx import BaseComponent, Registry
from tests.ui.button import Button
import os


@pytest.fixture
def jinja_env():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env = Environment(loader=FileSystemLoader(root_dir))
    BaseComponent.set_engine(env)
    yield env
    Registry.clear()


def test_button_render(jinja_env):
    button = Button(id="test-button", text="Click Me")    
    rendered = button.render()
    expected = '<button id="test-button">Click Me</button>\n<script>console.log(\'Button loaded\');\n\n</script>'
    
    assert str(rendered) == expected

