# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

# Ajouter le chemin du code source à la variable PATH
sys.path.insert(0, os.path.abspath('../src'))

# Configuration de Sphinx
project = 'Handy Car'
copyright = '2024, Rochdy BACHABI & Rochdyath BACHABI'
author = 'Rochdy BACHABI & Rochdyath BACHABI'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',   # Générer automatiquement la documentation à partir des docstrings
    'sphinx.ext.viewcode',  # Ajouter des liens pour afficher le code source
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'press'
html_static_path = ['_static']
