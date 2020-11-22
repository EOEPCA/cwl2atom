import logging
import yaml


class CwlLoader:
    def __init__(self, path):
        self.load_cwl(path)
        self.validate_cwl()

    def load_cwl(self, path):
        with open(path, 'r') as stream:
            try:
                self.cwl = yaml.safe_load(stream)
                stream.seek(0)
                self.cwl_content = ''.join(stream.readlines())
            except yaml.YAMLError as exc:
                logging.error(exc)
        return self.cwl_content

    def validate_cwl(self):
        for elem in self.cwl['$graph']:
            if elem['class'] == 'Workflow':
                self.workflow = elem
                return self.workflow
        return None

    def get_cwl_content(self):
        return self.cwl_content