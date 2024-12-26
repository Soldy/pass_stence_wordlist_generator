
import copy

separators=[".", " ", "_"]

words={
  "i":["I","i","we","you","U", "u",""],
  "do":["do","did"]
}
stence=[
  "i","do"
]
print_serial = 0


def combinatorb():
    w_l = [0]*len(stence)
    passw = [copy.deepcopy(w_l)]
    size_t = 1;
    for i in range(0, len(stence)):
        size_t = size_t * len(words[stence[i]])
    for i in range(0, size_t - 1):
        pos = len(w_l)-1
        w_l[pos] += 1
        while(w_l[pos] > len(words[stence[pos]]) - 1 ):
            w_l[pos] = 0
            pos = pos - 1
            w_l[pos] += 1 
        passw.append(copy.deepcopy(w_l))
    return passw


def to_stence(arr,sep):
    out = ""
    serial = 0
    for i in range(0, len(arr)):
        if "" != words[stence[i]][arr[i]]:
            if serial > 0:
                out += sep
            out += words[stence[i]][arr[i]]
            serial += 1
    return out

def full_print(inp):
    global print_serial
    print(inp)
    print_serial += 1



the_list = combinatorb()  
for l in range(0, len(the_list)):
    for s in range(0, len(separators)):
        full_print(to_stence(the_list[l], separators[s]))
