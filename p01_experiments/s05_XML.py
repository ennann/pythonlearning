from lxml import etree
import requests

note = """
<note>
<to>Tove</to>
<from>Jani</from>
<heading>Reminder</heading>
<body>
    Don't forget me this weekend!
    <div class="wsx_fade"/>
    <div class="wsx_scroll">
    <div class="wsx_scroll_bar"/>
    </div>
    <div class="niu_fade"/>
    <div class="niu_scroll">
    <div class="niu_scroll_bar"/>
    </div>
</body>
</note>
"""

tree = etree.XML(note)
results = tree.xpath("/note/text()")
print(results)
