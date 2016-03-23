# Decrypt a game on a 3DS console
This guide explains how you can decrypt a game's contents so you can extract its files on a computer.

## Requirements
* A 3DS system with one of the following:
    * Firmware version <=9.2.0-X, and access to homebrew
    * arm9loaderhax installed
* Decrypt9WIP by d0k3: https://github.com/d0k3/Decrypt9WIP/releases
  See its [README](https://github.com/d0k3/Decrypt9WIP#how-to-run-this--entry-points) on how to set it up.
* Some patience with huge games

## Setting up
1. Get the latest release of Decrypt9WIP.
2. Make two folders at the root of the SD card: `D9Game` and `Decrypt9`
3. Get these keys and place them at the root or `/Decrypt9` (you can find them online):
    - `slot0x25KeyX.bin` 7.x NCCH
        - Needed for decrypting Secure2 on Old3DS <7.0 or arm9loaderhax
        - MD5: 817fd1bffba60f79cf8cdf19caf28923
    - `slot0x18KeyX.bin` - New3DS 9.3 NCCH
        - Needed for decrypting Secure3 for some New3DS exclusive titles on Old3DS or arm9loaderhax
        - MD5: 32ae55444f3feca802a6ed251a619bc7
    - `slot0x1BKeyX.bin` - New3DS 9.6 NCCH
        - Needed for decrypting Secure4 for some New3DS exclusive titles in all cases
        - MD5: 79cd40405d0f5417ae73a064318cbf0d
    - `seeddb.bin` - 9.6 digital game/application encryption
        - Needed for digital/CIA games
        - Contains game-specific seeds
        - [SEEDDB Title List](http://pastebin.com/zNM8zYwa)

## Decrypting
1. Place your games (.3ds, .cci, .app, .cia) in `/D9Game`.
2. Enter Decrypt9 using one of the various entry points.
3. Choose "Game Decryptor Options".
4. Choose "NCCH/NCSD Decryptor" (.3ds, .cci, .app), or "CIA Decryptor (deep)" (.cia).
5. Wait for the process to finish.
6. Your games should now be decrypted and usable on a computer.

## Common Errors
`/Decrypt9/Decrypt9.log` can contain errors that might have happened decrypting games.
- "7.x crypto will fail on O3DS < 7.x or A9LH", "Secure3 crypto will fail", "Secure4 crypto will fail"
    - You need the appropriate key above.
- *More will be added here...*