from .commands import register_commands
from .messages import register_messages

def register_handlers(app):
    register_commands(app)
    register_messages(app)
