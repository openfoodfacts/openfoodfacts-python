# Changelog

## [3.0.0](https://github.com/openfoodfacts/openfoodfacts-python/compare/v2.7.0...v3.0.0) (2025-07-04)


### ⚠ BREAKING CHANGES

* fix should_download_file function ([#284](https://github.com/openfoodfacts/openfoodfacts-python/issues/284))
* improve asset and image download functions

### Features

* add `create_brand_taxonomy_mapping` function ([#306](https://github.com/openfoodfacts/openfoodfacts-python/issues/306)) ([f62b74d](https://github.com/openfoodfacts/openfoodfacts-python/commit/f62b74d822b3c4e340079428262f5b32fb770443))
* add `Flavor.from_product_type` method ([#308](https://github.com/openfoodfacts/openfoodfacts-python/issues/308)) ([1cda84e](https://github.com/openfoodfacts/openfoodfacts-python/commit/1cda84e8a04c0e07579a76ab901861980c23c657))
* add dataset support ([4250504](https://github.com/openfoodfacts/openfoodfacts-python/commit/4250504dda152b0af4a737ad79be7e78562f9311))
* add download_image function ([#243](https://github.com/openfoodfacts/openfoodfacts-python/issues/243)) ([265f10b](https://github.com/openfoodfacts/openfoodfacts-python/commit/265f10bfa9047c48874255fbc66d9bab32fa61c5))
* add face annotations support in OCRResult ([#333](https://github.com/openfoodfacts/openfoodfacts-python/issues/333)) ([da800f9](https://github.com/openfoodfacts/openfoodfacts-python/commit/da800f9cba1e484f773b38696651adc97a005f80))
* add get_image_from_url function in utils.py ([db35751](https://github.com/openfoodfacts/openfoodfacts-python/commit/db357510e7f092d5fc3d922465fcaa1c032b324a))
* add helper functions for Redis stream ([6fedef7](https://github.com/openfoodfacts/openfoodfacts-python/commit/6fedef784b569c453d8d1a352195edb787e83eea))
* add image URLs processing functions ([fea5c7b](https://github.com/openfoodfacts/openfoodfacts-python/commit/fea5c7b841ab8dcb0a7dfebdbee1c7e519d8456b))
* add ingredient analysis endpoint ([#285](https://github.com/openfoodfacts/openfoodfacts-python/issues/285)) ([10c42d2](https://github.com/openfoodfacts/openfoodfacts-python/commit/10c42d20e6cd6651eab597c00d200e0f00542580))
* add map_to_canonical_id function ([#287](https://github.com/openfoodfacts/openfoodfacts-python/issues/287)) ([cde7683](https://github.com/openfoodfacts/openfoodfacts-python/commit/cde7683aa7376b17ddc621a0a99efdcf94bbcf96))
* add new methods to TestRedisUpdate ([#349](https://github.com/openfoodfacts/openfoodfacts-python/issues/349)) ([1aa68da](https://github.com/openfoodfacts/openfoodfacts-python/commit/1aa68dab8410451e328709e4eeeb0421fdd6dfcf))
* add new openfoodfacts.ml module ([#293](https://github.com/openfoodfacts/openfoodfacts-python/issues/293)) ([27659fe](https://github.com/openfoodfacts/openfoodfacts-python/commit/27659fe2788c4273b93945790dcbe4824e3e5f4b))
* add OCR JSON parsing support ([abb9a7e](https://github.com/openfoodfacts/openfoodfacts-python/commit/abb9a7e7e33b1d56aa61a526745d7b9142697f7a))
* add PEP 561 compliance (typing in installed package) ([#215](https://github.com/openfoodfacts/openfoodfacts-python/issues/215)) ([ca7fc41](https://github.com/openfoodfacts/openfoodfacts-python/commit/ca7fc41ec9b3a7610af28db5683ec6344e3c3022))
* Add Release-Please ([0c7e656](https://github.com/openfoodfacts/openfoodfacts-python/commit/0c7e656bea662621da906cdacb133cb8192ba1aa))
* add Robotoff resource ([953ae41](https://github.com/openfoodfacts/openfoodfacts-python/commit/953ae419d613b874e109217e6764ef63bf2fdb44))
* add run_ocr_on_image_batch function ([decd94d](https://github.com/openfoodfacts/openfoodfacts-python/commit/decd94d8d1830dcef4b4e8c76e840fe753084c4c))
* add support for downloading obsolete product dump in ProductDataset ([1c26936](https://github.com/openfoodfacts/openfoodfacts-python/commit/1c2693681223968ef222d2bf1de60da6cb6c1468))
* add taxonomy.py ([198b0ed](https://github.com/openfoodfacts/openfoodfacts-python/commit/198b0ed9f0a68ca4516887aa214f25074b7f50dd))
* add UpdateListener class ([#304](https://github.com/openfoodfacts/openfoodfacts-python/issues/304)) ([56362ac](https://github.com/openfoodfacts/openfoodfacts-python/commit/56362ac1503c7534224d831bda8e3b7966f1f83a))
* allow fetching other datasets (obf, opff, opf) ([36a9625](https://github.com/openfoodfacts/openfoodfacts-python/commit/36a962599da1bcfd679c675432b330737b3189ba))
* allow to specify cache dir ([5126ba2](https://github.com/openfoodfacts/openfoodfacts-python/commit/5126ba22292728b11ddecab1b3b28f8bff19ba42))
* Auto-label PRs ([eeb88a8](https://github.com/openfoodfacts/openfoodfacts-python/commit/eeb88a836a65f3513e8f0b0f5c70ac2c9c942c4b))
* CodeQL Analysis ([0e11dc2](https://github.com/openfoodfacts/openfoodfacts-python/commit/0e11dc2daa6b75fdbd4114de031f92884d88f023))
* Force user agent in API ([#184](https://github.com/openfoodfacts/openfoodfacts-python/issues/184)) ([34024be](https://github.com/openfoodfacts/openfoodfacts-python/commit/34024beb0c4323cfa575b95f93d75d37bcc34784))
* improve asset and image download functions ([f5b4f90](https://github.com/openfoodfacts/openfoodfacts-python/commit/f5b4f90efb56e2ec775a8e11453818a6d6d8ef75))
* improve Redis API ([8f421e2](https://github.com/openfoodfacts/openfoodfacts-python/commit/8f421e20f1c8366f63578f123bc32565aca5b750))
* Improve SDK ([1453ab8](https://github.com/openfoodfacts/openfoodfacts-python/commit/1453ab89a294637f99ac707f85fdbd16c5db7259))
* major SDK revamp ([4edc3e7](https://github.com/openfoodfacts/openfoodfacts-python/commit/4edc3e7e013243b996a38f9e58d0cf6829dd2f6d))
* release package on Conda ([#94](https://github.com/openfoodfacts/openfoodfacts-python/issues/94)) ([7e0430c](https://github.com/openfoodfacts/openfoodfacts-python/commit/7e0430c3fa57f2754e6727de62202e87929a9446))


### Bug Fixes

* add `get_country_name` function ([d59e546](https://github.com/openfoodfacts/openfoodfacts-python/commit/d59e54608464739f1cb06a7d793b874e7a771187))
* add a function to parse ingredients ([d0aa579](https://github.com/openfoodfacts/openfoodfacts-python/commit/d0aa579653ae21c433a24600fc5ca72742e44986))
* add add_ingredient_in_taxonomy_field function from Robotoff ([64ee295](https://github.com/openfoodfacts/openfoodfacts-python/commit/64ee295f51da60be73327f8ffb8cabcba9df2669))
* add country support ([b2dfd53](https://github.com/openfoodfacts/openfoodfacts-python/commit/b2dfd5301273fdb316473a5f95fc720476608185))
* add country taxonomy ([06f0c16](https://github.com/openfoodfacts/openfoodfacts-python/commit/06f0c1622185f08a2ae05262a2c136521c45efba))
* add custom headers when performing requests with the API ([163b33b](https://github.com/openfoodfacts/openfoodfacts-python/commit/163b33bf74ce08fa747cab2ff305d154af552557))
* add FacetResource.get_products method ([d790389](https://github.com/openfoodfacts/openfoodfacts-python/commit/d790389e246a5e0e93ec789d93eb5c64bc61898d))
* add get_words_in_area function for OCR ([2ea5e27](https://github.com/openfoodfacts/openfoodfacts-python/commit/2ea5e27654bccb99ca01d394fda073ade52bafbf))
* add Lang enum ([ef5b32c](https://github.com/openfoodfacts/openfoodfacts-python/commit/ef5b32ca65e92a753a5cdc794868c1f87e1d5187))
* add min_id parameter to get_new_updates ([a19aeb5](https://github.com/openfoodfacts/openfoodfacts-python/commit/a19aeb51cbfe65756dba3db5ae975484834bf8a2))
* add more imports in __init__.py ([92937d0](https://github.com/openfoodfacts/openfoodfacts-python/commit/92937d0bb07f27349a98ad9c48ae7db58c6fce62))
* add more taxonomies ([d6da4e1](https://github.com/openfoodfacts/openfoodfacts-python/commit/d6da4e1268204e49b0e46c2dd63cb0cb568e6dc1))
* add new function to convert images to old schema ([#327](https://github.com/openfoodfacts/openfoodfacts-python/issues/327)) ([224c38c](https://github.com/openfoodfacts/openfoodfacts-python/commit/224c38cc202e94ba2ecb6ba5a68ba7f8609c4c49))
* add new functions related to barcodes ([6faadc1](https://github.com/openfoodfacts/openfoodfacts-python/commit/6faadc1ea00b9ade6dfad50ba9cd5c261a4dcf8a))
* add Pillow as optional dependency (+ extra) ([5ba7719](https://github.com/openfoodfacts/openfoodfacts-python/commit/5ba77194060ef203e739fb30395f89d12ef358bb))
* add select_image function to API.product ([d2d0805](https://github.com/openfoodfacts/openfoodfacts-python/commit/d2d0805bcd77cc5ee06dd7994f8e76fb74237a09))
* add session cookies to all update queries (if needed) ([e3b0de0](https://github.com/openfoodfacts/openfoodfacts-python/commit/e3b0de0aa217672161107b0bbf189e09474a4345))
* add timeout parameter to API ([b08b9d0](https://github.com/openfoodfacts/openfoodfacts-python/commit/b08b9d049d17ddc8804301c756aabaa455a6d755))
* Automate PyPI workflow  ([#89](https://github.com/openfoodfacts/openfoodfacts-python/issues/89)) ([2b947bc](https://github.com/openfoodfacts/openfoodfacts-python/commit/2b947bc304b04d0b000509fbb39ffc4854220bac))
* brands taxonomy might use xx language code ([#320](https://github.com/openfoodfacts/openfoodfacts-python/issues/320)) ([9e48a60](https://github.com/openfoodfacts/openfoodfacts-python/commit/9e48a60945440d119313ae38a9c46dfa2710eea3)), closes [#319](https://github.com/openfoodfacts/openfoodfacts-python/issues/319)
* correct path separator issue in extract_source_from_url function for Windows compatibility ([#280](https://github.com/openfoodfacts/openfoodfacts-python/issues/280)) ([385fbdb](https://github.com/openfoodfacts/openfoodfacts-python/commit/385fbdb9c2e27751c6494edead38b153103ce507))
* don't assume Pillow is available ([fd2f8f2](https://github.com/openfoodfacts/openfoodfacts-python/commit/fd2f8f2faad1f670e316374924cf42eed8d4fab0))
* fix api.py code ([27a9140](https://github.com/openfoodfacts/openfoodfacts-python/commit/27a9140589fe50b0fe82cd34a6e6bb969e8af19e))
* fix barcode splitting bug for image URL generation ([7250afb](https://github.com/openfoodfacts/openfoodfacts-python/commit/7250afb203fc9fc9d80315e0681f604e32a6b193))
* fix bug when min_id=None was provided ([d55db32](https://github.com/openfoodfacts/openfoodfacts-python/commit/d55db32d5c01ce79fbc9cf2a7d93ac9eb058826e))
* fix CI ([ef4e67d](https://github.com/openfoodfacts/openfoodfacts-python/commit/ef4e67d8a321a6abb8e39af4844f3509139ebeb5))
* fix Country enum ([8c0e926](https://github.com/openfoodfacts/openfoodfacts-python/commit/8c0e9260a6a73f662ade73d4f562d7feb5223566))
* fix extra dependency specification ([#296](https://github.com/openfoodfacts/openfoodfacts-python/issues/296)) ([90e06b6](https://github.com/openfoodfacts/openfoodfacts-python/commit/90e06b68ba872cf5668f2a93a9ecdc8fa798f6ba))
* fix Facet class ([82ab808](https://github.com/openfoodfacts/openfoodfacts-python/commit/82ab80809729aae40d4e1e65c5c2ab98c685baf2))
* fix FacetResource.get method ([d562063](https://github.com/openfoodfacts/openfoodfacts-python/commit/d562063ca28b8c06e993179f2929c4b2b4ff4fef))
* fix Flavor.opf domain ([70c6f6b](https://github.com/openfoodfacts/openfoodfacts-python/commit/70c6f6bdc9754b6ad418513de47103344c360b57))
* fix Flavor.opf domain ([acdd9f7](https://github.com/openfoodfacts/openfoodfacts-python/commit/acdd9f709ab8dc9bbd9bfcc71fe25a21b7933497))
* fix github actions ([070c338](https://github.com/openfoodfacts/openfoodfacts-python/commit/070c33846c85fdce3d4937e357d2d155d801bd76))
* fix github actions ([016e376](https://github.com/openfoodfacts/openfoodfacts-python/commit/016e37622b24ab109894cc3c3b9f9083ebca922f))
* fix isort config ([360f65c](https://github.com/openfoodfacts/openfoodfacts-python/commit/360f65c5deded308ec4ea721cef1e17bbaf76739))
* fix issue in map_to_canonical_id function ([#332](https://github.com/openfoodfacts/openfoodfacts-python/issues/332)) ([e383de1](https://github.com/openfoodfacts/openfoodfacts-python/commit/e383de11cc4aff9177887ee007aa0996b7240ff2)), closes [#331](https://github.com/openfoodfacts/openfoodfacts-python/issues/331)
* fix issue witn convert_to_legacy_schema function ([#335](https://github.com/openfoodfacts/openfoodfacts-python/issues/335)) ([9897443](https://github.com/openfoodfacts/openfoodfacts-python/commit/9897443a0af44ec92ed307c3b9fc3f9d4f349e23)), closes [#334](https://github.com/openfoodfacts/openfoodfacts-python/issues/334)
* fix mkdocs build ([a9de700](https://github.com/openfoodfacts/openfoodfacts-python/commit/a9de70081acf0d0c927141d0ae7bc0d02fdc4e05))
* fix mypy error ([2109758](https://github.com/openfoodfacts/openfoodfacts-python/commit/210975896b63dc089c284c9a525448cd84b72389))
* fix mypy errors ([5fd6abd](https://github.com/openfoodfacts/openfoodfacts-python/commit/5fd6abdc77778133562abd004bd67976c7904c49))
* fix mypy issues ([7bf9f67](https://github.com/openfoodfacts/openfoodfacts-python/commit/7bf9f67edbbbfa293d4bb4949479f5cdbd8b17b1))
* fix page_size parameter in facet.get_products ([9d99e6c](https://github.com/openfoodfacts/openfoodfacts-python/commit/9d99e6cae9745a72753e4726d17475a1ff910c9b))
* fix ProductResource.update method ([29c40ad](https://github.com/openfoodfacts/openfoodfacts-python/commit/29c40ad1360f20178bd6b23bce1acf9c99847847))
* fix release please ([39c15d2](https://github.com/openfoodfacts/openfoodfacts-python/commit/39c15d22fd61feb02acef9e04ffae435828389a0))
* fix release please ([d5a877c](https://github.com/openfoodfacts/openfoodfacts-python/commit/d5a877c09d4218f52be260d64d71cf34ee607af3))
* fix release please ([140e53e](https://github.com/openfoodfacts/openfoodfacts-python/commit/140e53e5b3263709e2407cb2f59445ac988324cf))
* fix should_download_file function ([#284](https://github.com/openfoodfacts/openfoodfacts-python/issues/284)) ([eb77a8c](https://github.com/openfoodfacts/openfoodfacts-python/commit/eb77a8ca5b873b28f51442987f8eb8c6f02b1f41))
* fix typing error ([dd51e71](https://github.com/openfoodfacts/openfoodfacts-python/commit/dd51e710e924396f2273dc70c2dbcbcf3c730778))
* fix undefined func in ocr.py ([ff5eaa2](https://github.com/openfoodfacts/openfoodfacts-python/commit/ff5eaa26b77f59717d7f28453fcd78029aae3b0f))
* fix wrong scale_x and scale_y for object detection models ([#302](https://github.com/openfoodfacts/openfoodfacts-python/issues/302)) ([8558d6d](https://github.com/openfoodfacts/openfoodfacts-python/commit/8558d6dc9a8fdeafeaec391350f35fa8b1350981))
* fix_upd_product ([506f7a8](https://github.com/openfoodfacts/openfoodfacts-python/commit/506f7a8b57918e0caff49747ded699d8176d599f))
* fixed search products by text ([#191](https://github.com/openfoodfacts/openfoodfacts-python/issues/191)) ([94c5600](https://github.com/openfoodfacts/openfoodfacts-python/commit/94c5600bb2babbd4fa80355f9e71d4847d896c27))
* improve ProductDataset class ([c777d0f](https://github.com/openfoodfacts/openfoodfacts-python/commit/c777d0f383e5b423b85e7853080ef383921844c2))
* improve RedisUpdate class ([1b90084](https://github.com/openfoodfacts/openfoodfacts-python/commit/1b9008463200c9a3a598669c4636ff9af9cd137c))
* improve sdk ([#193](https://github.com/openfoodfacts/openfoodfacts-python/issues/193)) ([07f224c](https://github.com/openfoodfacts/openfoodfacts-python/commit/07f224ca7bb55f38401ef3faa1b324094d9fdfc0))
* increase csv field_size_limit to accommodate large fields ([94be4d3](https://github.com/openfoodfacts/openfoodfacts-python/commit/94be4d3cda2adf2967062cfedc289337c5e99842))
* make predict_lang compatible with signature ([757cab9](https://github.com/openfoodfacts/openfoodfacts-python/commit/757cab9f104f2b5ff54cd44ad901b68779c4c20a))
* make RedisUpdate.product_type mandatory ([3cb66b1](https://github.com/openfoodfacts/openfoodfacts-python/commit/3cb66b1971b92514df9c965a2b9f9e7b51e5053f))
* **metadata:** add project repository URL ([#311](https://github.com/openfoodfacts/openfoodfacts-python/issues/311)) ([cbf38b4](https://github.com/openfoodfacts/openfoodfacts-python/commit/cbf38b4aed0a1af260b94811e44c7e327afe8635))
* **metadata:** set license to "MIT" (as in LICENSE file) ([#310](https://github.com/openfoodfacts/openfoodfacts-python/issues/310)) ([d82191c](https://github.com/openfoodfacts/openfoodfacts-python/commit/d82191c6448fef0759b03d6d9b6068954d2c0dbb))
* minor fix in ProductResource.get ([54a8809](https://github.com/openfoodfacts/openfoodfacts-python/commit/54a88096afa6961d332d749853fceb67c17ccbf6))
* only add HTTP auth headers when it's needed ([5c81025](https://github.com/openfoodfacts/openfoodfacts-python/commit/5c8102598d352f025298b41ff960d1ea1e87c6f4))
* provide authentification in POST requests ([545bbe9](https://github.com/openfoodfacts/openfoodfacts-python/commit/545bbe9b40cf9fa2169e11810f8aec9bcf537d00))
* relax constraint on Pillow dep ([#298](https://github.com/openfoodfacts/openfoodfacts-python/issues/298)) ([7bf368c](https://github.com/openfoodfacts/openfoodfacts-python/commit/7bf368cfcd403d5578e9bd4af501338dc2e97947))
* remove legacy notify field in OCRRegex ([#348](https://github.com/openfoodfacts/openfoodfacts-python/issues/348)) ([00abb17](https://github.com/openfoodfacts/openfoodfacts-python/commit/00abb17cc9b52d1aa32e29a0e8b711d79c1092d3))
* remove root logger ([453764c](https://github.com/openfoodfacts/openfoodfacts-python/commit/453764cf561ed8e867349f888e57e749108ebc85))
* remove unused variable in tests ([3a1375e](https://github.com/openfoodfacts/openfoodfacts-python/commit/3a1375ea718ffd4c2c19778d524c4681a0bb3c37))
* rename product.create into product.update ([23789d6](https://github.com/openfoodfacts/openfoodfacts-python/commit/23789d6234c9dd65b5760e5bd9a16b23deb461e9))
* update copyright year ([3c80d59](https://github.com/openfoodfacts/openfoodfacts-python/commit/3c80d5918fa03a66d0618a5a6f50937973ca33aa))
* update Country enum to use functional syntax instead ([633add8](https://github.com/openfoodfacts/openfoodfacts-python/commit/633add8bcd8b22faacf495cf6d651f44cfd7647b))
* use [project.optional-dependencies] instead of [tool.poetry.extras] ([#350](https://github.com/openfoodfacts/openfoodfacts-python/issues/350)) ([1012279](https://github.com/openfoodfacts/openfoodfacts-python/commit/1012279b91e91bb3c47b26632c02bacd33b16d72))
* use headless version of OpenCV ([#300](https://github.com/openfoodfacts/openfoodfacts-python/issues/300)) ([7c2fe0a](https://github.com/openfoodfacts/openfoodfacts-python/commit/7c2fe0a53c46023c280d8913c5d3a2f656e41483))
* use new barcode normalization ([b49b362](https://github.com/openfoodfacts/openfoodfacts-python/commit/b49b362f5fcbc422aef724688d7d4622b2a993fc))
* use poetry and pyproject.toml ([a7c1169](https://github.com/openfoodfacts/openfoodfacts-python/commit/a7c11697b8d2bb6aa48985b25e04d6c666af384c))


### Dependencies

* relax dependency constrains ([#295](https://github.com/openfoodfacts/openfoodfacts-python/issues/295)) ([4456195](https://github.com/openfoodfacts/openfoodfacts-python/commit/44561954fe744368eb417797037afabaa90fd575))
* relax dependency constraints ([4456195](https://github.com/openfoodfacts/openfoodfacts-python/commit/44561954fe744368eb417797037afabaa90fd575))


### Documentation

* add docstring ([5344310](https://github.com/openfoodfacts/openfoodfacts-python/commit/5344310a1abd7bd0ab2965714e3726a1a015c990))
* add documentation about taxonomy handling ([26cd3e5](https://github.com/openfoodfacts/openfoodfacts-python/commit/26cd3e5c32a0d33494aa2efb793fb98dc7cf6871))
* add missing changelog for [#223](https://github.com/openfoodfacts/openfoodfacts-python/issues/223) ([#282](https://github.com/openfoodfacts/openfoodfacts-python/issues/282)) ([b1134cc](https://github.com/openfoodfacts/openfoodfacts-python/commit/b1134cc1799029b794bb92687b126b7420bbb5cf))
* add mkdocs .pages file ([3533d29](https://github.com/openfoodfacts/openfoodfacts-python/commit/3533d2965f8892d403da304e6afc40ac8055547e))
* fix documentation (README.md, usage) ([41d4542](https://github.com/openfoodfacts/openfoodfacts-python/commit/41d45429e38ff1cd30afc2367221a9b265a28773))
* fix nav ([925e7e5](https://github.com/openfoodfacts/openfoodfacts-python/commit/925e7e5a440cbaa826dc1388972e7bf3ca461c46))
* https://python-poetry.org/docs/pyproject/#repository ([cbf38b4](https://github.com/openfoodfacts/openfoodfacts-python/commit/cbf38b4aed0a1af260b94811e44c7e327afe8635))
* improve documentation in taxonomy.py ([2942143](https://github.com/openfoodfacts/openfoodfacts-python/commit/2942143374d86bddc376166a8ab85d7d2316cc95))
* Make project REUSE v3.3 compliant ([#337](https://github.com/openfoodfacts/openfoodfacts-python/issues/337)) ([799bbaa](https://github.com/openfoodfacts/openfoodfacts-python/commit/799bbaa2a9f76357824c9aa321b6c51a44bf7576))
* Update PR template ([#102](https://github.com/openfoodfacts/openfoodfacts-python/issues/102)) ([8df0b3c](https://github.com/openfoodfacts/openfoodfacts-python/commit/8df0b3cc00dc424b2903dd148c75739185adea69))
* Update readme ([#101](https://github.com/openfoodfacts/openfoodfacts-python/issues/101)) ([f91ad0e](https://github.com/openfoodfacts/openfoodfacts-python/commit/f91ad0ec41f67e2b0374fe3b14af22175dec52ed))
* update readme.md ([2d6de77](https://github.com/openfoodfacts/openfoodfacts-python/commit/2d6de7719d38a1bd1d45340d86bb1ddb1a52822b))
* update readme.md ([903e167](https://github.com/openfoodfacts/openfoodfacts-python/commit/903e167827db93ebe436862c27a585d99c3c8d81))
* use README.md on Pypi ([6b7eda7](https://github.com/openfoodfacts/openfoodfacts-python/commit/6b7eda73f7beebcef66f78990d21ffca987c79fd))

## [2.7.0](https://github.com/openfoodfacts/openfoodfacts-python/compare/v2.6.1...v2.7.0) (2025-07-04)


### Features

* add new methods to TestRedisUpdate ([#349](https://github.com/openfoodfacts/openfoodfacts-python/issues/349)) ([1aa68da](https://github.com/openfoodfacts/openfoodfacts-python/commit/1aa68dab8410451e328709e4eeeb0421fdd6dfcf))


### Bug Fixes

* remove legacy notify field in OCRRegex ([#348](https://github.com/openfoodfacts/openfoodfacts-python/issues/348)) ([00abb17](https://github.com/openfoodfacts/openfoodfacts-python/commit/00abb17cc9b52d1aa32e29a0e8b711d79c1092d3))
* use [project.optional-dependencies] instead of [tool.poetry.extras] ([#350](https://github.com/openfoodfacts/openfoodfacts-python/issues/350)) ([1012279](https://github.com/openfoodfacts/openfoodfacts-python/commit/1012279b91e91bb3c47b26632c02bacd33b16d72))


### Documentation

* Make project REUSE v3.3 compliant ([#337](https://github.com/openfoodfacts/openfoodfacts-python/issues/337)) ([799bbaa](https://github.com/openfoodfacts/openfoodfacts-python/commit/799bbaa2a9f76357824c9aa321b6c51a44bf7576))

## [2.6.1](https://github.com/openfoodfacts/openfoodfacts-python/compare/v2.6.0...v2.6.1) (2025-06-12)


### Bug Fixes

* fix issue witn convert_to_legacy_schema function ([#335](https://github.com/openfoodfacts/openfoodfacts-python/issues/335)) ([9897443](https://github.com/openfoodfacts/openfoodfacts-python/commit/9897443a0af44ec92ed307c3b9fc3f9d4f349e23)), closes [#334](https://github.com/openfoodfacts/openfoodfacts-python/issues/334)

## [2.6.0](https://github.com/openfoodfacts/openfoodfacts-python/compare/v2.5.2...v2.6.0) (2025-05-30)


### Features

* add face annotations support in OCRResult ([#333](https://github.com/openfoodfacts/openfoodfacts-python/issues/333)) ([da800f9](https://github.com/openfoodfacts/openfoodfacts-python/commit/da800f9cba1e484f773b38696651adc97a005f80))


### Bug Fixes

* fix issue in map_to_canonical_id function ([#332](https://github.com/openfoodfacts/openfoodfacts-python/issues/332)) ([e383de1](https://github.com/openfoodfacts/openfoodfacts-python/commit/e383de11cc4aff9177887ee007aa0996b7240ff2)), closes [#331](https://github.com/openfoodfacts/openfoodfacts-python/issues/331)
* remove unused variable in tests ([3a1375e](https://github.com/openfoodfacts/openfoodfacts-python/commit/3a1375ea718ffd4c2c19778d524c4681a0bb3c37))

## [2.5.2](https://github.com/openfoodfacts/openfoodfacts-python/compare/v2.5.1...v2.5.2) (2025-05-21)


### Bug Fixes

* add new function to convert images to old schema ([#327](https://github.com/openfoodfacts/openfoodfacts-python/issues/327)) ([224c38c](https://github.com/openfoodfacts/openfoodfacts-python/commit/224c38cc202e94ba2ecb6ba5a68ba7f8609c4c49))

## [2.5.1](https://github.com/openfoodfacts/openfoodfacts-python/compare/v2.5.0...v2.5.1) (2025-04-03)


### Bug Fixes

* brands taxonomy might use xx language code ([#320](https://github.com/openfoodfacts/openfoodfacts-python/issues/320)) ([9e48a60](https://github.com/openfoodfacts/openfoodfacts-python/commit/9e48a60945440d119313ae38a9c46dfa2710eea3)), closes [#319](https://github.com/openfoodfacts/openfoodfacts-python/issues/319)
* **metadata:** add project repository URL ([#311](https://github.com/openfoodfacts/openfoodfacts-python/issues/311)) ([cbf38b4](https://github.com/openfoodfacts/openfoodfacts-python/commit/cbf38b4aed0a1af260b94811e44c7e327afe8635))
* **metadata:** set license to "MIT" (as in LICENSE file) ([#310](https://github.com/openfoodfacts/openfoodfacts-python/issues/310)) ([d82191c](https://github.com/openfoodfacts/openfoodfacts-python/commit/d82191c6448fef0759b03d6d9b6068954d2c0dbb))


### Documentation

* https://python-poetry.org/docs/pyproject/#repository ([cbf38b4](https://github.com/openfoodfacts/openfoodfacts-python/commit/cbf38b4aed0a1af260b94811e44c7e327afe8635))

## [2.5.0](https://github.com/openfoodfacts/openfoodfacts-python/compare/v2.4.0...v2.5.0) (2024-12-12)


### Features

* add `create_brand_taxonomy_mapping` function ([#306](https://github.com/openfoodfacts/openfoodfacts-python/issues/306)) ([f62b74d](https://github.com/openfoodfacts/openfoodfacts-python/commit/f62b74d822b3c4e340079428262f5b32fb770443))
* add `Flavor.from_product_type` method ([#308](https://github.com/openfoodfacts/openfoodfacts-python/issues/308)) ([1cda84e](https://github.com/openfoodfacts/openfoodfacts-python/commit/1cda84e8a04c0e07579a76ab901861980c23c657))

## [2.4.0](https://github.com/openfoodfacts/openfoodfacts-python/compare/v2.3.4...v2.4.0) (2024-12-11)


### Features

* add UpdateListener class ([#304](https://github.com/openfoodfacts/openfoodfacts-python/issues/304)) ([56362ac](https://github.com/openfoodfacts/openfoodfacts-python/commit/56362ac1503c7534224d831bda8e3b7966f1f83a))

## [2.3.4](https://github.com/openfoodfacts/openfoodfacts-python/compare/v2.3.3...v2.3.4) (2024-12-10)


### Bug Fixes

* fix wrong scale_x and scale_y for object detection models ([#302](https://github.com/openfoodfacts/openfoodfacts-python/issues/302)) ([8558d6d](https://github.com/openfoodfacts/openfoodfacts-python/commit/8558d6dc9a8fdeafeaec391350f35fa8b1350981))

## [2.3.3](https://github.com/openfoodfacts/openfoodfacts-python/compare/v2.3.2...v2.3.3) (2024-12-10)


### Bug Fixes

* use headless version of OpenCV ([#300](https://github.com/openfoodfacts/openfoodfacts-python/issues/300)) ([7c2fe0a](https://github.com/openfoodfacts/openfoodfacts-python/commit/7c2fe0a53c46023c280d8913c5d3a2f656e41483))

## [2.3.2](https://github.com/openfoodfacts/openfoodfacts-python/compare/v2.3.1...v2.3.2) (2024-12-10)


### Bug Fixes

* relax constraint on Pillow dep ([#298](https://github.com/openfoodfacts/openfoodfacts-python/issues/298)) ([7bf368c](https://github.com/openfoodfacts/openfoodfacts-python/commit/7bf368cfcd403d5578e9bd4af501338dc2e97947))

## [2.3.1](https://github.com/openfoodfacts/openfoodfacts-python/compare/v2.3.0...v2.3.1) (2024-12-10)


### Bug Fixes

* fix extra dependency specification ([#296](https://github.com/openfoodfacts/openfoodfacts-python/issues/296)) ([90e06b6](https://github.com/openfoodfacts/openfoodfacts-python/commit/90e06b68ba872cf5668f2a93a9ecdc8fa798f6ba))

## [2.3.0](https://github.com/openfoodfacts/openfoodfacts-python/compare/v2.2.0...v2.3.0) (2024-12-09)


### Features

* add new openfoodfacts.ml module ([#293](https://github.com/openfoodfacts/openfoodfacts-python/issues/293)) ([27659fe](https://github.com/openfoodfacts/openfoodfacts-python/commit/27659fe2788c4273b93945790dcbe4824e3e5f4b))


### Dependencies

* relax dependency constrains ([#295](https://github.com/openfoodfacts/openfoodfacts-python/issues/295)) ([4456195](https://github.com/openfoodfacts/openfoodfacts-python/commit/44561954fe744368eb417797037afabaa90fd575))
* relax dependency constraints ([4456195](https://github.com/openfoodfacts/openfoodfacts-python/commit/44561954fe744368eb417797037afabaa90fd575))

## [2.2.0](https://github.com/openfoodfacts/openfoodfacts-python/compare/v2.1.0...v2.2.0) (2024-11-06)


### Features

* add map_to_canonical_id function ([#287](https://github.com/openfoodfacts/openfoodfacts-python/issues/287)) ([cde7683](https://github.com/openfoodfacts/openfoodfacts-python/commit/cde7683aa7376b17ddc621a0a99efdcf94bbcf96))

## [2.1.0](https://github.com/openfoodfacts/openfoodfacts-python/compare/v2.0.0...v2.1.0) (2024-11-06)


### Features

* add ingredient analysis endpoint ([#285](https://github.com/openfoodfacts/openfoodfacts-python/issues/285)) ([10c42d2](https://github.com/openfoodfacts/openfoodfacts-python/commit/10c42d20e6cd6651eab597c00d200e0f00542580))

## [2.0.0](https://github.com/openfoodfacts/openfoodfacts-python/compare/v1.1.5...v2.0.0) (2024-11-05)


### ⚠ BREAKING CHANGES

* fix should_download_file function ([#284](https://github.com/openfoodfacts/openfoodfacts-python/issues/284))

### Features

* add support for downloading obsolete product dump in ProductDataset ([1c26936](https://github.com/openfoodfacts/openfoodfacts-python/commit/1c2693681223968ef222d2bf1de60da6cb6c1468))


### Bug Fixes

* correct path separator issue in extract_source_from_url function for Windows compatibility ([#280](https://github.com/openfoodfacts/openfoodfacts-python/issues/280)) ([385fbdb](https://github.com/openfoodfacts/openfoodfacts-python/commit/385fbdb9c2e27751c6494edead38b153103ce507))
* fix should_download_file function ([#284](https://github.com/openfoodfacts/openfoodfacts-python/issues/284)) ([eb77a8c](https://github.com/openfoodfacts/openfoodfacts-python/commit/eb77a8ca5b873b28f51442987f8eb8c6f02b1f41))


### Documentation

* add missing changelog for [#223](https://github.com/openfoodfacts/openfoodfacts-python/issues/223) ([#282](https://github.com/openfoodfacts/openfoodfacts-python/issues/282)) ([b1134cc](https://github.com/openfoodfacts/openfoodfacts-python/commit/b1134cc1799029b794bb92687b126b7420bbb5cf))

## [1.1.5](https://github.com/openfoodfacts/openfoodfacts-python/compare/v1.1.4...v1.1.5) (2024-10-14)


### Bug Fixes

* fix barcode splitting bug for image URL generation ([7250afb](https://github.com/openfoodfacts/openfoodfacts-python/commit/7250afb203fc9fc9d80315e0681f604e32a6b193))

## [1.1.4](https://github.com/openfoodfacts/openfoodfacts-python/compare/v1.1.3...v1.1.4) (2024-10-08)


### Bug Fixes

* add new functions related to barcodes ([6faadc1](https://github.com/openfoodfacts/openfoodfacts-python/commit/6faadc1ea00b9ade6dfad50ba9cd5c261a4dcf8a))
* increase csv field_size_limit to accommodate large fields ([94be4d3](https://github.com/openfoodfacts/openfoodfacts-python/commit/94be4d3cda2adf2967062cfedc289337c5e99842))
* make RedisUpdate.product_type mandatory ([3cb66b1](https://github.com/openfoodfacts/openfoodfacts-python/commit/3cb66b1971b92514df9c965a2b9f9e7b51e5053f))

## [1.1.3](https://github.com/openfoodfacts/openfoodfacts-python/compare/v1.1.2...v1.1.3) (2024-10-04)


### Bug Fixes

* don't assume Pillow is available ([fd2f8f2](https://github.com/openfoodfacts/openfoodfacts-python/commit/fd2f8f2faad1f670e316374924cf42eed8d4fab0))

## [1.1.2](https://github.com/openfoodfacts/openfoodfacts-python/compare/v1.1.1...v1.1.2) (2024-10-04)


### Bug Fixes

* improve ProductDataset class ([c777d0f](https://github.com/openfoodfacts/openfoodfacts-python/commit/c777d0f383e5b423b85e7853080ef383921844c2))
* only add HTTP auth headers when it's needed ([5c81025](https://github.com/openfoodfacts/openfoodfacts-python/commit/5c8102598d352f025298b41ff960d1ea1e87c6f4))
* use new barcode normalization ([b49b362](https://github.com/openfoodfacts/openfoodfacts-python/commit/b49b362f5fcbc422aef724688d7d4622b2a993fc))

## [1.1.1](https://github.com/openfoodfacts/openfoodfacts-python/compare/v1.1.0...v1.1.1) (2024-07-18)


### Bug Fixes

* fix bug when min_id=None was provided ([d55db32](https://github.com/openfoodfacts/openfoodfacts-python/commit/d55db32d5c01ce79fbc9cf2a7d93ac9eb058826e))

## [1.1.0](https://github.com/openfoodfacts/openfoodfacts-python/compare/v1.0.2...v1.1.0) (2024-07-18)


### Features

* improve Redis API ([8f421e2](https://github.com/openfoodfacts/openfoodfacts-python/commit/8f421e20f1c8366f63578f123bc32565aca5b750))

## [1.0.2](https://github.com/openfoodfacts/openfoodfacts-python/compare/v1.0.1...v1.0.2) (2024-07-18)


### Bug Fixes

* add min_id parameter to get_new_updates ([a19aeb5](https://github.com/openfoodfacts/openfoodfacts-python/commit/a19aeb51cbfe65756dba3db5ae975484834bf8a2))

## [1.0.1](https://github.com/openfoodfacts/openfoodfacts-python/compare/v1.0.0...v1.0.1) (2024-07-18)


### Bug Fixes

* improve RedisUpdate class ([1b90084](https://github.com/openfoodfacts/openfoodfacts-python/commit/1b9008463200c9a3a598669c4636ff9af9cd137c))

## [1.0.0](https://github.com/openfoodfacts/openfoodfacts-python/compare/v0.4.0...v1.0.0) (2024-07-17)


### ⚠ BREAKING CHANGES

* improve asset and image download functions

### Features

* add helper functions for Redis stream ([6fedef7](https://github.com/openfoodfacts/openfoodfacts-python/commit/6fedef784b569c453d8d1a352195edb787e83eea))
* improve asset and image download functions ([f5b4f90](https://github.com/openfoodfacts/openfoodfacts-python/commit/f5b4f90efb56e2ec775a8e11453818a6d6d8ef75))


### Bug Fixes

* add Pillow as optional dependency (+ extra) ([5ba7719](https://github.com/openfoodfacts/openfoodfacts-python/commit/5ba77194060ef203e739fb30395f89d12ef358bb))

## [0.4.0](https://github.com/openfoodfacts/openfoodfacts-python/compare/v0.3.0...v0.4.0) (2024-07-01)


### Features

* allow fetching other datasets (obf, opff, opf) ([#223](https://github.com/openfoodfacts/openfoodfacts-python/pull/223))
* add download_image function ([#243](https://github.com/openfoodfacts/openfoodfacts-python/issues/243)) ([265f10b](https://github.com/openfoodfacts/openfoodfacts-python/commit/265f10bfa9047c48874255fbc66d9bab32fa61c5))

## [0.3.0](https://github.com/openfoodfacts/openfoodfacts-python/compare/v0.2.1...v0.3.0) (2024-04-18)


### Features

* add get_image_from_url function in utils.py ([db35751](https://github.com/openfoodfacts/openfoodfacts-python/commit/db357510e7f092d5fc3d922465fcaa1c032b324a))
* add Robotoff resource ([953ae41](https://github.com/openfoodfacts/openfoodfacts-python/commit/953ae419d613b874e109217e6764ef63bf2fdb44))
* add run_ocr_on_image_batch function ([decd94d](https://github.com/openfoodfacts/openfoodfacts-python/commit/decd94d8d1830dcef4b4e8c76e840fe753084c4c))


### Bug Fixes

* fix ProductResource.update method ([29c40ad](https://github.com/openfoodfacts/openfoodfacts-python/commit/29c40ad1360f20178bd6b23bce1acf9c99847847))
* fix typing error ([dd51e71](https://github.com/openfoodfacts/openfoodfacts-python/commit/dd51e710e924396f2273dc70c2dbcbcf3c730778))
* make predict_lang compatible with signature ([757cab9](https://github.com/openfoodfacts/openfoodfacts-python/commit/757cab9f104f2b5ff54cd44ad901b68779c4c20a))

## [0.2.1](https://github.com/openfoodfacts/openfoodfacts-python/compare/v0.2.0...v0.2.1) (2024-04-02)


### Bug Fixes

* fix Flavor.opf domain ([acdd9f7](https://github.com/openfoodfacts/openfoodfacts-python/commit/acdd9f709ab8dc9bbd9bfcc71fe25a21b7933497))
* update copyright year ([3c80d59](https://github.com/openfoodfacts/openfoodfacts-python/commit/3c80d5918fa03a66d0618a5a6f50937973ca33aa))

## [0.2.0](https://github.com/openfoodfacts/openfoodfacts-python/compare/v0.1.12...v0.2.0) (2024-03-01)


### Features

* add PEP 561 compliance (typing in installed package) ([#215](https://github.com/openfoodfacts/openfoodfacts-python/issues/215)) ([ca7fc41](https://github.com/openfoodfacts/openfoodfacts-python/commit/ca7fc41ec9b3a7610af28db5683ec6344e3c3022))
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
