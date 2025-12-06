from tests.ui.unified_component import UnifiedComponent


def test_basic_rendering():
    component = UnifiedComponent(id="simple-1", text="Hello World")
    rendered = component._render()
    expected = '<script>console.log(\'Button loaded\');</script>\n<div id="simple-1" class="test-component">\n    <div class="text">Hello World</div>\n</div>\n'
    
    assert str(rendered) == expected


def test_basic_rendering_with_js():
    component = UnifiedComponent(id="test-button", text="Click Me")    
    rendered = component._render()
    expected = '<script>console.log(\'Button loaded\');</script>\n<div id="test-button" class="test-component">\n    <div class="text">Click Me</div>\n</div>\n'
    
    assert str(rendered) == expected

