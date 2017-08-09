def add_to_indexes(line):
    f = line.split('/')
    line=line.strip()


    # finding the main protocol areas
    protocol = "/".join(f[:len(f) - 1])

    # finding RLI and/or TPI numbers and subprotocol areas
    script = f[-1]
    script = script.strip()
    script = script.lower()
    scriptname=script
    script = (script.split('.'))[0]

    RLI = ""
    TPI = ""
    PR = ""
    subindex_rli = 0
    subindex_tpi = 0
    subindex_pr = 0
    if "rli_" in script:
        RLI = script[script.find('rli_') + 4:(script.find('_',script.find('rli_') + 4))]
        subindex_rli = script.find('_',script.find('rli_') + 4) + 1
    elif "rli" in script:
        if "_rli" in script or script[:2] == "rli":
            #RLI = script[script.find('rli') + 3:(script.find('_',script.find('rli') + 3))]
            #subindex_rli = script.find('_',script.find('rli') + 3) + 1
            if "rli" in script.split("_")[-1]:
                RLI = script[script.find('rli') + 3:]
                subindex_rli = len(script) - 1
            else:
                RLI = script[script.find('rli') + 3:(script.find('_', script.find('rli') + 3))]
                subindex_rli = script.find('_', script.find('rli') + 3) + 1

    if 'tpi_' in script:
        TPI = script[script.find('tpi_') + 4:(script.find('_',script.find('tpi_') + 4))]
        subindex_tpi = script.find('_',script.find('tpi_') + 4) + 1
    elif 'tpi' in script:
        if "_tpi" in script or script[0:2] == "tpi":
            TPI = script[script.find('tpi') + 3:(script.find('_',script.find('tpi') + 3))]
            subindex_tpi = script.find('_',script.find('tpi') + 3) + 1

    if 'pr_' in script:
        if "pr" in script.split("_")[-2] and (script.split("_")[-1]).isdigit():
            PR = script[script.find('pr_') + 3:]
            subindex_pr = len(script)-1
        else:
            PR = script[script.find('pr_') + 3:(script.find('_',script.find('pr_') + 3))]
            subindex_pr = script.find('_',script.find('pr_') + 3) + 1
    elif 'pr' in script:
        if "_pr" in script or script[:1] == "pr":
            if "pr" in script.split("_")[-1]:
                PR = script[script.find('pr') + 2:]
                subindex_pr = len(script) - 1
            else:
                PR = script[script.find('pr') + 2:(script.find('_',script.find('pr') + 2))]
                subindex_pr = script.find('_',script.find('pr') + 2) + 1


    if not PR.isdigit() or len(PR)==1:
        PR = ""
        subindex_pr = 0


    if subindex_rli==0 and re.findall(r"_(\d{4,5})_", script) and subindex_pr==0 and subindex_tpi==0:
        RLI= re.findall(r"_(\d{4,5})_", script)[0]
        subindex_rli = script.find('_',script.find(RLI)) + 1

    if subindex_rli > subindex_tpi and subindex_rli > subindex_pr:
        sub = script[subindex_rli:]
    elif subindex_tpi > subindex_pr:
        sub = script[subindex_tpi:]
    else:
        sub = script[subindex_pr:]


    #writing the splitted values to a file
    sub = sub.strip()
    sub = sub.split('_')
    sub = "  |  ".join(sub)
   # fout = open("C:/Users/jsaby/Downloads/scripts/test.txt", "a+")
   # fout.write(line + ", " + script + ", " + protocol + ", " + RLI + ", " + TPI + ", " + sub + "\n")

    line="http://cvs-bn.juniper.net/cgi-bin/viewvc.cgi/system-test/testscripts/" + line

    #creating script collection ie; dictionary of dictionaries
    scripts_db[script]={"script_name":scriptname, "path":line, "protocol":protocol, "RLI":RLI, "TPI":TPI, "PR":PR, "subareas":sub}



def insert_to_db(c, item):
    c.insert(item)




##main function
import re
import json
import pymongo
from pymongo import MongoClient

fullpath = "C:/Users/jsaby/Downloads/scripts/filenames.txt"
f = open(fullpath, "r")
scripts_db={}
for line in f:
    add_to_indexes(line)

Client = MongoClient()
db = Client["test"]
collection = db["scripts"]

Client.drop_database(db)

fjson=open("C:/Users/jsaby/Downloads/scripts/dumpsnew.json","a+")
for key in scripts_db:
    json.dump(scripts_db[key],fjson)
    insert_to_db(collection, scripts_db[key])







