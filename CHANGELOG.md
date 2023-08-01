# Changelog

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
