from array import array
(k, n) = list(map(int, input().split(" ")))


def binomial_coefficient(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    numerator = 1
    denominator = 1
    for i in range(1, min(k, n - k) + 1):
        numerator = (numerator * (n - i + 1)) % 998244353
        denominator = (denominator * i) % 998244353
    return (numerator // denominator)


binomials = array('l', [0] * ((n + 1) // 2 + 1))
# binomials = [0 for _ in range(n + 1)]
binomials[0] = 1
for i in range(1, ((n + 1) // 2 + 1)):
    # tmp = ((n - i + 1) * binomials[i - 1] // i) % 998244353
    tmp = binomial_coefficient(n, i)
    binomials.insert(i, tmp)


def calculateA(t, n, k):
    val = 0
    mod_value = pow(2, k)

    i = t
    while i <= n:
        if (i < n // 2 + 1):
            val = (val + binomials[i]) % 998244353
        else:
            val = (val + binomials[n - i]) % 998244353
        # val = (val + binomials[i]) % 998244353
        i += mod_value
    return val


for t in range(pow(2, k)):
    print(calculateA(t, n, k), " ", end='')
