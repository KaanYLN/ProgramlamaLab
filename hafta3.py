from sympy import Symbol,Limit

t = Symbol('t')
St = 5*t**2 + 2*t + 8

t1=Symbol('t1')
delta_t = Symbol('delta_t')

St1 = St.subs({t: t1})
St1_delta = St.subs({t: t1+delta_t})

L = Limit((St1_delta-St1)/delta_t, delta_t, 0).doit()
print L #  10*t1 + 2

from sympy import exp,sqrt,pi,Integral

x = Symbol('x')
p = exp(-(x-10)**2/2)/sqrt(2*pi)
I = Integral(p,(x,11,12)).doit().evalf()
print I
