import sys
input = sys.stdin.read

def main():
    data = input().split()
    n = int(data[0])
    MOD = 1000000007
    ans = 0
    index = 1

    for _ in range(n):
        a = int(data[index])
        b = int(data[index + 1])
        k = b
        index += 2
        
        if b == 0:
            continue
        
        tem = 1
        bi = 2
        b -= 1
        
        while b > 0:
            if b & 1 == 1:
                tem = (tem * bi) % MOD
            bi = (bi * bi) % MOD
            b >>= 1
        
        ans = (ans + a * k * tem) % MOD
    
    print(ans)

if __name__ == "__main__":
    main()
