from tests.ui.button import Button


def test_button_render():
    button = Button(id="test-button", text="Click Me")    
    rendered = button.render()
    expected = '<button id="test-button">Click Me</button>\n<script>console.log(\'Button loaded\');</script>'
    
    assert str(rendered) == expected

