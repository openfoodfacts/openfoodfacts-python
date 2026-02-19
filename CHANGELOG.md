# Changelog

## [3.4.4](https://github.com/openfoodfacts/openfoodfacts-python/compare/v3.4.3...v3.4.4) (2026-02-19)


### Bug Fixes

* fix nutrition schema ([#437](https://github.com/openfoodfacts/openfoodfacts-python/issues/437)) ([be2d214](https://github.com/openfoodfacts/openfoodfacts-python/commit/be2d2146e17450c236232950a793e3c43b0cb527))


### Technical

* use src layout to simplify packaging with uv ([#434](https://github.com/openfoodfacts/openfoodfacts-python/issues/434)) ([e9fd435](https://github.com/openfoodfacts/openfoodfacts-python/commit/e9fd435d148f2df09ccca56d0f10eb3939b86c34))

## [3.4.3](https://github.com/openfoodfacts/openfoodfacts-python/compare/v3.4.2...v3.4.3) (2026-02-13)


### Technical

* **deps-dev:** bump cryptography from 43.0.3 to 46.0.5 ([#424](https://github.com/openfoodfacts/openfoodfacts-python/issues/424)) ([c5b4349](https://github.com/openfoodfacts/openfoodfacts-python/commit/c5b43496fea0dec61b499ca1bcd04203527a3238))
* **deps:** bump protobuf from 5.29.5 to 5.29.6 ([#419](https://github.com/openfoodfacts/openfoodfacts-python/issues/419)) ([4e0c58a](https://github.com/openfoodfacts/openfoodfacts-python/commit/4e0c58a7ad9b97e1ee035df308e7c23cbc6af588))
* **deps:** upgrade dependencies ([#426](https://github.com/openfoodfacts/openfoodfacts-python/issues/426)) ([93be8e5](https://github.com/openfoodfacts/openfoodfacts-python/commit/93be8e587d7c1bdecea9cc84d8f6e278c475d5c3))
* improve tooling ([#430](https://github.com/openfoodfacts/openfoodfacts-python/issues/430)) ([c18d93f](https://github.com/openfoodfacts/openfoodfacts-python/commit/c18d93f72a62ecb6367e262d4e99d305ea4016ce))
* move NutritionV3 from robotoff to SDK ([#433](https://github.com/openfoodfacts/openfoodfacts-python/issues/433)) ([0b2bc01](https://github.com/openfoodfacts/openfoodfacts-python/commit/0b2bc01ff4e04bdf29fc22d8aa3b6bdcde0aae5e))
* remove reference to last release sha ([bef76a3](https://github.com/openfoodfacts/openfoodfacts-python/commit/bef76a3a9b113533f92f683ec10a660f20aa185e))
* replace black/isort/flake8 by ruff ([#429](https://github.com/openfoodfacts/openfoodfacts-python/issues/429)) ([3d3c20c](https://github.com/openfoodfacts/openfoodfacts-python/commit/3d3c20c43176cfda3ddff5fdefd0f6d0702da326))
* switch from poetry to uv ([#431](https://github.com/openfoodfacts/openfoodfacts-python/issues/431)) ([dcbd4fc](https://github.com/openfoodfacts/openfoodfacts-python/commit/dcbd4fc1491632460e406ebcc8a4067cfb689575))

## [3.4.2](https://github.com/openfoodfacts/openfoodfacts-python/compare/v3.4.1...v3.4.2) (2026-02-10)


### Bug Fixes

* fix pep8 issues ([059df93](https://github.com/openfoodfacts/openfoodfacts-python/commit/059df9368009da679d9da398e11e98cfc3dbf0f4))
* set-up explicitely licence file ([01147fd](https://github.com/openfoodfacts/openfoodfacts-python/commit/01147fdac2fa430015efa3376e2d9102d0ae47dc))
* update naming convention for APIVersion ([008c700](https://github.com/openfoodfacts/openfoodfacts-python/commit/008c700f5ce484df1995736c393fcb2d8ff97369))


### Technical

* **deps:** upgrade more Python versions ([f8093a7](https://github.com/openfoodfacts/openfoodfacts-python/commit/f8093a704108dd78580f103e6caca62f8595a8f5))
* **deps:** upgrade to new version of release please ([89b3251](https://github.com/openfoodfacts/openfoodfacts-python/commit/89b3251282a7a664fb3e9658010d9514e381d605))
* remove MANIFEST.in ([207d6c5](https://github.com/openfoodfacts/openfoodfacts-python/commit/207d6c5cb77c54617922c637e1c2cc51e1583007))

## [3.4.1](https://github.com/openfoodfacts/openfoodfacts-python/compare/v3.4.0...v3.4.1) (2026-02-10)


### Bug Fixes

* support more API version ([595fcf7](https://github.com/openfoodfacts/openfoodfacts-python/commit/595fcf75529b7073657e5cbaaac5c3854fc43b0d))
* support more API versions ([#420](https://github.com/openfoodfacts/openfoodfacts-python/issues/420)) ([595fcf7](https://github.com/openfoodfacts/openfoodfacts-python/commit/595fcf75529b7073657e5cbaaac5c3854fc43b0d))


### Dependencies

* **chore:** upgrade poetry ([919a366](https://github.com/openfoodfacts/openfoodfacts-python/commit/919a366031df757585f23c95ef97147f26bd38e9))

## [3.4.0](https://github.com/openfoodfacts/openfoodfacts-python/compare/v3.3.0...v3.4.0) (2026-02-04)


### Features

* **Taxonomy:** allow fetching 'stores' ([#406](https://github.com/openfoodfacts/openfoodfacts-python/issues/406)) ([ae27d85](https://github.com/openfoodfacts/openfoodfacts-python/commit/ae27d850136f1e4db5aa1fc459dd4d80adc19eea))


### Bug Fixes

* fix bug in how we apply NMS ([#417](https://github.com/openfoodfacts/openfoodfacts-python/issues/417)) ([26d1361](https://github.com/openfoodfacts/openfoodfacts-python/commit/26d136198d290bfa3a2c692cf273f7e107284054))
* **Taxonomy:** add missing nova_group URL mapping ([#408](https://github.com/openfoodfacts/openfoodfacts-python/issues/408)) ([f05108a](https://github.com/openfoodfacts/openfoodfacts-python/commit/f05108adc14e17e1974caa673b9433fd3ab50927))

## [3.3.0](https://github.com/openfoodfacts/openfoodfacts-python/compare/v3.2.0...v3.3.0) (2025-11-20)


### Features

* improve object detection pre-processing ([#400](https://github.com/openfoodfacts/openfoodfacts-python/issues/400)) ([2c3c58d](https://github.com/openfoodfacts/openfoodfacts-python/commit/2c3c58dc675284a0f31d48d395963f18ab190b33))

## [3.2.0](https://github.com/openfoodfacts/openfoodfacts-python/compare/v3.1.0...v3.2.0) (2025-11-18)


### Features

* add a `warning_missing` parameter to OCRResult.from_url function ([#399](https://github.com/openfoodfacts/openfoodfacts-python/issues/399)) ([9612b06](https://github.com/openfoodfacts/openfoodfacts-python/commit/9612b0655d424d48d804982e692e3db1c2517e40))
* Add data quality taxonomy URL ([#392](https://github.com/openfoodfacts/openfoodfacts-python/issues/392)) ([67e0768](https://github.com/openfoodfacts/openfoodfacts-python/commit/67e0768a1ff3173fb924f8b1f027eb4651916514))


### Bug Fixes

* use a temp filename to save files with `download_file` func ([#398](https://github.com/openfoodfacts/openfoodfacts-python/issues/398)) ([6f1eba5](https://github.com/openfoodfacts/openfoodfacts-python/commit/6f1eba57de0bfcc96b4e9c02bc3a1aad333fd7fe))

## [3.1.0](https://github.com/openfoodfacts/openfoodfacts-python/compare/v3.0.0...v3.1.0) (2025-09-25)


### Features

* implement POST /api/v3/product/{barcode}/images route ([#389](https://github.com/openfoodfacts/openfoodfacts-python/issues/389)) ([73704cf](https://github.com/openfoodfacts/openfoodfacts-python/commit/73704cf4e348813780af2125cefb2936fb55fce5))

## [3.0.0](https://github.com/openfoodfacts/openfoodfacts-python/compare/v2.9.0...v3.0.0) (2025-09-11)


### ⚠ BREAKING CHANGES

* **redis:** support `ocr_ready` event type ([#386](https://github.com/openfoodfacts/openfoodfacts-python/issues/386))

### Features

* **redis:** support `ocr_ready` event type ([#386](https://github.com/openfoodfacts/openfoodfacts-python/issues/386)) ([e4e598a](https://github.com/openfoodfacts/openfoodfacts-python/commit/e4e598aa9cb2b2bc48a7173122e7147deeb4e0fb))


### Bug Fixes

* allow to specify the page in FacetResource.get ([#381](https://github.com/openfoodfacts/openfoodfacts-python/issues/381)) ([11aa647](https://github.com/openfoodfacts/openfoodfacts-python/commit/11aa64732a35c05904e46b51ab3d778f42299f00)), closes [#292](https://github.com/openfoodfacts/openfoodfacts-python/issues/292)


### Documentation

* Add a REUSE.md for the Python SDK ([#385](https://github.com/openfoodfacts/openfoodfacts-python/issues/385)) ([72af8dd](https://github.com/openfoodfacts/openfoodfacts-python/commit/72af8ddf30bad656f902d8a384cf5b590514eeb0))

## [2.9.0](https://github.com/openfoodfacts/openfoodfacts-python/compare/v2.8.0...v2.9.0) (2025-08-21)


### Features

* improve facet functions ([#377](https://github.com/openfoodfacts/openfoodfacts-python/issues/377)) ([1084e05](https://github.com/openfoodfacts/openfoodfacts-python/commit/1084e05aa91450be6c0e82e4fc3e909d3f2f4091))


### Bug Fixes

* strip leading 0 before splitting barcodes ([#378](https://github.com/openfoodfacts/openfoodfacts-python/issues/378)) ([1247212](https://github.com/openfoodfacts/openfoodfacts-python/commit/12472127b8db41beba1d204d1224378b93e013cb))

## [2.8.0](https://github.com/openfoodfacts/openfoodfacts-python/compare/v2.7.0...v2.8.0) (2025-07-08)


### Features

* add new is_image_deletion method to RedisUpdate ([#359](https://github.com/openfoodfacts/openfoodfacts-python/issues/359)) ([9e3951c](https://github.com/openfoodfacts/openfoodfacts-python/commit/9e3951c392dfde4761b7cb99ffe2131ba4641738))


### Bug Fixes

* fix release please config ([fc77c07](https://github.com/openfoodfacts/openfoodfacts-python/commit/fc77c07a3509f56a3c9cbe617b5beeca8e050263))

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
