from five import grok
from plone.directives import dexterity, form
from ilo.workplan.content.workplan import IWorkplan

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IWorkplan)
    grok.require('zope2.View')
    grok.template('workplan_view')
    grok.name('view')

    def get_total_finance(self):

        import ipdb; ipdb.set_trace()
        activity = self.context
        test=  sum(activity.rbtc_actemp, activity.rbsa_actemp_hq,
                   activity.rbsa_regional, activity.tc_projects,
                   activity.itc_turin, activity.eos_company_oie,
                   activity.rbtc_oa, activity.fund_to_be_determinated)
