#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        newtuple = (len(sentence), sentence[0])
        return newtuple
    else:
        newtuple = (0, None)
        return newtuple
