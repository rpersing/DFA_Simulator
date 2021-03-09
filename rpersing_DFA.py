import sys

dfa = {}


def transition(state, symbol):
    for c in symbol:
        if c not in alphabet:
            print("Malformed.")
            sys.exit(0)
        state = dfa[state][c]

    if state not in accept_states:
        print("Rejected.")
    elif state in accept_states:
        print("Accepted!")


f = open(str(sys.argv[1]), "r")
string_feed = sys.argv[2]
states = f.readline().strip().split(",")
alphabet = f.readline().strip().split(",")
start_state = f.readline().strip()
accept_states = f.readline().strip().split(",")

for i in states:
    dfa[i] = {}

for i in f:
    start1 = "("
    end1 = ")"
    start2 = ">"
    end2 = " "
    result1 = (i.split(start1))[1].split(end1)[0]
    result2 = (i.split(start2))[1].split(end2)[0]
    transition_given = list(result1.strip().split(","))
    transition_result = list(result2.strip().split(","))
    for j in dfa:
        if transition_given[0] == j:
            dfa[j][transition_given[1]] = transition_result[0]

transition(start_state, string_feed)
