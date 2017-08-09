
##main function
import re
import json
import subprocess
#import pymongo
#from pymongo import MongoClient




#subprocess.call('C:/Program Files/Git/batchfiles/fullsync.bat', stdout=subprocess.PIPE, stderr=subprocess.PIPE)

subprocess.call('C:/Program Files/Git/batchfiles/dailysync.bat', stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#fullpath = "C:/Program Files/Git/filenames.txt"
#f = open(fullpath, "r")
#scripts_db={}
#for line in f:
    #add_to_indexes(line)

#Client = MongoClient()
#db = Client["test"]
#collection = db["scripts_git"]

#Client.drop_database(db)

#fjson=open("C:/Users/jsaby/Downloads/scripts/dumpsnew.json","a+")
#for key in scripts_db:
 #   json.dump(scripts_db[key],fjson)
  #  insert_to_db(collection, scripts_db[key])







