from pyjinhx import Registry
from tests.ui.unified_component import UnifiedComponent


def test_component_registry():
    Registry.clear()
    
    component1 = UnifiedComponent(id="simple-1", text="Hello")
    component2 = UnifiedComponent(id="btn-1", text="Click")
    
    registry = Registry.get()
    
    assert "simple-1" in registry
    assert "btn-1" in registry
    assert registry["simple-1"] == component1
    assert registry["btn-1"] == component2
    assert len(registry) == 2

