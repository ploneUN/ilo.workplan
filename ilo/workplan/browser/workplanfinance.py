from five import grok
from ilo.workplan.content.workplan import IWorkplan

grok.templatedir('templates')


class workplanfinance(grok.View):
    grok.context(IWorkplan)
    grok.name('workplanfinance')
    grok.require('zope2.View')
    grok.template('workplanfinance')

    def get_total_finance(self, activity):
        return sum((activity.rbtc_actemp, activity.rbsa_actemp_hq,
                   activity.rbsa_regional, activity.tc_projects,
                   activity.itc_turin, activity.eos_company_oie,
                   activity.rbtc_oa, activity.fund_to_be_determinated))

    def get_cumulative_finance(self, intervention, finance_field):
        return sum(getattr(i, finance_field) for i in intervention.values())

    def get_cumulative_total(self, intervention):
        return sum(self.get_total_finance(i) for i in intervention.values())
