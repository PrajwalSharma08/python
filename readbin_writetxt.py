import pickle
fo=open("readbinary.bin","rb")
f=pickle.load(fo)
fw=open("record.txt",'w')
fw.write(f)
fw.close()
fo.close()
