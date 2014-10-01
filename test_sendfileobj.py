
import os
import sys
from subprocess import Popen, PIPE


CUR_PATH = os.path.dirname(os.path.abspath(__file__))
EXAMPLE_BASE_PATH = CUR_PATH + '/examples'


def test_basic_example():
    out_proc = Popen([sys.executable, EXAMPLE_BASE_PATH + '/out.py'],
                     stdout=PIPE, stderr=PIPE, cwd=CUR_PATH)
    in_proc = Popen([sys.executable, EXAMPLE_BASE_PATH + '/in.py'],
                    stdout=PIPE, stderr=PIPE, cwd=CUR_PATH)
    out, err = in_proc.communicate()
    assert not err
    assert out.startswith('HTTP/1.0 301')
