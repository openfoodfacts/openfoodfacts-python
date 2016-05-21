import json
import random
import requests
import urllib
import re

traces = json.load(urllib.urlopen("http://world.openfoodfacts.org/traces.json"))
ingredients = json.load(urllib.urlopen("http://world.openfoodfacts.org/ingredients.json"))
stores = json.load(urllib.urlopen("http://world.openfoodfacts.org/stores.json"))
packaging_codes = json.load(urllib.urlopen("http://world.openfoodfacts.org/packager-codes.json"))
packagings = json.load(urllib.urlopen("http://world.openfoodfacts.org/packaging.json"))
brands = json.load(urllib.urlopen("http://world.openfoodfacts.org/brands.json"))
labels = json.load(urllib.urlopen("http://world.openfoodfacts.org/labels.json"))
categories = json.load(urllib.urlopen("http://world.openfoodfacts.org/categories.json"))
allergens = json.load(urllib.urlopen("http://world.openfoodfacts.org/allergens.json"))
additives = json.load(urllib.urlopen("http://world.openfoodfacts.org/additives.json"))
countries = json.load(urllib.urlopen("http://world.openfoodfacts.org/countries.json"))
purchase_places = json.load(urllib.urlopen("http://world.openfoodfacts.org/purchase-places.json"))
states = json.load(urllib.urlopen("http://world.openfoodfacts.org/states.json"))
entry_dates = json.load(urllib.urlopen("http://world.openfoodfacts.org/entry-dates.json"))
languages = json.load(urllib.urlopen("http://world.openfoodfacts.org/languages.json"))
product = json.load(urllib.urlopen("http://world.openfoodfacts.org/api/v0/product/"+ str(jr['code']) +".json"))
# http://world.openfoodfacts.org/api/v0/product/737628064502.json

search_url = "http://world.openfoodfacts.org/cgi/search.pl"
search_terms2 # search terms

# FIRST CRITERIA

tagtype_0
search_tag # choose a criterion...
brands # brands
categories # categories
packaging # packaging
labels # labels
origins # origins of ingredients
manufacturing_places # manufacturing or processing places
emb_codes # packager codes
purchase_places # purchase places
stores # stores
countries # countries
additives # additives
allergens # allergens
traces # traces
nutrition_grades # Nutrition grades
states # states
	

tag_contains_0
contains
does_not_contain


tag_0

additives # without # without_additives
without_additives # Without
additives # with # with_additives
with_additives # With
additives # indifferent # indifferent_additives
indifferent_additives # Indifferent	


# Ingredients from palm oil
ingredients_from_palm_oil # without # without_ingredients_from_palm_oil
without_ingredients_from_palm_oil # Without
ingredients_from_palm_oil # with # with_ingredients_from_palm_oil
with_ingredients_from_palm_oil # With
ingredients_from_palm_oil # indifferent # indifferent_ingredients_from_palm_oil"
indifferent_ingredients_from_palm_oil # Indifferent	



# Ingredients that may be from palm oil
ingredients_that_may_be_from_palm_oil # without # without_ingredients_that_may_be_from_palm_oil
without_ingredients_that_may_be_from_palm_oil # Without
ingredients_that_may_be_from_palm_oil # with # with_ingredients_that_may_be_from_palm_oil
with_ingredients_that_may_be_from_palm_oil # With
ingredients_that_may_be_from_palm_oil # indifferent # indifferent_ingredients_that_may_be_from_palm_oil
indifferent_ingredients_that_may_be_from_palm_oil # Indifferent	


# Ingredients from or that may be from palm oil
ingredients_from_or_that_may_be_from_palm_oil # without # without_ingredients_from_or_that_may_be_from_palm_oil
without_ingredients_from_or_that_may_be_from_palm_oil # Without
ingredients_from_or_that_may_be_from_palm_oil # with # with_ingredients_from_or_that_may_be_from_palm_oil
with_ingredients_from_or_that_may_be_from_palm_oil # With
ingredients_from_or_that_may_be_from_palm_oil # indifferent # indifferent_ingredients_from_or_that_may_be_from_palm_oil
indifferent_ingredients_from_or_that_may_be_from_palm_oil # Indifferent	


# Nutrients

nutriment_0 # nutriment_0 # 

search_nutriment # choose a nutriment...

