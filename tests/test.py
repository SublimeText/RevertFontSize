import json
import glob

def test_sublime_commands_are_valid():
    for f in glob.glob('*.sublime-commands'):
        json.load(open(f))

def test_sublime_keymaps_are_valid():
    for f in glob.glob('*.sublime-keymap'):
        json.load(open(f))

def test_package_control_messages_is_valid():
    msg = open('messages.json')
    json.load(msg)
