

# Definition of available categories for products
CATEGORIES = [
	('FOOD', 'Food'),
	('HOUSEHOLD', 'Household'),
	('OTHER', 'Other')
]


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