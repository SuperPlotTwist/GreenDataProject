

# Definition of available categories for products
CATEGORIES = [
	('FOOD', 'Food'),
	('HOUSEHOLD', 'Household'),
	('OTHER', 'Other')
]

def ctxt_cat(ctxt):
	"""
	Function that add categories to the dictionary
	ctxt. Used in views so that the dropdown "categories"
	is visible from all pages.
	"""
	cat_menu = [c for (c,n) in CATEGORIES]
	ctxt["cat_menu"] = cat_menu
	return ctxt


# Quantity units
UNITS = [
	('G', 'g'),
	('KG', 'kg'),
	('ML', 'mL'),
	('CL', 'cL'),
	('L', 'L')
]


# Possible materials
MATERIALS = [
	('PLASTIC', 'Plastic'),
	('GLASS', 'Glass'),
	('CARDBOARD', 'Cardboard'),
	('ALUMINIUM', 'Aluminium'),
	('PAPER', 'Paper')
]