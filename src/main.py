from prompt_toolkit import Application
from prompt_toolkit.widgets import Frame, Label, TextArea, Button
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.layout.containers import HSplit, VSplit
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.keys import Keys

host_field = TextArea(multiline=False)
port_field = TextArea(multiline=False)
user_field = TextArea(multiline=False)
password_field = TextArea(multiline=False)
db_name_field = TextArea(multiline=False)

db_credentials = {}

kb = KeyBindings()

@kb.add(Keys.ControlC)
def next_(event):
    event.app.exit()

@kb.add(Keys.Down)
def next_(event):
    event.app.layout.focus_next()

@kb.add(Keys.Tab)
def next_tab_(event):
    event.app.layout.focus_next()
    
@kb.add(Keys.Up)
def prev_(event):
    event.app.layout.focus_previous()

def handle_submit():
    db_credentials['host'] = host_field.text
    db_credentials['port'] = port_field.text
    db_credentials['user'] = user_field.text
    db_credentials['password'] = password_field.text
    db_credentials['db_name'] = db_name_field.text
    app.exit()

db_credentials_form = HSplit([
    Label(text="Database Credentials", style="bold"),
    Label(text='Use Down + Up to navigate between fields.'),
    Frame(body=HSplit([
        VSplit([
            Label(text="Host: "),
            host_field
            ]),
        VSplit([
            Label(text="Port: "),
            port_field
            ]),
        VSplit([
            Label(text="User: "),
            user_field            ]),
        VSplit([
            Label(text="Password: "),
            password_field
            ]),
        VSplit([
            Label(text="Database: "),
            db_name_field
            ])
            ])),
    Label(text=''),
    Button(text='Submit', handler=handle_submit)
])

app = Application(layout=Layout(db_credentials_form),key_bindings=kb,full_screen=True)

if __name__ == '__main__':
    app.run()
    print("creds ", db_credentials['host'])
    print("creds ", db_credentials['port'])
    print("creds ", db_credentials['user'])
    print("creds ", db_credentials['password'])
    print("creds ", db_credentials['db_name'])