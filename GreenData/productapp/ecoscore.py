from .presets import MATERIALS
from .models import PackagingInfo, Product




def _packageScore(pck:PackagingInfo):
	"""
	Compute the score for a single package element
	"""
	# Get the score of the material
	res = MATERIALS[pck.material][1]

	# Apply maluses if packaging is not recycled/recyclable
	if not pck.is_recyclable:
		res *= 0.5
	if not pck.is_recycled:
		res *= 0.7

	return res

def getEcoScore(p:Product):
	"""
	Compute the ecoscore of a product depending on its attributes
	"""
	prd_mass_gram = p.quantity

	# change mass coefficient depending on unit
	if p.quantity_unit in ['KG', 'L']:
		prd_mass_gram *= 1000
	elif p.quantity_unit in ['cL']:
		prd_mass_gram *= 10
	packagings = p.packaginginfo_set.all()

	if packagings.count() == 0:
		raise Exception("No packaging saved")

	sum_pck_masses = sum([pck.mass for pck in packagings])
	pck_weight_score_sum = sum([(pck.mass / sum_pck_masses) * _packageScore(pck) for pck in packagings])

	score = pck_weight_score_sum
	# if there is more mass of packaging than products, then proportional malus
	score *= min(1, prd_mass_gram/sum_pck_masses)

	return int(100*score)