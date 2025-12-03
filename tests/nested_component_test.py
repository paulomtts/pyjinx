from tests.ui.card import Card
from tests.ui.button import Button


def test_nested_component():
    button = Button(id="action-btn", text="Click Me")
    card = Card(id="card-1", title="My Card", content=button, html=["tests/ui/span.html"])
    
    rendered = card.render()

    assert rendered == """<div id="card-1" class="card">
    <h2>My Card</h2>
    <div class="card-content">
        <button id="action-btn">Click Me</button>
        <span>Extra HTML Content</span>
    </div>
</div>
<script>console.log('Button loaded');
console.log('Card loaded');</script>"""

