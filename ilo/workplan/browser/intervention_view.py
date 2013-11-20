from five import grok
from plone.directives import dexterity, form
from ilo.workplan.content.intervention import IIntervention

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IIntervention)
    grok.require('zope2.View')
    grok.template('intervention_view')
    grok.name('view')

