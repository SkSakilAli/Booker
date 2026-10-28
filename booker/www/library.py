
import frappe

def get_all_reading_status():
    return frappe.db.get_list(
        "Reading Status",
        fields=["name", "name1"],
        order_by="modified asc"
    )

def get_book_list(status: str):
    return frappe.db.get_list(
        "Book",
        filters={
        	"status":str(status)
        },
        fields=["name", "title", "image", "author", "description", "total_no_of_pages",
        		"pages_completed", "percentage_completed"],
        order_by="modified desc"
    )

def get_context(context):
    context.reading_status = get_all_reading_status()
    selected_status = frappe.form_dict.get("status")
    if not selected_status and context.reading_status:
         selected_status = str(context.reading_status[0].name)
    context.selected_status = selected_status
    context.books = get_book_list(selected_status)
    print(context.books)
    return context

