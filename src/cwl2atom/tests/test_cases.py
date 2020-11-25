import nose
import os
from nose.tools import assert_equal
# from src.cwl2atom.cwl_loader import CwlLoader
from cwl2atom import CwlLoader


def test_if_cwl_exist():
    nose.tools.assert_equal(os.path.exists("/home/farid/Videos/cwl2atom/example.cwl"), True,
                            "The path of cwl file for testing not exists")


class TestCases(CwlLoader):

    def __init__(self):
        self.cwl_reader = CwlLoader("/home/farid/Videos/cwl2atom/example.cwl")
        self.workflow = self.cwl_reader.workflow

    def test_if_workflow_class_exists(self):
        print("Wow")
        assert_equal(self.workflow['class'], "Workflow", "\'Workflow\' class is not exist in .cwl file")
        print("Done")

    def test_if_workflow_class_has_id(self):
        assert "id" in self.workflow

    def test_if_workflow_class_has_label(self):
        assert "label" in self.workflow

    def test_if_workflow_class_has_doc(self):
        assert "doc" in self.workflow


if __name__ == "__main__":
    nose.main()
