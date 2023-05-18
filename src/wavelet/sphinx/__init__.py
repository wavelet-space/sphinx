"""
Sphinx theme packaging.

See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package.
"""
from pathlib import Path
from typing import Dict


__version__ = "0.2.0"


def setup(app) -> Dict[str, bool]:
    
    app.add_html_theme('wavelet-sphinx-theme', str( Path(__file__).resolve().parent ))
    
    return {"parallel_read_safe": True, "parallel_write_safe": True}