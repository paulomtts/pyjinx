import os
from jinja2 import Environment, FileSystemLoader
from pyjinhx import BaseComponent, Registry
from tests.ui.unified_component import UnifiedComponent


def test_set_engine():
    original_engine = BaseComponent._engine
    
    custom_root = os.path.join(os.getcwd(), "tests")
    custom_env = Environment(loader=FileSystemLoader(custom_root))
    BaseComponent.set_engine(custom_env)
    
    assert BaseComponent._engine == custom_env
    assert BaseComponent._engine.loader.searchpath[0] == custom_root
    
    BaseComponent.set_engine(original_engine)


def test_detect_root_directory():
    root_dir = BaseComponent._detect_root_directory()
    
    assert os.path.exists(root_dir)
    assert os.path.exists(os.path.join(root_dir, "pyproject.toml"))


def test_component_reuse():
    shared_component = UnifiedComponent(id="shared-1", text="Shared Component")
    
    component = UnifiedComponent(
        id="parent-1",
        title="Parent",
        items=[shared_component, shared_component, shared_component]
    )
    
    rendered = component.render()
    
    assert 'shared-1' in str(rendered)
    assert str(rendered).count('shared-1') >= 3
    assert "Shared Component" in str(rendered)


def test_registry_in_template_context():
    Registry.clear()
    
    UnifiedComponent(id="global_component", text="Global Component")
    
    component = UnifiedComponent(
        id="parent-1",
        title="Parent",
        text="Parent Text"
    )
    
    template_source = """
    <div id="{{ id }}">
        <h1>{{ title }}</h1>
        <p>{{ text }}</p>
        {% if global_component %}
        <div class="global">{{ global_component }}</div>
        {% endif %}
    </div>
    """
    
    rendered = component._render(source=template_source)
    
    assert "Global Component" in str(rendered)
    assert "global_component" in str(rendered)


def test_html_method():
    component = UnifiedComponent(id="auto-1", text="Auto Render")
    
    rendered = component.__html__()
    
    assert rendered == """<div id="auto-1" class="test-component">
    <div class="text">Auto Render</div>
</div>

<script>console.log('Button loaded');</script>"""

