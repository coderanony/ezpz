male(raj).
male(aayush).
doctor(raj).
engineer(aayush).
nondetermale(X).
nondeterdoctor(X).
nondetermengineer(X).
ltobehusband(X):-male(X),(doctor(X);engineer(X)).
rtobehusband(X):-((male(X),doctor(X));(male(X),engineer(X))).

