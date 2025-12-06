from tests.ui.unified_component import UnifiedComponent


def test_empty_list():
    component = UnifiedComponent(
        id="empty-list-1",
        title="Empty List",
        items=[]
    )
    
    rendered = component.render()
    
    assert rendered == """<script>console.log('Button loaded');</script>
<div id="empty-list-1" class="test-component">
    <h2>Empty List</h2>
</div>
"""


def test_empty_dict():
    component = UnifiedComponent(
        id="empty-dict-1",
        title="Empty Dict",
        sections={}
    )
    
    rendered = component.render()
    
    assert rendered == """<script>console.log('Button loaded');</script>
<div id="empty-dict-1" class="test-component">
    <h2>Empty Dict</h2>
</div>
"""


def test_component_with_only_id():
    component = UnifiedComponent(id="minimal-1")
    
    rendered = component.render()
    
    assert rendered == """<script>console.log('Button loaded');</script>
<div id="minimal-1" class="test-component">
</div>
"""


def test_none_values_in_nested():
    component = UnifiedComponent(
        id="none-values-1",
        title="None Values",
        nested=None,
        items=None,
        sections=None
    )
    
    rendered = component.render()
    
    assert rendered == """<script>console.log('Button loaded');</script>
<div id="none-values-1" class="test-component">
    <h2>None Values</h2>
</div>
"""

