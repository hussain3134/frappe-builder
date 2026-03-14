import base64
import json

import pyperclip

import sys

try:
    compose_file = sys.argv[1]
except IndexError:
    compose_file = "build/docker-compose.yml"

try:
    config_file = sys.argv[2]
except IndexError:
    config_file = "build/template.toml"

with open(compose_file, "r") as f:
    compose = f.read()

with open(config_file, "r") as f:
    config = f.read()

template_object = {"compose": compose, "config": config}
template_object = json.dumps(template_object, indent=2)

print(template_object)

b = base64.b64encode(bytes(str(template_object), 'utf-8')) # bytes
base64_str = b.decode('utf-8')

print(base64_str)

pyperclip.copy(base64_str)
# pyperclip.copy(str(template_object))