import os, time, sys
os.system('clear')

# Color snippets
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)









logo2="""
\033[1;91m
\033[0;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\033[0;91m ████████\033[0;92m ██████ \033[0;91m ██    ██\033[0;92m ███████\033[0;91m    ██████\033[0;92m ║
║\033[0;91m    ██ \033[0;92m   ██   ██\033[0;91m ██    ██ \033[0;92m     ██\033[0;91m   ██    ██\033[0;92m║
║\033[0;91m    ██ \033[0;92m   ██████ \033[0;91m ████████\033[0;92m ███████\033[0;91m   ██    ██\033[0;92m║
║\033[0;91m    ██ \033[0;92m   ██   ██\033[0;91m ██    ██\033[0;92m ██    \033[0;91m    ██    ██\033[0;92m║
║\033[0;91m    ██ \033[0;92m   ██████ \033[0;91m ██    ██\033[0;92m ███████\033[0;91m █  ██████\033[0;92m ║
║                                             ║
║             \033[0;92m█████\033[0;91m  ██   \033[0;92m   ██               ║
║            \033[0;92m██   ██\033[0;91m ██     \033[0;92m ██               ║
║            \033[0;92m███████\033[0;91m ██  \033[0;92m    ██               ║
║            \033[0;92m██   ██\033[0;91m ██  \033[0;92m    ██               ║
║            \033[0;92m██   ██\033[0;91m ███████\033[0;92m ███████          ║
║                 \033[1;35m    Created By:-\033[1;34m Kali Linux\033[0;92m ║
\033[0;92m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝               \033[0;92m
\033[1;33m[01] Termux Setup   
[02] Set Termux Banner       
[03] Set Custom Termux Fornt    
[04] Make Phishing Link
[05] Camera Hack
[06] All Hack (Telegram Bot)
[07] URL Shorter     
[08] Bruteforce Attacked 
[09] Random Cloning                   
[10] File Cloning                   
[11] File Making
[12] SMS Bomber
[13] D-DOS Attacked
[14] Encode
[15] Set Termux Color Theme
[16] Remove Any Termux Banner
[17] Remove Any Termux Font
[18] Remove Termux Color Theme
[19] My Facebook Page
[20] Our Telegram Channel
[21] Our Facebook Group
[00] Exit
"""

