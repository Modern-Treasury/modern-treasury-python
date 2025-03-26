# Changelog

## 1.46.0 (2025-03-26)

Full Changelog: [v1.45.0...v1.46.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.45.0...v1.46.0)

### Features

* **client:** allow passing `NotGiven` for body ([#606](https://github.com/Modern-Treasury/modern-treasury-python/issues/606)) ([5e2c828](https://github.com/Modern-Treasury/modern-treasury-python/commit/5e2c828f1e4b653c0b00a5be4fd6c5bbd037bcee))


### Bug Fixes

* **ci:** ensure pip is always available ([#617](https://github.com/Modern-Treasury/modern-treasury-python/issues/617)) ([794bcb1](https://github.com/Modern-Treasury/modern-treasury-python/commit/794bcb1f0b03ae902ea78c38c5ad57664f233b35))
* **ci:** remove publishing patch ([#618](https://github.com/Modern-Treasury/modern-treasury-python/issues/618)) ([999f1af](https://github.com/Modern-Treasury/modern-treasury-python/commit/999f1af2b5438da6a5f05fdf63187e5f2ffec230))
* **client:** mark some request bodies as optional ([5e2c828](https://github.com/Modern-Treasury/modern-treasury-python/commit/5e2c828f1e4b653c0b00a5be4fd6c5bbd037bcee))
* **types:** handle more discriminated union shapes ([#616](https://github.com/Modern-Treasury/modern-treasury-python/issues/616)) ([9a47fa6](https://github.com/Modern-Treasury/modern-treasury-python/commit/9a47fa6322e4a56e215bbf406586813ca6f89e65))


### Chores

* add hash of OpenAPI spec/config inputs to .stats.yml ([#620](https://github.com/Modern-Treasury/modern-treasury-python/issues/620)) ([f902110](https://github.com/Modern-Treasury/modern-treasury-python/commit/f902110bed961118fcf13361864287b301e78996))
* **docs:** update client docstring ([#611](https://github.com/Modern-Treasury/modern-treasury-python/issues/611)) ([fa883e4](https://github.com/Modern-Treasury/modern-treasury-python/commit/fa883e4b24914befec18f97381c45d084f469a9b))
* fix typos ([#619](https://github.com/Modern-Treasury/modern-treasury-python/issues/619)) ([67d863d](https://github.com/Modern-Treasury/modern-treasury-python/commit/67d863d25ccda298199063d9400f37b0e0ff6b74))
* **internal:** bump rye to 0.44.0 ([#615](https://github.com/Modern-Treasury/modern-treasury-python/issues/615)) ([28bf2de](https://github.com/Modern-Treasury/modern-treasury-python/commit/28bf2dee8a88aec5c2c95f13ccaa1696140de3b1))
* **internal:** fix devcontainers setup ([#608](https://github.com/Modern-Treasury/modern-treasury-python/issues/608)) ([fcfdac5](https://github.com/Modern-Treasury/modern-treasury-python/commit/fcfdac51584dc4cd8ab4e6240a94d9ff59b56163))
* **internal:** properly set __pydantic_private__ ([#609](https://github.com/Modern-Treasury/modern-treasury-python/issues/609)) ([b86b6a0](https://github.com/Modern-Treasury/modern-treasury-python/commit/b86b6a03f7c0a4777b1cb2bc085d58ec0e7a70af))
* **internal:** remove extra empty newlines ([#614](https://github.com/Modern-Treasury/modern-treasury-python/issues/614)) ([52ce5d4](https://github.com/Modern-Treasury/modern-treasury-python/commit/52ce5d4f7600726bc5ce0b2d6f15e471730eb551))
* **internal:** remove unused http client options forwarding ([#612](https://github.com/Modern-Treasury/modern-treasury-python/issues/612)) ([3e72f74](https://github.com/Modern-Treasury/modern-treasury-python/commit/3e72f74d040cc233fd95fd342200f6c4ba22b232))


### Documentation

* update URLs from stainlessapi.com to stainless.com ([#610](https://github.com/Modern-Treasury/modern-treasury-python/issues/610)) ([5e01402](https://github.com/Modern-Treasury/modern-treasury-python/commit/5e0140295bdbc8045d104fcc121a54f1180ba153))

## 1.45.0 (2025-02-13)

Full Changelog: [v1.44.3...v1.45.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.44.3...v1.45.0)

### Features

* **client:** send `X-Stainless-Read-Timeout` header ([#602](https://github.com/Modern-Treasury/modern-treasury-python/issues/602)) ([065e191](https://github.com/Modern-Treasury/modern-treasury-python/commit/065e191656e204835606e23caef5e7771fd8ae53))


### Bug Fixes

* asyncify on non-asyncio runtimes ([#605](https://github.com/Modern-Treasury/modern-treasury-python/issues/605)) ([424ed0b](https://github.com/Modern-Treasury/modern-treasury-python/commit/424ed0b7f8585a7e79425a626d91264cfe9a75f9))


### Chores

* **internal:** bummp ruff dependency ([#601](https://github.com/Modern-Treasury/modern-treasury-python/issues/601)) ([0e2f4f3](https://github.com/Modern-Treasury/modern-treasury-python/commit/0e2f4f31538c58c74854ce5528a580d7d1bbce95))
* **internal:** change default timeout to an int ([#600](https://github.com/Modern-Treasury/modern-treasury-python/issues/600)) ([991c163](https://github.com/Modern-Treasury/modern-treasury-python/commit/991c163764bb7b546457e8e8ab8a6b1368db18aa))
* **internal:** fix type traversing dictionary params ([#603](https://github.com/Modern-Treasury/modern-treasury-python/issues/603)) ([2ea3f16](https://github.com/Modern-Treasury/modern-treasury-python/commit/2ea3f1693e00537f9b2c7d60930b3c92754a17b5))
* **internal:** minor formatting changes ([#598](https://github.com/Modern-Treasury/modern-treasury-python/issues/598)) ([0ce7295](https://github.com/Modern-Treasury/modern-treasury-python/commit/0ce7295ecbea3c7146699c200ac21e010b73786c))
* **internal:** minor type handling changes ([#604](https://github.com/Modern-Treasury/modern-treasury-python/issues/604)) ([cfd8109](https://github.com/Modern-Treasury/modern-treasury-python/commit/cfd8109e23e0393c4695e95101cba7a1cf92ca1d))

## 1.44.3 (2025-01-22)

Full Changelog: [v1.44.2...v1.44.3](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.44.2...v1.44.3)

### Bug Fixes

* **tests:** make test_get_platform less flaky ([#594](https://github.com/Modern-Treasury/modern-treasury-python/issues/594)) ([6bb3f77](https://github.com/Modern-Treasury/modern-treasury-python/commit/6bb3f7706b3e0735e09270b34d56443367679fe8))


### Chores

* **api:** adds new APIs for LedgerAccountSettlement LedgerEntries ([#597](https://github.com/Modern-Treasury/modern-treasury-python/issues/597)) ([61fa0db](https://github.com/Modern-Treasury/modern-treasury-python/commit/61fa0db2bd74765627697a030ef32bf0c31596c0))
* **internal:** avoid pytest-asyncio deprecation warning ([#595](https://github.com/Modern-Treasury/modern-treasury-python/issues/595)) ([319682d](https://github.com/Modern-Treasury/modern-treasury-python/commit/319682d3dc7f9eec142eccfeeb54b2a3553289e3))
* **internal:** bump pyright dependency ([#590](https://github.com/Modern-Treasury/modern-treasury-python/issues/590)) ([2303a04](https://github.com/Modern-Treasury/modern-treasury-python/commit/2303a04e8dcbe0ea0da22c1cdfe4b01a47f7479f))
* **internal:** minor style changes ([#596](https://github.com/Modern-Treasury/modern-treasury-python/issues/596)) ([b038560](https://github.com/Modern-Treasury/modern-treasury-python/commit/b0385607831db9c4860e2cf9d85a6db46ff3f35e))


### Documentation

* **raw responses:** fix duplicate `the` ([#593](https://github.com/Modern-Treasury/modern-treasury-python/issues/593)) ([b8e6ce9](https://github.com/Modern-Treasury/modern-treasury-python/commit/b8e6ce97e7cff97bdd26c6b059aa7773c5d60cad))


### Refactors

* quote more recursive references ([#592](https://github.com/Modern-Treasury/modern-treasury-python/issues/592)) ([0998f81](https://github.com/Modern-Treasury/modern-treasury-python/commit/0998f81a030170747a5a31f4e4f50747a488a446))

## 1.44.2 (2025-01-14)

Full Changelog: [v1.44.1...v1.44.2](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.44.1...v1.44.2)

### Bug Fixes

* **client:** only call .close() when needed ([#583](https://github.com/Modern-Treasury/modern-treasury-python/issues/583)) ([afaf8e9](https://github.com/Modern-Treasury/modern-treasury-python/commit/afaf8e9ad149cab8ed388e35a0a08c440a301a5a))
* correctly handle deserialising `cls` fields ([#587](https://github.com/Modern-Treasury/modern-treasury-python/issues/587)) ([1e0440f](https://github.com/Modern-Treasury/modern-treasury-python/commit/1e0440f869800e2f4588474c63a60b01b02e6409))


### Chores

* add missing isclass check ([#581](https://github.com/Modern-Treasury/modern-treasury-python/issues/581)) ([21691a3](https://github.com/Modern-Treasury/modern-treasury-python/commit/21691a39a12c1d0265db01ae25961c047afd9758))
* bump license year ([#578](https://github.com/Modern-Treasury/modern-treasury-python/issues/578)) ([c98915c](https://github.com/Modern-Treasury/modern-treasury-python/commit/c98915ced18e5b08f182e82e0a7a4e8fc75bea96))
* fix cyclical imports ([#588](https://github.com/Modern-Treasury/modern-treasury-python/issues/588)) ([d2473b2](https://github.com/Modern-Treasury/modern-treasury-python/commit/d2473b2895233e4968944faa3804453ece846506))
* **internal:** bump httpx dependency ([#582](https://github.com/Modern-Treasury/modern-treasury-python/issues/582)) ([379345e](https://github.com/Modern-Treasury/modern-treasury-python/commit/379345ead4073d57f8cca0fd32b15c404bdf2fa9))
* **internal:** update deps ([#589](https://github.com/Modern-Treasury/modern-treasury-python/issues/589)) ([4e2f499](https://github.com/Modern-Treasury/modern-treasury-python/commit/4e2f4998ebf133f8d56fd4693763703e00871d4b))
* small refactors ([#580](https://github.com/Modern-Treasury/modern-treasury-python/issues/580)) ([03a8166](https://github.com/Modern-Treasury/modern-treasury-python/commit/03a816615a1fee7e41b9c57e5d5eb0647a804cf5))


### Documentation

* fix typos ([#584](https://github.com/Modern-Treasury/modern-treasury-python/issues/584)) ([618e1ce](https://github.com/Modern-Treasury/modern-treasury-python/commit/618e1ce71e18a97aa518cc3656afea032b059255))
* more typo fixes ([#585](https://github.com/Modern-Treasury/modern-treasury-python/issues/585)) ([2c0734a](https://github.com/Modern-Treasury/modern-treasury-python/commit/2c0734aead00030dfd44112fe87423443a05b0d2))
* **readme:** fix misplaced period ([#586](https://github.com/Modern-Treasury/modern-treasury-python/issues/586)) ([4f8fb4d](https://github.com/Modern-Treasury/modern-treasury-python/commit/4f8fb4dbd8eb2a2b49c9e3756469d9d14a768dbd))

## 1.44.1 (2024-12-17)

Full Changelog: [v1.44.0...v1.44.1](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.44.0...v1.44.1)

### Chores

* **internal:** fix some typos ([#577](https://github.com/Modern-Treasury/modern-treasury-python/issues/577)) ([98eafda](https://github.com/Modern-Treasury/modern-treasury-python/commit/98eafdaee2d1a82a4179dced104bd91ebffc0bb6))
* **internal:** updated imports ([#573](https://github.com/Modern-Treasury/modern-treasury-python/issues/573)) ([d2600bf](https://github.com/Modern-Treasury/modern-treasury-python/commit/d2600bfc336d87a87c7e28f2794013ff7ddf80b5))


### Documentation

* **readme:** example snippet for client context manager ([#576](https://github.com/Modern-Treasury/modern-treasury-python/issues/576)) ([7c67e59](https://github.com/Modern-Treasury/modern-treasury-python/commit/7c67e59d0de855dcbd2dcc9998b585f71ef40302))

## 1.44.0 (2024-12-12)

Full Changelog: [v1.43.1...v1.44.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.43.1...v1.44.0)

### Chores

* **internal:** add support for TypeAliasType ([#572](https://github.com/Modern-Treasury/modern-treasury-python/issues/572)) ([5996dd2](https://github.com/Modern-Treasury/modern-treasury-python/commit/5996dd28174cad52dffae85465204f48b7194f8b))
* **internal:** bump pydantic dependency ([#567](https://github.com/Modern-Treasury/modern-treasury-python/issues/567)) ([ce22c80](https://github.com/Modern-Treasury/modern-treasury-python/commit/ce22c80cac2dce0e56cb937171e69cf8d325f1ab))
* **internal:** bump pyright ([#564](https://github.com/Modern-Treasury/modern-treasury-python/issues/564)) ([9425115](https://github.com/Modern-Treasury/modern-treasury-python/commit/9425115117bd609df8efe1bdcabc12d50d6b9e48))
* **internal:** bump pyright ([#571](https://github.com/Modern-Treasury/modern-treasury-python/issues/571)) ([ceb5b53](https://github.com/Modern-Treasury/modern-treasury-python/commit/ceb5b5340a9ef0d68586e0b0ff3c362b873c3a3a))
* make the `Omit` type public ([#566](https://github.com/Modern-Treasury/modern-treasury-python/issues/566)) ([e0efee5](https://github.com/Modern-Treasury/modern-treasury-python/commit/e0efee572e4d2a56c300577748e1381ebca3b60f))
* remove deprecated HTTP client options ([#568](https://github.com/Modern-Treasury/modern-treasury-python/issues/568)) ([5a50ac5](https://github.com/Modern-Treasury/modern-treasury-python/commit/5a50ac5b26e9844ca715359dfb203447d1dccf32))


### Documentation

* **readme:** fix http client proxies example ([#569](https://github.com/Modern-Treasury/modern-treasury-python/issues/569)) ([ec4df6a](https://github.com/Modern-Treasury/modern-treasury-python/commit/ec4df6aefa379ae45479d4da898d39eb16d3e965))

## 1.43.1 (2024-11-28)

Full Changelog: [v1.43.0...v1.43.1](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.43.0...v1.43.1)

### Bug Fixes

* **asyncify:** avoid hanging process under certain conditions ([#556](https://github.com/Modern-Treasury/modern-treasury-python/issues/556)) ([d64a12f](https://github.com/Modern-Treasury/modern-treasury-python/commit/d64a12fd009154f0180d4154c0b6920545ffdfc2))
* **client:** compat with new httpx 0.28.0 release ([#563](https://github.com/Modern-Treasury/modern-treasury-python/issues/563)) ([f70ecc8](https://github.com/Modern-Treasury/modern-treasury-python/commit/f70ecc84770dbaf4aa6b652b3fdf5c361df2082a))


### Chores

* **api:** additional fields for requests to get BalanceReports and create LegalEntities ([#557](https://github.com/Modern-Treasury/modern-treasury-python/issues/557)) ([e6eb038](https://github.com/Modern-Treasury/modern-treasury-python/commit/e6eb038c22ed677336cf95f593f06e62cf108c85))
* **internal:** exclude mypy from running on tests ([#562](https://github.com/Modern-Treasury/modern-treasury-python/issues/562)) ([308156f](https://github.com/Modern-Treasury/modern-treasury-python/commit/308156fc3af7463fb4976244397560f6db0f2ef8))
* **internal:** fix compat model_dump method when warnings are passed ([#558](https://github.com/Modern-Treasury/modern-treasury-python/issues/558)) ([148371f](https://github.com/Modern-Treasury/modern-treasury-python/commit/148371f5bc2b00b8438062643266c73bc7104240))
* remove now unused `cached-property` dep ([#560](https://github.com/Modern-Treasury/modern-treasury-python/issues/560)) ([913649b](https://github.com/Modern-Treasury/modern-treasury-python/commit/913649bb0f36732d5c4d1058d1de6b9e745a59e6))
* sync openapi spec ([#561](https://github.com/Modern-Treasury/modern-treasury-python/issues/561)) ([4753fa9](https://github.com/Modern-Treasury/modern-treasury-python/commit/4753fa909b756c7df43dc28179f682d98ac75f04))
* **tests:** limit array example length ([#554](https://github.com/Modern-Treasury/modern-treasury-python/issues/554)) ([2da7d34](https://github.com/Modern-Treasury/modern-treasury-python/commit/2da7d34dc508a2f36eee7a93c22254353fefb695))


### Documentation

* add info log level to readme ([#559](https://github.com/Modern-Treasury/modern-treasury-python/issues/559)) ([2e92ffd](https://github.com/Modern-Treasury/modern-treasury-python/commit/2e92ffd1bf10ac2b4a0aa7fe398faf7d9101cb46))

## 1.43.0 (2024-11-12)

Full Changelog: [v1.42.0...v1.43.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.42.0...v1.43.0)

### Features

* **project:** drop support for Python 3.7 ([#549](https://github.com/Modern-Treasury/modern-treasury-python/issues/549)) ([0f5bcc4](https://github.com/Modern-Treasury/modern-treasury-python/commit/0f5bcc49e99575ad3fb93515893dca2f84e00794))


### Bug Fixes

* don't use dicts as iterables in transform ([#547](https://github.com/Modern-Treasury/modern-treasury-python/issues/547)) ([42b1816](https://github.com/Modern-Treasury/modern-treasury-python/commit/42b1816a2ea7be3da1f26840d7fd306c130252f8))
* don't use dicts as iterables in transform ([#553](https://github.com/Modern-Treasury/modern-treasury-python/issues/553)) ([c23d201](https://github.com/Modern-Treasury/modern-treasury-python/commit/c23d201ba62cc5dfe9cb68132aab4eb1ecc1e4bb))
* support json safe serialization for basemodel subclasses ([#548](https://github.com/Modern-Treasury/modern-treasury-python/issues/548)) ([4a1905a](https://github.com/Modern-Treasury/modern-treasury-python/commit/4a1905a0896be876f316824255df8199184e32db))


### Chores

* **internal:** bump mypy ([#546](https://github.com/Modern-Treasury/modern-treasury-python/issues/546)) ([5bd9a84](https://github.com/Modern-Treasury/modern-treasury-python/commit/5bd9a84c360a6914f2874eb78fb548b9a3167324))
* **internal:** bump pytest to v8 & pydantic ([#544](https://github.com/Modern-Treasury/modern-treasury-python/issues/544)) ([2f4f9f3](https://github.com/Modern-Treasury/modern-treasury-python/commit/2f4f9f32ad0052e13cc8e0e3aca6c8de099b1966))
* **internal:** cleanup redundant cyclical import ([#551](https://github.com/Modern-Treasury/modern-treasury-python/issues/551)) ([212d322](https://github.com/Modern-Treasury/modern-treasury-python/commit/212d322d7dc9f318ec9b2290e1bc340867da848c))
* **tests:** adjust retry timeout values ([#550](https://github.com/Modern-Treasury/modern-treasury-python/issues/550)) ([dc1258e](https://github.com/Modern-Treasury/modern-treasury-python/commit/dc1258e01af33cd960eacaa8f5db7634723e387f))


### Documentation

* move comments in example snippets ([#552](https://github.com/Modern-Treasury/modern-treasury-python/issues/552)) ([b751366](https://github.com/Modern-Treasury/modern-treasury-python/commit/b751366255b55f2ae426d7d780396d42236b6e7f))

## 1.42.0 (2024-10-21)

Full Changelog: [v1.41.1...v1.42.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.41.1...v1.42.0)

### Features

* **api:** updates to required fields for ExpectedPayments ([#538](https://github.com/Modern-Treasury/modern-treasury-python/issues/538)) ([883df1a](https://github.com/Modern-Treasury/modern-treasury-python/commit/883df1a347923fe3425025f06c9c6bb11b54f0e8))


### Bug Fixes

* **client/async:** correctly retry in all cases ([#542](https://github.com/Modern-Treasury/modern-treasury-python/issues/542)) ([59612c4](https://github.com/Modern-Treasury/modern-treasury-python/commit/59612c41ca12c4ef8cb2a75fe9a6e5437d7cfcf3))


### Chores

* **internal:** bump ruff dependency ([#541](https://github.com/Modern-Treasury/modern-treasury-python/issues/541)) ([75fcd9a](https://github.com/Modern-Treasury/modern-treasury-python/commit/75fcd9acd5ab11f06671c6163103568875e753e7))
* **internal:** remove unused black config ([#543](https://github.com/Modern-Treasury/modern-treasury-python/issues/543)) ([a7b01a4](https://github.com/Modern-Treasury/modern-treasury-python/commit/a7b01a479f8ac8546460048281c716ec7cb9ede7))
* **internal:** update test syntax ([#540](https://github.com/Modern-Treasury/modern-treasury-python/issues/540)) ([9801e21](https://github.com/Modern-Treasury/modern-treasury-python/commit/9801e2114323e964ef357dac55a32b2d96ab9062))

## 1.41.1 (2024-10-07)

Full Changelog: [v1.41.0...v1.41.1](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.41.0...v1.41.1)

### Bug Fixes

* **client:** avoid OverflowError with very large retry counts ([#536](https://github.com/Modern-Treasury/modern-treasury-python/issues/536)) ([692bec5](https://github.com/Modern-Treasury/modern-treasury-python/commit/692bec55de1f314b13a93ebdcbc587c89103cad0))


### Chores

* add repr to PageInfo class ([#537](https://github.com/Modern-Treasury/modern-treasury-python/issues/537)) ([175fd3b](https://github.com/Modern-Treasury/modern-treasury-python/commit/175fd3bb8e69163bdc1ef6917d7611ad1e7609d3))
* **internal:** add support for parsing bool response content ([#535](https://github.com/Modern-Treasury/modern-treasury-python/issues/535)) ([c20fe34](https://github.com/Modern-Treasury/modern-treasury-python/commit/c20fe3435adf41ba9cc3ddc2aaa44b0a94f690ac))


### Documentation

* fix typo in fenced code block language ([#534](https://github.com/Modern-Treasury/modern-treasury-python/issues/534)) ([23d51a7](https://github.com/Modern-Treasury/modern-treasury-python/commit/23d51a72f010177a69231cc8feebbdac67626aa8))
* improve and reference contributing documentation ([#532](https://github.com/Modern-Treasury/modern-treasury-python/issues/532)) ([e991a66](https://github.com/Modern-Treasury/modern-treasury-python/commit/e991a66e853311397f1a877c90ae17ef0b7f10ca))

## 1.41.0 (2024-09-25)

Full Changelog: [v1.40.0...v1.41.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.40.0...v1.41.0)

### Features

* **api:** add `usbank_payment_application_reference_id` to `reference_number_type` ([#522](https://github.com/Modern-Treasury/modern-treasury-python/issues/522)) ([8544c6e](https://github.com/Modern-Treasury/modern-treasury-python/commit/8544c6e38e2daa025e642e890967e04712f2a3ff))
* **client:** allow overriding retry count header ([#531](https://github.com/Modern-Treasury/modern-treasury-python/issues/531)) ([b084527](https://github.com/Modern-Treasury/modern-treasury-python/commit/b084527d83ba13d404c0e6684e502fbc2ace00fb))
* **client:** send retry count header ([#528](https://github.com/Modern-Treasury/modern-treasury-python/issues/528)) ([5a85f89](https://github.com/Modern-Treasury/modern-treasury-python/commit/5a85f8960f530f7ad0cc7bb2af23ad538ee8a8cd))


### Bug Fixes

* **client:** handle domains with underscores ([#527](https://github.com/Modern-Treasury/modern-treasury-python/issues/527)) ([b19a0e8](https://github.com/Modern-Treasury/modern-treasury-python/commit/b19a0e8edd7946cd9e13a3b08d21eeb4fefdefea))


### Chores

* **api:** fields and parameters added to bulk actions, transactions and invoice creation ([#530](https://github.com/Modern-Treasury/modern-treasury-python/issues/530)) ([5221bfa](https://github.com/Modern-Treasury/modern-treasury-python/commit/5221bfa385fdf21c246509df64c3ae9ced50e8c6))
* **internal:** bump pyright / mypy version ([#526](https://github.com/Modern-Treasury/modern-treasury-python/issues/526)) ([7aa949b](https://github.com/Modern-Treasury/modern-treasury-python/commit/7aa949b62976095a0157431b7d9750e6b608d455))
* **internal:** bump ruff ([#525](https://github.com/Modern-Treasury/modern-treasury-python/issues/525)) ([0816f05](https://github.com/Modern-Treasury/modern-treasury-python/commit/0816f0516839b542c31b9938b30aa7e9affa4592))
* **internal:** update pydantic v1 compat helpers ([#529](https://github.com/Modern-Treasury/modern-treasury-python/issues/529)) ([1f9d3ae](https://github.com/Modern-Treasury/modern-treasury-python/commit/1f9d3aead62ea195e3d7f39a3dea3963428d71c7))


### Documentation

* update CONTRIBUTING.md ([#524](https://github.com/Modern-Treasury/modern-treasury-python/issues/524)) ([dfcbfa4](https://github.com/Modern-Treasury/modern-treasury-python/commit/dfcbfa4289958d7e9c8d28342bbb32434b828cf4))

## 1.40.0 (2024-09-09)

Full Changelog: [v1.39.0...v1.40.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.39.0...v1.40.0)

### Features

* **api:** add us_bank RTP ID's as reference_number_type ([#518](https://github.com/Modern-Treasury/modern-treasury-python/issues/518)) ([751a5fa](https://github.com/Modern-Treasury/modern-treasury-python/commit/751a5fa764bc85b1ebdc7dd3895bd6d993ba78b1))


### Chores

* add docstrings to raw response properties ([#519](https://github.com/Modern-Treasury/modern-treasury-python/issues/519)) ([d0f8b63](https://github.com/Modern-Treasury/modern-treasury-python/commit/d0f8b6335fdf9a5ec16d3c239d17b69b841c1fbf))
* **docs:** update description of `bankgirot` to `se_bankgirot` ([#521](https://github.com/Modern-Treasury/modern-treasury-python/issues/521)) ([8ce5255](https://github.com/Modern-Treasury/modern-treasury-python/commit/8ce52554524f1cd4f2e44edfaedddee13c84bb5b))
* pyproject.toml formatting changes ([#515](https://github.com/Modern-Treasury/modern-treasury-python/issues/515)) ([7b4ca37](https://github.com/Modern-Treasury/modern-treasury-python/commit/7b4ca373abed17c2d28e7a062d32f34e9d39d6b9))
* **test:** change test name ([#517](https://github.com/Modern-Treasury/modern-treasury-python/issues/517)) ([7ccc82b](https://github.com/Modern-Treasury/modern-treasury-python/commit/7ccc82b7ea65457fdeeddd1f9d978452be8218e8))


### Documentation

* **readme:** add section on determining installed version ([#520](https://github.com/Modern-Treasury/modern-treasury-python/issues/520)) ([b146e00](https://github.com/Modern-Treasury/modern-treasury-python/commit/b146e003bcb03b2a34934e07ae23319288fe1514))

## 1.39.0 (2024-08-20)

Full Changelog: [v1.38.0...v1.39.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.38.0...v1.39.0)

### Features

* **api:** add wells fargo reference number types ([#514](https://github.com/Modern-Treasury/modern-treasury-python/issues/514)) ([5789d00](https://github.com/Modern-Treasury/modern-treasury-python/commit/5789d008196c2a69f07517a5b5686b49c1081252))


### Chores

* **ci:** also run pydantic v1 tests ([#513](https://github.com/Modern-Treasury/modern-treasury-python/issues/513)) ([4ef2953](https://github.com/Modern-Treasury/modern-treasury-python/commit/4ef2953695e0676adc39971433dd7f68253d60c6))
* **client:** fix parsing union responses when non-json is returned ([#512](https://github.com/Modern-Treasury/modern-treasury-python/issues/512)) ([4981f38](https://github.com/Modern-Treasury/modern-treasury-python/commit/4981f383909156af097baf6384f52457691119c7))
* **internal:** use different 32bit detection method ([#510](https://github.com/Modern-Treasury/modern-treasury-python/issues/510)) ([8becaf4](https://github.com/Modern-Treasury/modern-treasury-python/commit/8becaf4a50782394e8be83bcee83c367061f7aff))

## 1.38.0 (2024-08-13)

Full Changelog: [v1.37.0...v1.38.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.37.0...v1.38.0)

### Features

* **api:** add pagination params 'created at' and 'updated at' ([#498](https://github.com/Modern-Treasury/modern-treasury-python/issues/498)) ([049b023](https://github.com/Modern-Treasury/modern-treasury-python/commit/049b0239140f8a8b4f475b033d5345896e5da7cc))
* **api:** updates ([#509](https://github.com/Modern-Treasury/modern-treasury-python/issues/509)) ([8bd91e1](https://github.com/Modern-Treasury/modern-treasury-python/commit/8bd91e10afe7d35cc93009aed78227f83e09ddfd))
* **client:** add `retries_taken` to raw response class ([#501](https://github.com/Modern-Treasury/modern-treasury-python/issues/501)) ([d34ae60](https://github.com/Modern-Treasury/modern-treasury-python/commit/d34ae608cc6ef1640f67a1fd1354ea0079bb6152))


### Chores

* **ci:** bump prism mock server version ([#506](https://github.com/Modern-Treasury/modern-treasury-python/issues/506)) ([336af40](https://github.com/Modern-Treasury/modern-treasury-python/commit/336af400e5062db05c279ae2678163a651bc935d))
* **ci:** limit release doctor target branches ([#493](https://github.com/Modern-Treasury/modern-treasury-python/issues/493)) ([80695d6](https://github.com/Modern-Treasury/modern-treasury-python/commit/80695d6f40a9ba1376a550e79430340751138b57))
* **docs:** document how to do per-request http client customization ([#492](https://github.com/Modern-Treasury/modern-treasury-python/issues/492)) ([8f53e57](https://github.com/Modern-Treasury/modern-treasury-python/commit/8f53e57ecb54eda4effd8b9b8228b3ec0bf57b98))
* **examples:** minor formatting changes ([#508](https://github.com/Modern-Treasury/modern-treasury-python/issues/508)) ([9a61853](https://github.com/Modern-Treasury/modern-treasury-python/commit/9a6185303f834fcc9422be0269eb47bf9da80da8))
* fix error message import example ([#496](https://github.com/Modern-Treasury/modern-treasury-python/issues/496)) ([1823f4f](https://github.com/Modern-Treasury/modern-treasury-python/commit/1823f4f4df8a7cbfe764c64d4e4b2de56805ab65))
* **internal:** add type construction helper ([#497](https://github.com/Modern-Treasury/modern-treasury-python/issues/497)) ([7c83312](https://github.com/Modern-Treasury/modern-treasury-python/commit/7c833121944592e2f73f80f299407a5681a2ff23))
* **internal:** bump pyright ([#500](https://github.com/Modern-Treasury/modern-treasury-python/issues/500)) ([3833a6f](https://github.com/Modern-Treasury/modern-treasury-python/commit/3833a6ff5423f8464fc29b717198db0129b50f0b))
* **internal:** bump ruff version ([#503](https://github.com/Modern-Treasury/modern-treasury-python/issues/503)) ([7ed0f1a](https://github.com/Modern-Treasury/modern-treasury-python/commit/7ed0f1aa7798b74f0edffe2e7503308f93df1290))
* **internal:** ensure package is importable in lint cmd ([#507](https://github.com/Modern-Treasury/modern-treasury-python/issues/507)) ([87614ea](https://github.com/Modern-Treasury/modern-treasury-python/commit/87614ea8e18cdfd80593dd8565121dd9023c76c2))
* **internal:** test updates ([#502](https://github.com/Modern-Treasury/modern-treasury-python/issues/502)) ([0be7d00](https://github.com/Modern-Treasury/modern-treasury-python/commit/0be7d00365a503ce955104b2e27677864fadaec0))
* **internal:** update formatting ([#490](https://github.com/Modern-Treasury/modern-treasury-python/issues/490)) ([7fb8bcb](https://github.com/Modern-Treasury/modern-treasury-python/commit/7fb8bcbb19ec6285eff4af565922d4f6a0e8cb4c))
* **internal:** update pydantic compat helper function ([#504](https://github.com/Modern-Treasury/modern-treasury-python/issues/504)) ([dfd567f](https://github.com/Modern-Treasury/modern-treasury-python/commit/dfd567f39c885a0ed7f8161e9a0e299fb4ee5c58))
* **internal:** updates ([#505](https://github.com/Modern-Treasury/modern-treasury-python/issues/505)) ([0335ce3](https://github.com/Modern-Treasury/modern-treasury-python/commit/0335ce3180aa6607f0a20345d5ad2828a340be1a))
* **internal:** use `TypeAlias` marker for type assignments ([#499](https://github.com/Modern-Treasury/modern-treasury-python/issues/499)) ([c4b61c9](https://github.com/Modern-Treasury/modern-treasury-python/commit/c4b61c9995261e3faf2536038c8a9b64e17ba164))
* **tests:** update prism version ([#495](https://github.com/Modern-Treasury/modern-treasury-python/issues/495)) ([1855ddc](https://github.com/Modern-Treasury/modern-treasury-python/commit/1855ddcf03505e1346ec9392e1bc24863651ba34))


### Documentation

* **readme:** fix example snippet imports ([#494](https://github.com/Modern-Treasury/modern-treasury-python/issues/494)) ([bcdb312](https://github.com/Modern-Treasury/modern-treasury-python/commit/bcdb312f5f125122a3d01b496529a7a8f55f3c10))

## 1.37.0 (2024-07-16)

Full Changelog: [v1.36.0...v1.37.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.36.0...v1.37.0)

### Features

* **api:** updates ([#487](https://github.com/Modern-Treasury/modern-treasury-python/issues/487)) ([2d456bc](https://github.com/Modern-Treasury/modern-treasury-python/commit/2d456bc0eb242ad4b80488e8f728d6f0c9a44ffa))


### Bug Fixes

* **client:** always respect content-type multipart/form-data if provided ([#478](https://github.com/Modern-Treasury/modern-treasury-python/issues/478)) ([f6b7b9e](https://github.com/Modern-Treasury/modern-treasury-python/commit/f6b7b9efc341e07e01102b1e63f175700c47b506))


### Chores

* **ci:** also run workflows for PRs targeting `next` ([#483](https://github.com/Modern-Treasury/modern-treasury-python/issues/483)) ([01ef021](https://github.com/Modern-Treasury/modern-treasury-python/commit/01ef02159c9c9bbd7fdbfba892d211b6225a41a9))
* **ci:** update rye to v0.35.0 ([#479](https://github.com/Modern-Treasury/modern-treasury-python/issues/479)) ([597c92c](https://github.com/Modern-Treasury/modern-treasury-python/commit/597c92cbd9fc918d846e9f999f83910dd9267e1f))
* **docs:** minor update to formatting of API link in README ([#488](https://github.com/Modern-Treasury/modern-treasury-python/issues/488)) ([ad63bdf](https://github.com/Modern-Treasury/modern-treasury-python/commit/ad63bdfcea5137f9065f8d7cdd15065e0f7295d5))
* **internal:** add helper function ([#481](https://github.com/Modern-Treasury/modern-treasury-python/issues/481)) ([ecd8aab](https://github.com/Modern-Treasury/modern-treasury-python/commit/ecd8aabfd60ad6fd622cea3502e842c261864c23))
* **internal:** add helper method for constructing `BaseModel`s ([#476](https://github.com/Modern-Treasury/modern-treasury-python/issues/476)) ([2502b91](https://github.com/Modern-Treasury/modern-treasury-python/commit/2502b9145e4c7d387a66c69014221c76ea8cc6de))
* **internal:** minor import restructuring ([#484](https://github.com/Modern-Treasury/modern-treasury-python/issues/484)) ([a62e05a](https://github.com/Modern-Treasury/modern-treasury-python/commit/a62e05a35880c001694ba73ff1d62fafc3d86950))
* **internal:** minor options / compat functions updates ([#486](https://github.com/Modern-Treasury/modern-treasury-python/issues/486)) ([0d66343](https://github.com/Modern-Treasury/modern-treasury-python/commit/0d663439e1977ae9add0160b07aa9221eb1ddcb9))
* **internal:** minor request options handling changes ([#480](https://github.com/Modern-Treasury/modern-treasury-python/issues/480)) ([00bc2b8](https://github.com/Modern-Treasury/modern-treasury-python/commit/00bc2b89afb6e98246d4025eaecfa1390fb4dfcb))
* **internal:** update formatting ([#489](https://github.com/Modern-Treasury/modern-treasury-python/issues/489)) ([baf8626](https://github.com/Modern-Treasury/modern-treasury-python/commit/baf86260d29a832f6ceb99101dfdf3342563df95))
* **internal:** update mypy ([#482](https://github.com/Modern-Treasury/modern-treasury-python/issues/482)) ([01781f2](https://github.com/Modern-Treasury/modern-treasury-python/commit/01781f2c47c23eb1be869ff08a9151b4accd8088))


### Documentation

* **examples:** use named params more ([#485](https://github.com/Modern-Treasury/modern-treasury-python/issues/485)) ([dddb80d](https://github.com/Modern-Treasury/modern-treasury-python/commit/dddb80db249a3d70cb610e1e9575d0983b4635cd))

## 1.36.0 (2024-07-01)

Full Changelog: [v1.35.1...v1.36.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.35.1...v1.36.0)

### Features

* **api:** updates ([#475](https://github.com/Modern-Treasury/modern-treasury-python/issues/475)) ([e71c1fe](https://github.com/Modern-Treasury/modern-treasury-python/commit/e71c1fe5bdcdab1232308bf8a8a840a23f572783))


### Bug Fixes

* **build:** include more files in sdist builds ([#470](https://github.com/Modern-Treasury/modern-treasury-python/issues/470)) ([e1a1296](https://github.com/Modern-Treasury/modern-treasury-python/commit/e1a1296002b6c093a4131f9361f9e8c3538e91b9))
* **client/async:** avoid blocking io call for platform headers ([#466](https://github.com/Modern-Treasury/modern-treasury-python/issues/466)) ([3223606](https://github.com/Modern-Treasury/modern-treasury-python/commit/322360602be73549eb8801b21cb7c05f4ffbbdf9))
* **docs:** fix link to advanced python httpx docs ([#468](https://github.com/Modern-Treasury/modern-treasury-python/issues/468)) ([77777f3](https://github.com/Modern-Treasury/modern-treasury-python/commit/77777f36cd3aceb12ef3b97d4ee7b2bc19070cf4))
* temporarily patch upstream version to fix broken release flow ([#469](https://github.com/Modern-Treasury/modern-treasury-python/issues/469)) ([6b9a431](https://github.com/Modern-Treasury/modern-treasury-python/commit/6b9a431974577316e563208e03bfc12e32f89338))


### Chores

* **deps:** bump anyio to v4.4.0 ([#471](https://github.com/Modern-Treasury/modern-treasury-python/issues/471)) ([d5f2656](https://github.com/Modern-Treasury/modern-treasury-python/commit/d5f2656dfe9847911b117e043d9f409569afce5d))
* gitignore test server logs ([#473](https://github.com/Modern-Treasury/modern-treasury-python/issues/473)) ([7816cbd](https://github.com/Modern-Treasury/modern-treasury-python/commit/7816cbd7e8136e18741bc974a53968baa660c8f9))
* **internal:** add reflection helper function ([#472](https://github.com/Modern-Treasury/modern-treasury-python/issues/472)) ([7622150](https://github.com/Modern-Treasury/modern-treasury-python/commit/7622150a2b0dcd4c464b6e50d0efb48760c1c403))
* **internal:** add rich as a dev dependency ([#474](https://github.com/Modern-Treasury/modern-treasury-python/issues/474)) ([1baa3f7](https://github.com/Modern-Treasury/modern-treasury-python/commit/1baa3f729889adb0b29a198409c13c56ed30faed))

## 1.35.1 (2024-06-17)

Full Changelog: [v1.35.0...v1.35.1](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.35.0...v1.35.1)

### Chores

* **internal:** add a `default_query` method ([#464](https://github.com/Modern-Treasury/modern-treasury-python/issues/464)) ([fe49309](https://github.com/Modern-Treasury/modern-treasury-python/commit/fe493098f94124def0de7dc9f6d6a2611240b042))

## 1.35.0 (2024-06-05)

Full Changelog: [v1.34.1...v1.35.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.34.1...v1.35.0)

### Features

* **api:** add kr_brn kr_crn kr_rrn enum values ([#459](https://github.com/Modern-Treasury/modern-treasury-python/issues/459)) ([cf93671](https://github.com/Modern-Treasury/modern-treasury-python/commit/cf93671a40644aaa3882bebf47c894e4b8904886))
* **api:** add risk rating field ([#461](https://github.com/Modern-Treasury/modern-treasury-python/issues/461)) ([439a96d](https://github.com/Modern-Treasury/modern-treasury-python/commit/439a96d019ec6cd82694f3a85d15834db0c094b4))


### Bug Fixes

* fix enum type to be non nullable ([#463](https://github.com/Modern-Treasury/modern-treasury-python/issues/463)) ([c3eaca4](https://github.com/Modern-Treasury/modern-treasury-python/commit/c3eaca4631c0f6d927c3cd6c8ad27def0f93861f))


### Chores

* **internal:** sync urls ([#462](https://github.com/Modern-Treasury/modern-treasury-python/issues/462)) ([8b3f81a](https://github.com/Modern-Treasury/modern-treasury-python/commit/8b3f81ac4e57fe7b258e7bc298fc0b16339a50b1))

## 1.34.1 (2024-05-30)

Full Changelog: [v1.34.0...v1.34.1](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.34.0...v1.34.1)

### Chores

* **internal:** add code reviewer ([#457](https://github.com/Modern-Treasury/modern-treasury-python/issues/457)) ([4ca3d0b](https://github.com/Modern-Treasury/modern-treasury-python/commit/4ca3d0b340db5b4e7199576d73016526a37d30bf))

## 1.34.0 (2024-05-28)

Full Changelog: [v1.33.0...v1.34.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.33.0...v1.34.0)

### Features

* **api:** add currency to ledger account categories ([#449](https://github.com/Modern-Treasury/modern-treasury-python/issues/449)) ([b50317b](https://github.com/Modern-Treasury/modern-treasury-python/commit/b50317bde4b2733bc522ff126e83ecfb3650c86b))
* **api:** invoice overdue reminders ([fbf7499](https://github.com/Modern-Treasury/modern-treasury-python/commit/fbf7499d4c69f8481ffb69b248deec8101f9341f))
* **api:** mark ConnectionLegalEntity response properties as required ([#455](https://github.com/Modern-Treasury/modern-treasury-python/issues/455)) ([2e7fe0d](https://github.com/Modern-Treasury/modern-treasury-python/commit/2e7fe0d773bf553161073cc8cddd722542de16e0))
* **api:** remove deprecated ledger account payouts ([#450](https://github.com/Modern-Treasury/modern-treasury-python/issues/450)) ([fbf7499](https://github.com/Modern-Treasury/modern-treasury-python/commit/fbf7499d4c69f8481ffb69b248deec8101f9341f))
* **api:** updates ([#442](https://github.com/Modern-Treasury/modern-treasury-python/issues/442)) ([084e590](https://github.com/Modern-Treasury/modern-treasury-python/commit/084e590c64073403f80708bfb4c81382f05837cd))


### Chores

* **ci:** update rye install location ([#451](https://github.com/Modern-Treasury/modern-treasury-python/issues/451)) ([4cc0291](https://github.com/Modern-Treasury/modern-treasury-python/commit/4cc02915977f06d7e2cdf9f91e8beff2c11d5e79))
* **ci:** update rye install location ([#452](https://github.com/Modern-Treasury/modern-treasury-python/issues/452)) ([75d3c8b](https://github.com/Modern-Treasury/modern-treasury-python/commit/75d3c8b11a45f6447351acd16e5f40b8c5841ee6))
* **client:** log response headers in debug mode ([#437](https://github.com/Modern-Treasury/modern-treasury-python/issues/437)) ([6ec701a](https://github.com/Modern-Treasury/modern-treasury-python/commit/6ec701ac602595030226a907d4932b1272d81f61))
* **docs:** add SECURITY.md ([#445](https://github.com/Modern-Treasury/modern-treasury-python/issues/445)) ([5fc4854](https://github.com/Modern-Treasury/modern-treasury-python/commit/5fc4854c77d2246e329b89d83011854d66c0a0f6))
* **docs:** streamline payment purpose and vendor failure handling ([#446](https://github.com/Modern-Treasury/modern-treasury-python/issues/446)) ([9049e1d](https://github.com/Modern-Treasury/modern-treasury-python/commit/9049e1ddbf10f8b28ed32bea6098d4dd7871e83e))
* **internal:** add link to openapi spec ([#439](https://github.com/Modern-Treasury/modern-treasury-python/issues/439)) ([53c0a71](https://github.com/Modern-Treasury/modern-treasury-python/commit/53c0a71785d407edc2d7efb8f145e8cb98d2ed71))
* **internal:** add scripts/test, scripts/mock and add ci job ([#440](https://github.com/Modern-Treasury/modern-treasury-python/issues/440)) ([8b138be](https://github.com/Modern-Treasury/modern-treasury-python/commit/8b138bed242b523a41e08966ab6bd498059b3500))
* **internal:** add slightly better logging to scripts ([#448](https://github.com/Modern-Treasury/modern-treasury-python/issues/448)) ([dec98a7](https://github.com/Modern-Treasury/modern-treasury-python/commit/dec98a746a5c1f9261527b7aaffbc70c2910df80))
* **internal:** bump mock server version to ~5.8.0 ([#441](https://github.com/Modern-Treasury/modern-treasury-python/issues/441)) ([0421e0e](https://github.com/Modern-Treasury/modern-treasury-python/commit/0421e0ee321ddfbb1027ce05094267fddf1daae3))
* **internal:** bump pydantic dependency ([#447](https://github.com/Modern-Treasury/modern-treasury-python/issues/447)) ([b2a507d](https://github.com/Modern-Treasury/modern-treasury-python/commit/b2a507de3e5fb4a4ddcd41776ea190c77723dd3b))
* **internal:** bump pyright ([#453](https://github.com/Modern-Treasury/modern-treasury-python/issues/453)) ([14e0e35](https://github.com/Modern-Treasury/modern-treasury-python/commit/14e0e35b37aef4926513638198937767942b03c1))
* **internal:** update bootstrap script ([#456](https://github.com/Modern-Treasury/modern-treasury-python/issues/456)) ([7e949cc](https://github.com/Modern-Treasury/modern-treasury-python/commit/7e949cc5987befd7efaa18ffb60408b6b4ba5ed9))


### Documentation

* **contributing:** update references to rye-up.com ([#454](https://github.com/Modern-Treasury/modern-treasury-python/issues/454)) ([3ccb5ff](https://github.com/Modern-Treasury/modern-treasury-python/commit/3ccb5ff96a80f1ff3040b53bfdfeaaaa7c0faddc))
* **readme:** fix misleading timeout example value ([#443](https://github.com/Modern-Treasury/modern-treasury-python/issues/443)) ([2f2efaa](https://github.com/Modern-Treasury/modern-treasury-python/commit/2f2efaa3409cff2095ef2901322b68d6adea402f))

## 1.33.0 (2024-04-26)

Full Changelog: [v1.32.0...v1.33.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.32.0...v1.33.0)

### Features

* **api:** various API updates ([#436](https://github.com/Modern-Treasury/modern-treasury-python/issues/436)) ([b9a26a2](https://github.com/Modern-Treasury/modern-treasury-python/commit/b9a26a2546132ac6213099772d75ac4471b351cb))


### Bug Fixes

* **docs:** doc improvements ([#430](https://github.com/Modern-Treasury/modern-treasury-python/issues/430)) ([0963b2b](https://github.com/Modern-Treasury/modern-treasury-python/commit/0963b2b94e06f4d53aaf9432f43f3ca5b43b9240))


### Chores

* **internal:** minor reformatting ([#435](https://github.com/Modern-Treasury/modern-treasury-python/issues/435)) ([d6143ed](https://github.com/Modern-Treasury/modern-treasury-python/commit/d6143ed612c5e32d9d3dd6d7643cf17ffee7c304))
* **internal:** reformat imports ([#434](https://github.com/Modern-Treasury/modern-treasury-python/issues/434)) ([1e7d696](https://github.com/Modern-Treasury/modern-treasury-python/commit/1e7d696d6b00c72050a44be74ba3c2b3d4041a34))
* **internal:** restructure imports ([#428](https://github.com/Modern-Treasury/modern-treasury-python/issues/428)) ([d5922d0](https://github.com/Modern-Treasury/modern-treasury-python/commit/d5922d0d126d8ec41f819154d3b7da7c16fba165))
* **internal:** update test helper function ([#433](https://github.com/Modern-Treasury/modern-treasury-python/issues/433)) ([7f9b5d6](https://github.com/Modern-Treasury/modern-treasury-python/commit/7f9b5d6c2040221fc4b1471a14ab7b240026db66))
* **internal:** use actions/checkout@v4 for codeflow ([#432](https://github.com/Modern-Treasury/modern-treasury-python/issues/432)) ([2f6b101](https://github.com/Modern-Treasury/modern-treasury-python/commit/2f6b101a8b9971340cfeac5a05862287f0aa5ce5))
* **tests:** rename test file ([#431](https://github.com/Modern-Treasury/modern-treasury-python/issues/431)) ([ddfc581](https://github.com/Modern-Treasury/modern-treasury-python/commit/ddfc581d5f8320050fd3c89ce4178eaac47377e4))

## 1.32.0 (2024-04-18)

Full Changelog: [v1.31.0...v1.32.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.31.0...v1.32.0)

### Features

* **api:** add ledger_transaction_id field to reversal ([#424](https://github.com/Modern-Treasury/modern-treasury-python/issues/424)) ([eaf6933](https://github.com/Modern-Treasury/modern-treasury-python/commit/eaf6933acf6d7ad8d09034beb03f5a23f11013d7))


### Chores

* fix typo ([#420](https://github.com/Modern-Treasury/modern-treasury-python/issues/420)) ([92296ad](https://github.com/Modern-Treasury/modern-treasury-python/commit/92296adc82dda45efd0111ebc896865f57efa154))
* **internal:** add lru_cache helper function ([#425](https://github.com/Modern-Treasury/modern-treasury-python/issues/425)) ([50024ed](https://github.com/Modern-Treasury/modern-treasury-python/commit/50024edaace4cc7de0bd9125cc51a0376ff49e59))
* **internal:** ban usage of lru_cache ([#426](https://github.com/Modern-Treasury/modern-treasury-python/issues/426)) ([8512ca1](https://github.com/Modern-Treasury/modern-treasury-python/commit/8512ca158be9439f06dbf7fb6f9602caab102ac4))
* **internal:** bump pyright to 1.1.359 ([#427](https://github.com/Modern-Treasury/modern-treasury-python/issues/427)) ([6791ec6](https://github.com/Modern-Treasury/modern-treasury-python/commit/6791ec655d33bf9169ac09606999c8df0627ac60))
* **internal:** formatting ([#423](https://github.com/Modern-Treasury/modern-treasury-python/issues/423)) ([6a75f13](https://github.com/Modern-Treasury/modern-treasury-python/commit/6a75f13793006071c956bbb9c7f072c8f08be1ac))


### Documentation

* **examples:** use counterparties in snippets ([#422](https://github.com/Modern-Treasury/modern-treasury-python/issues/422)) ([3e04d72](https://github.com/Modern-Treasury/modern-treasury-python/commit/3e04d729bd3344bad99bbb3969a117fe9ee74dc6))

## 1.31.0 (2024-04-09)

Full Changelog: [v1.30.0...v1.31.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.30.0...v1.31.0)

### Features

* **api:** add id type in_lei ([#417](https://github.com/Modern-Treasury/modern-treasury-python/issues/417)) ([eb4fff9](https://github.com/Modern-Treasury/modern-treasury-python/commit/eb4fff988eba220a827abd6bc7888b5222ee3199))
* **api:** update account number type enum ([#411](https://github.com/Modern-Treasury/modern-treasury-python/issues/411)) ([0dc3b7d](https://github.com/Modern-Treasury/modern-treasury-python/commit/0dc3b7dd682fed48f6880658b65310a7828709dc))
* **client:** add DefaultHttpxClient and DefaultAsyncHttpxClient ([#418](https://github.com/Modern-Treasury/modern-treasury-python/issues/418)) ([843bdcf](https://github.com/Modern-Treasury/modern-treasury-python/commit/843bdcf67446d16ad1e31d8fb7bc038adfb338d3))
* **models:** add to_dict & to_json helper methods ([#419](https://github.com/Modern-Treasury/modern-treasury-python/issues/419)) ([472e346](https://github.com/Modern-Treasury/modern-treasury-python/commit/472e3463dcb60ec0922a2428cef0f5951ae7c489))
* **package:** export default constants ([#409](https://github.com/Modern-Treasury/modern-treasury-python/issues/409)) ([7f7ede1](https://github.com/Modern-Treasury/modern-treasury-python/commit/7f7ede13ae026f7dc01a2b816634df6b8d118865))


### Bug Fixes

* **project:** use absolute github links on PyPi ([#412](https://github.com/Modern-Treasury/modern-treasury-python/issues/412)) ([d5a5578](https://github.com/Modern-Treasury/modern-treasury-python/commit/d5a5578acd518a5dfd04c5d8d3e22bf5d26dca06))


### Chores

* **client:** validate that max_retries is not None ([#414](https://github.com/Modern-Treasury/modern-treasury-python/issues/414)) ([f8d0405](https://github.com/Modern-Treasury/modern-treasury-python/commit/f8d04054145c254f05da10af70801a2b24aa0ff8))
* **internal:** defer model build for import latency ([#415](https://github.com/Modern-Treasury/modern-treasury-python/issues/415)) ([ada3d43](https://github.com/Modern-Treasury/modern-treasury-python/commit/ada3d43770506a53b0a2bcbfe95547efd4ff77c3))
* **internal:** streaming updates ([#416](https://github.com/Modern-Treasury/modern-treasury-python/issues/416)) ([c8da517](https://github.com/Modern-Treasury/modern-treasury-python/commit/c8da517d93c09964b3f4712b45eefa4c2e19264a))

## 1.30.0 (2024-03-26)

Full Changelog: [v1.29.0...v1.30.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.29.0...v1.30.0)

### Features

* **api:** add citibank enums ([#408](https://github.com/Modern-Treasury/modern-treasury-python/issues/408)) ([43766ea](https://github.com/Modern-Treasury/modern-treasury-python/commit/43766eaf8d15a39612556c7484f8df1898a5bef0))
* **api:** add date_formed property to legal entities ([#393](https://github.com/Modern-Treasury/modern-treasury-python/issues/393)) ([9a4b35d](https://github.com/Modern-Treasury/modern-treasury-python/commit/9a4b35d269e834123d127d440f6698de0fa0cb97))
* **api:** add line item metadata ([435ed52](https://github.com/Modern-Treasury/modern-treasury-python/commit/435ed52182687b264a67f515dd8c598d51effabe))
* **api:** extend list invoices query params ([#395](https://github.com/Modern-Treasury/modern-treasury-python/issues/395)) ([96b0eb8](https://github.com/Modern-Treasury/modern-treasury-python/commit/96b0eb8b989b29052617f2a8d4c84ae7d5b2d68e))
* **api:** introduce bulk transaction create ([#403](https://github.com/Modern-Treasury/modern-treasury-python/issues/403)) ([435ed52](https://github.com/Modern-Treasury/modern-treasury-python/commit/435ed52182687b264a67f515dd8c598d51effabe))
* **api:** rename `associated_legal_entity` to `child_legal_entity` ([#399](https://github.com/Modern-Treasury/modern-treasury-python/issues/399)) ([6c3404b](https://github.com/Modern-Treasury/modern-treasury-python/commit/6c3404b43c328ed586402853bf0b265e8c9eebe3))
* **api:** rename `id_type` enum from `cl_nut` to `cl_rut` ([6c3404b](https://github.com/Modern-Treasury/modern-treasury-python/commit/6c3404b43c328ed586402853bf0b265e8c9eebe3))
* **api:** updates ([#407](https://github.com/Modern-Treasury/modern-treasury-python/issues/407)) ([1d6a2f7](https://github.com/Modern-Treasury/modern-treasury-python/commit/1d6a2f735331837eb8cd0bdff5247e80a2f511a8))


### Bug Fixes

* revert regression with 3.7 support ([#406](https://github.com/Modern-Treasury/modern-treasury-python/issues/406)) ([9c0d235](https://github.com/Modern-Treasury/modern-treasury-python/commit/9c0d235b6e898b1aff433fac24632c5c0606c52a))


### Performance Improvements

* cache TypeAdapters ([#396](https://github.com/Modern-Treasury/modern-treasury-python/issues/396)) ([4e3f737](https://github.com/Modern-Treasury/modern-treasury-python/commit/4e3f737f25bd9eb55a4f3780e73394e215540039))


### Chores

* add back removed code ([b004844](https://github.com/Modern-Treasury/modern-treasury-python/commit/b004844d3aae539cc2eac22d957101afee2df2e2))
* **internal:** formatting change ([#404](https://github.com/Modern-Treasury/modern-treasury-python/issues/404)) ([dc0dcca](https://github.com/Modern-Treasury/modern-treasury-python/commit/dc0dccad5b41530f8246d8b457176f883a396725))
* **internal:** loosen input type for util function ([#400](https://github.com/Modern-Treasury/modern-treasury-python/issues/400)) ([b9152e1](https://github.com/Modern-Treasury/modern-treasury-python/commit/b9152e1462045e5ed6805b4066274ad2ca47c54b))
* **internal:** temporary commit ([1c3fcba](https://github.com/Modern-Treasury/modern-treasury-python/commit/1c3fcba29db3a35c70817ff8e0a61a922d3982e8))
* **internal:** update generated pragma comment ([#398](https://github.com/Modern-Treasury/modern-treasury-python/issues/398)) ([079cd15](https://github.com/Modern-Treasury/modern-treasury-python/commit/079cd156d88cf8b8a966d09cd07c5615194421ab))


### Documentation

* **contributing:** fix typo ([#405](https://github.com/Modern-Treasury/modern-treasury-python/issues/405)) ([85daac6](https://github.com/Modern-Treasury/modern-treasury-python/commit/85daac67182549dcaef4408f51bb634cf48450ba))
* fix typo in CONTRIBUTING.md ([#397](https://github.com/Modern-Treasury/modern-treasury-python/issues/397)) ([6bf2e54](https://github.com/Modern-Treasury/modern-treasury-python/commit/6bf2e5454e8dc68011b7cf8cf6b7f1feb1ee4240))
* **readme:** consistent use of sentence case in headings ([#401](https://github.com/Modern-Treasury/modern-treasury-python/issues/401)) ([83c0b59](https://github.com/Modern-Treasury/modern-treasury-python/commit/83c0b596aea61df02b0998d474113e7d9c0c4408))
* **readme:** document how to make undocumented requests ([#402](https://github.com/Modern-Treasury/modern-treasury-python/issues/402)) ([e6b9cec](https://github.com/Modern-Treasury/modern-treasury-python/commit/e6b9cec23184cbf8e536957f899d2a63b9cb19ee))

## 1.29.0 (2024-03-11)

Full Changelog: [v1.28.0...v1.29.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.28.0...v1.29.0)

### Features

* **api:** add legal_structure enum member ([#384](https://github.com/Modern-Treasury/modern-treasury-python/issues/384)) ([57666b1](https://github.com/Modern-Treasury/modern-treasury-python/commit/57666b1863ac06848b3c3f87f7513eddc8134a68))


### Chores

* **client:** improve error message for invalid http_client argument ([#387](https://github.com/Modern-Treasury/modern-treasury-python/issues/387)) ([2e3952e](https://github.com/Modern-Treasury/modern-treasury-python/commit/2e3952e0690e173f1866fef46989bba4ca20429d))
* **docs:** mention install from git repo ([#382](https://github.com/Modern-Treasury/modern-treasury-python/issues/382)) ([0ee2ab5](https://github.com/Modern-Treasury/modern-treasury-python/commit/0ee2ab53f2ceb52584703b1cde3a15ba9127aa61))
* export NOT_GIVEN sentinel value ([#391](https://github.com/Modern-Treasury/modern-treasury-python/issues/391)) ([1972ed3](https://github.com/Modern-Treasury/modern-treasury-python/commit/1972ed3c47e1b98a314d92dbdfa7c7bc409a052d))
* **internal:** add core support for deserializing into number response ([#388](https://github.com/Modern-Treasury/modern-treasury-python/issues/388)) ([7b2214a](https://github.com/Modern-Treasury/modern-treasury-python/commit/7b2214a6d6d7cc8a8147d119b39393b7dd9f34fa))
* **internal:** bump pyright ([#389](https://github.com/Modern-Treasury/modern-treasury-python/issues/389)) ([30782dc](https://github.com/Modern-Treasury/modern-treasury-python/commit/30782dc6a380cb5b378237ec85aa42b881d8d92a))
* **internal:** improve deserialisation of discriminated unions ([#392](https://github.com/Modern-Treasury/modern-treasury-python/issues/392)) ([85eed8c](https://github.com/Modern-Treasury/modern-treasury-python/commit/85eed8cf4dd70e1169acc70857dd8950bbd831df))
* **internal:** split up transforms into sync / async ([#385](https://github.com/Modern-Treasury/modern-treasury-python/issues/385)) ([b7c4c48](https://github.com/Modern-Treasury/modern-treasury-python/commit/b7c4c48dd6cdeafd7bce20cae73acddeb3e2bf68))
* **internal:** support more input types ([#386](https://github.com/Modern-Treasury/modern-treasury-python/issues/386)) ([79f79ed](https://github.com/Modern-Treasury/modern-treasury-python/commit/79f79edee7113b9631364a54be3e8642d31965fa))
* **internal:** support parsing Annotated types ([#390](https://github.com/Modern-Treasury/modern-treasury-python/issues/390)) ([0dc04be](https://github.com/Modern-Treasury/modern-treasury-python/commit/0dc04be6ab1df54aaf67240c29af3a3bd29ca544))

## 1.28.0 (2024-02-29)

Full Changelog: [v1.27.0...v1.28.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.27.0...v1.28.0)

### Features

* **api:** add legal_entities resource ([#381](https://github.com/Modern-Treasury/modern-treasury-python/issues/381)) ([57d6eb9](https://github.com/Modern-Treasury/modern-treasury-python/commit/57d6eb95d89254783b11ab9641df0c9801f46505))
* **api:** added foreign exchange rate information ([#375](https://github.com/Modern-Treasury/modern-treasury-python/issues/375)) ([167dd4e](https://github.com/Modern-Treasury/modern-treasury-python/commit/167dd4e002560f3fd8d18b26c60c92be764bcede))


### Chores

* **ci:** uses Stainless GitHub App for releases ([#370](https://github.com/Modern-Treasury/modern-treasury-python/issues/370)) ([992d666](https://github.com/Modern-Treasury/modern-treasury-python/commit/992d66631b6fe1d6cab082fc8e0d7aa249f0059b))
* **client:** use anyio.sleep instead of asyncio.sleep ([#378](https://github.com/Modern-Treasury/modern-treasury-python/issues/378)) ([b986304](https://github.com/Modern-Treasury/modern-treasury-python/commit/b9863040a36b02a9b4fae059b54101aba3b41ef1))
* **internal:** bump pyright ([#377](https://github.com/Modern-Treasury/modern-treasury-python/issues/377)) ([5b09470](https://github.com/Modern-Treasury/modern-treasury-python/commit/5b09470d873db017a0d0f6dd656130187f102e21))
* **internal:** bump rye to v0.24.0 ([#374](https://github.com/Modern-Treasury/modern-treasury-python/issues/374)) ([97ec7a1](https://github.com/Modern-Treasury/modern-treasury-python/commit/97ec7a19107a8cf1ebe349fc157e286d7e6bde02))
* **internal:** minor core client restructuring ([#379](https://github.com/Modern-Treasury/modern-treasury-python/issues/379)) ([fbf04eb](https://github.com/Modern-Treasury/modern-treasury-python/commit/fbf04eb4a0f68c2a44d46d88bf99daba0b41f034))
* **internal:** refactor release environment script ([#372](https://github.com/Modern-Treasury/modern-treasury-python/issues/372)) ([bc7ee03](https://github.com/Modern-Treasury/modern-treasury-python/commit/bc7ee034706701a91c821a1b7d34fd53f2fc25f4))
* **internal:** update deps ([#376](https://github.com/Modern-Treasury/modern-treasury-python/issues/376)) ([ec2a9eb](https://github.com/Modern-Treasury/modern-treasury-python/commit/ec2a9eb7994e2358053a36c4cff3a3901b18279d))


### Documentation

* **contributing:** improve wording ([#380](https://github.com/Modern-Treasury/modern-treasury-python/issues/380)) ([d8eefa6](https://github.com/Modern-Treasury/modern-treasury-python/commit/d8eefa663af1e496a4cd68b2076fde44549cc1cf))

## 1.27.0 (2024-02-13)

Full Changelog: [v1.26.0...v1.27.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.26.0...v1.27.0)

### Features

* **api:** updates ([#369](https://github.com/Modern-Treasury/modern-treasury-python/issues/369)) ([0a95ac5](https://github.com/Modern-Treasury/modern-treasury-python/commit/0a95ac5c75d2478d84ce3643c690448155d9b1ef))
* **api:** updates parameters, error codes ([#362](https://github.com/Modern-Treasury/modern-treasury-python/issues/362)) ([045d575](https://github.com/Modern-Treasury/modern-treasury-python/commit/045d575759730f0c3f774575fa6120eb907f5a80))


### Bug Fixes

* prevent crash when platform.architecture() is not allowed ([#364](https://github.com/Modern-Treasury/modern-treasury-python/issues/364)) ([268998e](https://github.com/Modern-Treasury/modern-treasury-python/commit/268998e42ac22e4fe58b5644abe42e48ba583e1c))
* **types:** loosen most List params types to Iterable ([#367](https://github.com/Modern-Treasury/modern-treasury-python/issues/367)) ([21b537b](https://github.com/Modern-Treasury/modern-treasury-python/commit/21b537b98fc22e5cbb17eab7962fe2c843e3d53d))


### Chores

* **interal:** make link to api.md relative ([#363](https://github.com/Modern-Treasury/modern-treasury-python/issues/363)) ([2aabaeb](https://github.com/Modern-Treasury/modern-treasury-python/commit/2aabaeb24bc0cdd63916bb6145fc6b382fb71732))
* **internal:** add lint command ([#366](https://github.com/Modern-Treasury/modern-treasury-python/issues/366)) ([9a1cdab](https://github.com/Modern-Treasury/modern-treasury-python/commit/9a1cdab477de7ef6b59f032c49fb7e3e9488d6d3))
* **internal:** support pre-release versioning ([#360](https://github.com/Modern-Treasury/modern-treasury-python/issues/360)) ([4d5f30f](https://github.com/Modern-Treasury/modern-treasury-python/commit/4d5f30f99381900a3af4844320524aa462aa2821))
* **internal:** support serialising iterable types ([#365](https://github.com/Modern-Treasury/modern-treasury-python/issues/365)) ([a0a776a](https://github.com/Modern-Treasury/modern-treasury-python/commit/a0a776af45dadc42eaa2c41cdab8e9561aa32b99))


### Documentation

* add CONTRIBUTING.md ([#368](https://github.com/Modern-Treasury/modern-treasury-python/issues/368)) ([52070bd](https://github.com/Modern-Treasury/modern-treasury-python/commit/52070bd755d88e30586f821fdcaf31b9ac1dce4e))

## 1.26.0 (2024-01-30)

Full Changelog: [v1.25.0...v1.26.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.25.0...v1.26.0)

### Features

* **client:** enable follow redirects by default ([#355](https://github.com/Modern-Treasury/modern-treasury-python/issues/355)) ([380e93d](https://github.com/Modern-Treasury/modern-treasury-python/commit/380e93d9fe7ec169c62ecaa4824369dca7e2b007))
* **client:** support parsing custom response types ([#358](https://github.com/Modern-Treasury/modern-treasury-python/issues/358)) ([78a0c73](https://github.com/Modern-Treasury/modern-treasury-python/commit/78a0c737e144aea7cf731d75166a9d4f835c6e31))


### Bug Fixes

* **ci:** ignore stainless-app edits to release PR title ([#352](https://github.com/Modern-Treasury/modern-treasury-python/issues/352)) ([8ade5d0](https://github.com/Modern-Treasury/modern-treasury-python/commit/8ade5d02b45dbb782f6bceb3622cd2c8dd220d3f))


### Chores

* **internal:** add internal helpers ([#353](https://github.com/Modern-Treasury/modern-treasury-python/issues/353)) ([79e0db0](https://github.com/Modern-Treasury/modern-treasury-python/commit/79e0db01aa21b38c3abd09ae06d116ec5bbd1c31))
* **internal:** cast type in mocked test ([#359](https://github.com/Modern-Treasury/modern-treasury-python/issues/359)) ([96f7655](https://github.com/Modern-Treasury/modern-treasury-python/commit/96f7655c4b96dfe1c78de3c26151ab9f9d298925))
* **internal:** enable ruff type checking misuse lint rule ([#357](https://github.com/Modern-Treasury/modern-treasury-python/issues/357)) ([d9579f9](https://github.com/Modern-Treasury/modern-treasury-python/commit/d9579f952c9b7ddc435f88a016bf1a25f0d8323d))
* **internal:** fix typing util function ([#346](https://github.com/Modern-Treasury/modern-treasury-python/issues/346)) ([3f69cab](https://github.com/Modern-Treasury/modern-treasury-python/commit/3f69cab2b0d0516349b0a01bb952a1aed59c914b))
* **internal:** remove redundant client test ([#348](https://github.com/Modern-Treasury/modern-treasury-python/issues/348)) ([5e162a5](https://github.com/Modern-Treasury/modern-treasury-python/commit/5e162a54605af4d11013121afe786930407dc788))
* **internal:** share client instances between all tests ([#351](https://github.com/Modern-Treasury/modern-treasury-python/issues/351)) ([1c66b08](https://github.com/Modern-Treasury/modern-treasury-python/commit/1c66b08ef8d302c33cc9cdf359a6972c07af0a73))
* **internal:** speculative retry-after-ms support ([#349](https://github.com/Modern-Treasury/modern-treasury-python/issues/349)) ([bc16acf](https://github.com/Modern-Treasury/modern-treasury-python/commit/bc16acf2a4a378915b53d6005bc4c49b250e6b47))
* **internal:** support multipart data with overlapping keys ([#356](https://github.com/Modern-Treasury/modern-treasury-python/issues/356)) ([c6ba152](https://github.com/Modern-Treasury/modern-treasury-python/commit/c6ba15253fba8b4bbed1e12da9456a6a9f18bc74))
* lazy load raw resource class properties ([#350](https://github.com/Modern-Treasury/modern-treasury-python/issues/350)) ([53495ec](https://github.com/Modern-Treasury/modern-treasury-python/commit/53495ec71f45ef9124024fcee500702b6ca11da1))


### Refactors

* remove unnecessary builtin import ([#354](https://github.com/Modern-Treasury/modern-treasury-python/issues/354)) ([ddc8ffc](https://github.com/Modern-Treasury/modern-treasury-python/commit/ddc8ffc83a690c46471a71f01aeffe5e686bbd0b))

## 1.25.0 (2024-01-16)

Full Changelog: [v1.24.0...v1.25.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.24.0...v1.25.0)

### Features

* add `None` default value to nullable response properties ([#334](https://github.com/Modern-Treasury/modern-treasury-python/issues/334)) ([93bd6c6](https://github.com/Modern-Treasury/modern-treasury-python/commit/93bd6c64387381e677b062fa3772f0b6e66f1a0c))
* **api:** add `ledger_transactions` to expected payment request ([#337](https://github.com/Modern-Treasury/modern-treasury-python/issues/337)) ([ba1fe46](https://github.com/Modern-Treasury/modern-treasury-python/commit/ba1fe465e5eeaab3000f337b6eeea2bbd8bee281))
* **api:** add create and delete operations for internal accounts balance reports ([#340](https://github.com/Modern-Treasury/modern-treasury-python/issues/340)) ([8ff1049](https://github.com/Modern-Treasury/modern-treasury-python/commit/8ff1049092ad68c1cfcdfd88a7e16f409bd04985))
* **client:** add support for streaming raw responses ([#342](https://github.com/Modern-Treasury/modern-treasury-python/issues/342)) ([2fd8c94](https://github.com/Modern-Treasury/modern-treasury-python/commit/2fd8c94d2740a2c7835afe66265e76981ce0744d))


### Bug Fixes

* **client:** ensure path params are non-empty ([#343](https://github.com/Modern-Treasury/modern-treasury-python/issues/343)) ([10749e1](https://github.com/Modern-Treasury/modern-treasury-python/commit/10749e12124f0d7d8ce95f8012f2eb232be802aa))


### Chores

* add .keep files for examples and custom code directories ([#338](https://github.com/Modern-Treasury/modern-treasury-python/issues/338)) ([68d8ff1](https://github.com/Modern-Treasury/modern-treasury-python/commit/68d8ff19c1ba7d7e1970339a73ec21b831de0332))
* add write_to_file binary helper method ([#345](https://github.com/Modern-Treasury/modern-treasury-python/issues/345)) ([50234bc](https://github.com/Modern-Treasury/modern-treasury-python/commit/50234bccc63ae60cfec784324f0aee1f5b508fc9))
* **client:** improve debug logging for failed requests ([#339](https://github.com/Modern-Treasury/modern-treasury-python/issues/339)) ([0b0789f](https://github.com/Modern-Treasury/modern-treasury-python/commit/0b0789f6bd27e589941b46003d7b09f985312c60))
* **internal:** loosen type var restrictions ([#336](https://github.com/Modern-Treasury/modern-treasury-python/issues/336)) ([8888141](https://github.com/Modern-Treasury/modern-treasury-python/commit/88881410674dc5cf4951b6a70ca6a8a1d88b8a81))
* **internal:** replace isort with ruff ([#332](https://github.com/Modern-Treasury/modern-treasury-python/issues/332)) ([f4be664](https://github.com/Modern-Treasury/modern-treasury-python/commit/f4be664be3d5d302601fca0c04f7becb56172477))
* **internal:** updates to proxy helper ([#344](https://github.com/Modern-Treasury/modern-treasury-python/issues/344)) ([4f12aac](https://github.com/Modern-Treasury/modern-treasury-python/commit/4f12aac161afbe3d78881446adb9be24bfc87e1e))
* use property declarations for resource members ([#335](https://github.com/Modern-Treasury/modern-treasury-python/issues/335)) ([90e8951](https://github.com/Modern-Treasury/modern-treasury-python/commit/90e895185dada8bf39413d365e7cab7ccdce446c))


### Documentation

* **readme:** improve api reference ([#341](https://github.com/Modern-Treasury/modern-treasury-python/issues/341)) ([bea446e](https://github.com/Modern-Treasury/modern-treasury-python/commit/bea446e79c3ca23de88c15ab8ad8b748ef042e3a))

## 1.24.0 (2024-01-02)

Full Changelog: [v1.23.1...v1.24.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.23.1...v1.24.0)

### Features

* **api:** remove reversed and reversing ledger account status type ([#322](https://github.com/Modern-Treasury/modern-treasury-python/issues/322)) ([0c03887](https://github.com/Modern-Treasury/modern-treasury-python/commit/0c038878e9d91e055388380d5ddbd525822179d2))
* **api:** updates ([#315](https://github.com/Modern-Treasury/modern-treasury-python/issues/315)) ([778352f](https://github.com/Modern-Treasury/modern-treasury-python/commit/778352f011002e16303a245242f4dc7a87f3c7eb))


### Bug Fixes

* avoid leaking memory when Client.with_options is used ([#316](https://github.com/Modern-Treasury/modern-treasury-python/issues/316)) ([6e6b257](https://github.com/Modern-Treasury/modern-treasury-python/commit/6e6b257318061ff15a017dcae9646a3287295824))
* **client:** correctly use custom http client auth ([#330](https://github.com/Modern-Treasury/modern-treasury-python/issues/330)) ([af5287b](https://github.com/Modern-Treasury/modern-treasury-python/commit/af5287b7092a33fe6d5ae306c01e74e6baf519ee))
* **errors:** properly assign APIError.body ([#314](https://github.com/Modern-Treasury/modern-treasury-python/issues/314)) ([67627a3](https://github.com/Modern-Treasury/modern-treasury-python/commit/67627a3f7ea47584ea95d597808bd54d1ae3cfdd))


### Chores

* **ci:** run release workflow once per day ([#321](https://github.com/Modern-Treasury/modern-treasury-python/issues/321)) ([af16395](https://github.com/Modern-Treasury/modern-treasury-python/commit/af163956e68d59f371785a44d127ec9d10fbacbf))
* **internal:** add bin script ([#327](https://github.com/Modern-Treasury/modern-treasury-python/issues/327)) ([05bfe94](https://github.com/Modern-Treasury/modern-treasury-python/commit/05bfe94c979c1815e330edafcfca2dc0f937f5c9))
* **internal:** bump license ([#331](https://github.com/Modern-Treasury/modern-treasury-python/issues/331)) ([8cb7937](https://github.com/Modern-Treasury/modern-treasury-python/commit/8cb7937708f3a2a032a2a66cfcc088df6de8a398))
* **internal:** enable more lint rules ([#313](https://github.com/Modern-Treasury/modern-treasury-python/issues/313)) ([046e84d](https://github.com/Modern-Treasury/modern-treasury-python/commit/046e84d17f2239779fcbd8e358f322fe9b8309e6))
* **internal:** fix typos ([#325](https://github.com/Modern-Treasury/modern-treasury-python/issues/325)) ([9be3fdd](https://github.com/Modern-Treasury/modern-treasury-python/commit/9be3fdde3f65fe8e2223206d75ae4805ea62930d))
* **internal:** minor updates to pagination ([#311](https://github.com/Modern-Treasury/modern-treasury-python/issues/311)) ([90cb5cd](https://github.com/Modern-Treasury/modern-treasury-python/commit/90cb5cde7cb08e64e9a7b68f75496870a5153142))
* **internal:** minor utils restructuring ([#324](https://github.com/Modern-Treasury/modern-treasury-python/issues/324)) ([817e69b](https://github.com/Modern-Treasury/modern-treasury-python/commit/817e69b9a68b1ba0d56c45dd50044121652590c3))
* **internal:** reformat imports ([#309](https://github.com/Modern-Treasury/modern-treasury-python/issues/309)) ([9acbb03](https://github.com/Modern-Treasury/modern-treasury-python/commit/9acbb03939cee4a3f32726d1eb556f33b7bf78b9))
* **internal:** reformat imports ([#312](https://github.com/Modern-Treasury/modern-treasury-python/issues/312)) ([2fec25c](https://github.com/Modern-Treasury/modern-treasury-python/commit/2fec25c955f4d901953ceda660a4e9bc451d1391))
* **internal:** update formatting ([#310](https://github.com/Modern-Treasury/modern-treasury-python/issues/310)) ([c8ce56f](https://github.com/Modern-Treasury/modern-treasury-python/commit/c8ce56ff74fb9c1bba514a881eadb5e56f9213b8))
* **internal:** updates to base client ([#323](https://github.com/Modern-Treasury/modern-treasury-python/issues/323)) ([d717ab1](https://github.com/Modern-Treasury/modern-treasury-python/commit/d717ab1eb8d1a73e12d0e4239d06839064e65be5))
* **internal:** use ruff instead of black for formatting ([#329](https://github.com/Modern-Treasury/modern-treasury-python/issues/329)) ([8aa1f23](https://github.com/Modern-Treasury/modern-treasury-python/commit/8aa1f23197c974e4cb3bda321fc1ef88030f6545))
* **package:** bump minimum typing-extensions to 4.7 ([#326](https://github.com/Modern-Treasury/modern-treasury-python/issues/326)) ([92448b7](https://github.com/Modern-Treasury/modern-treasury-python/commit/92448b7406b60350d29f2769a4952cc95b478cbd))


### Documentation

* improve README timeout comment ([#317](https://github.com/Modern-Treasury/modern-treasury-python/issues/317)) ([777630c](https://github.com/Modern-Treasury/modern-treasury-python/commit/777630ca24a7694a7ac2756423eab556debe34cb))


### Refactors

* **client:** simplify cleanup ([#318](https://github.com/Modern-Treasury/modern-treasury-python/issues/318)) ([3000062](https://github.com/Modern-Treasury/modern-treasury-python/commit/3000062dde43792e8e880abf24b00388d21a3067))
* remove unused model types used in params ([#320](https://github.com/Modern-Treasury/modern-treasury-python/issues/320)) ([7731c5c](https://github.com/Modern-Treasury/modern-treasury-python/commit/7731c5c5257f4dfab58e5a54073af53249875c10))
* simplify internal error handling ([#319](https://github.com/Modern-Treasury/modern-treasury-python/issues/319)) ([c911df5](https://github.com/Modern-Treasury/modern-treasury-python/commit/c911df5e686b84d551d29c519fc51a839eb24ffb))

## 1.23.1 (2023-12-04)

Full Changelog: [v1.23.0...v1.23.1](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.23.0...v1.23.1)

### Bug Fixes

* **client:** correct base_url setter implementation ([#304](https://github.com/Modern-Treasury/modern-treasury-python/issues/304)) ([0362dce](https://github.com/Modern-Treasury/modern-treasury-python/commit/0362dcec36b99978b17cf4edd65d23e983d2c10b))
* **client:** ensure retried requests are closed ([#301](https://github.com/Modern-Treasury/modern-treasury-python/issues/301)) ([ae36851](https://github.com/Modern-Treasury/modern-treasury-python/commit/ae368516e44b2027e32a74f0742f66fe21b7f589))


### Chores

* **client:** improve copy method ([#291](https://github.com/Modern-Treasury/modern-treasury-python/issues/291)) ([85a47d1](https://github.com/Modern-Treasury/modern-treasury-python/commit/85a47d1221114d66209704ecc8c9e86d4669debc))
* **deps:** bump mypy to v1.7.1 ([#297](https://github.com/Modern-Treasury/modern-treasury-python/issues/297)) ([478ebc7](https://github.com/Modern-Treasury/modern-treasury-python/commit/478ebc7fd42d4e29081354f43f0c14a29dc2e673))
* **internal:** add tests for proxy change ([#300](https://github.com/Modern-Treasury/modern-treasury-python/issues/300)) ([f37e526](https://github.com/Modern-Treasury/modern-treasury-python/commit/f37e5264624ce21d2037a4dc7fe7f4e32aef1580))
* **internal:** options updates ([#294](https://github.com/Modern-Treasury/modern-treasury-python/issues/294)) ([ddb98bd](https://github.com/Modern-Treasury/modern-treasury-python/commit/ddb98bdd6d9c4d67c48e1d0f511a16c601fce1d4))
* **internal:** replace string concatenation with f-strings ([#303](https://github.com/Modern-Treasury/modern-treasury-python/issues/303)) ([7c02a27](https://github.com/Modern-Treasury/modern-treasury-python/commit/7c02a2712217e2439fe276e83d7ae70c8cd82512))
* **internal:** revert recent options change ([#295](https://github.com/Modern-Treasury/modern-treasury-python/issues/295)) ([9c20edd](https://github.com/Modern-Treasury/modern-treasury-python/commit/9c20edd87abdd7a284d0c6007658ab57510e41a6))
* **internal:** send more detailed x-stainless headers ([#296](https://github.com/Modern-Treasury/modern-treasury-python/issues/296)) ([3c46c06](https://github.com/Modern-Treasury/modern-treasury-python/commit/3c46c06e29e65bc6788ecd693f9ac00bb0bd98a2))
* **internal:** update lock file ([#298](https://github.com/Modern-Treasury/modern-treasury-python/issues/298)) ([071b8d9](https://github.com/Modern-Treasury/modern-treasury-python/commit/071b8d94cd5c1be925e94c7c70bc7254c2deabe6))
* **internal:** updates to proxy helper ([#299](https://github.com/Modern-Treasury/modern-treasury-python/issues/299)) ([e6c67a4](https://github.com/Modern-Treasury/modern-treasury-python/commit/e6c67a46a37eccb68911aaab888fd6137778c2b4))
* **package:** add license classifier metadata ([#293](https://github.com/Modern-Treasury/modern-treasury-python/issues/293)) ([c8c3d75](https://github.com/Modern-Treasury/modern-treasury-python/commit/c8c3d75be96a4b77390a11872afacb0a0ebcce44))
* **package:** lift anyio v4 restriction ([#305](https://github.com/Modern-Treasury/modern-treasury-python/issues/305)) ([9f0db06](https://github.com/Modern-Treasury/modern-treasury-python/commit/9f0db065c81a46ca63730731e112cce5cf7a6184))


### Documentation

* **readme:** update example snippets ([#302](https://github.com/Modern-Treasury/modern-treasury-python/issues/302)) ([b603520](https://github.com/Modern-Treasury/modern-treasury-python/commit/b6035204b745c8488bf3a6eba349fdfdd7de3ce5))

## 1.23.0 (2023-11-21)

Full Changelog: [v1.22.0...v1.23.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.22.0...v1.23.0)

### Features

* **api:** updates ([#290](https://github.com/Modern-Treasury/modern-treasury-python/issues/290)) ([4c353bd](https://github.com/Modern-Treasury/modern-treasury-python/commit/4c353bd459c28589d320945ba3d07b2fe3686367))


### Bug Fixes

* **client:** attempt to parse unknown json content types ([#288](https://github.com/Modern-Treasury/modern-treasury-python/issues/288)) ([1ebfa3e](https://github.com/Modern-Treasury/modern-treasury-python/commit/1ebfa3e38ee4508bb32772e876aac50912cf6ee7))

## 1.22.0 (2023-11-17)

Full Changelog: [v1.21.0...v1.22.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.21.0...v1.22.0)

### Features

* **api:** add dk_interbank_clearing_code and dk_nets enum members ([#276](https://github.com/Modern-Treasury/modern-treasury-python/issues/276)) ([7a9e489](https://github.com/Modern-Treasury/modern-treasury-python/commit/7a9e489f71be91fab3ab5761e3bc942a67d86141))
* **api:** updates ([#272](https://github.com/Modern-Treasury/modern-treasury-python/issues/272)) ([441b8f1](https://github.com/Modern-Treasury/modern-treasury-python/commit/441b8f1e2c993d44e6460a050e83c9d2043a29f7))
* **client:** support passing chunk size for binary responses ([#275](https://github.com/Modern-Treasury/modern-treasury-python/issues/275)) ([d97b06d](https://github.com/Modern-Treasury/modern-treasury-python/commit/d97b06d89b72d3f34a414bb39b77e061754ffb31))
* **client:** support reading the base url from an env variable ([#285](https://github.com/Modern-Treasury/modern-treasury-python/issues/285)) ([a49743f](https://github.com/Modern-Treasury/modern-treasury-python/commit/a49743f686bafdf39c9306c40171979cc488e33e))


### Bug Fixes

* **client:** retry if SSLWantReadError occurs in the async client ([#281](https://github.com/Modern-Treasury/modern-treasury-python/issues/281)) ([9d4ebc6](https://github.com/Modern-Treasury/modern-treasury-python/commit/9d4ebc6f449bb76e6b650d1fcd143fbe1481e2c5))
* **client:** serialise pydantic v1 default fields correctly in params ([#280](https://github.com/Modern-Treasury/modern-treasury-python/issues/280)) ([44bc532](https://github.com/Modern-Treasury/modern-treasury-python/commit/44bc5325eb274561d7dda1b46e6ad4402b57e7cc))
* **models:** mark unknown fields as set in pydantic v1 ([#279](https://github.com/Modern-Treasury/modern-treasury-python/issues/279)) ([3101a6a](https://github.com/Modern-Treasury/modern-treasury-python/commit/3101a6a36c5574f8cd6caf316483d6bcb817700c))


### Chores

* **internal:** base client updates ([#278](https://github.com/Modern-Treasury/modern-treasury-python/issues/278)) ([445ca02](https://github.com/Modern-Treasury/modern-treasury-python/commit/445ca025c37fa73a22ccbd358fb7972b748f0224))
* **internal:** fix devcontainer interpeter path ([#283](https://github.com/Modern-Treasury/modern-treasury-python/issues/283)) ([8158c02](https://github.com/Modern-Treasury/modern-treasury-python/commit/8158c027980a4a66702efbeb3f91a39bab5db53a))
* **internal:** fix typo in NotGiven docstring ([#282](https://github.com/Modern-Treasury/modern-treasury-python/issues/282)) ([170338f](https://github.com/Modern-Treasury/modern-treasury-python/commit/170338f7ede9f26a3673f9cf04591ccfc53ab906))
* **internal:** improve github devcontainer setup ([#274](https://github.com/Modern-Treasury/modern-treasury-python/issues/274)) ([b3b1b02](https://github.com/Modern-Treasury/modern-treasury-python/commit/b3b1b02cc1fd381179438866a9b248c0d5a764f8))
* **internal:** update type hint for helper function ([#287](https://github.com/Modern-Treasury/modern-treasury-python/issues/287)) ([3bf66fb](https://github.com/Modern-Treasury/modern-treasury-python/commit/3bf66fb826fedf71fe232183b5f784370fcbd97a))


### Documentation

* fix code comment typo ([#284](https://github.com/Modern-Treasury/modern-treasury-python/issues/284)) ([1610591](https://github.com/Modern-Treasury/modern-treasury-python/commit/1610591311027cc3a37678cefa739a294a21f000))
* **readme:** minor updates ([#286](https://github.com/Modern-Treasury/modern-treasury-python/issues/286)) ([aa07685](https://github.com/Modern-Treasury/modern-treasury-python/commit/aa07685d621bf4afb6ce68a9a61bfa9669a75f2f))
* reword package description ([#277](https://github.com/Modern-Treasury/modern-treasury-python/issues/277)) ([20cfecc](https://github.com/Modern-Treasury/modern-treasury-python/commit/20cfeccc1516c2bc4af2faa3a6ec653ec12ce47f))

## 1.21.0 (2023-11-07)

Full Changelog: [v1.20.0...v1.21.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.20.0...v1.21.0)

### Features

* **client:** allow binary returns ([#261](https://github.com/Modern-Treasury/modern-treasury-python/issues/261)) ([3cdcc11](https://github.com/Modern-Treasury/modern-treasury-python/commit/3cdcc11f012b4185a237775297e2bdfa3ea51497))
* **client:** support passing BaseModels to request params at runtime ([#263](https://github.com/Modern-Treasury/modern-treasury-python/issues/263)) ([b5f251f](https://github.com/Modern-Treasury/modern-treasury-python/commit/b5f251f185ee6ac1b3dfb7eed1512dbe63c2103f))
* **client:** support passing httpx.Timeout to method timeout argument ([#269](https://github.com/Modern-Treasury/modern-treasury-python/issues/269)) ([b8bbd4f](https://github.com/Modern-Treasury/modern-treasury-python/commit/b8bbd4f49f4dedb1155604e9cae22a8fa208d629))


### Bug Fixes

* **binaries:** don't synchronously block in astream_to_file ([#264](https://github.com/Modern-Treasury/modern-treasury-python/issues/264)) ([a6cc7ee](https://github.com/Modern-Treasury/modern-treasury-python/commit/a6cc7ee2a495117939e57e748bc02dcabdadd0f3))
* prevent TypeError in Python 3.8 (ABC is not subscriptable) ([#268](https://github.com/Modern-Treasury/modern-treasury-python/issues/268)) ([763a9d4](https://github.com/Modern-Treasury/modern-treasury-python/commit/763a9d4d0be2476e43779fe643d9e26ab84241c4))


### Chores

* **docs:** fix github links ([#271](https://github.com/Modern-Treasury/modern-treasury-python/issues/271)) ([3b9cd0c](https://github.com/Modern-Treasury/modern-treasury-python/commit/3b9cd0c7a2cad462705666f06aebc3345228ff37))
* **internal:** fix some typos ([#270](https://github.com/Modern-Treasury/modern-treasury-python/issues/270)) ([fba0a65](https://github.com/Modern-Treasury/modern-treasury-python/commit/fba0a651e6c3ae6e67bfb7e0a824b46370787cbb))
* **internal:** remove unused int/float conversion ([#266](https://github.com/Modern-Treasury/modern-treasury-python/issues/266)) ([b419653](https://github.com/Modern-Treasury/modern-treasury-python/commit/b41965318bdcb2172345f9a062637fde806665fc))


### Documentation

* **api:** improve method signatures for named path params ([#265](https://github.com/Modern-Treasury/modern-treasury-python/issues/265)) ([bf4006c](https://github.com/Modern-Treasury/modern-treasury-python/commit/bf4006ccb4be551e272487b3d888656132fde54c))
* **readme:** improve example snippets ([#267](https://github.com/Modern-Treasury/modern-treasury-python/issues/267)) ([fbf4205](https://github.com/Modern-Treasury/modern-treasury-python/commit/fbf4205a0220192b005e7f47225de8f4a897a20f))

## 1.20.0 (2023-10-31)

Full Changelog: [v1.19.0...v1.20.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.19.0...v1.20.0)

### Features

* **api:** updates ([#253](https://github.com/Modern-Treasury/modern-treasury-python/issues/253)) ([b94afc8](https://github.com/Modern-Treasury/modern-treasury-python/commit/b94afc87b2f474093dbead5946a7a93af18f41af))
* **client:** support accessing raw response objects ([#256](https://github.com/Modern-Treasury/modern-treasury-python/issues/256)) ([a8cc529](https://github.com/Modern-Treasury/modern-treasury-python/commit/a8cc5299938a555420c7684731346fb50ce716ed))
* **github:** include a devcontainer setup ([#260](https://github.com/Modern-Treasury/modern-treasury-python/issues/260)) ([840d376](https://github.com/Modern-Treasury/modern-treasury-python/commit/840d3762955a22fcd20c03fa9f9cdccceffbf7a4))
* **package:** add classifiers ([#259](https://github.com/Modern-Treasury/modern-treasury-python/issues/259)) ([a16d816](https://github.com/Modern-Treasury/modern-treasury-python/commit/a16d816ef5e56de0e78fc5011b73c5058cb4c0a9))


### Chores

* **docs:** remove old migration guide ([#251](https://github.com/Modern-Treasury/modern-treasury-python/issues/251)) ([ecb2c32](https://github.com/Modern-Treasury/modern-treasury-python/commit/ecb2c323bd24eeb6700313559df548b1aa802932))
* **internal:** minor restructuring of base client ([#258](https://github.com/Modern-Treasury/modern-treasury-python/issues/258)) ([8a0a728](https://github.com/Modern-Treasury/modern-treasury-python/commit/8a0a7284348d6e1da94d1b98054619e04c1078d4))
* **internal:** minor type reference restructuring ([#252](https://github.com/Modern-Treasury/modern-treasury-python/issues/252)) ([8a0a010](https://github.com/Modern-Treasury/modern-treasury-python/commit/8a0a0102df19ee984ff55e9f97488975638f31d7))
* **internal:** require explicit overrides ([#255](https://github.com/Modern-Treasury/modern-treasury-python/issues/255)) ([ed9dd52](https://github.com/Modern-Treasury/modern-treasury-python/commit/ed9dd52587b7f68f9be88149f68af3df16008426))


### Documentation

* improve to dictionary example ([#250](https://github.com/Modern-Treasury/modern-treasury-python/issues/250)) ([a7d0f8d](https://github.com/Modern-Treasury/modern-treasury-python/commit/a7d0f8d0b8218d60370c03637e37ddbc58e898da))

## 1.19.0 (2023-10-24)

Full Changelog: [v1.18.0...v1.19.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.18.0...v1.19.0)

### Features

* **api:** updates ([#245](https://github.com/Modern-Treasury/modern-treasury-python/issues/245)) ([d2c3b80](https://github.com/Modern-Treasury/modern-treasury-python/commit/d2c3b806ff61d56c91cbdb8c65c3e9fff2efaf27))
* **client:** add logging setup ([#224](https://github.com/Modern-Treasury/modern-treasury-python/issues/224)) ([4a540b5](https://github.com/Modern-Treasury/modern-treasury-python/commit/4a540b505b58eac686c35766261ace9ad17e3382))
* **client:** add support for passing in a httpx client ([#220](https://github.com/Modern-Treasury/modern-treasury-python/issues/220)) ([16b9d40](https://github.com/Modern-Treasury/modern-treasury-python/commit/16b9d40e40f20cea1884e1c81bea985e0c6be8ee))
* **client:** adjust retry behavior to be exponential backoff ([#247](https://github.com/Modern-Treasury/modern-treasury-python/issues/247)) ([7dcfdd8](https://github.com/Modern-Treasury/modern-treasury-python/commit/7dcfdd8b38cc719f68df63ec62ba7acae602918d))
* **client:** improve file upload types ([#246](https://github.com/Modern-Treasury/modern-treasury-python/issues/246)) ([a192dee](https://github.com/Modern-Treasury/modern-treasury-python/commit/a192dee8333405765ffc379775d4e367f95f3419))
* **client:** support passing httpx.URL instances to base_url ([#237](https://github.com/Modern-Treasury/modern-treasury-python/issues/237)) ([802e85e](https://github.com/Modern-Treasury/modern-treasury-python/commit/802e85e523db5d2e0d94f1db5085c0c1d1d350d8))
* make webhook headers case insensitive ([#227](https://github.com/Modern-Treasury/modern-treasury-python/issues/227)) ([6baf034](https://github.com/Modern-Treasury/modern-treasury-python/commit/6baf034ce21595a756ccd505e49252c1ad639562))
* **types:** consolidate direction enums into a shared TransactionDirection type ([#231](https://github.com/Modern-Treasury/modern-treasury-python/issues/231)) ([7e9ec69](https://github.com/Modern-Treasury/modern-treasury-python/commit/7e9ec69ebcbbb20913b9a4b1ef9624daa9adabf2))


### Bug Fixes

* **api:** use date-time for effective_at ([#242](https://github.com/Modern-Treasury/modern-treasury-python/issues/242)) ([e128e73](https://github.com/Modern-Treasury/modern-treasury-python/commit/e128e73881e0084d5c177d477c8e2d3ab5d68136))
* **client:** accept io.IOBase instances in file params ([#232](https://github.com/Modern-Treasury/modern-treasury-python/issues/232)) ([fb6de07](https://github.com/Modern-Treasury/modern-treasury-python/commit/fb6de0731518256b6b87ee015504c226699e4a6c))
* **client:** correctly handle arguments with env vars ([#225](https://github.com/Modern-Treasury/modern-treasury-python/issues/225)) ([c62c991](https://github.com/Modern-Treasury/modern-treasury-python/commit/c62c991d4df056a12015d852071728f6d6fd3def))


### Chores

* **internal:** bump mypy ([#244](https://github.com/Modern-Treasury/modern-treasury-python/issues/244)) ([9e6ed39](https://github.com/Modern-Treasury/modern-treasury-python/commit/9e6ed39bc925e7365f31c829ab4e28b90803a4ec))
* **internal:** bump pyright ([#243](https://github.com/Modern-Treasury/modern-treasury-python/issues/243)) ([165f298](https://github.com/Modern-Treasury/modern-treasury-python/commit/165f29833a2e267fc213116097a91a72800d22f6))
* **internal:** cleanup some redundant code ([#230](https://github.com/Modern-Treasury/modern-treasury-python/issues/230)) ([30ca9ed](https://github.com/Modern-Treasury/modern-treasury-python/commit/30ca9edcfa3ed9f877c744c5a5535b7f6d1d37d6))
* **internal:** enable lint rule ([#229](https://github.com/Modern-Treasury/modern-treasury-python/issues/229)) ([c5ee67d](https://github.com/Modern-Treasury/modern-treasury-python/commit/c5ee67d16f097bbc60343ff9c5ec7ffc2e1a7a51))
* **internal:** improve publish script ([#236](https://github.com/Modern-Treasury/modern-treasury-python/issues/236)) ([50bd455](https://github.com/Modern-Treasury/modern-treasury-python/commit/50bd4551d9dd835f2be9c843065c9496f383b1e8))
* **internal:** migrate from Poetry to Rye ([#235](https://github.com/Modern-Treasury/modern-treasury-python/issues/235)) ([4ba80bb](https://github.com/Modern-Treasury/modern-treasury-python/commit/4ba80bb792d5ade9ae74023775befab628e46c49))
* **internal:** update gitignore ([#239](https://github.com/Modern-Treasury/modern-treasury-python/issues/239)) ([b2e34d5](https://github.com/Modern-Treasury/modern-treasury-python/commit/b2e34d5b143aca1e74f027ec57a00e9f7f1ec484))
* **internal:** update gitignore ([#240](https://github.com/Modern-Treasury/modern-treasury-python/issues/240)) ([ae8b3c4](https://github.com/Modern-Treasury/modern-treasury-python/commit/ae8b3c42170416a4881d0f70f7a6cf4a610f7a94))
* **internal:** update lock file ([#238](https://github.com/Modern-Treasury/modern-treasury-python/issues/238)) ([bb60a6a](https://github.com/Modern-Treasury/modern-treasury-python/commit/bb60a6aa3ad6d5644041a512c907352ccb41052f))
* update comment ([#228](https://github.com/Modern-Treasury/modern-treasury-python/issues/228)) ([8b3e213](https://github.com/Modern-Treasury/modern-treasury-python/commit/8b3e213d54dbe2c4df52e09c4d4a8a3d394f4596))
* update README ([#222](https://github.com/Modern-Treasury/modern-treasury-python/issues/222)) ([384203f](https://github.com/Modern-Treasury/modern-treasury-python/commit/384203f9264ac7a1030b8ab340f885f8d3d2253f))


### Documentation

* improve error message for invalid file param type ([#234](https://github.com/Modern-Treasury/modern-treasury-python/issues/234)) ([1fecd4c](https://github.com/Modern-Treasury/modern-treasury-python/commit/1fecd4c82d39193ae635450f3d8b009b4d50162c))
* organisation -&gt; organization (UK to US English) ([#233](https://github.com/Modern-Treasury/modern-treasury-python/issues/233)) ([7fb749a](https://github.com/Modern-Treasury/modern-treasury-python/commit/7fb749aa52ac070d258de9c68f763246c5c92b0c))


### Refactors

* **test:** refactor authentication tests ([#223](https://github.com/Modern-Treasury/modern-treasury-python/issues/223)) ([dd134aa](https://github.com/Modern-Treasury/modern-treasury-python/commit/dd134aa67592ad0e30497df2fa9b6f847c6e9470))

## 1.18.0 (2023-10-09)

Full Changelog: [v1.17.1...v1.18.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.17.1...v1.18.0)

### Features

* **client:** add forwards-compatible pydantic methods ([#219](https://github.com/Modern-Treasury/modern-treasury-python/issues/219)) ([b1a9311](https://github.com/Modern-Treasury/modern-treasury-python/commit/b1a9311cb2ab79dc3698124ea69d84582ec12bb1))
* **client:** handle retry-after header with a date format ([#216](https://github.com/Modern-Treasury/modern-treasury-python/issues/216)) ([947a747](https://github.com/Modern-Treasury/modern-treasury-python/commit/947a7477b9c5c3d932c0622d4ec366ba2f079c90))

## 1.17.1 (2023-10-02)

Full Changelog: [v1.17.0...v1.17.1](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.17.0...v1.17.1)

### Chores

* **tests:** improve raw response test ([#214](https://github.com/Modern-Treasury/modern-treasury-python/issues/214)) ([456480a](https://github.com/Modern-Treasury/modern-treasury-python/commit/456480ace69584a28c68c899520504e85e323975))

## 1.17.0 (2023-09-25)

Full Changelog: [v1.16.0...v1.17.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.16.0...v1.17.0)

### Features

* **api:** updates ([#209](https://github.com/Modern-Treasury/modern-treasury-python/issues/209)) ([27fc6bf](https://github.com/Modern-Treasury/modern-treasury-python/commit/27fc6bfbfd34d54888563cc2351118ffab64fa33))
* **package:** export a root error type ([#212](https://github.com/Modern-Treasury/modern-treasury-python/issues/212)) ([73bf24d](https://github.com/Modern-Treasury/modern-treasury-python/commit/73bf24d1cd0429cbbf4117c38633cc9b3951f173))


### Bug Fixes

* **client:** don't error by default for unexpected content types ([#210](https://github.com/Modern-Treasury/modern-treasury-python/issues/210)) ([0762e5f](https://github.com/Modern-Treasury/modern-treasury-python/commit/0762e5f9f298a244da024c36e66ccf8658c5ccfc))
* **client:** properly configure model set fields ([#205](https://github.com/Modern-Treasury/modern-treasury-python/issues/205)) ([2f8c907](https://github.com/Modern-Treasury/modern-treasury-python/commit/2f8c907591ae43e92f194e71964de3a58178d27c))


### Chores

* **internal:** add helpers ([#206](https://github.com/Modern-Treasury/modern-treasury-python/issues/206)) ([adedb5e](https://github.com/Modern-Treasury/modern-treasury-python/commit/adedb5e0a9bf645cdee5c3ec1be430a729c42853))
* **internal:** move error classes from _base_exceptions to _exceptions (⚠️ breaking) ([#211](https://github.com/Modern-Treasury/modern-treasury-python/issues/211)) ([f252a33](https://github.com/Modern-Treasury/modern-treasury-python/commit/f252a333dce04b58f212c31b42b7fa03b449b3e8))


### Documentation

* add some missing inline documentation ([#202](https://github.com/Modern-Treasury/modern-treasury-python/issues/202)) ([37804de](https://github.com/Modern-Treasury/modern-treasury-python/commit/37804de665eb98bdf7c706b6d8394c2ed9be5598))

## 1.16.0 (2023-09-11)

Full Changelog: [v1.15.0...v1.16.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.15.0...v1.16.0)

### Features

* fixes tests where an array has to have unique enum values ([#196](https://github.com/Modern-Treasury/modern-treasury-python/issues/196)) ([1e582ba](https://github.com/Modern-Treasury/modern-treasury-python/commit/1e582baa5782a61f757d4a9060f15209ba14c081))


### Bug Fixes

* **client:** properly handle optional file params ([#194](https://github.com/Modern-Treasury/modern-treasury-python/issues/194)) ([08db5c4](https://github.com/Modern-Treasury/modern-treasury-python/commit/08db5c435d42eb86bf7e7dc1f6c9239164c2cdef))


### Chores

* **internal:** minor update ([#198](https://github.com/Modern-Treasury/modern-treasury-python/issues/198)) ([2372dd7](https://github.com/Modern-Treasury/modern-treasury-python/commit/2372dd7dfcbb152e8b08bed89c99eeb16247fbd0))
* **internal:** update base client ([#197](https://github.com/Modern-Treasury/modern-treasury-python/issues/197)) ([f8969c8](https://github.com/Modern-Treasury/modern-treasury-python/commit/f8969c8f7f21d629864e08b33986cb774a2657b5))
* **internal:** update pyright ([#201](https://github.com/Modern-Treasury/modern-treasury-python/issues/201)) ([087470d](https://github.com/Modern-Treasury/modern-treasury-python/commit/087470dbeda6205a6012d3e8ddfa3b03d74ad7b2))
* **internal:** updates ([#200](https://github.com/Modern-Treasury/modern-treasury-python/issues/200)) ([5c940e0](https://github.com/Modern-Treasury/modern-treasury-python/commit/5c940e01787e6218769823908cf20c6627b645e7))


### Documentation

* **readme:** add link to api.md ([#199](https://github.com/Modern-Treasury/modern-treasury-python/issues/199)) ([bd499a1](https://github.com/Modern-Treasury/modern-treasury-python/commit/bd499a10002e3ae158e70f6221b94eacb9472d1d))

## 1.15.0 (2023-09-01)

Full Changelog: [v1.14.0...v1.15.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.14.0...v1.15.0)

### Features

* add support for Pydantic v2 ([#181](https://github.com/Modern-Treasury/modern-treasury-python/issues/181)) ([85709bb](https://github.com/Modern-Treasury/modern-treasury-python/commit/85709bbf02d619c3f3ee77164b3519fbc2caf14e))


### Chores

* **ci:** setup workflows to create releases and release PRs ([#186](https://github.com/Modern-Treasury/modern-treasury-python/issues/186)) ([2897c74](https://github.com/Modern-Treasury/modern-treasury-python/commit/2897c74b8a53b9ae2256cdde7204faecbca75dc8))
* **internal:** add `pydantic.generics` import for compatibility ([#189](https://github.com/Modern-Treasury/modern-treasury-python/issues/189)) ([4eb74d8](https://github.com/Modern-Treasury/modern-treasury-python/commit/4eb74d84c6530aac2e94db644d166a7f21a6f689))
* **internal:** bump pydantic dep ([#183](https://github.com/Modern-Treasury/modern-treasury-python/issues/183)) ([039e10e](https://github.com/Modern-Treasury/modern-treasury-python/commit/039e10efdbf08e8c0e37f64c86d7d0524b7dba65))
* **internal:** minor formatting changes ([#193](https://github.com/Modern-Treasury/modern-treasury-python/issues/193)) ([7f0aba8](https://github.com/Modern-Treasury/modern-treasury-python/commit/7f0aba8e493cd2bae08dae8e5380e67c9eb9693b))
* **internal:** minor restructuring ([#191](https://github.com/Modern-Treasury/modern-treasury-python/issues/191)) ([ea1703d](https://github.com/Modern-Treasury/modern-treasury-python/commit/ea1703d25df908945fb02a0f13b9490394cd99ae))
* **internal:** update anyio ([#184](https://github.com/Modern-Treasury/modern-treasury-python/issues/184)) ([aad6ac7](https://github.com/Modern-Treasury/modern-treasury-python/commit/aad6ac7752700cdc8efe255d45be642e93b770d0))
* **internal:** use shared params references ([#188](https://github.com/Modern-Treasury/modern-treasury-python/issues/188)) ([6188ec5](https://github.com/Modern-Treasury/modern-treasury-python/commit/6188ec57f83ea49d4d5c8717ad2684232c031923))


### Documentation

* **readme:** reference pydantic helpers ([#192](https://github.com/Modern-Treasury/modern-treasury-python/issues/192)) ([08abce9](https://github.com/Modern-Treasury/modern-treasury-python/commit/08abce9073badb359b082608721e8f14e007f105))

## [1.14.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.13.0...v1.14.0) (2023-08-15)


### Features

* allow a default timeout to be set for clients ([#176](https://github.com/Modern-Treasury/modern-treasury-python/issues/176)) ([1798742](https://github.com/Modern-Treasury/modern-treasury-python/commit/17987428b3be710b854e96967e3ebdbf42afa10e))
* **api:** add `metadata` in several places it was missing; add `description` ([#163](https://github.com/Modern-Treasury/modern-treasury-python/issues/163)) ([8f5f131](https://github.com/Modern-Treasury/modern-treasury-python/commit/8f5f1314bd321742d971321cda1f01c6d37ff6b0))
* **api:** support multiple `id`s in `ledger` `retrieve`/`list` endpoints ([#174](https://github.com/Modern-Treasury/modern-treasury-python/issues/174)) ([a6939c6](https://github.com/Modern-Treasury/modern-treasury-python/commit/a6939c604b57cc90b5308515e6cf4443f2411979))
* **api:** updates ([#166](https://github.com/Modern-Treasury/modern-treasury-python/issues/166)) ([8d5c102](https://github.com/Modern-Treasury/modern-treasury-python/commit/8d5c102ad3d3e203302c8a19e2ddc56a472693c0))


### Bug Fixes

* **client:** fix array query param serialization ([#175](https://github.com/Modern-Treasury/modern-treasury-python/issues/175)) ([7509dfe](https://github.com/Modern-Treasury/modern-treasury-python/commit/7509dfe1501036ea068f351080f9da2a7da28f61))


### Documentation

* **readme:** remove beta status + document versioning policy ([#167](https://github.com/Modern-Treasury/modern-treasury-python/issues/167)) ([cbc1bf8](https://github.com/Modern-Treasury/modern-treasury-python/commit/cbc1bf8b98031165814f72d56ca2dc275927a256))


### Styles

* prefer importing types directly instead of module names ([#177](https://github.com/Modern-Treasury/modern-treasury-python/issues/177)) ([00094f7](https://github.com/Modern-Treasury/modern-treasury-python/commit/00094f704cfb56c0a80689123be02ddabfc9eea0))


### Chores

* assign default reviewers to release PRs ([#178](https://github.com/Modern-Treasury/modern-treasury-python/issues/178)) ([9e5c3a1](https://github.com/Modern-Treasury/modern-treasury-python/commit/9e5c3a1932b56761d48c6c24bf6c60889ebdd448))
* **deps:** bump typing-extensions to 4.5 ([#172](https://github.com/Modern-Treasury/modern-treasury-python/issues/172)) ([5f2d470](https://github.com/Modern-Treasury/modern-treasury-python/commit/5f2d4706ad46d4ab321dd0b64b09d8eb69e8e4d6))
* **internal/deps:** update lock file ([#171](https://github.com/Modern-Treasury/modern-treasury-python/issues/171)) ([43f0e4f](https://github.com/Modern-Treasury/modern-treasury-python/commit/43f0e4fb307f9c677672fc7c8b7bc556a2c9872d))
* **internal:** bump certifi dependency ([#169](https://github.com/Modern-Treasury/modern-treasury-python/issues/169)) ([a6e48a2](https://github.com/Modern-Treasury/modern-treasury-python/commit/a6e48a24050cf8d83d2916a927947616bd3c7e62))
* **internal:** bump pytest-asyncio ([#173](https://github.com/Modern-Treasury/modern-treasury-python/issues/173)) ([72e1329](https://github.com/Modern-Treasury/modern-treasury-python/commit/72e13293f029b3d9c3d8434b99dbe46096e128b6))
* **internal:** minor formatting change ([#179](https://github.com/Modern-Treasury/modern-treasury-python/issues/179)) ([5ff2fe7](https://github.com/Modern-Treasury/modern-treasury-python/commit/5ff2fe75d2fa6622aa5e2e4a7b8739c49731040a))
* **internal:** minor import restructuring ([#170](https://github.com/Modern-Treasury/modern-treasury-python/issues/170)) ([ebf2ac9](https://github.com/Modern-Treasury/modern-treasury-python/commit/ebf2ac9385e7e027666f2733b2822486a5c56fd8))
* **internal:** update mypy to v1.4.1 ([#165](https://github.com/Modern-Treasury/modern-treasury-python/issues/165)) ([b712b7b](https://github.com/Modern-Treasury/modern-treasury-python/commit/b712b7b4d7d127671ed2dd1ee03bd8d499e4ba29))
* **internal:** update ruff to v0.0.282 ([#168](https://github.com/Modern-Treasury/modern-treasury-python/issues/168)) ([487add7](https://github.com/Modern-Treasury/modern-treasury-python/commit/487add7ea17b2e36f8bdb1a7a4b5bf604e212e93))

## [1.13.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.12.1...v2.0.0) (2023-08-01)


### ⚠ BREAKING CHANGES

* **types:** rename account connection flow to account collection flow ([#150](https://github.com/Modern-Treasury/modern-treasury-python/issues/150))
* **api:** update parameters for virtual account create request ([#148](https://github.com/Modern-Treasury/modern-treasury-python/issues/148))

### Features

* **api:** update parameters for virtual account create request ([#148](https://github.com/Modern-Treasury/modern-treasury-python/issues/148)) ([3425e69](https://github.com/Modern-Treasury/modern-treasury-python/commit/3425e690f5bb0f91fea1ff14439e3552e2f8f55c))
* **api:** updates ([#152](https://github.com/Modern-Treasury/modern-treasury-python/issues/152)) ([742738b](https://github.com/Modern-Treasury/modern-treasury-python/commit/742738b5846b0b8cb1d3b6fb25cbaa0148e03697))
* **api:** updates ([#155](https://github.com/Modern-Treasury/modern-treasury-python/issues/155)) ([f25dc19](https://github.com/Modern-Treasury/modern-treasury-python/commit/f25dc19a8355d4dd76d46a3d4fab05ed511691ba))
* **client:** add client close handlers ([#157](https://github.com/Modern-Treasury/modern-treasury-python/issues/157)) ([c0af2dd](https://github.com/Modern-Treasury/modern-treasury-python/commit/c0af2ddd92823af2c24fe1af6eeac559e4bf9ed4))
* **test:** unskip file uploads tests ([#162](https://github.com/Modern-Treasury/modern-treasury-python/issues/162)) ([d79ce4b](https://github.com/Modern-Treasury/modern-treasury-python/commit/d79ce4b7f2d981e699cf41adaf63243fe9548aa6))


### Bug Fixes

* **api:** add response body to `VirtualAccounts.retrieve()` and update resources ([#146](https://github.com/Modern-Treasury/modern-treasury-python/issues/146)) ([3eaa8e4](https://github.com/Modern-Treasury/modern-treasury-python/commit/3eaa8e4863067787644e6864d3a1776fcddc5cd1))
* **client:** correctly handle environment variable access ([#156](https://github.com/Modern-Treasury/modern-treasury-python/issues/156)) ([81d62ae](https://github.com/Modern-Treasury/modern-treasury-python/commit/81d62ae33834742c0f8384a3b339ffc5289112df))


### Refactors

* **types:** rename account connection flow to account collection flow ([#150](https://github.com/Modern-Treasury/modern-treasury-python/issues/150)) ([907bcf2](https://github.com/Modern-Treasury/modern-treasury-python/commit/907bcf2d54454aa48f6835b70d54654d88eecf18))


### Documentation

* **readme:** reference "client" in errors section and add missing import ([#149](https://github.com/Modern-Treasury/modern-treasury-python/issues/149)) ([cef699a](https://github.com/Modern-Treasury/modern-treasury-python/commit/cef699aff03f14453a6b1f0a8b6f26f93c39cbfc))
* **readme:** use `client` everywhere for consistency ([#154](https://github.com/Modern-Treasury/modern-treasury-python/issues/154)) ([ca1a571](https://github.com/Modern-Treasury/modern-treasury-python/commit/ca1a571abbc45f30dd1fa0df49874edd2557613e))


### Chores

* **internal:** add `codegen.log` to `.gitignore` ([#147](https://github.com/Modern-Treasury/modern-treasury-python/issues/147)) ([a710e9f](https://github.com/Modern-Treasury/modern-treasury-python/commit/a710e9f8225078b196427e26b88e0e0705c92d6d))
* **internal:** bump pyright ([#160](https://github.com/Modern-Treasury/modern-treasury-python/issues/160)) ([dc18763](https://github.com/Modern-Treasury/modern-treasury-python/commit/dc1876330cafc4bba545c10622836603e1107240))
* **internal:** bump pyright ([#161](https://github.com/Modern-Treasury/modern-treasury-python/issues/161)) ([68e8e73](https://github.com/Modern-Treasury/modern-treasury-python/commit/68e8e732d44630279950f65b47c9d3094cf0ccde))
* **internal:** make demo example runnable and more portable ([#159](https://github.com/Modern-Treasury/modern-treasury-python/issues/159)) ([91a9f15](https://github.com/Modern-Treasury/modern-treasury-python/commit/91a9f1561548311f2c8298e739a056ba9658a698))
* **internal:** minor reformatting of code ([#158](https://github.com/Modern-Treasury/modern-treasury-python/issues/158)) ([e39e033](https://github.com/Modern-Treasury/modern-treasury-python/commit/e39e0331d3b3d27d3b5d5ddd1956fad87fa609e6))
* **package:** pin major versions of dependencies ([#144](https://github.com/Modern-Treasury/modern-treasury-python/issues/144)) ([f248913](https://github.com/Modern-Treasury/modern-treasury-python/commit/f248913b7dc4fe90f02dc2818f5a2fcf97bd0f7d))

## [1.12.1](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.12.0...v1.12.1) (2023-07-08)


### Bug Fixes

* **deps:** pin pydantic to less than v2.0 ([#139](https://github.com/Modern-Treasury/modern-treasury-python/issues/139)) ([34535f4](https://github.com/Modern-Treasury/modern-treasury-python/commit/34535f484d614f9ddee3941ba958961c03029197))


### Chores

* **internal:** update lock file ([#141](https://github.com/Modern-Treasury/modern-treasury-python/issues/141)) ([2f66b2f](https://github.com/Modern-Treasury/modern-treasury-python/commit/2f66b2f6fae04b42fde7ba1a12bab336bd325142))
* **package:** pin major versions of dependencies ([#143](https://github.com/Modern-Treasury/modern-treasury-python/issues/143)) ([d606e35](https://github.com/Modern-Treasury/modern-treasury-python/commit/d606e3575836af5bc7a1dbfc9b242b045b31d29e))

## [1.12.0](https://github.com/Modern-Treasury/modern-treasury-python/compare/v1.11.0...v1.11.1) (2023-06-30)

### Refactor!
* move some positional params to named params + updates ([#131](https://github.com/Modern-Treasury/modern-treasury-python/pull/131))

### Docs
* point to github repo instead of email contact ([#129](https://github.com/Modern-Treasury/modern-treasury-python/pull/129)) 
* slight improvement to file uploads example ([#127](https://github.com/Modern-Treasury/modern-treasury-python/pull/127))
* minor restructuring ([#136](https://github.com/Modern-Treasury/modern-treasury-python/pull/136))
* add trailing newlines ([#134] (https://github.com/Modern-Treasury/modern-treasury-python/pull/134))
* minor reordering of types and properties ([#135](https://github.com/Modern-Treasury/modern-treasury-python/pull/135))


### Features
* always document positional arguments & options arguments ([#124](https://github.com/Modern-Treasury/modern-treasury-python/pull/124))
* add support for current_return property ([#118](https://github.com/Modern-Treasury/modern-treasury-python/pull/118))
* add 0C, 0N & 0S to payment order subtype ([#117](https://github.com/Modern-Treasury/modern-treasury-python/pull/117))
### Fix 
* properly separate query and body params ([#126](https://github.com/Modern-Treasury/modern-treasury-python/pull/126))
* small improvement to handling server-sent events ([#120](https://github.com/Modern-Treasury/modern-treasury-python/pull/120))

### CI
* update release config ([#128](https://github.com/Modern-Treasury/modern-treasury-python/pull/128))

### Chores

* add overloads to client.get for streaming ([#130](https://github.com/Modern-Treasury/modern-treasury-python/issues/114)) 
* improve internal test helper ([#125](https://github.com/Modern-Treasury/modern-treasury-python/pull/125))
* restructure core streaming implementation ([#123](https://github.com/Modern-Treasury/modern-treasury-python/pull/123))
* add empty request preparation method ([#122](https://github.com/Modern-Treasury/modern-treasury-python/pull/122))
* minor formatting change ([#121](https://github.com/Modern-Treasury/modern-treasury-python/pull/121))
* update lock file ([#119](https://github.com/Modern-Treasury/modern-treasury-python/pull/119))
* add tests for base url handling ([#116](https://github.com/Modern-Treasury/modern-treasury-python/pull/116))
* configure automatic releases + sync latest changes  ([#113](https://github.com/Modern-Treasury/modern-treasury-python/pull/113))
* update certifi ([#133](https://github.com/Modern-Treasury/modern-treasury-python/pull/133))
