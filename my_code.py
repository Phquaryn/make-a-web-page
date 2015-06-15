import  pywapi
import string

noaa_result = pywapi.get_weather_from_noaa('KALB')

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

print generateHTML("How is the weather? ", "How's the weather? ")
print "NOAA says: It is " + string.lower(noaa_result['weather']) + " and " + noaa_result['temp_f'] + "F now in Albany, NY.\n"
