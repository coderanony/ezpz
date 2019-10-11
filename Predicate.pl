batsman(sachin,batsman).
cricketer(batsman,cricketer).
nondetermbatsman(X,Y).
nondetermcricketer(X,Y).
profile(X,Y):-batsman(X,Z),cricketer(Z,Y).
