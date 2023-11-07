# Changelog

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
