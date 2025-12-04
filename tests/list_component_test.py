from tests.ui.button import Button
from tests.ui.button_list import ButtonList
from tests.ui.container import Container


def test_list_component():
    button1 = Button(id="btn-1", text="First Button")
    button2 = Button(id="btn-2", text="Second Button")
    button3 = Button(id="btn-3", text="Third Button")
    
    button4 = Button(id="btn-4", text="Fourth Button")
    button5 = Button(id="btn-5", text="Fifth Button")
    
    button_list1 = ButtonList(
        id="list-1",
        title="Action Buttons",
        buttons=[button1, button2, button3]
    )
    
    button_list2 = ButtonList(
        id="list-2",
        title="More Buttons",
        buttons=[button4, button5]
    )
    
    container = Container(
        id="container-1",
        name="Button Container",
        button_lists=[button_list1, button_list2]
    )
    
    rendered = container.render()
    
    assert rendered == """<div id="container-1" class="container">
    <h1>Button Container</h1>
    <div class="container-content">
        
        <div class="list-wrapper">
            <div id="list-1" class="button-list">
    <h3>Action Buttons</h3>
    <ul>
        
        <li><button id="btn-1">First Button</button></li>
        
        <li><button id="btn-2">Second Button</button></li>
        
        <li><button id="btn-3">Third Button</button></li>
        
    </ul>
</div>

        </div>
        
        <div class="list-wrapper">
            <div id="list-2" class="button-list">
    <h3>More Buttons</h3>
    <ul>
        
        <li><button id="btn-4">Fourth Button</button></li>
        
        <li><button id="btn-5">Fifth Button</button></li>
        
    </ul>
</div>

        </div>
        
    </div>
</div>

<script>console.log('Button loaded');</script>"""

