[[Category:Developer]]
[[Category:API]]
== Status ==
Currently the API is mainly used internally for [[Project:Mobile_Apps|Cordova application]], but does not follow good practices in API design.
It is also used by several application and while not yet stable, doesn't change much.
You can have a look at the source code of the app (https://github.com/openfoodfacts/cordova-app/blob/master/www/off.js and https://github.com/openfoodfacts/cordova-app/blob/master/www/index.html)

== Getting help with the API ==
You can ask for help on using the API in this [[https://openfoodfacts.slack.com/messages/api/|API channel on Slack]].

== Testing ==
* You should do all your test edits on http://world.openfoodfacts.net (ask for the password on Slack)
* Do not hesitate to create a global account for your app if you don't want to implement Open Food Facts user creation in your app right now.
== Bugs ==
* Do not hesitate to file a bug if you find an issue in the API, or need an improvement.
* https://github.com/openfoodfacts/openfoodfacts-server/issues

== READ API Documentation ==
=== Downloading static data ===
http://world.openfoodfacts.org/data

=== Field reference ===
The [[fields used]] in the api.
http://world.openfoodfacts.org/data/data-fields.txt

=== JSON interface ===
=== Countries ===
You can either use the global (world) for locales (fr, en…)

A few things to note: 
* if you use a country subdomain instead of world, you get products for that countries only which might change the language but also the name of the fields, in that case you need to use the local language
** http://fr.openfoodfacts.org/categorie/pizzas.json
** an alternative is to specify the language in the subdomain: http://fr-en.openfoodfacts.org/category/pizzas.json

=== Reading a product ===
See http://fr.openfoodfacts.org/data or http://en.openfoodfacts.org/data
The requested subdomain will be the locale fetched.

* http://world.openfoodfacts.org/api/v0/product/737628064502.xml
* http://world.openfoodfacts.org/api/v0/product/737628064502.json

==== Fields within a product ====
===== Images =====
* image_small_url
* image_thumb_url
* image_url
====== Front ======
* "image_front_url"
* "image_front_small_url"
* "image_front_thumb_url"
====== Ingredients ======
* "image_ingredients_url"
* "image_ingredients_small_url"
* "image_ingredients_thumb_url"
====== Nutrition ======
* "image_nutrition_url"
* "image_nutrition_small_url"
* "image_nutrition_thumb_url"

=== Searching for products ===
==== General principles ====
===== Advanced Search =====
====== Parameters ======
You can basically use all the parameters you'd use in a [http://world.openfoodfacts.org/cgi/search.pl?action=display&sort_by=unique_scans_n&page_size=20&action=display graphical advanced search on the site]<br>
* sort_by=unique_scans_n
* page_size=50 (20 by default, 1000 at most)
* page=2
* jqm=1 to search results pages on the web site to get results in a jquerymobile format.
===== Examples<sup>(remember to do tests on world.openfoodfacts.net - login and password: off )</sup> ===== 
<pre>http://world.openfoodfacts.org/cgi/search.pl?search_terms=coke&search_simple=1&jqm=1</pre>
<pre>http://world.openfoodfacts.org/cgi/search.pl?search_terms=banania&search_simple=1&action=process&json=1</pre>
<pre>http://world.openfoodfacts.org/cgi/search.pl?search_terms=banania&search_simple=1&action=process&xml=1</pre>

===== Generic Search =====
====== Combining Tags to get custom results ======
Combining tags works, letting you create thousands of APIs
* http://world.openfoodfacts.org/packager-code/emb-35069c/brand/sojasun.json

==== Languages ====
Languages on the packaging of the product.
=====List of languages present on packaging =====
* http://world.openfoodfacts.org/languages.json
* http://world.openfoodfacts.org/languages.xml
=====List of products with given language on packaging =====
* http://world.openfoodfacts.org/language/italian.json
* http://world.openfoodfacts.org/language/italian.xml

=====Getting suggestions for languages=====
* http://world.openfoodfacts.org/cgi/suggest.pl?lc=fr&tagtype=languages&string=a

===== List of multilingual products =====
* http://world.openfoodfacts.org/language/multilingual.json
* http://world.openfoodfacts.org/language/multilingual.xml

===== List of products by language count =====
* http://world.openfoodfacts.org/language/1.json
* http://world.openfoodfacts.org/language/1.xml
* http://world.openfoodfacts.org/language/2.json
* http://world.openfoodfacts.org/language/2.xml
* http://world.openfoodfacts.org/language/3.json
* http://world.openfoodfacts.org/language/3.xml


====Labels====
=====List of labels=====
* http://world.openfoodfacts.org/labels.json
* http://world.openfoodfacts.org/labels.xml
=====Individual label=====
* http://world.openfoodfacts.org/label/utz-certified.json
* http://world.openfoodfacts.org/label/utz-certified.xml

=====Getting suggestions for labels=====
* http://world.openfoodfacts.org/cgi/suggest.pl?lc=fr&tagtype=labels&string=a

====Categories====
=====List of categories=====
* http://world.openfoodfacts.org/categories.json
* http://world.openfoodfacts.org/categories.xml
=====Individual category=====
* http://world.openfoodfacts.org/category/baby-foods.json
* http://world.openfoodfacts.org/category/baby-foods.xml
=====Getting suggestions for categories=====
* http://world.openfoodfacts.org/cgi/suggest.pl?lc=fr&tagtype=categories&string=a


====Status of products====
=====List of States =====
* http://world.openfoodfacts.org/states.json
* http://world.openfoodfacts.org/states.xml
=====Individual Status =====
* http://world.openfoodfacts.org/state/complete.json
* http://world.openfoodfacts.org/state/complete.xml
=====Getting suggestions for states=====
* http://world.openfoodfacts.org/cgi/suggest.pl?lc=fr&tagtype=states&string=a

====Packaging====
=====List of Packagings=====
* http://world.openfoodfacts.org/packaging.json
* http://world.openfoodfacts.org/packaging.xml

=====Individual Packaging=====
* http://world.openfoodfacts.org/packaging/cardboard.json
* http://world.openfoodfacts.org/packaging/cardboard.xml
====Brands====
=====List of Brands=====
* http://world.openfoodfacts.org/brands.json
* http://world.openfoodfacts.org/brands.xml
=====Individual Brand=====
* http://world.openfoodfacts.org/brand/monoprix.json
* http://world.openfoodfacts.org/brand/monoprix.xml
====Purchase Place of products====
=====List of Purchase Place =====
* http://world.openfoodfacts.org/purchase-places.json
* http://world.openfoodfacts.org/purchase-places.xml
=====Individual Purchase Place =====
* http://world.openfoodfacts.org/purchase-place/marseille-5.json
* http://world.openfoodfacts.org/purchase-place/marseille-5.xml
====Store of products====
=====List of Stores=====
* http://world.openfoodfacts.org/stores.json
* http://world.openfoodfacts.org/stores.xml
=====Individual Store=====
* http://world.openfoodfacts.org/store/super-u.json
* http://world.openfoodfacts.org/store/super-u.xml
====Country of products====
=====List of Countries =====
* http://world.openfoodfacts.org/countries.json
* http://world.openfoodfacts.org/countries.xml
=====Individual Country =====
* http://world.openfoodfacts.org/country/france.json
* http://world.openfoodfacts.org/country/france.xml

=====Getting suggestions for Countries=====
* http://world.openfoodfacts.org/cgi/suggest.pl?lc=fr&tagtype=countries&string=f
==== Ingredients ====
===== List of detected ingredients =====
* http://world.openfoodfacts.org/ingredients.json
* http://world.openfoodfacts.org/ingredients.xml

===== List of products where an ingredient has been detected =====
* http://world.openfoodfacts.org/ingredient/sucre.xml
* http://world.openfoodfacts.org/ingredient/sucre.json
<pre>Do not make the assumption that the ingredient is or is not present based on this. Parsing errors happen.</pre>

=====Getting suggestions for ingredients (ONLY FOR OBF at the moment) =====
* http://world.openbeautyfacts.org/cgi/suggest.pl?lc=fr&tagtype=ingredients&string=f

====Trace of products====
=====List of Traces =====
* http://world.openfoodfacts.org/traces.json
* http://world.openfoodfacts.org/traces.xml
=====Individual Trace =====
* http://world.openfoodfacts.org/trace/eggs.json
* http://world.openfoodfacts.org/trace/eggs.xml

=====Getting suggestions for traces =====
* http://world.openfoodfacts.org/cgi/suggest.pl?lc=fr&tagtype=traces&string=m

====Additive of products====
=====List of Additives =====
* http://world.openfoodfacts.org/additives.json
* http://world.openfoodfacts.org/additives.xml
=====Individual Additive=====
* http://world.openfoodfacts.org/additive/e301-sodium-ascorbate.json
* http://world.openfoodfacts.org/additive/e301-sodium-ascorbate.xml


=====Getting suggestions for additives =====
* http://world.openfoodfacts.org/cgi/suggest.pl?lc=fr&tagtype=additives&string=e

====allergens of products====
=====List of allergens=====
* http://world.openfoodfacts.org/allergens.json
* http://world.openfoodfacts.org/allergens.xml
=====Individual allergen=====
* http://world.openfoodfacts.org/allergen/fish.json
* http://world.openfoodfacts.org/allergen/fish.xml

=====Getting suggestions for allergens =====
* http://world.openfoodfacts.org/cgi/suggest.pl?lc=fr&tagtype=allergens&string=a

====Barcodes====
=====List of List of barcodes beginning with a given number =====
* http://world.openfoodfacts.org/codes.json
* http://world.openfoodfacts.org/codes.xml

=====List of barcodes beginning with 3596710 =====
* http://world.openfoodfacts.org/code/3596710xxxxxx.json
* http://world.openfoodfacts.org/code/3596710xxxxxx.xml

====Entry dates====
=====List of entry dates =====
* http://world.openfoodfacts.org/entry-dates.json
* http://world.openfoodfacts.org/entry-dates.xml
=====List of products with a given entry date =====
* http://world.openfoodfacts.org/entry-date/2015.json
* http://world.openfoodfacts.org/entry-date/2015.xml

====Packager codes====
=====List of Packager codes =====
* http://world.openfoodfacts.org/packager-codes.json
* http://world.openfoodfacts.org/packager-codes.xml
=====List of products with given Packager code =====
* http://world.openfoodfacts.org/packager-code/emb-35069c.json
* http://world.openfoodfacts.org/packager-code/emb-35069c.xml

=====List of Packaging cities =====
* http://world.openfoodfacts.org/cities.json
* http://world.openfoodfacts.org/cities.xml

=====List of products with given Packaging city =====
* http://world.openfoodfacts.org/city/argenteuil-val-d-oise-france.json
* http://world.openfoodfacts.org/city/argenteuil-val-d-oise-france.xml

== WRITE API Documentation ==
=== Posting photos ===
* Use the POST method on /cgi/product_image_upload.pl
** code: the barcode
** imagefield: (front | ingredients | nutrition)
** imgupload_front : your image file if imagefield:front
** imgupload_ingredients: your image file if imagefield:ingredients
** imgupload_nutrition: your image file if imagefield:nutrition

Important:
* there must be a HTTP header "Content-Type: multipart/form-data" in the HTTP POST request.
* the imageupload_(front|ingredients|nutrition) name, size and data needs to be encoded in the multipart/form-data format, usually your HTTP request library will do that for you
* all parameters need to be passed as POST parameters, do not put some in the URL


Example: <sup>(remember to do tests on world.openfoodfacts.net - login and password: off )</sup>
<pre>
http://world.openfoodfacts.org/cgi/product_image_upload.pl
</pre>
<pre>
http://world.openfoodfacts.net/cgi/product_image_upload.pl?code=654345678
</pre>

=== Posting a new product ===
* Product post to http://world.openfoodfacts.org/cgi/product_jqm2.pl <sup>(remember to do tests on world.openfoodfacts.net - login and password: off )</sup>

* URL for your tests : <pre>http://world.openfoodfacts.net/cgi/product_jqm2.pl</pre>
==== Quick overview ====
** var foodfact = { barcode : '3073780969000', name : 'KIRI GOUTER 280G 8 PORTIONS', energy: 500, energy_unit: "kJ", weight: 282 };
** var postData = {
** code         : foodfact.barcode,
** user_id      : "mesinfosnutritionelles",
** password     : "****",
** product_name : foodfact.name?foodfact.name:foodfact.shop_label,
** quantity     : foodfact.weight?""+foodfact.weight+" g":undefined,
** stores       : "Intermarché",
** nutriment_energy      :foodfact.energy,
** nutriment_energy_unit :foodfact.energy_unit,
** nutrition_data_per    :"serving"
** {"status_verbose":"fields saved","status":1}

==== Example ====
<sup>(remember to do tests on world.openfoodfacts.net - login and password: off)</sup><br>
===== Query 1 =====
<pre>http://world.openfoodfacts.net/cgi/product_jqm2.pl?code=072417136160&product_name=Maryland%20Choc%20Chip&quantity=230g&nutriment_energy=450&nutriment_energy_unit=kJ&nutrition_data_per=serving&ingredients_text=Fortified%20wheat%20flour%2C%20Chocolate%20chips%20%2825%25%29%2C%20Sugar%2C%20Palm%20oil%2C%20Golden%20syrup%2C%20Whey%20and%20whey%20derivatives%20%28Milk%29%2C%20Raising%20agents%2C%20Salt%2C%20Flavouring&traces=Milk%2C+Soya%2C+Nuts%2C+Wheat</pre>
===== Result 2 =====
<pre>http://uk.openfoodfacts.net/product/0072417136160/maryland-choc-chip</pre>

===== Query 2 =====
<pre>http://world.openfoodfacts.org/cgi/product_jqm2.pl?code=3073780969000&user_id=usernameexample&password=*****&product_name=KIRI%20GOUTER%20280G%208%20PORTIONS&quantity=282%20g&stores=Intermarch%C3%A9&nutriment_energy=500&nutriment_energy_unit=kJ&nutrition_data_per=serving</pre>
===== Result 2 =====
<pre></pre>

==== See editing a product for details on fields ====
==== Posting several values for a field ====
When adding values, send to the field labels as comma separated values that are canonicalized and added to the _tags array
<pre>labels = "labelA, labelB"</pre>
Reading back, use labels_tags to get an array of labels

=== Editing an existing product ===
==== Posting additional photos ====
* Photos post on /cgi/product_image_upload.pl
** code: the barcode
** imagefield: (front | ingredients | nutrition)
===== Select the Front picture =====
* imgupload_front : your image file if imagefield:front
===== Select the Ingredients picture =====
* imgupload_ingredients: your image file if imagefield:ingredients
===== Select the Nutrition Facts picture =====
* imgupload_nutrition: your image file if imagefield:nutrition

==== Editing the product ====
==== Give the barcode ====
<pre>code=072417136160</pre>


==== Add the brand ====
<pre>brand=Heinz</pre>

==== Add the name ====
<pre>product_name=Maryland%20Choc%20Chip</pre>
==== Add the quantity ====
<pre>quantity=230g</pre>
==== Add the packager code ====
<pre>emb_codes=EMB%2013330</pre>
==== Add the packaging type ====
<pre>packaging=Cardboard</pre>

==== Add the labels ====
<pre>labels=Vegan%2C%20Fat%20free</pre>

==== Add the Stores where bought ====
<pre>stores=Intermarch%C3%A9</pre>
==== Add the category ====
<pre>categories=Cookies</pre>
==== Add the best before date ====
<pre>expiration_date=</pre>

==== Add the link to the official webpage of the product ====
<pre>link=</pre>

==== Add the ingredients ====
<pre>ingredients_text=Fortified%20wheat%20flour%2C%20Chocolate%20chips%20%2825%25%29%2C%20Sugar%2C%20Palm%20oil%2C%20Golden%20syrup%2C%20Whey%20and%20whey%20derivatives%20%28Milk%29%2C%20Raising%20agents%2C%20Salt%2C%20Flavouring</pre>
==== Add ingredient traces ====
<pre>traces=Milk%2C+Soya%2C+Nuts%2C+Wheat</pre>

==== Add the main language ====
You can set the main language of the product.<br>
<pre>lang=fr</pre><br><br>
(NOT LIVE YET)In the case of a multilingual product, you can specify the main language of the product, and you can then specify values and images for different languages by suffixing the language code to the other fields.

==== Add the nutrition facts ====
===== Indicate the absence of nutrition facts=====
<pre>no_nutriments : indicates if the nutrition facts are indicated on the food label</pre>
===== Add nutrition facts values, units and base =====
====== Define the basis for the values ======
<pre>nutrition_data_per=100g</pre>
<br>'''OR'''<br>
<pre>nutrition_data_per=serving</pre>
<pre>serving_size=38g</pre>

====== Input values and units ======
<pre>nutriment_energy=450</pre>
<pre>nutriment_energy_unit=kJ</pre>

====== Values ======
<pre>
nutriment_energy
nutriment_proteins
nutriment_casein
nutriment_serum-proteins
nutriment_nucleotides
nutriment_carbohydrates
nutriment_sugars
nutriment_sucrose
nutriment_glucose
nutriment_fructose
nutriment_lactose
nutriment_maltose
nutriment_maltodextrins
nutriment_starch
nutriment_polyols
nutriment_fat
nutriment_saturated-fat
nutriment_butyric-acid
nutriment_caproic-acid
nutriment_caprylic-acid
nutriment_capric-acid
nutriment_lauric-acid
nutriment_myristic-acid
nutriment_palmitic-acid
nutriment_stearic-acid
nutriment_arachidic-acid
nutriment_behenic-acid
nutriment_lignoceric-acid
nutriment_cerotic-acid
nutriment_montanic-acid
nutriment_melissic-acid
nutriment_monounsaturated-fat
nutriment_polyunsaturated-fat
nutriment_omega-3-fat
nutriment_alpha-linolenic-acid
nutriment_eicosapentaenoic-acid
nutriment_docosahexaenoic-acid
nutriment_omega-6-fat
nutriment_linoleic-acid
nutriment_arachidonic-acid
nutriment_gamma-linolenic-acid
nutriment_dihomo-gamma-linolenic-acid
nutriment_omega-9-fat
nutriment_oleic-acid
nutriment_elaidic-acid
nutriment_gondoic-acid
nutriment_mead-acid
nutriment_erucic-acid
nutriment_nervonic-acid
nutriment_trans-fat
nutriment_cholesterol
nutriment_fiber
nutriment_sodium
nutriment_alcohol : % vol of alcohol
nutriment_vitamin-a
nutriment_vitamin-d
nutriment_vitamin-e
nutriment_vitamin-k
nutriment_vitamin-c
nutriment_vitamin-b1
nutriment_vitamin-b2
nutriment_vitamin-pp
nutriment_vitamin-b6
nutriment_vitamin-b9
nutriment_vitamin-b12
nutriment_biotin
nutriment_pantothenic-acid
nutriment_silica
nutriment_bicarbonate
nutriment_potassium
nutriment_chloride
nutriment_calcium
nutriment_phosphorus
nutriment_iron
nutriment_magnesium
nutriment_zinc
nutriment_copper
nutriment_manganese
nutriment_fluoride
nutriment_selenium
nutriment_chromium
nutriment_molybdenum
nutriment_iodine
nutriment_caffeine
nutriment_taurine
nutriment_ph : pH (no unit)
</pre>

====== Units ======
<pre>
nutriment_energy_unit
nutriment_proteins_unit
nutriment_casein_unit
nutriment_serum-proteins_unit
nutriment_nucleotides_unit
nutriment_carbohydrates_unit
nutriment_sugars_unit
nutriment_sucrose_unit
nutriment_glucose_unit
nutriment_fructose_unit
nutriment_lactose_unit
nutriment_maltose_unit
nutriment_maltodextrins_unit
nutriment_starch_unit
nutriment_polyols_unit
nutriment_fat_unit
nutriment_saturated-fat_unit
nutriment_butyric-acid_unit
nutriment_caproic-acid_unit
nutriment_caprylic-acid_unit
nutriment_capric-acid_unit
nutriment_lauric-acid_unit
nutriment_myristic-acid_unit
nutriment_palmitic-acid_unit
nutriment_stearic-acid_unit
nutriment_arachidic-acid_unit
nutriment_behenic-acid_unit
nutriment_lignoceric-acid_unit
nutriment_cerotic-acid_unit
nutriment_montanic-acid_unit
nutriment_melissic-acid_unit
nutriment_monounsaturated-fat_unit
nutriment_polyunsaturated-fat_unit
nutriment_omega-3-fat_unit
nutriment_alpha-linolenic-acid_unit
nutriment_eicosapentaenoic-acid_unit
nutriment_docosahexaenoic-acid_unit
nutriment_omega-6-fat_unit
nutriment_linoleic-acid_unit
nutriment_arachidonic-acid_unit
nutriment_gamma-linolenic-acid_unit
nutriment_dihomo-gamma-linolenic-acid_unit
nutriment_omega-9-fat_unit
nutriment_oleic-acid_unit
nutriment_elaidic-acid_unit
nutriment_gondoic-acid_unit
nutriment_mead-acid_unit
nutriment_erucic-acid_unit
nutriment_nervonic-acid_unit
nutriment_trans-fat_unit
nutriment_cholesterol_unit
nutriment_fiber_unit
nutriment_sodium_unit
nutriment_alcohol_unit : % vol of alcohol
nutriment_vitamin-a_unit
nutriment_vitamin-d_unit
nutriment_vitamin-e_unit
nutriment_vitamin-k_unit
nutriment_vitamin-c_unit
nutriment_vitamin-b1_unit
nutriment_vitamin-b2_unit
nutriment_vitamin-pp_unit
nutriment_vitamin-b6_unit
nutriment_vitamin-b9_unit
nutriment_vitamin-b12_unit
nutriment_biotin_unit
nutriment_pantothenic-acid_unit
nutriment_silica_unit
nutriment_bicarbonate_unit
nutriment_potassium_unit
nutriment_chloride_unit
nutriment_calcium_unit
nutriment_phosphorus_unit
nutriment_iron_unit
nutriment_magnesium_unit
nutriment_zinc_unit
nutriment_copper_unit
nutriment_manganese_unit
nutriment_fluoride_unit
nutriment_selenium_unit
nutriment_chromium_unit
nutriment_molybdenum_unit
nutriment_iodine_unit
nutriment_caffeine_unit
nutriment_taurine_unit
nutriment_ph_unit : pH (no unit)
</pre>

===== Adding the alcohol % of wine =====
12% wine
<pre>nutriment_unit=%25%20vol&nutriment_alcohol=12</pre>

===== Adding the carbon footprint =====
<pre>nutriment_carbon-footprint</pre>
<pre>nutriment_carbon-footprint_unit</pre>

=== Adding a comment to your edit ===
<pre>comment=Automated%20Edit</pre>

== Open Beauty Facts experimental and specific APIs ==
=== Ingredients ===
Very experimental. Do not rely on this for allergen or ingredient parsing yet.
==== List of ingredients detected by the current experimental parser ====
* http://world.openbeautyfacts.org/ingredients.json
* http://world.openbeautyfacts.org/ingredients.xml

==== Products where the current experimental parser could not detect aluminium salts ====
* http://world.openbeautyfacts.org/ingredient/-aluminum-salts.json
* http://world.openbeautyfacts.org/ingredient/-aluminum-salts.xml

==== Products where the current experimental parser could detect aluminium salts ====
* http://world.openbeautyfacts.org/ingredient/aluminum-salts.json
* http://world.openbeautyfacts.org/ingredient/aluminum-salts.xml

=== Period after Opening ===
* http://world.openbeautyfacts.org/periods-after-opening.json
* http://world.openbeautyfacts.org/periods-after-opening.xml
=== List of products with a given Period after Opening ===
* http://world.openbeautyfacts.org/period-after-opening/12-months.json
* http://world.openbeautyfacts.org/period-after-opening/12-months.xml

== Roadmap ==
[[API/Roadmap]]

== Language Bindings==
* [[API/Ruby|Ruby bindings]] - https://github.com/openfoodfacts/openfoodfacts-ruby - gem install openfoodfacts
* [[API/Python|Python bindings]]
