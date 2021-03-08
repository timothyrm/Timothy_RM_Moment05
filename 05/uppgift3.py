def areaf(x):     
    areaf = r*r*pi
    return areaf #returnar funktionen som jag skapade för o räkna ut area


def omkretsf(x):
    omkretsf= 2*r*pi
    return omkretsf #samma fast omkrets

pi = 3.14
r = float(input("ange en radie för cirkeln"))

 
print(f"radien är      :   {r}") #printar radien

print(f"arean är       :   {areaf(r)}") #printar arean
print(f"omkretsen är   :   {omkretsf(r)}") #printar omkretsen
