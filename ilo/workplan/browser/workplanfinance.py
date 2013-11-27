from five import grok
from Products.CMFCore.interfaces import IContentish

grok.templatedir('templates')

class workplanfinance(grok.View):
    grok.context(IContentish)
    grok.name('workplanfinance')
    grok.require('zope2.View')
    grok.template('workplanfinance')
