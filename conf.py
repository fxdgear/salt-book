# Basic project info
project = u'The Salt Book'
copyright = u'Nick Lang, et al.'
version = '0.1'
release = '0.1'

# Build options
templates_path = ['_templates']
exclude_patterns = ['_build', 'README.rst']
source_suffix = '.rst'
master_doc = 'index'

# HTML options
html_theme = 'djangobook'
html_theme_path = ['themes']
html_static_path = ['_static']
pygments_style = 'sphinx'
html_use_index = False          # FIXME once proper index directives are added.
html_show_sourcelink = False
html_show_sphinx = False
html_title = "The Salt Book"
html_add_permalinks = False     # FIXME once styles are fixed to get the hover back.

# LATEX builder
latex_documents = [
  ('index', 'TheSaltBook.tex', u'The Salt Book',
   u'Nick Lang, et al.', 'manual'),
]

# texinfo builder
texinfo_documents = [
    ('index', 'TheSaltBook.tex', u'The Salt Book',
     u'Nick Lang, et al.', 'manual'),
    ]

# ePub builder
epub_title = u'The Salt Book'
epub_author = u'Nick Lang, et al.'
epub_publisher = u'Nick Lang, et al.'
epub_copyright = u'Nick Lang, et al.'
