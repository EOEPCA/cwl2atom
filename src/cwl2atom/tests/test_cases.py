from src.cwl2atom.cwl_loader import CwlLoader
import nose
import os
from nose.tools import assert_equal

cwl_dir = "example.cwl"


def test_if_cwl_exist():
    nose.tools.assert_equal(os.path.exists(cwl_dir), True,
                            "The path of cwl file for testing not exists")


class TestCases:
    cwl_obj = CwlLoader(cwl_dir)
    cwl_content = cwl_obj.get_cwl_content()
    workflow = cwl_obj.workflow

    def test_if_workflow_class_exists(self):
        try:
            assert_equal(self.workflow['class'], "Workflow", "\'Workflow\' class is not exist in .cwl file")
        finally:
            print("workflow test done")

    def test_if_workflow_class_has_id(self):
        assert "id" in self.workflow

    def test_if_workflow_class_has_label(self):
        assert "label" in self.workflow

    def test_if_workflow_class_has_doc(self):
        assert "doc" in self.workflow


if __name__ == "__main__":
    nose.main()
