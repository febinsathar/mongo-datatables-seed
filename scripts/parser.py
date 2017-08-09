##main function
sourcepath = "C:/Users/jsaby/Downloads/scripts/EX_QFX_151 Scripts.txt"
destinationpath =  "C:/Users/jsaby/Downloads/scripts/EX_QFX_151_Scripts_only_scenarios.txt"
f = open(sourcepath, "r")
fo= open(destinationpath, "w")
for line in f:
    print(line)
    line=line.split(" ")
    print(line[6])
    fo.write(line[6]+"\n")
