Ax=int(input("Ax : "))
Ay=int(input("Ay : "))
Az=int(input("Az : "))
Bx=int(input("Bx : "))
By=int(input("By : "))
Bz=int(input("Bz : "))

z=Ax*By-Ay*Bx
y=Az*Bx-Ax*Bz
x=Ay*Bz-Az*By

print("\n",x,"x + ",y,"y + ",z,"z")

input()