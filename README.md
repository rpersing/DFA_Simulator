# DFA_Simulator
A program that simulates deterministic finite-state automata.


.dfa files should be formatted as such

q0,q1,bob,q3
a,b
q0
q1,q3
(q0,a)->q1
(q0,b)->q0
(q1,a)->q1
(q1,b)->q3
(bob,a)->q3
(bob,b)->q3
(q3,a)->q3
(q3,b)->bob
