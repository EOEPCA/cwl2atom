import os
from nose.tools import assert_equal
import nose
from cwl2atom import CwlLoader


def test_if_cwl_exist():
    nose.tools.assert_equal(os.path.exists("src/cwl2atom/tests/data/example.cwl"), True,
                            "The path of cwl file for testing not exists")


class TestCases:

    def __init__(self):
        self.cwl_reader = CwlLoader("src/cwl2atom/tests/data/example.cwl")
        self.workflow = self.cwl_reader.workflow

    def test_if_workflow_class_exists(self):
        assert_equal(self.workflow['class'], "Workflow", "\'Workflow\' class is not exist in .cwl file")

    def test_if_workflow_class_has_id(self):
        assert "id" in self.workflow

    def test_if_workflow_class_has_label(self):
        assert "label" in self.workflow

    def test_if_workflow_class_has_doc(self):
        assert "doc" in self.workflow


if __name__ == "__main__":
    nose.main()
