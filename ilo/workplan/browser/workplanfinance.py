from five import grok
from ilo.workplan.content.workplan import IWorkplan

grok.templatedir('templates')


class workplanfinance(grok.View):
    grok.context(IWorkplan)
    grok.name('workplanfinance')
    grok.require('zope2.View')
    grok.template('workplanfinance')
