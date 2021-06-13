#!/usr/bin/python3
# ==== LINE ABOVE IS MAGICKS! MUST BE FIRST LINE OF FILE =====

# =========== LINE BELOW IS ALSO MAGIC! ===========
# ======== Use "html" or "plain" as approp. ======= 
print("Content-Type: text/html\n")

# ====== NEXT LINE ALSO REQUIRED ======
print("")

import cgi
import cgitb
import trends

cgitb.enable()

descriptions = ['Six feet under', 'Terminally ill', 'Hospitalized, but likely recovery', 'Had a small accident, but not too bad', 'Consistently Healthy', 'Alive and well']

# ~~~~~~~~~~~~~~~ support functions ~~~~~~~~~~~~~~~
def fs2d():
    '''
    Convert return val of FieldStorage() into standard dictionary
    '''
    d = {}
    L = []
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

term = fs2d()['search']

html_header=""" <!DOCTYPE html>\n <!-- Clyde Sinclair
     IntroCS pd00 
     HWxx -- subj 
     yyyy-mm-dd
--> 
<html lang="en">
  <head>
    <meta charset="utf-8"/>
    <title>THAT TITLE BAR TEXT THO</title>
  </head>
  <body>
"""

html_footer="""
  </body>
</html>
"""

health = trends.status(term)
top_trends = ['a trend', 'a trend two', 'another trend', 'a fourth trend', 'this is the fifth trend', 'one more trend', 'even more trends', 'eighth trend', 'trend num.9', 'the last trend']

if health == 1:
	health_desc = 'Better than ever!'
	color = 'rgb(33, 190, 83)'
	text_shadow = 'rgb(0, 101, 39)'
elif health >= 0.75:
	health_desc = 'Alive and well'
	color = 'rgb(33, 190, 83)'
	text_shadow = 'rgb(0, 101, 39)'
elif health >= 0.30:
	health_desc = 'Consistently healthy'
	color = 'rgb(154, 199, 115)'
	text_shadow = 'rgb(69, 144, 37)'
elif health >= 0.15:
	health_desc = 'Had a small accident, but not too bad'
	color = 'rgb(201, 198, 101)'
	text_shadow = 'rgb(157, 119, 35)'
elif health >= 0.05:
	health_desc = 'Hospitalized, but possible recovery'
	color = 'rgb(214, 155, 17)'
	text_shadow = 'rgb(164, 65, 1)'
elif health >= 0.02:
	health_desc = 'Terminally ill'
	color = 'rgb(224, 90, 45)'
	text_shadow = 'rgb(103, 1, 4)'
elif health == -1:
	health_desc = 'Not enough data'
	color = 'rgb(169, 169, 169)'
	health = 0
	text_shadow = 'rgb(39, 37, 104)'
else:
	health_desc = 'Six feet under'
	color = 'rgb(128, 128, 128)'
	text_shadow = 'rgb(10, 10, 60)'

top_charts = trends.charts()[0][:10]

content = str(open('status.html', 'r').read())
content = content.format(name=term, health=round(health * 100, 1), popular=top_charts, health_desc=health_desc, color=color, text_shadow=text_shadow)

#assemble html string
html_entire_page =  html_header
html_entire_page += content
html_entire_page += html_footer


print(content)
