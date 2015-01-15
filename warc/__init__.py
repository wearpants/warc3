"""
warc
~~~~

Python library to work with WARC files.

:copyright: (c) 2012 Internet Archive
"""

from .warc import WARCFile, WARCRecord, WARCHeader, WARCReader
from .utils import HTTPObject

def open(filename, mode="rb", format = None):
    """Shorthand for WARCFile(filename, mode).

    Auto detects file and opens it.

    """
    if filename.endswith(".warc") or filename.endswith(".warc.gz"):
        return WARCFile(filename, mode)
    else:
        raise IOError("Don't know how to open non-warc files.")
