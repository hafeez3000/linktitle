# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "linktitle"
app_title = "Linktitle"
app_publisher = "Pau Rosello"
app_description = "Changes the defualt Link implementation"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "paurosello@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/linktitle/css/linktitle.css"
app_include_js = "/assets/js/linktitle.min.js"

# include js, css files in header of web template
# web_include_css = "/assets/linktitle/css/linktitle.css"
# web_include_js = "/assets/linktitle/js/linktitle.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "linktitle.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "linktitle.install.before_install"
# after_install = "linktitle.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "linktitle.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"linktitle.tasks.all"
# 	],
# 	"daily": [
# 		"linktitle.tasks.daily"
# 	],
# 	"hourly": [
# 		"linktitle.tasks.hourly"
# 	],
# 	"weekly": [
# 		"linktitle.tasks.weekly"
# 	]
# 	"monthly": [
# 		"linktitle.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "linktitle.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "linktitle.event.get_events"
# }

