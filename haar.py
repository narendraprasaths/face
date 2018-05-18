from pylab import*;
from scipy.misc import*;
from turtle import*
import turtle;
turtle.speed(50)
i=imread("naren.png")[::-1];s=256;
h=i.shape;
i=imfilter(imresize(i,(s,s)),'blur')
setup(h[1]*4.2,h[0]*4.2);setworldcoordinates(0,0,s,-s);f=forward;r=right
def h(l,a=90):
 x,y=pos()
 if l==1and i[-y,x]>128:f(2**l-1)
 else:
  if l:l-=1;r(a);h(l,-a);f(1);r(-a);h(l,a);f(1);h(l,a);r(-a);f(1);h(l,-a);r(a)
h(8)
