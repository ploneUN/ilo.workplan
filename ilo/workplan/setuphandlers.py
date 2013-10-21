from collective.grok import gs
from ilo.workplan import MessageFactory as _

@gs.importstep(
    name=u'ilo.workplan', 
    title=_('ilo.workplan import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('ilo.workplan.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
