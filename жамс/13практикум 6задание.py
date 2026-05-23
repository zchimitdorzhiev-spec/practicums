variants = []

for h in range(1, 10):
    for o in range(10):
        for d in range(10):
            for m in range(1, 10):
                for a in range(10):
                    for t in range(10):
                        digits = {h, o, d, m, a, t}
                        if len(digits) == 6:
                            hod = h * 100 + o * 10 + d
                            mat = m * 100 + a * 10 + t
                            if hod * 3 == mat:
                                variants.append((hod, mat))

variants.sort()
for hod, mat in variants:
    print(f"{hod}+{hod}+{hod}={mat}")