from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
def supplier_fields():
    custom_fields = {
        "Supplier": [
            dict(fieldname='gstin', label='GSTIN',
                fieldtype='Data', insert_after='gst_category',depends_on='eval: (doc.supplier_type == "Company") && (doc.gst_category != "Unregistered")',mandatory_depends_on='eval: (doc.supplier_type == "Company") && (doc.gst_category != "Unregistered")'),
       ]
    }
    create_custom_fields(custom_fields)
