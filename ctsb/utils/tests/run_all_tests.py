import os
import re
from ctsb.utils.tests.test_dataset_registry import test_dataset_registry
from ctsb.utils.tests.test_download_tools import test_download_tools
from ctsb.utils.tests.test_random import test_random
from ctsb.utils.tests.test_registration_tools import test_registration_tools

# add all unit tests in datset_registry
def run_all_tests():
    print("\nrunning all utils tests...\n")
    test_dataset_registry()
    test_download_tools()
    test_random()
    test_registration_tools()
    print("\nall utils tests passed\n")

if __name__ == '__main__':
    run_all_tests()