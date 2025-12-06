import pytest
from jinja2 import Environment, DictLoader
from jinja2.exceptions import TemplateNotFound
from pyjinhx import BaseComponent, Registry
from tests.ui.unified_component import UnifiedComponent
from tests.ui.no_js_component import NoJsComponent


def test_invalid_empty_id():
    with pytest.raises(ValueError, match="ID is required"):
        UnifiedComponent(id="", text="Test")


def test_invalid_none_id():
    with pytest.raises(ValueError, match="ID is required"):
        UnifiedComponent(id=None, text="Test")


def test_missing_template_file():
    class MissingTemplateComponent(BaseComponent):
        id: str
        text: str
    
    component = MissingTemplateComponent(id="missing-1", text="Test")
    
    with pytest.raises(TemplateNotFound):
        component.render()


def test_missing_js_file_handles_gracefully():
    component = NoJsComponent(id="no-js-1", text="Test")
    
    rendered = component.render()
    
    assert rendered == """<div id="no-js-1">Test</div>
"""


def test_non_filesystem_loader_error():
    class TestComponent(BaseComponent):
        id: str
        text: str
    
    dict_loader = DictLoader({"template.html": "<div>{{ text }}</div>"})
    env = Environment(loader=dict_loader)
    BaseComponent.set_engine(env)
    
    component = TestComponent(id="test-1", text="Test")
    
    with pytest.raises(ValueError, match="Jinja2 loader must be a FileSystemLoader"):
        component.render()
    
    BaseComponent.set_engine(None)


def test_duplicate_component_id_warning(caplog):
    import logging
    logging.getLogger("pyjinhx").setLevel(logging.WARNING)
    
    Registry.clear()
    
    component1 = UnifiedComponent(id="duplicate-1", text="First")
    assert Registry.get()["duplicate-1"] == component1
    
    component2 = UnifiedComponent(id="duplicate-1", text="Second")
    
    assert len(Registry.get()) == 1
    assert Registry.get()["duplicate-1"] == component2
    
    assert "While registering" in caplog.text
    assert "duplicate-1" in caplog.text


def test_missing_extra_html_file():
    component = UnifiedComponent(
        id="missing-html-1",
        text="Test",
        html=["tests/ui/nonexistent.html"]
    )
    
    with pytest.raises(FileNotFoundError):
        component.render()


def test_missing_extra_js_file_handles_gracefully():
    component = UnifiedComponent(
        id="missing-js-1",
        text="Test",
        js=["tests/ui/nonexistent.js"]
    )
    
    rendered = component.render()
    
    assert '<div' in str(rendered)
    assert 'missing-js-1' in str(rendered)
    assert "console.log('Button loaded');" in str(rendered)
    assert "nonexistent" not in str(rendered)
