#!/usr/bin/env python
import struct
import binascii
import sys
import argparse

# Set up the CLI parser and generate help
parser = argparse.ArgumentParser(description='RSF file generator for 3DS exheader manipulation')
parser.add_argument('-r', '--rom',
	help='3DS rom file', metavar='FILE', required=True, nargs=1)
parser.add_argument('-e', '--exheader',
	help='decrypted exheader.bin file', metavar='FILE', required=True, nargs=1)
parser.add_argument('-o', '--rsf',
	help='RSF file to use as a template and to write to', metavar='FILE', required=True, nargs=1)
parser.add_argument('-f', '--regionfree',
	help='icon.bin file to apply region free patch', metavar='FILE', nargs=1)
parser.add_argument('-s', '--spoof',
	action='store_true',
	help='apply firmware spoofing')

# Parse the command line for supplied arguments
args = parser.parse_args()

with open(args.rom[0], "rb") as f:
	f.seek(0x1109) # UniqueId
	uid = f.read(4)
	uid = binascii.hexlify(uid)[::-1]
	c = list(uid)
	c[::2], c[1::2] = c[1::2], c[::2]
	uid = "".join(c)
	f.seek(0x1110) # CompanyCode
	read = f.read(2)
	ccode = "".join(struct.unpack('<cc', read))
	f.seek(0x1150) # ProductCode
	read = f.read(10)
	pcode = "".join(struct.unpack('<cccccccccc', read))
	pcode = pcode.rstrip(' \0')
	f.close
	with open(args.exheader[0], "rb") as f:
	
		f.seek(0) # Title
		read = f.read(8)
		title = "".join(struct.unpack('<cccccccc', read))
		title = title.rstrip(' \0')
		
		f.seek(0xE) # Remaster version
		rver = f.read(2)
		rver = (binascii.hexlify(rver))[::-1]
		c = list(rver)
		c[::2], c[1::2] = c[1::2], c[::2]
		rver = "".join(c)
		
		f.seek(0x1C) # Stacksize
		stack = f.read(4)
		stack = (binascii.hexlify(stack))[::-1]
		c = list(stack)
		c[::2], c[1::2] = c[1::2], c[::2]
		stack = "".join(c)
		
		f.seek(0x40) # Dependencies
		dep = range(48)
		for i in range(48):
			dep[i] = f.read(8)
			dep[i] = binascii.hexlify(dep[i])[::-1]
			c = list(dep[i])
			c[::2], c[1::2] = c[1::2], c[::2]
			dep[i] = "".join(c)
		f.seek(0x247) # Uses extended save data access?
		r = f.read(1)
		uext = binascii.hexlify(r)
		if uext == "00":
			f.seek(0x230) # ExtSaveDataId
			exts = f.read(8)
			exts = (binascii.hexlify(exts))[::-1]
			c = list(exts)
			c[::2], c[1::2] = c[1::2], c[::2]
			exts = "".join(c)
			f.seek(0x238) # System save id 1
			ssid1 = f.read(4)
			ssid1 = (binascii.hexlify(ssid1))[::-1]
			c = list(ssid1)
			c[::2], c[1::2] = c[1::2], c[::2]
			ssid1 = "".join(c)
			f.seek(0x23C) # System save id 2
			ssid2 = f.read(4)
			ssid2 = (binascii.hexlify(ssid2))[::-1]
			c = list(ssid2)
			c[::2], c[1::2] = c[1::2], c[::2]
			ssid2 = "".join(c)
			f.seek(0x240) # Other save id 1
			osid1 = f.read(3)
			osid1 = (binascii.hexlify(osid1))[::-1]
			c = list(osid1)
			c[::2], c[1::2] = c[1::2], c[::2]
			osid1 = "".join(c)
			osid1 = osid1[1:]
			f.seek(0x242) # Other save id 2
			osid2 = f.read(3)
			osid2 = (binascii.hexlify(osid2))[::-1]
			c = list(osid2)
			c[::2], c[1::2] = c[1::2], c[::2]
			osid2 = "".join(c)
			osid2 = osid2[:5]
			f.seek(0x245) # Other save id 2
			osid3 = f.read(3)
			osid3 = (binascii.hexlify(osid3))[::-1]
			c = list(osid3)
			c[::2], c[1::2] = c[1::2], c[::2]
			osid3 = "".join(c)
			osid3 = osid3[1:]
		
		if uext == "10":
			f.seek(0x240) # Other save id 1
			esid1 = f.read(3)
			esid1 = (binascii.hexlify(esid1))[::-1]
			c = list(esid1)
			c[::2], c[1::2] = c[1::2], c[::2]
			esid1 = "".join(c)
			esid1 = esid1[1:]
			f.seek(0x242) # Other save id 2
			esid2 = f.read(3)
			esid2 = (binascii.hexlify(esid2))[::-1]
			c = list(esid2)
			c[::2], c[1::2] = c[1::2], c[::2]
			esid2 = "".join(c)
			esid2 = esid2[:5]
			f.seek(0x245) # Other save id 2
			esid3 = f.read(3)
			esid3 = (binascii.hexlify(esid3))[::-1]
			c = list(esid3)
			c[::2], c[1::2] = c[1::2], c[::2]
			esid3 = "".join(c)
			esid3 = esid3[1:]
			
			f.seek(0x230) # Other save id 1
			esid4 = f.read(3)
			esid4 = (binascii.hexlify(esid4))[::-1]
			c = list(esid4)
			c[::2], c[1::2] = c[1::2], c[::2]
			esid4 = "".join(c)
			esid4 = esid4[1:]
			f.seek(0x232) # Other save id 2
			esid5 = f.read(3)
			esid5 = (binascii.hexlify(esid5))[::-1]
			c = list(esid5)
			c[::2], c[1::2] = c[1::2], c[::2]
			esid5 = "".join(c)
			esid5 = esid5[:5]
			f.seek(0x235) # Other save id 2
			esid6 = f.read(3)
			esid6 = (binascii.hexlify(esid6))[::-1]
			c = list(esid6)
			c[::2], c[1::2] = c[1::2], c[::2]
			esid6 = "".join(c)
			esid6 = esid6[1:]
			
		
		f.seek(0x248) # Access control FileSystemAccess
		r = f.read(6)
		c = (binascii.hexlify(r))
		c = list(c)
		c[::2], c[1::2] = c[1::2], c[::2]
		fsaccess=["#"] * 21
		if c[0] == "1":
			fsaccess[0] = "-"
		if c[0] == "2":
			fsaccess[1] = "-"
		if c[0] == "4":
			fsaccess[2] = "-"
		if c[0] == "8":
			fsaccess[3] = "-"
		if c[1] == "1":
			fsaccess[4] = "-"
		if c[1] == "2":
			fsaccess[5] = "-"
		if c[1] == "4":
			fsaccess[6] = "-"
		if c[1] == "8":
			fsaccess[7] = "-"
		if c[2] == "1":
			fsaccess[8] = "-"
		if c[2] == "2":
			fsaccess[9] = "-"
		if c[2] == "4":
			fsaccess[10] = "-"
		if c[2] == "8":
			fsaccess[11] = "-"
		if c[3] == "1":
			fsaccess[12] = "-"
		if c[3] == "2":
			fsaccess[13] = "-"
		if c[3] == "4":
			fsaccess[14] = "-"
		if c[3] == "8":
			fsaccess[15] = "-"
		if c[4] == "1":
			fsaccess[16] = "-"
		if c[4] == "2":
			fsaccess[17] = "-"
		if c[4] == "4":
			fsaccess[18] = "-"
		if c[4] == "8":
			fsaccess[19] = "-"
		if c[5] == "1":
			fsaccess[20] = "-"
		
		f.seek(0x250) # ServiceAccessControl
		svcacc = range(32)
		for i in range(32):
			r = f.read(8)
			r = r.rstrip("\0")
			svcacc[i] = r
		
		f.seek(0x394) # Access control ARM11
		b = f.read(1)
		b = binascii.hexlify(b)
		b = bin(int(b, 16))[2:]
		b = b.zfill(9)[::-1]
		b = list(b)
		accesslist = range(9)
		for i in range (0, 9):
			if b[i] == "1":
				accesslist[i] = "true "
			elif b[i] == "0":
				accesslist[i] = "false"
			i += 1
		
		f.seek(0x39C)
		b = f.read(1)
		b = str(int(binascii.hexlify(b), 16))
		kr = 0
		if b != "255":
			kmin = b
			kr = 1
		f.seek(0x39D)
		b = f.read(1)
		b = str(int(binascii.hexlify(b), 16))
		if b != "255":
			kmaj = "0" + b

		with open(args.rsf[0], "r+b") as f:
			f.seek(0x28) # Title
			s = str(title)
			s = s.rstrip("0")
			s = "\"" + title + "\" "
			f.write(s)
			f.seek(0x52) # CompanyCode
			s=str(ccode)
			f.write(s)
			f.seek(0x73) # ProductCode
			s = str(pcode)
			s = s.rstrip("0")
			s ="\"" + s + "\""
			f.write(s)
			f.seek(0x16D) # UniqueId
			s=str(uid)
			f.write(s)
			if uext == "00":
				f.seek(0x4B5)
				f.write("E")
				f.seek(0x4C6) # ExtSavaDataId
				s=str(exts)
				f.write(s)
				f.seek(0x4EF) # System save id 1
				s=str(ssid1)
				f.write(s)
				f.seek(0x50E) # System save id 2
				s=str(ssid2)
				f.write(s)
				f.seek(0x534) # Other save id 1
				s=str(osid1)
				f.write(s)
				f.seek(0x555) # Other save id 2
				s=str(osid2)
				f.write(s)
				f.seek(0x576) # Other save id 3
				s=str(osid3)
				f.write(s)
			if uext == "10":
				f.seek(0x96C)
				f.write("True ")
				f.seek(0x10C9)
				f.write("A")
				f.seek(0x10E4)
				s = str(esid1)
				if s != "00000":
					s = "- 0x" + s
					f.write(s)
				f.seek(0x10F2)
				s = str(esid2)
				if s != "00000":
					s = "- 0x" + s
					f.write(s)
				f.seek(0x1100)
				s = str(esid3)
				if s != "00000":
					s = "- 0x" + s
					f.write(s)
				f.seek(0x110E)
				s = (esid4)
				if s != "00000":
					s = "- 0x" + s
					f.write(s)
				f.seek(0x111C)
				s = (esid5)
				if s != "00000":
					s = "- 0x" + s
					f.write(s)
				f.seek(0x112A)
				s = (esid6)
				if s != "00000":
					s = "- 0x" + s
					f.write(s)
			f.seek(0x595) # File System Access
			f.write(fsaccess[0])
			f.seek(0x5B5)
			f.write(fsaccess[1])
			f.seek(0x5D1)
			f.write(fsaccess[2])
			f.seek(0x5EE)
			f.write(fsaccess[3])
			f.seek(0x5FA)
			f.write(fsaccess[4])
			f.seek(0x60E)
			f.write(fsaccess[5])
			f.seek(0x620)
			f.write(fsaccess[6])
			f.seek(0x62B)
			f.write(fsaccess[7])
			f.seek(0x63C)
			f.write(fsaccess[8])
			f.seek(0x647)
			f.write(fsaccess[9])
			f.seek(0x657)
			f.write(fsaccess[10])
			f.seek(0x667)
			f.write(fsaccess[11])
			f.seek(0x67C)
			f.write(fsaccess[12])
			f.seek(0x699)
			f.write(fsaccess[13])
			f.seek(0x6A9)
			f.write(fsaccess[14])
			f.seek(0x6BF)
			f.write(fsaccess[15])
			f.seek(0x6D5)
			f.write(fsaccess[16])
			f.seek(0x6E9)
			f.write(fsaccess[17])
			f.seek(0x6FC)
			f.write(fsaccess[18])
			f.seek(0x707)
			f.write(fsaccess[19])
			f.seek(0x713)
			f.write(fsaccess[20])
			if kr == 1:
				if args.spoof:
					f.seek(0x9C7)
					f.write("R")
					f.seek(0x9E8)
					f.write("02")
					f.seek(0x9EF)
					f.write("R")
					f.seek(0xA10)
					f.write("33")
					print "[SPOOF] Applied."
				else:
					f.seek(0x9C7)
					f.write("R")
					f.seek(0x9E8)
					f.write(kmaj)
					f.seek(0x9EF)
					f.write("R")
					f.seek(0xA10)
					f.write(kmin)
					print "[SPOOF] Not applied."
			f.seek(0x1168) # Service Access Control
			for i in range(32):
				if svcacc[i] != "":
					s="- " + str(svcacc[i]) + " "
					s= s.ljust(11,"#")
					f.write(s)
					f.seek(5,1)
			f.seek(0x13A2) # Remaster version
			s=str(rver)
			f.write(s)
			f.seek(0x13B7) # Stacksize
			s=str(stack)
			f.write(s)
			f.seek(0x13D5) # Dependencies
			for i in range(48):
				if dep[i] != "0000000000000000":
					s="a: 0x" + str(dep[i]) + "L"
					f.write(s)
					f.seek(6,1)
			f.close

			if args.regionfree:
				with open(args.regionfree[0], "r+b") as f:
					f.seek(8216)
					f.write("\x7F\xFF\xFF\xFF")
					f.close
					print "[REGION FREE] Applied."
			else:
				pass
