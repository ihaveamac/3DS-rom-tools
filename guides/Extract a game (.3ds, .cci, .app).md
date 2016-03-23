# Extract a game's contents (.3ds, .cci, .app)
This guide explains how you can extract the contents out of a game, decrypted or using XORpads.

## Requirements
* A decrypted game (use "Decrypt a game using a 3DS"), the more preferable option
  **or** XORpads for a rom (use "Generating XORpads for a 3ds/cxi" (WIP))
* [ctrtool](https://github.com/profi200/Project_CTR/releases)
  If you are not using a 64-bit operating system, you must build the source yourself for now.
* [3dstool](https://github.com/dnasdw/3dstool/releases), required if using XORpads
  If you are not using Windows, you must build the source yourself for now.
* Basic knowledge of the Terminal/Command Line

## Useful notes
* NCCH partitions of a rom

    Partition | Use | Type
    --- | --- | ---
    0 | Game Executable | CXI
    1 | Manual | CFA
    2 | Download Play Child container | CFA
    6 | New3DS Update Data | CFA
    7 | Old3DS Update Data | CFA

## Method 1 - Decrypted game with ctrtool
1. Put your rom in its own folder.
2. Extract the contents of the rom. For example, to extract the ExeFS and RomFS to directories from first NCCH partition:

    ```bash
    ctrtool -n 0 --exefsdir=exefs --romfsdir=romfs game.3ds
    ```

    Explanation of possible arguments:
    * `-n part` or `--ncch=part` - NCCH partition to use (use the table above), required
    * `--exheader=file` - File to save the Extended Header to
    * `--logo=file` - File to save the Logo to
    * `--plainrgn=file` - File to save the Plain region to
    * `--exefs=file` - File to save the ExeFS to
    * `--exefsdir=dir` - Directory to save the ExeFS contents to
    * `--romfs=file` - File to save the RomFS to
    * `--romfsdir=dir` - Directory to save the RomFS contents to
    * `--listromfs` - List RomFS contents

## Method 2 - Decrypted game with 3dstool
*Work in progress*

## Method 2 - XORpads with 3dstool
*Work in progress*