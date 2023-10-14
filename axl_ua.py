import random
def generate_android_user_agent():
    user_agents = []
    for _ in range(10):
        user_agent = f"[FBAN/FB4A;FBAV/"+str(random.randint(199,399))+".0.0."+str(random.randint(1,9))+"."+str(random.randint(99,199))+";FBBV/"+str(random.randint(111111111,999999999))+";FBDM/{density="+str(random.randint(2,3))+"."+str(random.randint(2,5))+",width=1080,height="+str(random.randint(1400,1499))+"};FBLC/"+str(random.choice(["en_US"]))+";FBRV/0;FBCR/"+str(random.choice(["Telenor","Banglalink","TNT","FASTWEB","Jazz Nepal","Nepal Telecom","Telstra","Jazz","Warid Nepal","Jio 4G","Zong Nepal","Warid","Zain","Azercell"]))+";FBMF/samsung;FBBD/"+str(random.choice(["samung"]))+";FBPN/com.facebook.katana;FBDV/"+str(random.choice(["SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935F","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820","SPH-L720","SM-S906E"]))+";FBSV/"+str(random.randint(9,12))+";FBOP/1;FBCA/arm64-v8a:;]"
        user_agents.append(user_agent)
    return user_agents

android_user_agents = generate_android_user_agent()
for user_agent in android_user_agents:
    colour = random.choice(['\033[91m','\033[92m','\033[93m','\033[94m','\033[95m','\033[96m','\033[97m'])
    print(colour+'\n'+user_agent)