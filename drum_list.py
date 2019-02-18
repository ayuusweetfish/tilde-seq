s = []
for l in open('drum_list.txt'):
    s.append(l.rstrip('\n'))

a = list(range(len(s)))
a.sort(key=lambda x: s[x])

b = [0] * len(s)
for i in range(len(s)): b[a[i]] = i

for i in range(len(s)):
    print('drum_names[%d] = "%s"\ndrum_names[%d].pos = %d' %
        (i, s[i] + ('*' if i >= 12 else ''), i, b[i]))
