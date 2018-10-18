# Import
import pdftables_api

# API key
api = "izhexad818vp"

c = pdftables_api.Client(api)
c.xlsx_single('input.pdf', 'output.xlsx')

