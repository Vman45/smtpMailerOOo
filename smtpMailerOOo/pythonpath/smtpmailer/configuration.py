#!
# -*- coding: utf_8 -*-

# General configuration
g_extension = 'smtpMailerOOo'
g_identifier = 'com.gmail.prrvchr.extensions.%s' % g_extension
g_logger = '%s.Logger' % g_identifier
g_wizard_paths = (1, 2, 3)
g_wizard_page = 2

# Mailer Wizard configuration
g_default_columns = ['Resource']
g_column_index = 0
#g_column_filters = (0, 1, 4)
g_column_filters = ('HomeEmail', 'WorkEmail', 'OtherEmail')
g_table_index = 0
g_fetchsize = 1000
