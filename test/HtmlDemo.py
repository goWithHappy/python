from html.parser import HTMLParser
from html.entities import name2codepoint

#书写自己的解析类，注意要继承HTMLParser类
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
       print('handle_starttag:')
       print('<%s>'%tag)
    def handle_endtag(self, tag):
        print('handle_endtag:')
        print('</%s/>'%tag)
    def handle_startendtag(self, tag, attrs):
        print('handle_startendtag:')
        print('<%s/>'%tag)
    def handle_data(self, data):
        print('handle_data:')
        print(data)
    def handle_comment(self, data):
        print('handle_comment:')
        print('<!--',data, '-->')
    def handle_entityref(self, name):
        print('handle_entityref:')
        print('&%s;'%name)
    def handle_charref(self, name):
        print('handle_charref:')
        print('&#%s;'%name)
parser=MyHTMLParser()
#feed方法可以多次进行调用并不需要一次把整个HTML字符串都塞进去，可以一部分一部分来塞
#特殊字符有两种特殊字符&nbsp，一种是数字表示的&#1234
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>'''
            )

