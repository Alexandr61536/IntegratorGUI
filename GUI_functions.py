from math import sin
def Read_Data (filename):
    FlagInvFile=False
    try:
        with open(filename, "r") as InputFile:
            inp = []
            FuncX=[]
            InitialFuncY=[]
            for line in InputFile.readlines():
                inp.append(line)
            eps=int(inp[0].split()[0])
            C=int(inp[0].split()[1])
            for x in inp[1].split():
                FuncX.append(int(x))
            for y in inp[2].split():
                InitialFuncY.append(int(y))
            RightBord, LeftBord  = map(float, line.split())

            '''
            FlagInvFile=False
            i=-6.82
            FuncX=[]
            InitialFuncY=[]
            while i <= 6.28:
                FuncX.append(i)
                InitialFuncY.append(sin(i)+sin(21*i))
                i+=0.001
            eps=0.001
            C=0
            LeftBord=-6.28
            RightBord=6.28
            '''

            Data={
            'eps': eps,
            'C': C,
            'InitialFuncY': InitialFuncY,
            'FuncX': FuncX,
            'RightBord': RightBord,
            'LeftBord': LeftBord,
            'FlagInvFile': FlagInvFile
            }
            return Data

    except:
        #FlagInvFile=True
        return {"FlagInvFile":FlagInvFile}
