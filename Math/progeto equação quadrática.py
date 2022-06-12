
delta=(b**2)-4*a*c
if delta<0 :
    print('resultado imaginário')
else:
    g=(-b+(delta**1/2)/2*a)  # type: float
    v=(-b-(delta**1/2)/2*a)  # type: float
    print('As raíses equação descritas, são:{} e {}'.format(g,v))