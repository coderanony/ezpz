student(raj).
student(rahul).
hscstudent(raj).
sscstudent(raj).
sscstudent(rahul).
nondetermhscstudent(X).
nondetermsscstudent(X).
nondetermstudent(X).
lbscit(X):-((student(X),hscstudent(X)),sscstudent(X)).
rbscit(X):-(student(X),(hscstudent(X),sscstudent(X))).


