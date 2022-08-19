f = list()
n = 150
for i in range(n):
  f.append(0)
f[0] = 1
#f[1] = 2
#u[2] = u[1] + get_next_divisible_number(n+1) #2,3,5

def is_prime_factor(n):
  if n==1:
    return True
  if n%2==0:
    return is_prime_factor(n//2)
  elif n%3 ==0:
    return is_prime_factor(n//3)
  elif n%5 ==0:
    return is_prime_factor(n//5)
  else:
    return False

def get_next_divisible_number(n):
  if n == 1:
    return 2
  if is_prime_factor(n):
    return n
  else:
    return get_next_divisible_number(n+1)

def get_ugly_number(n):
  for i in range(2, n+1):
    f[i-1] = get_next_divisible_number(f[i-2]+1)
  return f[n-1]

print(get_ugly_number(n))
#print(f)
#print(is_prime_factor(14))


