from django.shortcuts import render
from productapp.presets import ctxt_cat


def client_error_view(request, err_msg: str, err_code: int):
	"""
	render an html template used for error handlong
	"""
	ctxt = ctxt_cat({})
	ctxt["error_code"] = err_code
	ctxt["error_msg"] = err_msg

	return render(request, 'error_template.html', ctxt, status=err_code)