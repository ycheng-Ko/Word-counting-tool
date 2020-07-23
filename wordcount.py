import sys
import docx

"""Define Functions"""
def readfile(fname):
    f = open(fname, "r")

    return [line.rstrip('\n') for line in f]

"""Main"""
fname = sys.argv[1]

para_list = readfile( fname )
para_num = 0
total_num = 0

#output = docx.Document()
for i in range( len(para_list) ):   
    word =  para_list[i].split()
    if len(word) > 1:
        if i < len(para_list) - 1:     
            print( para_list[i] , end=' ')
            para_num += len(word)
        else:                               # The last paragraph
            print( para_list[i], end=' ')
            para_num += len(word)
            print(f"({para_num})")
            total_num += para_num
    else:
        if i > 1:
            print(f"({para_num})\n")
            total_num += para_num
            para_num = 0
        
print(f"\n({total_num} words)")