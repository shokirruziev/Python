## 1 Leap year
def year_chek(yil):
return (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0)
yil=int(input(&quot;Yilni kiriting &quot;))
if not isinstance(yil, int):
raise ValueError(&quot;Year must be an integer.&quot;)
print(year_chek(yil))

2. Conditional Statements Exercise
def n_chek(n):
if n%2==1:
return &#39;Wired&#39;
elif n&gt;=2 and n&lt;=5:
return &#39;Not Wired&#39;
elif n&gt;=6 and n&lt;=20:
return &#39;Wired&#39;
else:
return &#39;Not wired&#39;

n=int(input(&quot;Son kiriting &quot;))
if not isinstance(n, int):
raise ValueError(&quot;Son must be an integer.&quot;)
print(n_chek(n))

## 3
a=7
b=17
ls=[]
def fin(a,b):
if a%2==0:
ls.append(a)

a=a+1
if a&lt;b:
fin(a,b)
return ls
print(fin(a,b))
