import logging
import sys
import yaml
import os
from .atom import Atom
from .cwl_loader import CwlLoader
from lxml import etree
import datetime
import click
import hashlib

logging.basicConfig(stream=sys.stderr,
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%dT%H:%M:%S')


@click.command()
@click.argument('path')
def main(path):
    cwl_obj = CwlLoader(path)
    cwl_content = cwl_obj.get_cwl_content()
    workflow = cwl_obj.workflow

    template = '''<?xml version="1.0"?>
                  <feed xmlns="http://www.w3.org/2005/Atom">
                        <entry>
                            <title type="text"></title>
                            <summary type="html"></summary>
                            <date xmlns="http://purl.org/dc/elements/1.1/"></date>
                            <identifier xmlns="http://purl.org/dc/elements/1.1/"></identifier>
                        </entry>
                  </feed>'''

    m = hashlib.md5()
    m.update(cwl_content.encode('utf-8'))

    identifier = m.hexdigest()

    atom_template = Atom(etree.fromstring(template))

    atom_template.set_identifier(identifier)
    atom_template.set_title_text(workflow['label'])
    atom_template.set_summary_text(workflow['doc'])

    atom_template.set_dcdate(datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'))

    offering = atom_template.create_offering(code='http://www.opengis.net/eoc/applicationContext/cwl',
                                             content=cwl_content)

    atom_template.add_offering(offering)

    sys.stdout.write(b'<?xml version="1.0" encoding="UTF-8"?>\n'.decode('utf-8'))
    sys.stdout.write(etree.tostring(atom_template.root,
                                    pretty_print=True).decode('utf-8'))


if __name__ == "__main__":
    main()