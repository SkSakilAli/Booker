# Copyright (c) 2026, Sakil and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Book(Document):
	def before_save(self):
		if self.total_no_of_pages:
			self.percentage_completed : int = (self.pages_completed*100)/self.total_no_of_pages
		else:
			self.percentage_completed = 0

