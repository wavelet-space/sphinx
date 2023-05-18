from pathlib import Path
from setuptools import setup, find_namespace_packages


readme_path = Path(__file__).resolve().parent / "README.md"

setup(
    name = 'wavelet-sphinx-theme',
    version = "0.2.0",
    license = 'MIT',
    author = 'Wavelet',
    author_email = 'contact@wavelet.space',
    description = 'Wavelet sphinx theme',
    long_description = readme_path.read_text(encoding = 'utf-8'),
    packages = find_namespace_packages(where="src"),
    package_dir = {"": "src"},
    include_package_data = True,
    entry_points = {
        'sphinx.html_themes': [
            'wavelet-sphinx-theme = wavelet.sphinx',
        ]
    },
    install_requires = [
        'sphinx_rtd_theme >=1.0.0',
        'sphinx-copybutton'
    ],
    classifiers = [
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)