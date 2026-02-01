# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'the-derivation'
copyright = "2026, 'Abdullah al Azmi, Tanvir Jahan'"
author = "'Abdullah al Azmi, Tanvir Jahan'"
release = '0.1'
language = 'en'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_nb",
    # "sphinx_rtd_theme",
    # "sphinx_copybutton",
    # "sphinx.ext.extlinks",
    # "sphinxcontrib.youtube",
    # "sphinx.ext.intersphinx",
]

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "tasklist",
]
myst_heading_anchors = 3

# MyST-NB configuration (for Jupyter Notebooks)
nb_execution_mode = "off"  # Prevent auto-execution
nb_merge_streams = True  # Merge stdout and stderr streams

# Source suffix - Define which parser handles which file type
source_suffix = {
    ".md": "myst-nb", # Use MyST-NB for Markdown files
    ".ipynb": "myst-nb", # Use MyST-NB for Jupyter Notebooks
}

templates_path = ['_templates']
exclude_patterns = [
    "docs",
    "_build",
    ".venv",
    ".vscode",
    ".doctrees",
    ".gitignore",
    "LICENSE",
    "README.md",
    "**/.ipynb_checkpoints/*",
]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

html_theme_options = {
    'logo_only': True,
}

html_logo = "../resource/the-derivation-logo.svg"