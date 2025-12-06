from tests.ui.unified_component import UnifiedComponent


def test_nested_item_property_access():
    nested = UnifiedComponent(id="nested-btn", text="Nested Button")
    component = UnifiedComponent(id="prop-access-1", nested=nested)
    
    rendered = component._render()
    
    assert rendered == """<div id="prop-access-1" class="test-component">
    <div class="nested">
        <p>Nested component ID: nested-btn</p>
        <p>Nested component text: Nested Button</p>
        <div id="nested-btn" class="test-component">
    <div class="text">Nested Button</div>
</div>

    </div>
</div>

<script>console.log('Button loaded');</script>"""

