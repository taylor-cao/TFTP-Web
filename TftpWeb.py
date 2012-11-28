"""TftpWeb - A web interface for TFTP servers."""

import ConfigParser
import os 

from bottle import route, run
from bottle import jinja2_view as view, jinja2_template as template

config = ConfigParser.RawConfigParser()
config.read(["TftpWeb.conf"])

ROOT = config.get("TFTP Server", "root")

TEMPLATE = """
        <h3>Directories</h3>
        {% if dirnames %}
            <ul>
            {% for dirname in dirnames %}
                <li>
                    {% if relpath %}
                        <a href="http://{{ host }}:{{ port }}/{{ relpath }}/{{ dirname }}">
                    {% else %}
                        <a href="http://{{ host }}:{{ port }}/{{ dirname }}">
                    {% endif %}
                            {{ dirname }}
                        </a>
                </li>
            {% endfor %}
            </ul>
        {% else %}
            There are no directories under this path.
        {% endif %}
        <h3>Files</h3>
        <ul>
        {% for filename in filenames %}
            <li>
                {% if relpath %}
                    <a href="tftp://{{ host }}/{{ relpath }}/{{ filename }}">
                {% else %}
                    <a href="tftp://{{ host }}/{{ filename }}">
                {% endif %}
                    {{ filename }}
                </a>
            </li>
        {% endfor %}
        </ul>
"""

@route('/')
@route('/<relpath:re:[a-zA-Z_/]+>')
def index(relpath=''):
    abspath = os.path.join(ROOT, relpath)
    print abspath
    try:
        dir_list = os.listdir(abspath)
        filenames = [filename for filename in dir_list if os.path.isfile(
                     os.path.join(ROOT, filename))]
        dirnames = [dirname for dirname in dir_list if os.path.isdir(
                    os.path.join(ROOT, filename))]
    except OSError:
        return "No such file or directory."
    return template(TEMPLATE, host=host, port=port, relpath=relpath,
                    filenames=filenames, dirnames=dirnames)

host = config.get("Web Server", "host")
port  = config.get("Web Server", "port")
run(host=host, port=port)

