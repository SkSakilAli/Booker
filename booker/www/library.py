
import frappe

def get_all_reading_status():
    return frappe.db.get_list(
        "Reading Status",
        fields=["name", "name1"],
        order_by="modified asc"
    )

def get_book_list(status: None):
    if not status:
    	status =1
    return frappe.db.get_list(
        "Book",
        filters={
        	"status":str(status)
        },
        fields=["name", "title", "image", "author", "description"],
        order_by="modified desc"
    )

def get_context(context):
    context.reading_status = get_all_reading_status()
    print(context.reading_status)
    selected_status = frappe.form_dict.get("status")
    context.selected_status = selected_status
    context.books = get_book_list(selected_status)
    print(context.books)
    return context

