# 3DS-rom-stuff

some stuff when doing things with Nintendo 3DS games and applications (.3ds/.cci, .cia)

* `ncchinfo_gen.py` - generates `ncchinfo.bin`, which will generate XORpads for a game's ExHeader/ExeFS/RomFS on a 3DS console
* `ncchinfo_gen_exefs.py` - generates `ncchinfo.bin` which will only generate XORpads for a rom's ExeFS
* `rsfgen.py` - generates a .rsf, using a .3ds/.cci, decrypted exheader, and a template rsf ([original source](https://gbatemp.net/threads/release-exinjector-inject-original-exheaders-into-repacked-roms.373839/page-16#post-5298180))
* `rsfgen-norom.py` - modified rsfgen, generates a .rsf only using decrypted exheader and a template rsf, does not automatically get CompanyCode, ProductCode, or UniqueId
* `dummy.rsf` - a template rsf for use with rsfgen; must have DOS line endings (CR LF, try unix2dos if your generated rsf looks strange) ([original source](https://gist.github.com/mid-kid/d9c4ce50407c71ec9ef3))