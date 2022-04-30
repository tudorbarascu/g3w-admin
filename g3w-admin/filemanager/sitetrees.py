from sitetree.utils import item
from core.utils.tree import G3Wtree

sitetrees = (
    # Define a tree with `tree` function.
    G3Wtree('filemanager_sidebar_right', title='File Manager sidebar right', module='filemanager', items=[
        item('FILE MANAGER', '#', type_header=True),
        item('Files', 'filemanager-home', icon_css_class='fa fa-database', description='Accedi al file manager...'),
    ]),

    G3Wtree('filemanager_sidebar_right_en', title='STRESS navabar', module='filemanager', items=[
        item('FILE MANAGER', '#', type_header=True),
        item('Files', 'filemanager-home', icon_css_class='fa fa-database',
             description='Go to file manager application...'),
    ]),

    G3Wtree('filemanager_sidebar_right_fr', title='STRESS navabar', module='filemanager', items=[
        item('GESTIONNAIRE DE FICHIERS', '#', type_header=True),
        item('Files', 'filemanager-home', icon_css_class='fa fa-database',
             description='Allez dans l\'application du gestionnaire de fichiers...'),
    ]),

    G3Wtree('filemanager_sidebar_right_ro', title='STRESS navabar', module='filemanager', items=[
        item('Gestionare fișiere', '#', type_header=True),
        item('Fișiere', 'filemanager-home', icon_css_class='fa fa-database',
             description='Deschide aplicația de gestionare fișiere ...'),
    ]),
)