energy # Energy
energy-from-fat # Energy from fat
fat # Fat
saturated-fat # Saturated fat
butyric-acid # Butyric acid (4:0)
caproic-acid # Caproic acid (6:0)
caprylic-acid # Caprylic acid (8:0)
capric-acid # Capric acid (10:0)
lauric-acid # Lauric acid (12:0)
myristic-acid # Myristic acid (14:0)
palmitic-acid # Palmitic acid (16:0)
stearic-acid # Stearic acid (18:0)
arachidic-acid # Arachidic acid (20:0)
behenic-acid # Behenic acid (22:0)
lignoceric-acid # Lignoceric acid (24:0)
cerotic-acid # Cerotic acid (26:0)
montanic-acid # Montanic acid (28:0)
melissic-acid # Melissic acid (30:0)
monounsaturated-fat # Monounsaturated fat
polyunsaturated-fat # Polyunsaturated fat
omega-3-fat # Omega 3 fatty acids
alpha-linolenic-acid # Alpha-linolenic acid / ALA (18:3 n-3)
eicosapentaenoic-acid # Eicosapentaenoic acid / EPA (20:5 n-3)
docosahexaenoic-acid # Docosahexaenoic acid / DHA (22:6 n-3)
omega-6-fat # Omega 6 fatty acids
linoleic-acid # Linoleic acid / LA (18:2 n-6)
arachidonic-acid # Arachidonic acid / AA / ARA (20:4 n-6)
gamma-linolenic-acid # Gamma-linolenic acid / GLA (18:3 n-6)
dihomo-gamma-linolenic-acid # Dihomo-gamma-linolenic acid / DGLA (20:3 n-6)
omega-9-fat # Omega 9 fatty acids
oleic-acid # Oleic acid (18:1 n-9)
elaidic-acid # Elaidic acid (18:1 n-9)
gondoic-acid # Gondoic acid (20:1 n-9)
mead-acid # Mead acid (20:3 n-9)
erucic-acid # Erucic acid (22:1 n-9)
nervonic-acid # Nervonic acid (24:1 n-9)
trans-fat # Trans fat
cholesterol # Cholesterol
carbohydrates # Carbohydrate
sugars # Sugars
sucrose # Sucrose
glucose # Glucose
fructose # Fructose
lactose # Lactose
maltose # Maltose
maltodextrins # Maltodextrins
starch # Starch
polyols # Sugar alcohols (Polyols)
fiber # Dietary fiber
proteins # Proteins
casein # casein
serum-proteins # Serum proteins
nucleotides # Nucleotides
salt # Salt
sodium # Sodium
alcohol # Alcohol
vitamin-a # Vitamin A
beta-carotene # Beta carotene
vitamin-d # Vitamin D
vitamin-e # Vitamin E
vitamin-k # Vitamin K
vitamin-c # Vitamin C (ascorbic acid)
vitamin-b1 # Vitamin B1 (Thiamin)
vitamin-b2 # Vitamin B2 (Riboflavin)
vitamin-pp # Vitamin B3 / Vitamin PP (Niacin)
vitamin-b6 # Vitamin B6 (Pyridoxin)
vitamin-b9 # Vitamin B9 (Folic acid / Folates)
vitamin-b12 # Vitamin B12 (cobalamin)
biotin # Biotin
pantothenic-acid # Pantothenic acid / Pantothenate (Vitamin B5)
silica # Silica
bicarbonate # Bicarbonate
potassium # Potassium
chloride # Chloride
calcium # Calcium
phosphorus # Phosphorus
iron # Iron
magnesium # Magnesium
zinc # Zinc
copper # Copper
manganese # Manganese
fluoride # Fluoride
selenium # Selenium
chromium # Chromium
molybdenum # Molybdenum
iodine # Iodine
caffeine # Caffeine
taurine # Taurine
ph # pH
fruits-vegetables-nuts # Fruits, vegetables and nuts (minimum)
collagen-meat-protein-ratio # Collagen/Meat protein ratio (maximum)
cocoa # Cocoa (minimum)
chlorophyl # Chlorophyl
carbon-footprint # Carbon footprint / CO2 emissions
nutrition-score-fr # Experimental nutrition score
nutrition-score-uk # Nutrition score - UK

# Comparison of nutrients

nutriment_compare_0 # nutriment_compare_0 # 
lt # &lt;
lte # &lt;=
gt # &gt;
gte # &gt;=
eq # =
		
# Value to compare the nutrients to
nutriment_value_0

# Output
sort_by # sort_by
unique_scans_n # Popularity
product_name # Product name
created_t # Add date
last_modified_t # Edit date


# Results per page	
page_size # page_size
20 # 20
50 # 50
100 # 100
250 # 250
500 # 500
1000 # 1000

