# Import
import pdftables_api

# API key
api = "izhexad818vp"

c = pdftables_api.Client(api)
c.xlsx('input.pdf', 'output.xlsx')