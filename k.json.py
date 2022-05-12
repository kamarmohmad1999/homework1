import json
q1="""the range of ip address is between :
a)0-128
b)0-255"""
q2="""arp is a :
a)network
b)protocol"""
q3="""tcp is a :
a)network
b)protocol"""
q4="""udp is a :
a)network
b)protocol"""
q5="""rip is a :
a)network
b)protocol"""
q6="""router work on :
a)network layer
b)datalink layer"""
q7="""bridge work on :
a)network layer
b)datalink layer"""
q8="""switch work on :
a)network layer
b)datalink layer"""
q9="""the default subnet mask of class B is:
a)255.0.0.0
b)255.255.0.0"""
q10="""the default subnet mask of class c is:
a)255.255.255.0
b)255.255.0.0"""
q11="""the default subnet mask of class A is:
a)255.255.0.0
b)255.0.0.0"""
q12="""the data originally start to communication from :
a)network layer
b)physical layer"""
q13="""sacch is one way channel:
a)true
b)false"""
q14="""the result of the process 2+2 is :
a)4
b)6"""
q15="""the result off the process 2+10 is :
a)12
b)6"""
q16="""the result off the process 2+8/2**3*2-1 is :
a)3
b)6"""
q17="""data transmission in both direction at once is called :
a)half duplex
b)full duplex"""
q18="""how many months in ayear :
a)12
b)16"""
q19="""the result off the process 2+5 is :
a)7
b)6"""
q20="""the result off the process 2+2*5 is :
a)12
b)6"""
d={q1:'b',q2:'b',q3:'b',q4:'b',q5:'b',q6:'a',q7:'a',q8:'b',q9:'b',q10:'a',q11:'b',q12:'b',q13:'b',q14:'a',q15:'a',q16:'a',q17:'b',q18:'a',q19:'a',q20:'a'}
k=json.dumps(d)
with open ("k.json","w")as f:
    f.write(k)




    
