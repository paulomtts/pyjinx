from tests.ui.unified_component import UnifiedComponent


def test_basic_rendering_with_js_and_extra_js():
    component = UnifiedComponent(
        id="extra-js-1",
        text="Extra JS Component",
        js=["tests/ui/extra_script.js"]
    )
    rendered = component._render()
    
    assert rendered == """<div id="extra-js-1" class="test-component">
    <div class="text">Extra JS Component</div>
</div>

<script>console.log('Button loaded');
console.log('Extra script loaded');

</script>"""

