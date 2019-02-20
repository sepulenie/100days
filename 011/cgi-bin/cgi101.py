#!/usr/bin/python3
import cgi
form = cgi.FieldStorage()
print('Content-type: text/html\n')
print('<title>Reply Page</title>')
if not 'user' in form:
    print('<h1>Who are you?</h1>')
else:
    print('<h1><i>%s</i>, Privet</h1>' % cgi.escape(form['user'].value))

