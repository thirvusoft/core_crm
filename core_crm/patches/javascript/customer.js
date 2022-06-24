frappe.ui.form.on('Customer', {
    customer_primary_address:function(frm){ 
        if(cur_frm.doc.customer_type=="Individual"){
            frappe.db.get_value('Address', {'name':cur_frm.doc.customer_primary_address}, 'tax_category', function(r) {
                cur_frm.set_value("tax_category", r.tax_category)
            });
            refresh_field("tax_category");
        }    

    },
    gstin:function(frm){
        let result =  frm.doc.gstin.trim().slice(0, 2);
        if(result==33){
            cur_frm.set_value("tax_category","In-State");
        }
        else{
            cur_frm.set_value("tax_category","Out-State");     

        }
        refresh_field("tax_category");

    },
    gst_category:function(frm){
        if(frm.doc.gst_category=="Unregistered"){
            cur_frm.set_value("tax_category","")
        }
        refresh_field("tax_category");
    }
});


