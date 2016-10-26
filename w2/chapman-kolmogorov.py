def chap_kol(i, j, exp, M, N):
	if exp == 1:
		return M[i][j]
	else:
		return sum(M[i][k]*chap_kol(k, j, exp - 1, M, N) for k in range(N))

with open('matrix','r') as f:
	exp = int(f.readline())
	P_ij = tuple(map(int, f.readline().split(" ")))
	M = []
	for line in f.readlines():
		l = list(map(float, line.split(" ")))
		M.append(l)
	N = len(M)

result = chap_kol(P_ij[0], P_ij[1], exp, M, N)
print(result)