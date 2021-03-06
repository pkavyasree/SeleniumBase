"""
This module contains test-state related exceptions.
Raising one of these in a test will cause the
test-state to be logged appropriately in the database
for tests that use the SeleniumBase MySQL plugin.
"""


class BlockedTest(Exception):
    """Raise this to mark a test as Blocked"""
    pass


class SkipTest(Exception):
    """Raise this to mark a test as Skipped."""
    pass


class DeprecatedTest(Exception):
    """Raise this to mark a test as Deprecated."""
    pass
