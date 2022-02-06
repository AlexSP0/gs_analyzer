class GsKey:
    name = None 
    path = None
    name = None
    type = None
    description = None
    enum_parameters_or_range = None

    def parsePathAndName(self, line):
        first_space = line.index(" ")
        next_space = line.index(" ", first_space+1)
        self.path = line[0:first_space]
        self.name = line[first_space+1:next_space]
    
    def parseType(self, answer):
        lines = answer.splitlines(False)
        self.type = lines[0]
        if(len(lines) > 1):
            self.enum_parameters_or_range =""
            for i in range(1, len(lines)):
                self.enum_parameters_or_range = self.enum_parameters_or_range + lines[i]

    def parseDescription(self, description):
        lines = description.splitlines(False)
        self.description = "".join(lines)

    def getTotalLine(self):
        if(self.enum_parameters_or_range != None):
            totalLine = self.path + "|" + self.name + "|" + self.description + "|" + self.type + "|" + self.enum_parameters_or_range + "\n"
        else:
            totalLine = self.path + "|" + self.name + "|" + self.description + "|" + self.type + "\n"
        return totalLine
    
    def setKeyFromLine(self, line):
        key_param = line.split("|")
        self.path = key_param[0]
        self.name = key_param[1]
        self.description = key_param[2]
        self.type = key_param[3]
        if(len(key_param)>4):
            self.enum_parameters_or_range = key_param[4]
            

    

