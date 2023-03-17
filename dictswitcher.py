import bballdicts

def get_swap_dict(d):
    return {v: k for k, v in d.items()}

d_swap = get_swap_dict(bballdicts.teamdict)
print(d_swap)
with open('bballdicts.py', 'a') as f:
    f.write(str(d_swap))
f.close()