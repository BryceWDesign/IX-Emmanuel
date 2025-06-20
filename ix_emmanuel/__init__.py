"""
IX-Emmanuel Package Initialization

Sets up the IX-Emmanuel namespace and exposes core modules.
"""

from .core.emmanuel_core import EmmanuelCore
from .core.emmanuel_interface import run_emmanuel_cli
from .core.gibson_adapter import GibsonAdapter

__all__ = [
    "EmmanuelCore",
    "run_emmanuel_cli",
    "GibsonAdapter"
]
