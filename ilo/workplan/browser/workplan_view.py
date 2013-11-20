from five import grok
from plone.directives import dexterity, form
from ilo.workplan.content.workplan import IWorkplan

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IWorkplan)
    grok.require('zope2.View')
    grok.template('workplan_view')
    grok.name('view')
