def _parse_macros(self):
    self._init_macros()
    self._iter_lines(self._parse_macro)
    

def _parse_macro(self, line, p, o):
    macro = line.split("(")[0]
    l = line[1:].split(")")
    if line[0] != "$":
        return line
    elif macro not in self._macros:
        self._flag = False
        self._line = o
        self._errm = "Taj macro ne postoji"
        return ""
    elif l[1] != "" or len(l) > 2:
        self._flag = False
        self._line = o
        self._errm = "Kod poslije macroa"
        return ""
    else:
        if macro == self._macros[0]:
            l = line.split("(")[1].split(",")
            A = l[0]
            B = ""
            for i in l[1]:
                if i.isdigit():
                    B = B + i
                if i.isalpha():
                    B = B + i
            return f"@{A}\nD=M\n@{B}\nM=D"
        
        elif macro == self._macros[1]:
            l = line.split("(")[1].split(",")
            A = l[0]
            B = ""
            for i in(l[1]):
                if i.isdigit():
                    B = B + i
                if i.isalpha():
                    B = B + i
            return f"@{A}\nD=M\n@swap\nM=D\n@{B}\nD=M\n@{A}\nM=D\n@swap\nD=M\n@{B}\nM=D"
    
        elif macro == self._macros[2]:
           l = line.split("(")[1].split(",")
           A = l[0]
           B = ""
           D = ""
           for i in l[1]:
               if i.isdigit():
                   B = B + i
               if i.isalpha():
                   B = B + i
           for i in l[2]:
               if i.isdigit():
                   D = D + i
               if i.isalpha():
                   D = D + i
           return f"@{A}\nD=M\n@{B}\nD=D+M\n@{D}\nM=D"
       
        
            
    
def _init_macros(self):
    self._macros = ["$MV","$SWP","$SUM","$WHILE","$END"]