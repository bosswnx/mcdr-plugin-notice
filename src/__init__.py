import mcdreforged.api.all as mcdr
import json

NOTICE_FILE = 'notices.json'
data = {}

def on_load(server: mcdr.PluginServerInterface, old):
    register_command(server)
    load_data(server)
    pass

def register_command(server: mcdr.PluginServerInterface):
    builder = mcdr.SimpleCommandBuilder()

    builder.arg('<id>', mcdr.Integer())
    builder.arg('<notice>', mcdr.Text())
    builder.arg('<type>', mcdr.Text())

    builder.command('!!notice list', list_all_notices)

    builder.register_command(server)

def load_data(server: mcdr.PluginServerInterface):
    try:
        with open(NOTICE_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

def list_all_notices(source: mcdr.CommandSource):
    pass