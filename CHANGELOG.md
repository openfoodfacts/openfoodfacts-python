# Changelog

## [0.2.0](https://github.com/openfoodfacts/openfoodfacts-python/compare/v0.1.12...v0.2.0) (2024-01-29)


### Features

* Force user agent in API ([#184](https://github.com/openfoodfacts/openfoodfacts-python/issues/184)) ([34024be](https://github.com/openfoodfacts/openfoodfacts-python/commit/34024beb0c4323cfa575b95f93d75d37bcc34784))


### Bug Fixes

* add a function to parse ingredients ([d0aa579](https://github.com/openfoodfacts/openfoodfacts-python/commit/d0aa579653ae21c433a24600fc5ca72742e44986))
* add add_ingredient_in_taxonomy_field function from Robotoff ([64ee295](https://github.com/openfoodfacts/openfoodfacts-python/commit/64ee295f51da60be73327f8ffb8cabcba9df2669))
* add custom headers when performing requests with the API ([163b33b](https://github.com/openfoodfacts/openfoodfacts-python/commit/163b33bf74ce08fa747cab2ff305d154af552557))
* add FacetResource.get_products method ([d790389](https://github.com/openfoodfacts/openfoodfacts-python/commit/d790389e246a5e0e93ec789d93eb5c64bc61898d))
* add timeout parameter to API ([b08b9d0](https://github.com/openfoodfacts/openfoodfacts-python/commit/b08b9d049d17ddc8804301c756aabaa455a6d755))
* fix Facet class ([82ab808](https://github.com/openfoodfacts/openfoodfacts-python/commit/82ab80809729aae40d4e1e65c5c2ab98c685baf2))
* fix FacetResource.get method ([d562063](https://github.com/openfoodfacts/openfoodfacts-python/commit/d562063ca28b8c06e993179f2929c4b2b4ff4fef))
* fix page_size parameter in facet.get_products ([9d99e6c](https://github.com/openfoodfacts/openfoodfacts-python/commit/9d99e6cae9745a72753e4726d17475a1ff910c9b))
* fixed search products by text ([#191](https://github.com/openfoodfacts/openfoodfacts-python/issues/191)) ([94c5600](https://github.com/openfoodfacts/openfoodfacts-python/commit/94c5600bb2babbd4fa80355f9e71d4847d896c27))
* improve sdk ([#193](https://github.com/openfoodfacts/openfoodfacts-python/issues/193)) ([07f224c](https://github.com/openfoodfacts/openfoodfacts-python/commit/07f224ca7bb55f38401ef3faa1b324094d9fdfc0))
* minor fix in ProductResource.get ([54a8809](https://github.com/openfoodfacts/openfoodfacts-python/commit/54a88096afa6961d332d749853fceb67c17ccbf6))


### Documentation

* add documentation about taxonomy handling ([26cd3e5](https://github.com/openfoodfacts/openfoodfacts-python/commit/26cd3e5c32a0d33494aa2efb793fb98dc7cf6871))
* add mkdocs .pages file ([3533d29](https://github.com/openfoodfacts/openfoodfacts-python/commit/3533d2965f8892d403da304e6afc40ac8055547e))
* fix nav ([925e7e5](https://github.com/openfoodfacts/openfoodfacts-python/commit/925e7e5a440cbaa826dc1388972e7bf3ca461c46))

## [0.1.12](https://github.com/openfoodfacts/openfoodfacts-python/compare/v0.1.11...v0.1.12) (2023-11-10)


### Bug Fixes

* add select_image function to API.product ([d2d0805](https://github.com/openfoodfacts/openfoodfacts-python/commit/d2d0805bcd77cc5ee06dd7994f8e76fb74237a09))
* add session cookies to all update queries (if needed) ([e3b0de0](https://github.com/openfoodfacts/openfoodfacts-python/commit/e3b0de0aa217672161107b0bbf189e09474a4345))
* provide authentification in POST requests ([545bbe9](https://github.com/openfoodfacts/openfoodfacts-python/commit/545bbe9b40cf9fa2169e11810f8aec9bcf537d00))

## [0.1.11](https://github.com/openfoodfacts/openfoodfacts-python/compare/v0.1.10...v0.1.11) (2023-10-31)


### Bug Fixes

* add get_words_in_area function for OCR ([2ea5e27](https://github.com/openfoodfacts/openfoodfacts-python/commit/2ea5e27654bccb99ca01d394fda073ade52bafbf))
* fix mypy issues ([7bf9f67](https://github.com/openfoodfacts/openfoodfacts-python/commit/7bf9f67edbbbfa293d4bb4949479f5cdbd8b17b1))

## [0.1.10](https://github.com/openfoodfacts/openfoodfacts-python/compare/v0.1.9...v0.1.10) (2023-10-03)


### Bug Fixes

* fix undefined func in ocr.py ([ff5eaa2](https://github.com/openfoodfacts/openfoodfacts-python/commit/ff5eaa26b77f59717d7f28453fcd78029aae3b0f))

## [0.1.9](https://github.com/openfoodfacts/openfoodfacts-python/compare/v0.1.8...v0.1.9) (2023-08-17)


### Bug Fixes

* add `get_country_name` function ([d59e546](https://github.com/openfoodfacts/openfoodfacts-python/commit/d59e54608464739f1cb06a7d793b874e7a771187))
* add more imports in __init__.py ([92937d0](https://github.com/openfoodfacts/openfoodfacts-python/commit/92937d0bb07f27349a98ad9c48ae7db58c6fce62))

## [0.1.8](https://github.com/openfoodfacts/openfoodfacts-python/compare/v0.1.7...v0.1.8) (2023-08-09)


### Bug Fixes

* add Lang enum ([ef5b32c](https://github.com/openfoodfacts/openfoodfacts-python/commit/ef5b32ca65e92a753a5cdc794868c1f87e1d5187))

## [0.1.7](https://github.com/openfoodfacts/openfoodfacts-python/compare/v0.1.6...v0.1.7) (2023-08-09)


### Bug Fixes

* fix Country enum ([8c0e926](https://github.com/openfoodfacts/openfoodfacts-python/commit/8c0e9260a6a73f662ade73d4f562d7feb5223566))

## [0.1.6](https://github.com/openfoodfacts/openfoodfacts-python/compare/v0.1.5...v0.1.6) (2023-08-09)


### Bug Fixes

* add country taxonomy ([06f0c16](https://github.com/openfoodfacts/openfoodfacts-python/commit/06f0c1622185f08a2ae05262a2c136521c45efba))
* add more taxonomies ([d6da4e1](https://github.com/openfoodfacts/openfoodfacts-python/commit/d6da4e1268204e49b0e46c2dd63cb0cb568e6dc1))
* fix api.py code ([27a9140](https://github.com/openfoodfacts/openfoodfacts-python/commit/27a9140589fe50b0fe82cd34a6e6bb969e8af19e))
* update Country enum to use functional syntax instead ([633add8](https://github.com/openfoodfacts/openfoodfacts-python/commit/633add8bcd8b22faacf495cf6d651f44cfd7647b))

## [0.1.5](https://github.com/openfoodfacts/openfoodfacts-python/compare/v0.1.4...v0.1.5) (2023-07-21)


### Bug Fixes

* fix github actions ([016e376](https://github.com/openfoodfacts/openfoodfacts-python/commit/016e37622b24ab109894cc3c3b9f9083ebca922f))
* fix isort config ([360f65c](https://github.com/openfoodfacts/openfoodfacts-python/commit/360f65c5deded308ec4ea721cef1e17bbaf76739))
* fix mypy error ([2109758](https://github.com/openfoodfacts/openfoodfacts-python/commit/210975896b63dc089c284c9a525448cd84b72389))
* fix release please ([39c15d2](https://github.com/openfoodfacts/openfoodfacts-python/commit/39c15d22fd61feb02acef9e04ffae435828389a0))
* fix release please ([140e53e](https://github.com/openfoodfacts/openfoodfacts-python/commit/140e53e5b3263709e2407cb2f59445ac988324cf))


### Documentation

* improve documentation in taxonomy.py ([2942143](https://github.com/openfoodfacts/openfoodfacts-python/commit/2942143374d86bddc376166a8ab85d7d2316cc95))
