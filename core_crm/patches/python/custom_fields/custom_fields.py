from core_crm.patches.python.custom_fields.customer import customer_fields
from core_crm.patches.python.custom_fields.supplier import supplier_fields


def execute():
    customer_fields()
    supplier_fields()
