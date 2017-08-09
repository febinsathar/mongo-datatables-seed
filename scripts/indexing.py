
def add_to_index(pro_list,file):
    ##function to create the index
    for item in pro_list:
        temp=item
        temp=temp.split("_")
        if len(temp)==1:
            if not item in op:
                op[item]={}
                op[item]['all']=[file]
            else:
                if not 'all' in op[item]:
                    op[item]['all']=[file]
                else:
                    op[item]['all'].append(file)


        if not temp[0] in op:
            op[temp[0]]={}
            if not item in op[temp[0]]:
                op[temp[0]][item]=[file]
            else:
                op[temp[0]][item].append(file)
        else:
            if not item in op[temp[0]]:
                op[temp[0]][item]=[file]
            else:
                op[temp[0]][item].append(file)
    print(op)
    return


def lookup(protocol,subcategory):
    ##function to lookup the index [have to add the scope of printing the whole suite if protocol value entered is "all"]
    if op[protocol][subcategory]:
        print(op[protocol][subcategory])
    else:
        print("given category not found")
    return




##main function
import os
i=1
rootdir="F:/juniper/"
op={}

##adding files to index from the root directory traversing through all the files in the subfolders one by one
for root, subdirs, files in os.walk(rootdir):
    fullpath=os.path.join(root)
    if(files):
        for file in files:
            fullpath=os.path.join(root,file)
            fullpath=fullpath.replace("\\","/")
            print(fullpath)
            f = open(fullpath, "r")
            fread = f.readline()
            fread = fread.split(":")
            fread = fread[1].split(",")
            add_to_index(fread,file)


print("input arguments in the syntax: <protocol,subcategory> (enter 'all' in protocol to display the entire test script database,//"
      "enter 'all' in subcategory to run the scripts covering whole protocol")
ip=input()
inp=ip.split(',')
for i in range(1,len(inp)):
    lookup(inp[0],inp[i])