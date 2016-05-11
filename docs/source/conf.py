# -*- coding: utf-8 -*-

import sphinx_rtd_theme


extensions = [
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.graphviz',
]

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = u'Bitcoin: Some Nuts and Bolts'
copyright = u'2016, Sylvain Bellemare'
author = u'Sylvain Bellemare'

version = u'2016.03.27'
release = u'2016.03.27'

language = None

exclude_patterns = []

pygments_style = 'sphinx'

todo_include_todos = True

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']
htmlhelp_basename = 'BitcoinNutsAndBoltsdoc'

latex_elements = {}

latex_documents = [
    (master_doc,
     'BitcoinNutsAndBolts.tex',
     u'Bitcoin Nuts And Bolts Documentation',
     u'Sylvain Bellemare', 'manual'),
]

man_pages = [
    (master_doc,
     'bitcoinnutsandbolts',
     u'Bitcoin Nuts And Bolts Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc,
     'BitcoinNutsAndBolts',
     u'Bitcoin Nuts And Bolts Documentation',
     author,
     'BitcoinNutsAndBolts',
     'One line description of project.',
     'Miscellaneous'),
]

extensions += [
    'hieroglyph',
]

slide_title = 'Bitcoin: Nuts and Bolts'
slide_theme = 'slides2'
slide_levels = 3

slide_theme_options = {
    'subtitle': '',
    'favicon': "'favicon.png'",
    'presenters': [
        {
            'name': author,
            'twitter': '@sbellem',
            'email': 'sylvain@ascribe.io',
            'www': 'ascribe.io',
            'github': 'sbellem'
        },
    ],
}

intersphinx_mapping = {'https://docs.python.org/': None}
