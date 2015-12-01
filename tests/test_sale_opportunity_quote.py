# This file is part of the sale_opportunity_quote module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class SaleOpportunityQuoteTestCase(ModuleTestCase):
    'Test Sale Opportunity Quote module'
    module = 'sale_opportunity_quote'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SaleOpportunityQuoteTestCase))
    return suite