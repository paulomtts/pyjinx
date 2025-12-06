from pyjinhx.base import Object
from markupsafe import Markup
from tests.ui.unified_component import UnifiedComponent


def test_object_with_props_none():
    obj = Object(html="<span>Test HTML</span>", props=None)
    
    assert obj.html == "<span>Test HTML</span>"
    assert obj.props is None
    assert str(obj) == Markup("<span>Test HTML</span>")


def test_object_str_method():
    obj = Object(html="<div>Content</div>", props=None)
    
    result = str(obj)
    
    assert result == "<div>Content</div>"
    assert isinstance(result, str)


def test_object_with_component_props():
    component = UnifiedComponent(id="obj-test-1", text="Object Test")
    
    obj = Object(html="<div>Rendered</div>", props=component)
    
    assert obj.html == "<div>Rendered</div>"
    assert obj.props == component
    assert obj.props.id == "obj-test-1"
    assert obj.props.text == "Object Test"


def test_object_in_template_context():
    component = UnifiedComponent(
        id="wrapper-obj-1",
        title="Wrapper",
        nested=UnifiedComponent(id="nested-obj-1", text="Nested")
    )
    
    rendered = component.render()
    
    assert "nested-obj-1" in str(rendered)
    assert "Nested component ID: nested-obj-1" in str(rendered)
    assert "Nested component text: Nested" in str(rendered)


def test_object_from_extra_html():
    component = UnifiedComponent(
        id="extra-html-obj-1",
        text="Test",
        html=["tests/ui/extra_content.html"]
    )
    
    rendered = component.render()
    
    assert "Extra HTML Content" in str(rendered)
    assert "<span>Extra HTML Content</span>" in str(rendered)

