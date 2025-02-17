"""Python linter to check TODO comments for consistency and best practice.
"""
from ._checker import Checker
from ._error import Error
from ._rules import register_rule, rules
from ._token import Token


__version__ = '0.3.0'

# keep sorted
__all__ = [
    'Checker',
    'Error',
    'register_rule',
    'rules',
    'Token',
]
