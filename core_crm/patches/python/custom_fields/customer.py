from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
def customer_fields():
    custom_fields = {
        "Customer": [
            dict(fieldname='gstin', label='GSTIN',
                fieldtype='Data', insert_after='account_manager',depends_on='eval: (doc.customer_type == "Company") && (doc.gst_category != "Unregistered")',mandatory_depends_on='eval: (doc.customer_type == "Company") && (doc.gst_category != "Unregistered")'),
        ]
    }
    create_custom_fields(custom_fields)