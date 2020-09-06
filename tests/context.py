import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from tern_to_md import generate_licenses_summary
from tern_to_md import generate_copyright_info