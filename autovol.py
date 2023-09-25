import os
import datetime
import hashlib

# Hashing File
def hash_file(filename):
	samplemd5 = hashlib.md5()
	samplesha1 = hashlib.sha1()
	global samplemd5hash
	global samplesha1hash
	with open(filename, 'rb') as file:
		chunk = 0
		while chunk != b'':
			chunk = file.read(1024 * 1024)
			samplemd5.update(chunk)
			samplesha1.update(chunk)
		samplemd5hash = samplemd5.hexdigest()
		samplesha1hash = samplesha1.hexdigest()

# * Fetching vol3.py -- Change this to your respective volatility
vol3path = ''

# Fetching Sample Name/Path
samplepath = str(input("Input your sample full path here: ")).replace("\\", "\\\\")
samplename = samplepath.split('\\')[-1]
outputpath = '\\'.join(samplepath.split('\\')[:-1])
output = outputpath + samplename
output2 = output[:-4]
output3 = output2+'\\'+samplename
date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
hash_file(samplepath)

# Check folder exist 
if not os.path.exists(output2):
	os.mkdir(output2)

print("\n		 Running AutoVol [Automatic Volatility]")
print(f"		 Name 	: {samplename}")
print(f"		 Path 	: {samplepath}")
print(f'		 Time 	: {date}')
print(f'		 Size 	: {os.path.getsize(samplepath)/(1024*1024*1024):.8f} GB')
print(f"		 MD5 	: {samplemd5hash}")
print(f"		 SHA1 	: {samplesha1hash}")
print("")
print(f" 		 Output Saved To: {output2}")
print("")

os.system(f"echo Name: {samplename} >> {output3}_brief.txt")
os.system(f"echo Path: {samplepath} >> {output3}_brief.txt")
os.system(f"echo MD5: {samplemd5hash} >> {output3}_brief.txt")
os.system(f"echo SHA1: {samplesha1hash} >> {output3}_brief.txt")

print(f"[+] Fetching Info, PsList, PsTree, NetScan, NetStat, CmdLine")
print("")

# Output Sample info
print("[+] Fetching sample info")
os.system(f'python {vol3path} -f {samplepath} windows.info > {output3}_info.txt' )

# Output Sample pslist
print("[+] Fetching sample pslist")
os.system(f'python {vol3path} -f {samplepath} windows.pslist > {output3}_pslist.tsv')

# Output Sample pstree
print("[+] Fetching sample pstree")
os.system(f'python {vol3path} -f {samplepath} windows.pstree > {output3}_pstree.tsv')

# Output Sample netscan
print("[+] Fetching sample netscan")
os.system(f'python {vol3path} -f {samplepath} windows.netscan > {output3}_netscan.tsv')

# Output Sample netstat
print("[+] Fetching sample netstat")
os.system(f'python {vol3path} -f {samplepath} windows.netstat > {output3}_netstat.tsv')

# Output Sample cmdline
print("[+] Fetching sample cmdline")
os.system(f'python {vol3path} -f {samplepath} windows.cmdline > {output3}_cmdline.tsv')

# Output Sample cmdlist
print(f'\n\n[+] Done | Saved to : {output2}\n')
