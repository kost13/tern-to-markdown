import unittest
import tempfile
import os

from context import generate_licenses_summary


class TestLicensesSummary(unittest.TestCase):

    def test_licenses_list(self):    
        test_cases_dir = os.path.join(os.path.dirname(__file__),'test_cases')
        src_file = test_cases_dir + '/out_case1_light.yml'

        with tempfile.TemporaryDirectory() as temp_dir:
            dest_file = temp_dir + '/test_licenses.md'
            self.assertTrue(generate_licenses_summary.generate_summary(src_file, dest_file, False))

            with open(dest_file, 'r') as f:
                results = f.read().split('\n')

        self.assertTrue(len(results) > 2)

        result_licenses = results[2].split('; ')
        result_licenses.sort()         

        with open(test_cases_dir + '/case1_licenses.txt', 'r') as f:
            licenses = f.read().split('\n')
            
        licenses.sort()

        self.assertEqual(len(result_licenses), len(licenses))

        for i in range(len(licenses)):
            self.assertEqual(licenses[i].strip(), result_licenses[i].strip())


if __name__ == '__main__':
    unittest.main()



    





