# 3DS ROM Tools
Tools and guides for working with Nintendo 3DS games and applications (.3ds/.cci, .cia)

There exist some work-in-progress guides at this repository's Wiki: https://github.com/ihaveamac/3DS-rom-stuff/wiki

## NCCHInfo generation - `/ncchinfo_gen`
* `ncchinfo_gen.py` - generates `ncchinfo.bin`, which will generate XORpads for a game's ExHeader/ExeFS/RomFS on a 3DS console ([original source](https://github.com/d0k3/Decrypt9WIP/blob/2935c881f436cc940f44a9455c2ae63aff1744d8/scripts/ncchinfo_gen.py))
* `ncchinfo_gen_exefs.py` - generates `ncchinfo.bin` which will only generate XORpads for a rom's ExeFS
* `ncchinfo_gen_exheader.py` - generates `ncchinfo.bin` which will only generate XORpads for a rom's ExHeader

## RSF generation - `/rsfgen`
* `rsfgen.py` - generates a .rsf, using a .3ds/.cci, decrypted exheader, and a template rsf ([original source](https://gbatemp.net/threads/release-exinjector-inject-original-exheaders-into-repacked-roms.373839/page-16#post-5298180))
* `rsfgen_cia.py` - modified rsfgen, generates a .rsf, using a decrypted .cia and a template rsf
* `rsfgen_norom.py` - modified rsfgen, generates a .rsf only using decrypted exheader and a template rsf, does not automatically get CompanyCode, ProductCode, or UniqueId
* `dummy.rsf` - a template rsf for use with rsfgen; must have DOS line endings (CR LF, try unix2dos if your generated rsf looks strange) ([original source](https://gist.github.com/mid-kid/d9c4ce50407c71ec9ef3))
