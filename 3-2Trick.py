def scheme(number, n_gates=0, num=0):
    list_of_fs = []
    list_of_gs = []
    list_of_mid = []
    list_of_xy = []
    list_of_xpy = []
    list_of_nxy = []
    list_of_nxpy = []
    firstbs = []
    secondbs = []
    thirdbs = []
    list_of_nths = []
    list_of_xpy_nnxy = []
    list_fcomp = []
    n_gates = number

    for i in range(int(number / 3)):
        firstbs.append(num)
        secondbs.append(num + int(number / 3))
        thirdbs.append(num + 2 * int(number / 3))
        not_third = n_gates
        print(f"GATE {not_third} NOT {thirdbs[i]}")
        list_of_nths.append(not_third)
        n_gates += 1
        print(f"GATE {n_gates} AND {firstbs[i]} {secondbs[i]}")
        list_of_xy.append(n_gates)
        n_gates += 1
        print(f"GATE {n_gates} OR {firstbs[i]} {secondbs[i]}")
        list_of_xpy.append(n_gates)
        n_gates += 1
        if num + i == 0:
            print(f"GATE {n_gates} AND {thirdbs[i]} {not_third}")
            list_of_mid.append(f"OUTPUT {n_gates}")
            list_of_mid.append(f"OUTPUT {n_gates}")
            n_gates += 1
        num += 1
    for i in range(int(number / 3)):
        print(f"GATE {n_gates} NOT {list_of_xy[i]}")
        list_of_nxy.append(n_gates)
        n_gates += 1
        print(f"GATE {n_gates} NOT {list_of_xpy[i]}")
        list_of_nxpy.append(n_gates)
        n_gates += 1
    for i in range(int(number / 3)):
        print(f"GATE {n_gates} AND {list_of_xpy[i]} {list_of_nxy[i]}")
        list_of_xpy_nnxy.append(n_gates)
        n_gates += 1
        print(f"GATE {n_gates} OR {list_of_xy[i]} {list_of_nxpy[i]}")
        n_gates += 1
    for i in range(int(number / 3)):
        print(f"GATE {n_gates} AND {thirdbs[i]} {list_of_xpy_nnxy[i]}")
        list_fcomp.append(n_gates)
        n_gates += 1
        print(f"GATE {n_gates} AND {thirdbs[i]} {list_of_xpy_nnxy[i] + 1}")
        n_gates += 1
        print(f"GATE {n_gates} AND {list_of_nths[i]} {list_of_xpy_nnxy[i]}")
        n_gates += 1
    for i in range(int(number / 3)):
        print(f"GATE {n_gates} OR {list_of_xy[i]} {list_fcomp[i]}")
        list_of_fs.append(f"OUTPUT {n_gates}")
        n_gates += 1
        print(f"GATE {n_gates} OR {list_fcomp[i] + 1} {list_fcomp[i] + 2}")
        list_of_gs.append(f"OUTPUT {n_gates}")
        n_gates += 1

    outn = 0
    for i in range(len(list_of_gs)):
        print(f"{list_of_gs[i][0:6]} {outn} {list_of_gs[i][7:]}")
        outn += 1

    for i in range(len(list_of_mid)):
        print(f"{list_of_mid[i][0:6]} {outn} {list_of_mid[i][7:]}")
        outn += 1

    for i in range(len(list_of_fs)):
        print(f"{list_of_fs[i][0:6]} {outn} {list_of_fs[i][7:]}")
        outn += 1


n = int(input())
inp = n * 3
scheme(inp)
