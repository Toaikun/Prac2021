from bottle import get, post, request, run, template 
from pyfiglet import Figlet, FigletFont



@get('/pyfiglet_task') 
def main():
    return template('''
        <form action="/pyfiglet_task" method="post">
            Input Text: <input name="text" type="text" value="Type something here..."/>
            <select name="font">
            %for i in fonts:
            	<option value = {{i}}> {{i}} </option>
            %end
            </select>
            Color: <input type="color" name="color">
            <input value="Transform text" type="submit" />
        </form>
    ''', fonts = FigletFont.getFonts())

@post('/pyfiglet_task')
def transform():
	return template('''
        <form action="/pyfiglet_task" method="post">
            Input Text: <input name="text" type="text" value="{{prev_text}}"/>
            Font: <select name="font">
            <option selcted="selected">{{font}}</option>
            %for i in fonts:
            	<option value = {{i}}> {{i}} </option>
            %end
            </select>
            Color: <input type="color" name="color" value={{color}}>
            <input value="Transform text" type="submit" />
        </form>
       	<pre ><font color={{color}}>{{text}}</font></pre>
    ''',
    fonts = FigletFont.getFonts(),
    text = Figlet(request.forms.get("font")).renderText(request.forms.get("text")),
    color = request.forms.get("color"),
    font = request.forms.get("font"),
    prev_text = request.forms.get("text"))


run(host='localhost', port='8080')