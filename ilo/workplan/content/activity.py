from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.multilingualbehavior.directives import languageindependent
from collective import dexteritytextindexer

from ilo.workplan import MessageFactory as _


# Interface class; used to define content-type schema.

class IActivity(form.Schema, IImageScaleTraversable):
    """
    """
    title = schema.TextLine(
        title=_(u'Title'),
        description=_(''),
        )

    startDate = schema.Date(
        title=_(u'Start Date'),
        description=_(''),
        )

    endDate = schema.Date(
        title=_(u'End Date'),
        description=_(''),
        )

    resources_required = schema.Text(
        title=_(u'Total resources required and  sources of funding'
                u'US$ and P work-months'),
        description=_(''),
        )

    resources_available = schema.Text(
        title=_(u'Total resources available and sources of funding (US$ and P'
                'work-months g'),
        description=_(''),
        )

    resource_gap = schema.Text(
        title=_(u'Anticipated Resource Gap'),
        description=_(''),
        )

    form.fieldset('finance',
                  label=_(u'Finance'),
                  fields=['epapo_number',
                          'rbtc_actemp',
                          'rbsa_actemp_hq',
                          'rbsa_regional',
                          'tc_projects',
                          'itc_turin',
                          'eos_company_oie',
                          'rbtc_oa',
                          'fund_to_be_determinated',
                          ],
                  required=False,
                  )

    epapo_number = schema.Int(
        title=_(u'EPA/PO Number'),
        description=_('e.g. 9119448'),
        required=False,
        )

    rbtc_actemp = schema.Float(
        title=_(u'RBTC ACTEMP'),
        description=_('e.g. 5500'),
        required=False,
        )

    rbsa_actemp_hq = schema.Float(
        title=_(u'RBSA ACTEMP HQ'),
        description=_('e.g. 4000'),
        required=False,
        )

    rbsa_regional = schema.Float(
        title=_(u'RBSA Regional'),
        description=_('e.g. 7300'),
        required=False,
        )

    tc_projects = schema.Float(
        title=_(u'TC projects'),
        description=_('e.g. 3450'),
        required=False,
        )

    itc_turin = schema.Float(
        title=_(u'ITC Turin'),
        description=_('e.g. 1200'),
        required=False,
        )

    eos_company_oie = schema.Float(
        title=_(u'EOs, COMPANY, OIE'),
        description=_('e.g. 7000'),
        required=False,
        )

    rbtc_oa = schema.Float(
        title=_(u'RBTC OA'),
        description=_('e.g. 5600'),
        required=False,
        )

    fund_to_be_determinated = schema.Float(
        title=_(u'Fund to be determinated'),
        description=_('e.g. 50000'),
        required=False,
        )

alsoProvides(IActivity, IFormFieldProvider)
