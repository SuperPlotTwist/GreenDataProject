

# Definition of available categories for products
CATEGORIES = [
	('FOOD', 'Food'),
	('HOUSEHOLD', 'Household'),
	('OTHER', 'Other'),
	('COSMETIC', 'Cosmetics')
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
# Model : MATERIALS[id] = (name, ecoscore)
MATERIALS = {
	"PLASTIC": ('Plastic', 0.3),
	"GLASS": ('Glass', 1.0),
	"CARDBOARD": ('Cardboard', 0.7),
	"ALUMINUM": ('Aluminum', 0.8),
	"PAPER": ('Paper', 0.9)
}

MATERIAL_AS_CHOICES = [(k, MATERIALS[k][0]) for k in MATERIALS]