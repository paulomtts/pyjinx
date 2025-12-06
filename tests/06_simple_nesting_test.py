from tests.ui.unified_component import UnifiedComponent


def test_simple_nesting():
    nested = UnifiedComponent(id="action-btn", text="Click Me")
    component = UnifiedComponent(
        id="wrapper-1",
        title="My Wrapper",
        nested=nested
    )
    
    rendered = component._render()
    
    assert rendered == """<div id="wrapper-1" class="test-component">
    <h2>My Wrapper</h2>
    <div class="nested">
        <p>Nested component ID: action-btn</p>
        <p>Nested component text: Click Me</p>
        <div id="action-btn" class="test-component">
    <div class="text">Click Me</div>
</div>

    </div>
</div>

<script>console.log('Button loaded');</script>"""


def test_simple_nesting_with_extra_html():
    nested = UnifiedComponent(id="action-btn", text="Click Me")
    component = UnifiedComponent(
        id="wrapper-1",
        title="My Wrapper",
        nested=nested,
        html=["tests/ui/extra_content.html"]
    )
    
    rendered = component._render()
    
    assert rendered == """<div id="wrapper-1" class="test-component">
    <h2>My Wrapper</h2>
    <div class="nested">
        <p>Nested component ID: action-btn</p>
        <p>Nested component text: Click Me</p>
        <div id="action-btn" class="test-component">
    <div class="text">Click Me</div>
</div>

    </div><span>Extra HTML Content</span>
</div>

<script>console.log('Button loaded');</script>"""

