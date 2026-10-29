# Copyright (c) 2026, Sakil and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator


class Book(WebsiteGenerator):

	def before_save(self):
		if self.total_no_of_pages:
			self.percentage_completed : int = (self.pages_completed*100)/self.total_no_of_pages
		else:
			self.percentage_completed = 0

		#Add route for webview
		self.route = self.title

	def get_context(self, context):
		context.book = self
		context.test = "Hello World"
		return context
