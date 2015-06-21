

def generateHTML(topic,description):
    html_text_1 = '''
<div class="concept">
    <div class="topic">
        ''' + topic
    html_text_2 = '''
    </div>
    <div class="description">
        ''' + description
    html_text_3 = '''
    </div>
</div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

print generateHTML("How are you?","How's the weather?")