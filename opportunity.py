#This file is part of sale_opportunity_quote module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['SaleOpportunity', 'Sale']


class SaleOpportunity:
    __metaclass__ = PoolMeta
    __name__ = 'sale.opportunity'

    quotes = fields.One2Many('sale.sale', 'opportunity', 'Sales')

    def create_sale(self):
        sale = super(SaleOpportunity, self).create_sale()
        sale.opportunity = self
        return sale


class Sale:
    __metaclass__ = PoolMeta
    __name__ = 'sale.sale'

    opportunity = fields.Many2One('sale.opportunity', 'Opportunity')
