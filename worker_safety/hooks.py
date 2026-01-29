fixtures = ["Web Page"]


app_name = "worker_safety"
app_title = "Worker Safety"
app_publisher = "Jeslin Stephy"
app_description = "Smart Industry Management System with Integrated Worker Safety & Risk Monitoring"
app_email = "jeslinstephy@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/worker_safety/css/worker_safety.css"
# app_include_js = "/assets/worker_safety/js/worker_safety.js"

# include js, css files in header of web template
# web_include_css = "/assets/worker_safety/css/worker_safety.css"
# web_include_js = "/assets/worker_safety/js/worker_safety.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "worker_safety/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "worker_safety.utils.jinja_methods",
# 	"filters": "worker_safety.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "worker_safety.install.before_install"
# after_install = "worker_safety.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "worker_safety.uninstall.before_uninstall"
# after_uninstall = "worker_safety.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "worker_safety.utils.before_app_install"
# after_app_install = "worker_safety.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "worker_safety.utils.before_app_uninstall"
# after_app_uninstall = "worker_safety.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "worker_safety.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"worker_safety.tasks.all"
# 	],
# 	"daily": [
# 		"worker_safety.tasks.daily"
# 	],
# 	"hourly": [
# 		"worker_safety.tasks.hourly"
# 	],
# 	"weekly": [
# 		"worker_safety.tasks.weekly"
# 	],
# 	"monthly": [
# 		"worker_safety.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "worker_safety.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "worker_safety.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "worker_safety.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["worker_safety.utils.before_request"]
# after_request = ["worker_safety.utils.after_request"]

# Job Events
# ----------
# before_job = ["worker_safety.utils.before_job"]
# after_job = ["worker_safety.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"worker_safety.auth.validate"
# ]