def main():
	os.system('clear')
	print(logo2)
	kali = input('\033[1;34mEnter Your Choice \033[1;31;40m>>>\033[1;33;40m ')
	if kali in ["1", "01","a","A"]:
		os.system('clear')
		os.system('cd')
		os.system('git clone https://github.com/Kali-Linux20/TBH-Setup')
		os.system('cd TBH-Setup')
		os.system('python TBH-Setup.py')
		
		
	elif kali in ["2", "02","b","B"]:
		os.system('clear')
		os.system("espeak -a 300 \"TBH , Command, coming, soon,Now , you, can,try, this,\"")
		slowprint(f"\033[0;92mTBH  Command Coming Soon...Now  You Can Try This")
		os.system('git clone https://github.com/remo7777/T-Header.git')
		os.system('cd T-Header/')
		os.system('bash t-header.sh')
	
	elif kali in ["3","03","C","c"]:
		os.system('clear')
		os.system("espeak -a 300 \"TBH , Command, coming, soon,Now , you, can,try, this,\"")
		slowprint(f"\033[0;92mTBH  Command Coming Soon...Now  You Can Try This")
		os.system('git clone https://github.com/htr-tech/tstyle')
		os.system('cd tstyle')
		os.system('bash setup.sh')
	
	elif kali in ["4","04","D","d"]:
		os.system('clear')
		os.system("espeak -a 300 \"TBH , Command, coming, soon,Now , you, can,try, this,\"")
		slowprint(f"\033[0;92mTBH  Command Coming Soon...Now  You Can Try This")
		os.system('pkg install tur-repo')
		os.system('pkg install zphisher')
		os.system('zphisher')
	
	elif kali in ["5","05","E","e"]:
		os.system('clear')
		os.system("espeak -a 300 \"TBH , Command, coming, soon,Now , you, can,try, this,\"")
		slowprint(f"\033[0;92mTBH  Command Coming Soon...Now  You Can Try This")
		os.system('git clone https://github.com/KasRoudra/CamHacker')
		os.system('cd CamHacker')
		os.system('bash ch.sh')
	
	elif kali in ["6","06","F","f"]:
		os.system('clear')
		os.system("espeak -a 300 \"TBH , Telegram, Bot, coming, soon,Now , you, can,try, this,\"")
		slowprint(f"\033[0;92mTBH Telegram  Bot Coming Soon...Now  You Can Try This")
		os.system('xdg-open https://t.me/Mobilehacking01bot')
	
	elif kali in ["7","07","g","G"]:
		os.system('clear')
		os.system("espeak -a 300 \"TBH , Command, coming, soon,Now , you, can,try, this,\"")
		slowprint(f"\033[0;92mTBH  Command Coming Soon...Now  You Can Try This")
		os.system('git clone https://github.com/jaykali/maskphish')
		os.system('cd maskphish')
		os.system('bash maskphish.sh')
	
	elif kali in ["8","08","h","H"]:
		os.system('clear')
		os.system("espeak -a 300 \"TBH , Command, coming, soon,Now , you, can,try, this,\"")
		slowprint(f"\033[0;92mTBH  Command Coming Soon...Now  You Can Try This")
		os.system('git clone https://github.com/MrHacker-X/BruteX.git/')
		os.system('cd BruteX')
		os.system('bash setup.sh ')
		os.system('python brutex.py')
	
	elif kali in ["9","09","i","I"]:
		os.system('clear')
	
	elif kali in ["10","j","J"]:
		os.system('clear')
	
	elif kali in ["11","k","K"]:
		os.system('clear')
		os.system("espeak -a 300 \"TBH , Command, coming, soon,Now , you, can,try, this,\"")
		slowprint(f"\033[0;92mTBH  Command Coming Soon...Now  You Can Try This")
		os.system('rm -rf FILE')
		os.system('git clone --depth=1 https://️github.️com/Hannan-404/FILE')
		os.system('cd FILE')
		os.system('python FILE.py')
	
	elif kali in ["12","l","L"]:
		os.system('clear')
		os.system("espeak -a 300 \"TBH , Command, coming, soon,Now , you, can,try, this,\"")
		slowprint(f"\033[0;92mTBH  Command Coming Soon...Now  You Can Try This")
		os.system('git clone https://github.com/Toxic-Noob/ToxicBomber')
		os.system('cd ToxicBomber')
		os.system('python Tbomb.py')
	
	elif kali in ["13","M","m"]:
		os.system('clear')
		os.system("espeak -a 300 \"TBH , Command, coming, soon,Now , you, can,try, this,\"")
		slowprint(f"\033[0;92mTBH  Command Coming Soon...Now  You Can Try This")
		os.system('git clone https://github.com/Rihan444/DOS-DDOS-Tools')
		os.system('cd DOS-DDOS-Tools')
		os.system('python2 DOS.py')
	
	elif kali in ["14","n","N"]:
		os.system('clear')
		os.system('clear')
		os.system('clear')
		os.system('clear')
	
	elif kali in ["15","o","O"]:
		os.system('clear')
		os.system("espeak -a 300 \"TBH , Command, coming, soon,Now , you, can,try, this,\"")
		slowprint(f"\033[0;92mTBH  Command Coming Soon...Now  You Can Try This")
		os.system('git clone https://github.com/h4ck3r0/Termux-os')
		os.system('cd Termux-os')
		os.system('bash os.sh')
	
	elif kali in ["16","p","P"]:
		os.system('clear')
		os.system("espeak -a 300 \"TBH , Command, coming, soon,Now , you, can,try, this,\"")
		slowprint(f"\033[0;92mTBH  Command Coming Soon...Now  You Can Try This")
		os.system('clear')
		os.system('clear')
		os.system('clear')
	
	elif kali in ["17","q","Q"]:
		os.system('clear')
		os.system("espeak -a 300 \"TBH , Command, coming, soon,Now , you, can,try, this,\"")
		slowprint(f"\033[0;92mTBH  Command Coming Soon...Now  You Can Try This")
		os.system('clear')
		os.system('clear')
		os.system('clear')
	
	elif kali in ["18","r","R"]:
		os.system('clear')
		os.system("espeak -a 300 \"TBH , Command, coming, soon,Now , you, can,try, this,\"")
		slowprint(f"\033[0;92mTBH  Command Coming Soon...Now  You Can Try This")
		os.system('clear')
		os.system('clear')
		os.system('clear')
	
	elif kali in ["19","s","S"]:
		os.system('clear')
	
	elif kali in ["20","t","T"]:
		os.system('clear')
		
	elif kali in ["0","00","exit","Exit","EXIT"]:
		os.system('exit')
		os.system('clear')
	else:
		slowprint("\033[1;32mInvalid Option!")
		time.sleep(1.5)
		main()

main()
