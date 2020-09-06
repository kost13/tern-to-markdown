import unittest
import tempfile
import os

from context import generate_copyright_info


class TestCopyrightInfo(unittest.TestCase):

    def test_licenses_list(self):    
        test_cases_dir = os.path.join(os.path.dirname(__file__),'test_cases')
        src_file = test_cases_dir + '/out_case1_light.yml'

        with tempfile.TemporaryDirectory() as temp_dir:
            dest_file = temp_dir + '/test_licenses.md'
            self.assertTrue(generate_copyright_info.generate_output(src_file, dest_file))


if __name__ == '__main__':
    unittest.main()