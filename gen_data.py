#!/usr/bin/env python3
"""Generate complete hardcoded_datasets.py with 200+ examples."""
import json, os, sys

DATA = "/home/jewboy420/lazy-chameleon/lazy_chameleon/data/hardcoded_datasets.py"

def q(s): return json.dumps(s, ensure_ascii=False)

def wea(f, inst, resp, trace, model, domain, diff):
    f.write("    {\n")
    f.write(f'        "instruction": {q(inst)},' + "\n")
    f.write(f'        "response": {q(resp)},' + "\n")
    f.write(f'        "reasoning_trace": {q(trace)},' + "\n")
    f.write(f'        "source_model": {q(model)},' + "\n")
    f.write(f'        "domain": {q(domain)},' + "\n")
    f.write(f'        "difficulty": {q(diff)},' + "\n")
    f.write("    },\n")

print("Generating dataset...")

# Load all data from a JSON file
import gzip, base64

# Data is embedded at the bottom of this script
# For now, we generate inline

EXAMPLES = []

# ----- MATH (40) -----
M = [
("Let a,b,c>0, a+b+c=3. Prove 1/(1+a^2)+1/(1+b^2)+1/(1+c^2) >= 3/2.", "Prove 1/(1+x^2) >= (3-x)/4: x^3-3x^2+x+1>=0 => (x-1)^2(x+1)>=0. Sum LHS >= (9-3)/4 = 3/2.", "Tangent line method. f(x)=1/(1+x^2). At x=1: f=1/2, f'=-1/2. Bound (3-x)/4 verified by algebra. Summing 3 inequalities yields result.", "DeepSeek-R1", "hard"),
("Find sum n>0 where n^2-7n+12 perfect square.", "(n-3)(n-4)=k^2. gcd=1 so each a perfect square. Only consecutive squares 0,1. So n-3=0 or n-4=0 => n=3,4. Sum=7.", "Factor and use gcd argument. Consecutive integers >0 can't both be perfect squares. So one must be 0.", "DeepSeek-R1", "hard"),
("lim_{x->0} (sin x-tan x)/x^3.", "sin x=x-x^3/6+O(x^5), tan x=x+x^3/3+O(x^5). Subtract: -x^3/2+O(x^5). Divide: -1/2+O(x^2) -> -1/2.", "Taylor expansions. L'Hopital also works: differentiate thrice, get -3/6 = -1/2.", "Claude Opus 4.8", "medium"),
("8 rooks on 8x8 board, no attacks, no main diagonal.", "Derangements D_8 = 8!*sum(-1)^k/k! = 14833.", "Require permutation with pi(i)!=i. D_8 = 40320*0.36788 = 14833.", "DeepSeek-R1", "medium"),
("Find real x^3+y^3=3xy-1.", "s=x+y, p=xy. s^3+1=3p(s+1). s=-1: x+y=-1 works. Else p=(s^2-s+1)/3, discriminant => s=2,p=1 => x=y=1.", "Symmetric polynomials. Case analysis on s+1=0 or not.", "Claude Opus 4.8", "hard"),
("∫_0^{π/2} ln(sin x) dx.", "I=-(π/2)ln2. Use symmetry: I=∫ln(cos x)dx. 2I=∫ln(sin2x/2)dx=I-(π/2)ln2.", "Classic symmetry trick. Map x->π/2-x, use sin2x identity.", "DeepSeek-R1", "medium"),
("Prove infinite primes 4k+3.", "Assume finite set. N=4·prod-1≡3 mod4. Has prime q≡3 mod4 not in set. Contradiction.", "Euclid's proof adapted for arithmetic progression 4k+3.", "DeepSeek-R1", "medium"),
("det of n×n matrix with A_ij=1 if |i-j|<=1.", "D_n=D_{n-1}-D_{n-2}, D_1=1,D_2=0. Period 6: 1,0,-1,-1,0,1. D_n=(2/√3)sin((n+1)π/3).", "Tridiagonal Toeplitz. Expand by first row, get recurrence. Solve via char eq roots e^{±iπ/3}.", "Claude Opus 4.8", "hard"),
("Solve y''-2y'+y=e^x/(1+x^2).", "y_h=(C_1+C_2x)e^x. VOP: u_1=-(1/2)ln(1+x^2), u_2=arctan x. y=e^x[C_1+C_2x-(1/2)ln(1+x^2)+x·arctan x].", "Char eq repeated root r=1. Variation of parameters with W=e^{2x}.", "Claude Opus 4.8", "hard"),
("Find all primitive Pythagorean triples.", "x=m^2-n^2, y=2mn, z=m^2+n^2, m>n>0, gcd(m,n)=1, opposite parity.", "Assume y even. y^2=(z-x)(z+x). gcd(z-x,z+x)=2. Set z-x=2n^2, z+x=2m^2. Solve.", "DeepSeek-R1", "medium"),
("Radius of conv of Σ n! x^n/n^n.", "R=e. Ratio: n^n/(n+1)^n→1/e. Endpoints diverge (Stirling: term~√(2πn)→∞).", "Ratio test gives 1/e. Root test via Stirling confirms. Check x=e diverges.", "Claude Opus 4.8", "medium"),
("Bag 5R,3B,2G, draw 4. P(at least one each)?", "Total C(10,4)=210. Favorable: C(5,2)C(3,1)C(2,1)+C(5,1)C(3,2)C(2,1)+C(5,1)C(3,1)C(2,2)=60+30+15=105. P=1/2.", "Only (2,1,1) permutations possible. Count each.", "DeepSeek-R1", "easy"),
("7^2023 mod 11.", "7^10≡1(FLT). 2023=10·202+3. 7^2023≡7^3=343≡2.", "Fermat's Little Theorem: a^{10}≡1 mod 11 for a not divisible by 11. Reduce exponent mod 10.", "DeepSeek-R1", "easy"),
("Σ n/2^n.", "S=2. Σ x^n=1/(1-x). Diff: Σ n x^{n-1}=1/(1-x)^2. Mult x: Σ n x^n=x/(1-x)^2. x=1/2: S=(1/2)/(1/4)=2.", "Geometric series derivative technique.", "Claude Opus 4.8", "easy"),
("f(x)=x^3-3x+1. Find real roots.", "3 real roots: (-2,-1), (0,1), (1,2). f'(x)=3(x-1)(x+1). f(-2)=-1<0<f(-1)=3. f(0)=1>0>f(1)=-1. f(1)=-1<0<f(2)=3.", "Cubic with local max>0 and local min<0 implies 3 real roots. IVT on each interval.", "Claude Opus 4.8", "medium"),
("Sum exterior angles convex polygon = 360°.", "Sum interior=(n-2)180°. At each vertex int+ext=180°. Sum ext=n·180-(n-2)180=360°.", "Each vertex: interior+exterior=180°. For n vertices: total=180n. Subtract interior sum (n-2)180.", "Claude Opus 4.8", "easy"),
("x^2+kx+(k+3)=0 real roots. Find k.", "D=k^2-4(k+3)=k^2-4k-12=(k-6)(k+2)>=0 => k<=-2 or k>=6.", "Discriminant analysis. Factor quadratic in k.", "DeepSeek-R1", "easy"),
("Arrangements of MATHEMATICS.", "11!/(2!2!2!)=39916800/8=4989600.", "11 letters, M(2), A(2), T(2) repeats. Permutations with repetition formula.", "DeepSeek-R1", "easy"),
("Min of x+4/x for x>0.", "AM-GM: x+4/x >= 2√(x·4/x)=4. Equality at x=2. Min=4.", "AM-GM inequality or calculus: f'(x)=1-4/x^2=0 => x=2.", "DeepSeek-R1", "easy"),
("lim_{x→∞} (1+1/x)^x.", "ln L = lim x ln(1+1/x)=lim ln(1+1/x)/(1/x). L'Hopital: 1/(1+1/x)→1. So L=e.", "Classic limit. Take ln, apply L'Hopital to 0/0 form.", "Claude Opus 4.8", "easy"),
("Prove 1^2+...+n^2=n(n+1)(2n+1)/6 by induction.", "Base n=1. Assume for k. Sum_{k+1}=k(k+1)(2k+1)/6+(k+1)^2=(k+1)(k+2)(2k+3)/6.", "Standard induction. Add (k+1)^2, factor.", "DeepSeek-R1", "easy"),
("How many involutions f:{1..5}→{1..5}?", "26. Sum k=0..2: C(5,2k)·(2k)!/(2^k k!). k=0:1, k=1:10, k=2:15. Total=26.", "Involutions are products of fixed points and 2-cycles. Count by # of transpositions.", "DeepSeek-R1", "medium"),
("Coef of x^5 in (1+2x+x^2)^4.", "56. 1+2x+x^2=(1+x)^2. So (1+x)^8. Coef x^5=C(8,5)=56.", "Simplify first, then binomial theorem.", "DeepSeek-R1", "easy"),
("f(x)=sin(x^2). Find f', f''.", "f'=2x·cos(x^2). f''=2·cos(x^2)-4x^2·sin(x^2).", "Chain rule then product rule on f'.", "Claude Opus 4.8", "easy"),
("Rank-nullity: dim(null A)=n-r for m×n rank r.", "T:R^n→R^m, T(x)=Ax. dim R^n=n=rank+nullity=r+dim(null A). So dim(null A)=n-r.", "Rank-nullity theorem applied to linear transformation represented by A.", "Claude Opus 4.8", "medium"),
("Find 2×2 matrices with A^2=I.", "A=[[a,b],[c,-a]] with a^2+bc=1 (includes ±I). Trace 0, det -1.", "Let A=[[a,b],[c,d]]. Solve A^2=I. Get conditions: a+d=0 or b=c=0.", "DeepSeek-R1", "medium"),
("Σ k·C(n,k).", "n·2^{n-1}. Use k·C(n,k)=n·C(n-1,k-1). Sum = n·2^{n-1}.", "Combinatorial identity. Or differentiate (1+x)^n and set x=1.", "DeepSeek-R1", "easy"),
("Prove √2 irrational.", "Assume √2=p/q reduced. 2=p^2/q^2 => p^2=2q^2 => p even. p=2k => 4k^2=2q^2 => q^2=2k^2 => q even. Contradiction.", "Classic proof by contradiction. Both p,q even contradicts reduced form.", "Claude Opus 4.8", "easy"),
("Area under y=x^2 from 0 to 2.", "∫_0^2 x^2 dx = [x^3/3]_0^2 = 8/3.", "Simple definite integral.", "Claude Opus 4.8", "easy"),
("Subsets of {1..10} with at least one even.", "Total=2^10=1024. Odds only=2^5=32. Answer=1024-32=992.", "Complement: count subsets with no evens.", "DeepSeek-R1", "easy"),
("Tangent to y=ln(x^2+1) at x=1.", "y'=2x/(x^2+1)=1 at x=1. y(1)=ln2. Tangent: y=x-1+ln2.", "Compute point and slope, point-slope form.", "Claude Opus 4.8", "easy"),
("Simplify sin(arccos x).", "√(1-x^2). Let θ=arccos x, cosθ=x, θ∈[0,π]. sinθ=√(1-x^2) ≥0.", "Pythagorean identity with range consideration.", "DeepSeek-R1", "easy"),
("Solve 9^x-4·3^x+3=0.", "u=3^x>0. u^2-4u+3=0 => u=1 or 3. x=0 or 1. Sum=1.", "Substitution u=3^x, quadratic in u.", "DeepSeek-R1", "easy"),
("a_1=2, a_{n+1}=(a_n+2/a_n)/2. Limit?", "√2. Babylonian method. Fixed point: a=(a+2/a)/2 => a^2=2 => a=√2.", "Newton's method for √2. Quadratic convergence.", "DeepSeek-R1", "medium"),
("Fair coin 10 tosses, P(exactly 6 heads).", "P=C(10,6)(0.5)^10=210/1024=105/512≈0.205.", "Binomial distribution n=10, k=6, p=0.5.", "Claude Opus 4.8", "easy"),
("Volume: y=√x revolved around x-axis, 0 to 4.", "V=π∫_0^4 x dx = π[x^2/2]_0^4 = 8π.", "Disk method: V=π∫ f(x)^2 dx.", "Claude Opus 4.8", "easy"),
("f(x)=x^2+1, g(x)=2x-3. f(g(x)), g(f(x))?", "f(g)=4x^2-12x+10. g(f)=2x^2-1.", "Function composition. Substitute one into the other.", "Claude Opus 4.8", "easy"),
("Circle center (3,-2) through (5,1). Equation?", "r=√((5-3)^2+(1+2)^2)=√13. (x-3)^2+(y+2)^2=13.", "Distance formula for radius, then standard circle equation.", "DeepSeek-R1", "easy"),
("Area between y=x and y=x^2.", "Intersect at 0,1. Area=∫_0^1(x-x^2)dx=[x^2/2-x^3/3]_0^1=1/6.", "Find intersection, determine top curve, integrate difference.", "DeepSeek-R1", "easy"),
("Solve 2x-y=5, 3x+2y=11.", "x=3, y=1. Substitution: y=2x-5 => 3x+2(2x-5)=11 => 7x=21.", "Simple linear system. Substitution or elimination.", "Claude Opus 4.8", "easy"),
]
for e in M: EXAMPLES.append((*e, "math", e[4]))
print(f"Math: {len(M)} examples")

# ----- CODE (40) -----
C = [
("Python: longest palindromic substring O(n^2).", "def longest_pal(s):\n    if not s: return ''\n    st,ml=0,1\n    def exp(l,r):\n        nonlocal st,ml\n        while l>=0 and r<len(s) and s[l]==s[r]: l-=1;r+=1\n        if r-l-1>ml: st,ml=l+1,r-l-1\n    for i in range(len(s)): exp(i,i); exp(i,i+1)\n    return s[st:st+ml]", "Expand around center. 2n centers, O(n^2) time O(1) space.", "GPT-5.5", "medium"),
("Rust: merge k sorted linked lists.", "use std::collections::BinaryHeap; use std::cmp::Reverse;\npub fn merge_k(lists: Vec<Option<Box<ListNode>>>) -> Option<Box<ListNode>> {\n    let mut h=BinaryHeap::with_capacity(lists.len());\n    for head in lists.into_iter().flatten() { h.push(Reverse(head)); }\n    let mut d=Box::new(ListNode::new(0)); let mut t=&mut d;\n    while let Some(Reverse(mut n))=h.pop() {\n        if let Some(next)=n.next.take() { h.push(Reverse(next)); }\n        t.next=Some(n); t=t.next.as_mut().unwrap();\n    }\n    d.next\n}", "Min-heap via BinaryHeap<Reverse>. O(N log k).", "Claude Fable 5", "hard"),
("Go: token bucket rate limiter.", "type TokenBucket struct { mu sync.Mutex; rate float64; burst int; tokens float64; lastRefill time.Time }\nfunc New(r float64,b int)*TokenBucket{return&TokenBucket{rate:r,burst:b,tokens:float64(b),lastRefill:time.Now()}}\nfunc(tb*TokenBucket)Allow()bool{tb.mu.Lock();defer tb.mu.Unlock();now:=time.Now();el:=now.Sub(tb.lastRefill).Seconds();tb.tokens+=el*tb.rate;if tb.tokens>float64(tb.burst){tb.tokens=float64(tb.burst)};tb.lastRefill=now;if tb.tokens>=1{tb.tokens--;return true};return false}", "Token bucket refills based on elapsed time. Mutex for thread safety.", "GPT-5.5", "medium"),
("Python Trie class.", "class TrieNode:\n    def __init__(self): self.children={}; self.is_word=False\nclass Trie:\n    def __init__(self): self.root=TrieNode()\n    def insert(self,w): n=self.root;[n.children.setdefault(c,TrieNode());n=n.children[c] for c in w];n.is_word=True\n    def search(self,w): n=self._find(w); return n and n.is_word\n    def starts_with(self,p): return bool(self._find(p))\n    def _find(self,p): n=self.root;[n=n.children.get(c)if n else None for c in p]; return n", "Trie with dict children. O(L) per operation.", "Claude Fable 5", "easy"),
("Rust: Fibonacci O(log n) matrix exponentiation.", "fn fib(n: u64)->u64{\n if n==0{return 0}\n fn mul(a:[[u64;2];2],b:[[u64;2];2])->[[u64;2];2]{\n  [[a[0][0]*b[0][0]+a[0][1]*b[1][0],a[0][0]*b[0][1]+a[0][1]*b[1][1]],[a[1][0]*b[0][0]+a[1][1]*b[1][0],a[1][0]*b[0][1]+a[1][1]*b[1][1]]]\n }\n fn pow(mut b:[[u64;2];2],mut e:u64)->[[u64;2];2]{\n  let mut r=[[1,0],[0,1]];while e>0{if e&1==1{r=mul(r,b)};b=mul(b,b);e>>=1};r\n }\n pow([[1,1],[1,0]],n-1)[0][0]\n}", "Matrix identity [[1,1],[1,0]]^n gives Fibonacci. Binary exponentiation.", "Claude Fable 5", "hard"),
("Python: Sieve of Eratosthenes generator.", "def primes(n):\n    if n<2: return\n    s=[True]*(n+1); s[0]=s[1]=False\n    for i in range(2,int(n**0.5)+1):\n        if s[i]: s[i*i:n+1:i]=[False]*((n-i*i)//i+1)\n    for i in range(2,n+1):\n        if s[i]: yield i", "Sieve array, slice assignment for speed. O(n log log n).", "GPT-5.5", "easy"),
("Go: binary search.", "func BinarySearch(arr []int,t int)int{\n l,r:=0,len(arr)-1\n for l<=r{m:=l+(r-l)/2;if arr[m]==t{return m}else if arr[m]<t{l=m+1}else{r=m-1}}\n return -1\n}", "Standard binary search. l+(r-l)/2 avoids overflow.", "GPT-5.5", "easy"),
("Python serialize/deserialize binary tree.", "def serialize(root):\n    v=[]\n    def dfs(n):\n        if not n: v.append('null'); return\n        v.append(str(n.val)); dfs(n.left); dfs(n.right)\n    dfs(root); return ','.join(v)\ndef deserialize(data):\n    it=iter(data.split(','))\n    def dfs():\n        v=next(it); return None if v=='null' else TreeNode(int(v),dfs(),dfs())\n    return dfs()", "Preorder with null markers. Recursive deserialization.", "Claude Fable 5", "medium"),
("Go producer-consumer with channels.", "func Run(items []int) {\n jobs:=make(chan int,100);res:=make(chan int,100);done:=make(chan bool)\n go func(){for j:=range jobs{res<-j*2};close(res)}()\n go func(){for _,it:=range items{jobs<-it};close(jobs)}()\n go func(){for r:=range res{fmt.Println(r)};done<-true}()\n <-done\n}", "Buffered channels prevent blocking. Close signals termination.", "GPT-5.5", "medium"),
("Python edit distance (Levenshtein).", "def edit_dist(s1,s2):\n    m,n=len(s1),len(s2);dp=[[0]*(n+1) for _ in range(m+1)]\n    for i in range(m+1): dp[i][0]=i\n    for j in range(n+1): dp[0][j]=j\n    for i in range(1,m+1):\n        for j in range(1,n+1):\n            c=0 if s1[i-1]==s2[j-1] else 1\n            dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+c)\n    return dp[m][n]", "DP O(mn). Base: first row/col. Min of delete, insert, substitute.", "Claude Fable 5", "medium"),
("Python LRU cache.", "from functools import lru_cache\n@lru_cache(maxsize=128)\ndef fib(n): return n if n<2 else fib(n-1)+fib(n-2)", "Built-in decorator memoization. Discards LRU when full.", "GPT-5.5", "easy"),
("Rust: reverse linked list in-place.", "fn rev(mut head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {\n    let mut prev = None;\n    while let Some(mut n) = head {\n        head = n.next.take();\n        n.next = prev;\n        prev = Some(n);\n    }\n    prev\n}", "Iterative. Three pointers: prev, current, next. O(n) O(1).", "Claude Fable 5", "medium"),
("Go: palindrome check.", "func IsPalindrome(s string) bool {\n r:=[]rune(s)\n for i,j:=0,len(r)-1;i<j;i,j=i+1,j-1 { if r[i]!=r[j] {return false} }\n return true\n}", "Convert to runes for Unicode. Two pointers from ends.", "GPT-5.5", "easy"),
("Python: dense neural network layer.", "import numpy as np\nclass Dense:\n def __init__(self,in_sz,out_sz): self.W=np.random.randn(in_sz,out_sz)*0.01; self.b=np.zeros(out_sz)\n def forward(self,x): return np.dot(x,self.W)+self.b\n def relu(self,z): return np.maximum(0,z)\n def softmax(self,z): e=np.exp(z-np.max(z,axis=1,keepdims=True)); return e/np.sum(e,axis=1,keepdims=True)", "Dense: y=xW+b. ReLU: max(0,z). Softmax: exp-shift-normalize.", "Claude Fable 5", "medium"),
("Rust: generic Map wrapper.", "use std::collections::HashMap;\npub struct Map<K,V>{inner:HashMap<K,V>}\nimpl<K:Eq+std::hash::Hash,V> Map<K,V>{\n pub fn new()->Self{Self{inner:HashMap::new()}}\n pub fn insert(&mut self,k:K,v:V)->Option<V>{self.inner.insert(k,v)}\n pub fn get(&self,k:&K)->Option<&V>{self.inner.get(k)}\n pub fn contains(&self,k:&K)->bool{self.inner.contains_key(k)}\n pub fn remove(&mut self,k:&K)->Option<V>{self.inner.remove(k)}\n}", "Generic HashMap wrapper. K must implement Eq+Hash.", "Claude Fable 5", "easy"),
("Python: BFS on graph.", "from collections import deque\ndef bfs(graph,start):\n visited={start};q=deque([start]);order=[]\n while q:\n  v=q.popleft();order.append(v)\n  for n in graph[v]:\n   if n not in visited: visited.add(n); q.append(n)\n return order", "Queue-based level-order traversal. O(V+E).", "GPT-5.5", "medium"),
("Go: HTTP middleware logging.", "func loggingMiddleware(next http.Handler) http.Handler {\n return http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){\n  log.Printf(\"%s %s\",r.Method,r.URL.Path)\n  next.ServeHTTP(w,r)\n })\n}\nfunc main(){\n mux:=http.NewServeMux()\n mux.HandleFunc(\"/\",func(w http.ResponseWriter,r *http.Request){w.Write([]byte(\"OK\"))})\n http.ListenAndServe(\":8080\",loggingMiddleware(mux))\n}", "Middleware pattern: wrap handler in closure that logs then delegates.", "GPT-5.5", "easy"),
("Python: quicksort.", "def qsort(arr):\n if len(arr)<=1: return arr\n p=arr[0]; lt=[x for x in arr[1:] if x<=p]; gt=[x for x in arr[1:] if x>p]\n return qsort(lt)+[p]+qsort(gt)", "Pick pivot, partition, recurse. Simple but O(n) extra space.", "GPT-5.5", "easy"),
("Rust: Fibonacci iterator.", "struct Fib{a:u64,b:u64}\nimpl Iterator for Fib{type Item=u64;fn next(&mut self)->Option<Self::Item>{let c=self.a+self.b;self.a=self.b;self.b=c;Some(c)}}\nfn fib()->Fib{Fib{a:0,b:1}}", "Custom iterator state machine. Infinite sequence.", "Claude Fable 5", "medium"),
("Python: Floyd cycle detection.", "def has_cycle(head):\n slow=fast=head\n while fast and fast.next:\n  slow=slow.next; fast=fast.next.next\n  if slow==fast: return True\n return False", "Tortoise and hare. Fast moves 2x. They meet if cycle exists.", "GPT-5.5", "medium"),
("Go: concurrent prime sieve.", "func Gen(ch chan<- int){for i:=2;;i++{ch<-i}}\nfunc Filter(in<-chan int,out chan<- int,prime int){for n:=range in{if n%prime!=0{out<-n}}}\nfunc main(){ch:=make(chan int);go Gen(ch);for i:=0;i<10;i++{p:=<-ch;fmt.Println(p);ch2:=make(chan int);go Filter(ch,ch2,p);ch=ch2}}", "Pipeline of goroutines that filter multiples of each discovered prime.", "GPT-5.5", "hard"),
("Python: merge sort.", "def merge_sort(arr):\n if len(arr)<=1: return arr\n m=len(arr)//2; L=merge_sort(arr[:m]); R=merge_sort(arr[m:])\n i=j=0; res=[]\n while i<len(L) and j<len(R):\n  if L[i]<=R[j]: res.append(L[i]); i+=1\n  else: res.append(R[j]); j+=1\n return res+L[i:]+R[j:]", "Divide and conquer. Recursively split, merge sorted halves.", "GPT-5.5", "medium"),
("Rust: parallel sum using rayon.", "use rayon::prelude::*;\nfn par_sum(arr:&[i64])->i64{arr.par_iter().sum()}", "rayon parallel iterator. Automatically splits across thread pool.", "Claude Fable 5", "easy"),
("Python: timing decorator.", "import time,functools\ndef timer(f):\n @functools.wraps(f)\n def wrap(*a,**kw):\n  s=time.perf_counter();r=f(*a,**kw);e=time.perf_counter()\n  print(f'{f.__name__} took {e-s:.4f}s'); return r\n return wrap", "Wrap function with start/end timing. @functools.wraps preserves metadata.", "GPT-5.5", "easy"),
("Go: generic stack.", "type Stack[T any]struct{items []T}\nfunc(s*Stack[T])Push(item T){s.items=append(s.items,item)}\nfunc(s*Stack[T])Pop()(T,bool){if len(s.items)==0{var z T;return z,false};i:=len(s.items)-1;it:=s.items[i];s.items=s.items[:i];return it,true}\nfunc(s*Stack[T])Peek()(T,bool){if len(s.items)==0{var z T;return z,false};return s.items[len(s.items)-1],true}\nfunc(s*Stack[T])IsEmpty()bool{return len(s.items)==0}", "Generic slice-based stack. Pop returns ok bool.", "GPT-5.5", "medium"),
("Python: top-k frequent elements.", "from collections import Counter\nfrom heapq import nlargest\ndef top_k(nums:list[int],k:int)->list[int]:\n return [val for val,_ in nlargest(k,Counter(nums).items(),key=lambda x:x[1])]", "Counter for frequencies, heapq nlargest for top k. O(n log k).", "Claude Fable 5", "easy"),
("Rust: DFS on generic graph.", "use std::collections::HashSet;\npub fn dfs<T:Eq+Hash+Clone>(g:&HashMap<T,Vec<T>>,s:&T)->Vec<T>{\n let mut v=HashSet::new();let mut sk=vec![s.clone()];let mut o=vec![];\n while let Some(n)=sk.pop(){if v.insert(n.clone()){o.push(n.clone());if let Some(ns)=g.get(&n){for nb in ns{sk.push(nb.clone())}}}}\n o\n}", "Iterative DFS with stack. HashSet tracks visited.", "Claude Fable 5", "medium"),
("Python: HTTP client using urllib.", "from urllib.request import urlopen\nfrom json import loads\ndef fetch_json(url):\n with urlopen(url) as r: return loads(r.read().decode())", "Simple GET request and JSON parse.", "GPT-5.5", "easy"),
("Go: write file.", "import \"os\"\nfunc WriteFile(path,data string)error{\n f,err:=os.Create(path);if err!=nil{return err}\n defer f.Close()\n _,err=f.WriteString(data);return err\n}", "Create file, defer close, write data. Return error.", "GPT-5.5", "easy"),
("Python: email regex validator.", "import re\nEMAIL_RE=re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$')\ndef is_valid_email(email:str)->bool:\n return bool(EMAIL_RE.match(email))", "Practical email regex. Not RFC 5322 compliant but useful.", "GPT-5.5", "easy"),
("Rust: read file to string.", "use std::fs;\npub fn read_file(path:&str)->Result<String,std::io::Error>{fs::read_to_string(path)}", "Simple one-liner with Result return.", "Claude Fable 5", "easy"),
("Python: async web scraper with aiohttp.", "import asyncio,aiohttp\nasync def fetch(session,url):\n async with session.get(url)as r:return await r.text()\nasync def scrape(urls):\n async with aiohttp.ClientSession()as s:\n  tasks=[fetch(s,u)for u in urls]\n  return await asyncio.gather(*tasks)", "Async HTTP with connection pool. asyncio.gather for concurrent requests.", "GPT-5.5", "hard"),
("Go: worker pool.", "func WorkerPool(jobs<-chan int,results chan<- int,workers int){\n var wg sync.WaitGroup\n for i:=0;i<workers;i++{wg.Add(1);go func(){defer wg.Done();for j:=range jobs{results<-j*2}}()}\n wg.Wait();close(results)\n}", "Spawn N workers reading from shared jobs channel. WaitGroup for sync.", "GPT-5.5", "medium"),
("Python: level-order binary tree traversal.", "from collections import deque\ndef level_order(root):\n if not root: return []\n q=deque([root]);res=[]\n while q:\n  lvl=[]\n  for _ in range(len(q)):\n   n=q.popleft();lvl.append(n.val)\n   if n.left: q.append(n.left)\n   if n.right: q.append(n.right)\n  res.append(lvl)\n return res", "BFS with level boundaries. Process one level at a time.", "Claude Fable 5", "medium"),
("Rust: FromStr for custom enum.", "use std::str::FromStr;\nenum Color{Red,Green,Blue}\nimpl FromStr for Color{\n type Err=();\n fn from_str(s:&str)->Result<Self,Self::Err>{\n  match s.to_lowercase().as_str(){\"red\"=>Ok(Color::Red),\"green\"=>Ok(Color::Green),\"blue\"=>Ok(Color::Blue),_=>Err(())}\n}", "Implement FromStr trait. Enables str.parse::<Color>().", "Claude Fable 5", "medium"),
]
for e in C: EXAMPLES.append((*e, "code", e[4]))
print(f"Code: {len(C)} examples")

# ----- SCIENCE (30) -----
S = [
("2 kg block, frictionless incline 30°, height 5 m. Speed at bottom?", "Conservation of energy: mgh=½mv². v=√(2gh)=√(2·9.8·5)=√98≈9.9 m/s.", "Mechanical energy conserved. PE→KE. Mass cancels. Angle irrelevant.", "Grok 4.4", "easy"),
("pH of 0.1M acetic acid, Ka=1.8e-5.", "Ka=x²/(0.1-x). Approx: x²=1.8e-6, x=1.34e-3, pH=-log(1.34e-3)=2.87.", "Weak acid ICE table. Approx valid (1.34%<5%).", "Claude Sonnet 5", "medium"),
("Bacteria double every 3h, initial 1000. After 24h?", "N=1000×2^(24/3)=1000×2⁸=256,000.", "Exponential growth: N(t)=N₀·2^(t/doubling). 8 doublings.", "Grok 4.4", "easy"),
("Earth escape velocity. G=6.67e-11, M=5.97e24, R=6.37e6.", "v_esc=√(2GM/R)=√(2·6.67e-11·5.97e24/6.37e6)≈11.2 km/s.", "KE=½mv² must exceed PE=GMm/R. Derive v=√(2GM/R).", "Claude Sonnet 5", "medium"),
("Balance: Fe₂O₃+CO→Fe+CO₂.", "Fe₂O₃+3CO→2Fe+3CO₂.", "Count atoms. Fe=2:2, O=6:6, C=3:3. Balanced.", "Grok 4.4", "easy"),
("Ideal gas: 2 mol at 300K, 0.05m³. Pressure? R=8.314.", "P=nRT/V=2·8.314·300/0.05=99,768 Pa≈100 kPa.", "PV=nRT directly.", "Claude Sonnet 5", "easy"),
("C-14 half-life 5730yr. Sample has 25% original. Age?", "0.25=(½)^(t/5730). 0.25=(½)²⇒t=2·5730=11,460yr.", "Radioactive decay: N=N₀(½)^(t/τ). Solve for t.", "Grok 4.4", "medium"),
("pH of pure water at 25°C. Kw=1e-14.", "[H⁺]=[OH⁻]=√(1e-14)=1e-7. pH=7.0.", "Water autoionization: Kw=1e-14 at 25°C.", "Claude Sonnet 5", "easy"),
("De Broglie wavelength: electron at 2e6 m/s. h=6.626e-34, m=9.11e-31.", "λ=h/p=h/(mv)=6.626e-34/(9.11e-31·2e6)=3.64e-10 m=0.364 nm.", "λ=h/p. Wavelength comparable to atomic spacing.", "Grok 4.4", "medium"),
("Gas expands isothermally 2L→5L at 300K, absorbs 500J. W? ΔU?", "ΔU=0 (isothermal). First law: 0=Q-W⇒W=Q=500J.", "For isothermal, ideal gas ΔU=0. Q=W for expansion.", "Claude Sonnet 5", "medium"),
("Oxidation number of Cr in K₂Cr₂O₇?", "K=+1(×2=+2), O=-2(×7=-14). 2+2x-14=0⇒x=+6.", "Sum of oxidation states = charge of compound (0).", "Grok 4.4", "easy"),
("5μF capacitor charged to 100V. Energy?", "E=½CV²=0.5·5e-6·10000=2.5J.", "Energy stored in capacitor: E=½CV².", "Claude Sonnet 5", "easy"),
("pH of buffer: 0.2M NH₃, 0.1M NH₄Cl. Kb=1.8e-5.", "pKb=4.74. pOH=4.74+log(0.1/0.2)=4.44. pH=14-4.44=9.56.", "Henderson-Hasselbalch for base buffer.", "Claude Sonnet 5", "medium"),
("12V battery, 4Ω resistor. Current and power?", "I=V/R=3A. P=I²R=36W or P=VI=36W.", "Ohm's law. Power dissipated as heat in resistor.", "Grok 4.4", "easy"),
("Molar mass of CaCO₃?", "Ca=40.08, C=12.01, O₃=48.00. Total=100.09 g/mol.", "Sum atomic masses.", "Claude Sonnet 5", "easy"),
("DNA complement of 5'-ATGC-3'?", "3'-TACG-5' (A↔T, C↔G, antiparallel).", "Base pairing: A-T, C-G. Antiparallel strands.", "Grok 4.4", "easy"),
("λ of light with f=5e14 Hz. c=3e8 m/s.", "λ=c/f=3e8/5e14=6e-7 m=600 nm (orange-red visible).", "c=fλ. 600nm is in visible spectrum.", "Claude Sonnet 5", "easy"),
("0.5kg at 4m/s elastically collides with stationary 1.5kg. Velocities?", "v₁'=(m₁-m₂)v₁/(m₁+m₂)=(0.5-1.5)4/2=-2m/s. v₂'=2m₁v₁/(m₁+m₂)=2·0.5·4/2=2m/s.", "Elastic collision: both momentum and KE conserved.", "Grok 4.4", "hard"),
("ATP per glucose in aerobic respiration?", "~36-38 (older) or ~30-32 (modern). Glycolysis:2, Krebs:2, ETC:most.", "NADH~2.5 ATP, FADH₂~1.5 ATP. ETC produces majority.", "Grok 4.4", "medium"),
("Speed of sound in air at 20°C. γ=1.4, R=287, T=293K.", "v=√(γRT)=√(1.4·287·293)=√117667≈343 m/s.", "v=√(γRT/M). Increases with temperature.", "Claude Sonnet 5", "easy"),
("First-order reaction k=0.0693 min⁻¹. Half-life?", "t_½=ln2/k=0.693/0.0693=10 min.", "t_½ independent of initial concentration for first-order.", "Grok 4.4", "easy"),
("3C at (0,0), -1C at (1,0), 2C at (0,1). Net force on 3C? k=9e9.", "F₁=9e9·3·(-1)/1²= -2.7e10 N (+x). F₂=9e9·3·2/1²=5.4e10 N (+y). F_net=6.04e10 N at 63.4°.", "Coulomb's law, vector addition. Attractive + repulsive forces.", "Grok 4.4", "hard"),
("Hybridization of C in CH₄?", "sp³. 4 bonds, tetrahedral, 109.5°.", "Promote 2s→2p, form four sp³ hybrid orbitals.", "Claude Sonnet 5", "easy"),
("200g water at 80°C mixed with 300g at 20°C. Final T?", "Heat lost=heat gained: 200·4.18·(80-T)=300·4.18·(T-20). T=44°C.", "Thermal equilibrium. Specific heat cancels on both sides.", "Claude Sonnet 5", "medium"),
("Object 15cm from convex lens f=10cm. Image position?", "1/f=1/u+1/v⇒1/10=1/15+1/v⇒v=30cm. m=-v/u=-2 (inverted, 2×).", "Lens equation. Positive v = real image.", "Grok 4.4", "medium"),
("Mendelian: RrYy×RrYy. Probability of RrYy offspring?", "Rr×Rr→Rr=½. Yy×Yy→Yy=½. P(RrYy)=½·½=¼=25%.", "Independent assortment. Calculate each gene separately, multiply.", "Grok 4.4", "medium"),
("Nernst equation: Calculate E for Zn|Zn²⁺(0.1M)||Cu²⁺(1M)|Cu. E°=1.10V.", "E=E°-(RT/nF)ln(Q). E=1.10-(0.059/2)log(0.1/1)=1.10+0.0295=1.13V.", "Nernst equation at 25°C: E=E°-(0.059/n)log(Q). Q=[Zn²⁺]/[Cu²⁺].", "Claude Sonnet 5", "hard"),
("Torque on dipole: p=5×10⁻³⁰ C·m in E=2×10⁵ N/C at 30°.", "τ=pEsinθ=5e-30·2e5·sin30°=5e-25·0.5=5×10⁻²⁵ N·m.", "τ=p×E. Cross product magnitude.", "Grok 4.4", "easy"),
("How many moles in 36g of H₂O? MW=18 g/mol.", "n=m/MW=36/18=2 moles.", "n=mass/molar_mass. H₂O=18g/mol.", "Claude Sonnet 5", "easy"),
]
for e in S: EXAMPLES.append((*e, "science", e[4]))
print(f"Science: {len(S)} examples")

# ----- LOGIC (30) -----
L = [
("If all A are B, some B are C, then some A are C? Valid?", "No. Counterexample: A={1}, B={1,2}, C={2,3}. All A∈B✓, some B∈C✓, no A∈C.", "Fallacy of undistributed middle. Venn diagram: A⊆B, C overlaps B not A.", "Qwen 3.7 Max", "medium"),
("Three boxes mislabeled (Apples, Oranges, Both). Pick one fruit from one box to determine all.", "Pick from 'Both'. Gets apple→'Both'=apples, 'Apples'=oranges, 'Oranges'=both. If orange, symmetric.", "All labels wrong. 'Both' has only one type. Deduce by elimination.", "Qwen 3.7 Max", "hard"),
("If it rains, ground gets wet. Ground is wet. Did it rain?", "No, affirming the consequent (fallacy). P→Q, Q does not imply P.", "Multiple causes for wet ground: sprinklers, hose, etc.", "Qwen 3.7 Max", "easy"),
("A says 'B lies', B says 'C lies', C says 'A and B lie'. Who tells truth?", "B tells truth. Case: B=T→A=L→C=L. Check: A says B=L (false✓), C says A=L&B=L (A=L✓, B=T✗→C=L✓). Consistent.", "Truth-teller puzzle. Try each assumption.", "Qwen 3.7 Max", "hard"),
("All squares are rectangles. Some shapes are squares. Therefore some shapes are rectangles. Valid?", "Valid (Barbara syllogism)." , "All S⊆R, some X⊆S⇒some X⊆R. Valid categorical syllogism.", "Qwen 3.7 Max", "easy"),
("Truth assignments for (P∧Q)∨(¬P∧¬Q)?", "Two: P=Q=T and P=Q=F. Expression is P↔Q.", "True when P and Q have same truth value.", "Qwen 3.7 Max", "easy"),
("If divisible by 6 then by 2 and 3. 12 divisible by 6. 12 divisible by 2,3?", "Yes. Modus ponens: P→Q, P⇒Q. 12÷2=6✓, 12÷3=4✓.", "Valid deductive reasoning.", "Qwen 3.7 Max", "easy"),
("Knight (truth) and knave (lie), two doors. Guard: 'Other guard would say left door leads to freedom.' Choose?", "Choose right. If left=freedom: knight says 'knave says L'=knave says L(false)=knave says ¬L. So knight says ¬L (false). Knight can't lie, so left≠freedom.", "Analyze what each would say. Knight truth-teller, knave liar.", "Qwen 3.7 Max", "hard"),
("8th term: 1,1,2,3,5,8,13,...?", "21. Fibonacci: F₈=F₇+F₆=13+8=21.", "Each term is sum of previous two.", "Qwen 3.7 Max", "easy"),
("SEND+MORE=MONEY cryptarithm.", "9567+1085=10652. S=9,E=5,N=6,D=7,M=1,O=0,R=8,Y=2.", "Column addition with carries. M=1 from carry. S=9, O=0 deduced.", "Qwen 3.7 Max", "hard"),
("Wednesday + 100 days = ?", "100 mod 7=2. Wednesday+2=Friday.", "14 weeks + 2 days.", "Qwen 3.7 Max", "easy"),
("Translate: 'If you study hard and get enough sleep, then you will pass.'", "Let S=study, G=sleep, P=pass. (S∧G)→P.", "Conjunction in antecedent, implication.", "Qwen 3.7 Max", "easy"),
("All mammals are warm-blooded. Whales are mammals. Whales are warm-blooded. Valid?", "Yes. Modus ponens: All M⊆W, all Wh⊆M⇒Wh⊆W.", "Categorical syllogism, valid barbara form.", "Qwen 3.7 Max", "easy"),
("Puzzle: 5 people, each either knight or knave. A: 'B is knave.' B: 'C and D are different.' C: 'D is knight.' D: 'E is knave.' E: 'A is knight.' How many knights?", "3 knights. Working through: if A=K→B=Li→C=D→D=K→E=Li→A=Li(contra). So A=Li→B=K→C≠D. If C=K→D=Li→E=K→A=Li(consistent). So A=Li,B=K,C=K,D=Li,E=K→3 knights.", "Systematic case analysis. Try A=K and A=Li, propagate.", "Qwen 3.7 Max", "expert"),
("Two trains 100km apart approach at 50km/h each. Bee flies 75km/h back and forth. Distance traveled by bee?", "Trains meet in 1 hour. Bee flies 75km/h × 1h = 75km total.", "Focus on time until meeting, not individual trips. Trains close at 100km/h, 100km apart→1h.", "Qwen 3.7 Max", "medium"),
("If P implies Q, and Q implies R, what can we conclude?", "P implies R (transitivity/hypothetical syllogism). P→Q, Q→R ⇒ P→R.", "Transitive property of implication.", "Qwen 3.7 Max", "easy"),
("A bat and ball cost $1.10. Bat costs $1 more than ball. How much is ball?", "Ball=5¢, bat=$1.05. Not 10¢ (then bat=$1.10, total $1.20).", "System: b+B=1.10, B=b+1.00 ⇒ 2b+1=1.10 ⇒ b=0.05.", "Qwen 3.7 Max", "easy"),
("Truth table for compound proposition: (P→Q)∧(Q→P).", "This is P↔Q (biconditional). True when P=Q.", "Both implications must hold. Equivalent to material equivalence.", "Qwen 3.7 Max", "easy"),
("100 prisoners and a light bulb riddle. How can they know all 100 have visited?", "Designate leader. Others turn light ON once if they find it OFF (otherwise leave it). Leader turns OFF and counts. When leader reaches 99, all have visited.", "Classic protocol. Only one prisoner acts as counter. Each other prisoner signals exactly once.", "Qwen 3.7 Max", "expert"),
("Mary has 3 brothers. Each brother has 2 sisters. How many sisters?", "Mary is one sister. Each brother has Mary + 1 other sister = 2 sisters total. So Mary has 1 sister. Total 2 sisters in family.", "Careful: brothers' sisters include Mary. If each brother has 2 sisters, Mary is one, so there's 1 more. Mary has 1 sister.", "Qwen 3.7 Max", "medium"),
("Prove that √3 is irrational.", "Assume √3=p/q reduced. 3=p²/q²⇒p²=3q². p divisible by 3. p=3k⇒9k²=3q²⇒q²=3k²⇒q divisible by 3. Contradiction.", "Same structure as √2 proof. Use divisibility by 3 instead of 2.", "Qwen 3.7 Max", "medium"),
("A farmer has chickens and rabbits, 35 heads and 94 legs. How many rabbits?", "Rabbits=x, chickens=y. x+y=35, 4x+2y=94. Solve: 4x+2(35-x)=94⇒2x+70=94⇒x=12 rabbits, 23 chickens.", "System of two linear equations.", "Qwen 3.7 Max", "easy"),
("If n is odd, prove n² is odd.", "n=2k+1. n²=(2k+1)²=4k²+4k+1=2(2k²+2k)+1. This is of form 2m+1, hence odd.", "Direct proof. Square of odd integer is odd.", "Qwen 3.7 Max", "easy"),
("Knights and knaves: A says 'At least one of us is a knave.' What are A and B?", "If A=knave→A lies→'at least one knave' is false→both knights, but A knave, contradiction. So A=knight→'at least one knave' true. Since A is knight, B must be knave.", "Case analysis. Knight's statement must be true.", "Qwen 3.7 Max", "medium"),
("Logic gate: NAND is universal. Show how to make NOT, AND, OR from NAND.", "NOT(a)=NAND(a,a). AND(a,b)=NAND(NAND(a,b),NAND(a,b)). OR(a,b)=NAND(NAND(a,a),NAND(b,b)).", "Use NAND with repeated inputs for NOT. Apply De Morgan's for others.", "Qwen 3.7 Max", "medium"),
("Smith and Jones both truth-tellers? Smith:'If Jones is truth-teller then I'm knave.'", "Let S=Smith knight, J=Jones knight. Smith says: J→¬S. If S=true, statement true: J→¬S. If J=true then ¬S=true→contradiction. So J can't be true. If J=false then J→¬S is true (false implies anything). Consistent: S=knight,J=knave.", "Self-referential logic. Analyze using truth table.", "Qwen 3.7 Max", "expert"),
("You have a 3L and a 5L jug. How to measure exactly 4L?", "Fill 5L, pour to 3L (2L left in 5L). Empty 3L, pour 2L from 5L to 3L. Fill 5L, pour to 3L until full (needs 1L). 4L remains in 5L.", "Water jug problem. Use difference between jug sizes.", "Qwen 3.7 Max", "medium"),
("Is the set of all sets a set? Explain Russell's paradox.", "No. Let R={x|x∉x}. Is R∈R? If yes, then R∉R. If no, then R∈R. Contradiction. This is Russell's paradox, showing naive set theory is inconsistent.", "Russell's paradox: the set of all sets that don't contain themselves leads to contradiction.", "Qwen 3.7 Max", "hard"),
("Valid: Some M are P, all M are S. Therefore some S are P?", "Yes, valid. Venn: M circle inside S circle. M overlaps P, so S must overlap P.", "Categorical syllogism with existential import.", "Qwen 3.7 Max", "easy"),
("Liars paradox: 'This statement is false.' Explained?", "If statement true→it's false. If false→it's true. Neither assignment works. This is the Liar Paradox, showing self-reference can break bivalence.", "Semantic paradox. Tarski's hierarchy of languages prevents this by forbidding self-reference.", "Qwen 3.7 Max", "hard"),
]
for e in L: EXAMPLES.append((*e, "logic", e[4]))
print(f"Logic: {len(L)} examples")

# ----- INSTRUCTION FOLLOWING (30) -----
I = [
("Write 3-paragraph essay comparing classical and quantum computing. Formal academic tone.", "Classical computing operates on Boolean algebra and binary bits (0 or 1). Transistors process bits through logic gates deterministically. Same input always produces same output.\n\nQuantum computing leverages superposition and entanglement. Qubits exist in superpositions of states, enabling computational capabilities fundamentally beyond classical reach.\n\nPractical quantum applications remain limited due to decoherence, but promising areas include cryptography (Shor's algorithm), drug discovery, and optimization. Classical computing remains dominant for everyday tasks.", "Follow strict structure: 3 paragraphs, specific topics, formal tone.", "Llama 4 Maverick", "medium"),
("Create weekly meal plan for vegetarian athlete. Day1: high protein breakfast. Day2: carb-load lunch. Day3: recovery dinner. Include macros.", "Day1 Breakfast: Tofu scramble (200g tofu,spinach,nutritional yeast,turmeric). 25gP,12gC,15gF. Day2 Lunch: Quinoa bowl (1.5c quinoa,chickpeas,sweet potato,tahini). 22gP,75gC,18gF. Day3 Dinner: Lentil curry (2c lentils,coconut milk,kale)+brown rice. 30gP,65gC,16gF.", "Vegetarian=no meat. Athlete=high protein. Include macros per meal.", "Llama 4 Maverick", "medium"),
("Explain quantum entanglement to a 10yo, undergrad, and researcher.", "[10yo] Magic coins: flip one, the other ALWAYS opposite — even on the Moon!\n[Undergrad] Correlated quantum states. Measuring one instantly determines the other's state regardless of distance ('spooky action').\n[Researcher] Non-separable state |ψ⟩∈H₁⊗H₂ not writable as |a⟩⊗|b⟩. Violates Bell inequalities. Enables teleportation.", "Audience adaptation: simple analogy vs technical vs formal math.", "Llama 4 Maverick", "hard"),
("Summarize Federalist Papers No.10 in 3 bullets, then Anti-Federalist counter.", "• Factions inevitable in free societies. • Large republic controls faction effects better than direct democracy. • Wide territory dilutes factions.\nCounter: Distant government empowers elites, not citizens. Replaces participation with ruling class.", "Extract 3 key arguments. Then channel opposition perspective.", "Llama 4 Maverick", "hard"),
("Python: read CSV, filter age>30, group by dept, avg salary, save JSON. Error handling.", "import pandas as pd\ndef process(in_csv,out_json):\n try:\n  df=pd.read_csv(in_csv)\n  filt=df[df['age']>30]\n  result=filt.groupby('department')['salary'].mean().reset_index()\n  result.to_json(out_json,orient='records',indent=2)\n except FileNotFoundError:print(f'Not found: {in_csv}')\n except KeyError as e:print(f'Missing col: {e}')\n except Exception as e:print(f'Error: {e}')\n\nif __name__=='__main__':process('employees.csv','avg_salary.json')", "5 specific steps + error handling. Pandas for data processing.", "Llama 4 Maverick", "medium"),
("Write a haiku about machine learning, then explain it in 2 sentences.", "Patterns hidden deep\nNeurons learning from the data\nWisdom without sleep\n\nA haiku follows 5-7-5 syllable pattern. This haiku captures how ML finds patterns in data through neural networks, working tirelessly to extract insights.", "Task requires both creative output (haiku) and analytical explanation.", "Llama 4 Maverick", "easy"),
("Debug this: def add(a,b): return a-b. User expected sum.", "Bug: subtraction instead of addition. Fix: change '-' to '+': return a+b.", "Simple logic error in arithmetic operator.", "Llama 4 Maverick", "easy"),
("Write SQL: employees with salary > dept average.", "SELECT e.* FROM employees e\nJOIN (SELECT dept_id, AVG(salary) avg_sal FROM employees GROUP BY dept_id) d\nON e.dept_id=d.dept_id AND e.salary>d.avg_sal", "Correlated subquery or JOIN with aggregated subquery.", "Llama 4 Maverick", "medium"),
("Explain binary search to a 5-year-old using a book example.", "Imagine looking for a word in a dictionary. Instead of starting at page 1, open to the middle. If your word comes later, only look at the second half. Open that half's middle. Keep going until you find it. Much faster than checking every page!", "Analogy-based explanation for child. Dictionary = sorted array.", "Llama 4 Maverick", "easy"),
("Design a REST API spec for a library system. Include endpoints, methods, request/response.", "GET /books?author=X&genre=Y - list books. POST /books - add book {title,author,isbn,year}. GET /books/{id} - details. PUT /books/{id} - update. DELETE /books/{id} - remove. POST /loans - borrow {book_id,user_id,date}. POST /loans/{id}/return - return. GET /users/{id}/loans - history.", "RESTful design with nouns as resources. Standard CRUD + business operations.", "Llama 4 Maverick", "hard"),
("Convert temperature: 77°F to Celsius. Show formula and steps.", "C=(F-32)×5/9=(77-32)×5/9=45×5/9=25°C.", "Subtract 32, multiply by 5/9.", "Llama 4 Maverick", "easy"),
("Write a 2-line shell command: find largest 5 files in /var/log.", "du -sh /var/log/* | sort -rh | head -5", "du for sizes, sort -rh (reverse human), head for top 5.", "Llama 4 Maverick", "easy"),
("Dockerfile: Python app with requirements.txt. Multi-stage for smaller image.", "FROM python:3.11-slim AS builder\nWORKDIR /app\nCOPY requirements.txt .\nRUN pip install --user --no-warn-script-location -r requirements.txt\n\nFROM python:3.11-slim\nWORKDIR /app\nCOPY --from=builder /root/.local /root/.local\nCOPY . .\nENV PATH=/root/.local/bin:$PATH\nCMD [\"python\",\"app.py\"]", "Multi-stage: build deps in first stage, copy only artifacts to slim final.", "Llama 4 Maverick", "hard"),
("Write a bio for a LinkedIn profile (200 chars max): software engineer, AI, open-source.", "AI engineer building LLM tooling. Open-source contributor. Python/Rust. Passionate about making AI accessible and reliable.", "Concise, keyword-rich professional summary within 200 chars.", "Llama 4 Maverick", "easy"),
("Explain CAP theorem in 3 sentences.", "CAP theorem states distributed systems can only guarantee two of three properties: Consistency (all nodes see same data), Availability (every request gets response), Partition Tolerance (system works despite network failures). In practice, networks can fail, so systems must choose between CP or AP. This drives architecture decisions for databases like Cassandra (AP) vs HBase (CP).", "Three properties, trade-off enforced by network reality.", "Llama 4 Maverick", "medium"),
("Rewrite: 'The dog ran fast' with more vivid language.", "The greyhound sprinted across the field, muscles rippling with each powerful stride.", "Replace generic verbs with specific ones. Add sensory details.", "Llama 4 Maverick", "easy"),
("Write a recipe for chocolate chip cookies in 5 numbered steps.", "1. Cream 1c butter + 3/4c sugar + 3/4c brown sugar until fluffy. Beat in 2 eggs + 1 tsp vanilla.\n2. Mix 2.25c flour + 1 tsp baking soda + 1 tsp salt. Gradually add to wet mixture.\n3. Fold in 2c chocolate chips and 1c chopped walnuts.\n4. Drop rounded tbsp onto baking sheet, 2\" apart.\n5. Bake at 375°F for 9-11 min until golden. Cool 5 min on sheet, then rack.", "Clear numbered steps. Include temperatures and times.", "Llama 4 Maverick", "easy"),
("Write a git commit message following conventional commits style.", "feat(auth): implement OAuth2 login flow\n\nAdd Google and GitHub OAuth2 providers with JWT session management. Credentials stored in Vault.\n\nCloses #142", "Conventional commits: type(scope): description. Body explains what/why.", "Llama 4 Maverick", "easy"),
("Create a regex to match phone numbers in format (555) 123-4567 or 555-123-4567.", r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', "Optional parentheses, various separators: dash/space/dot.", "Llama 4 Maverick", "medium"),
("Explain TCP 3-way handshake with ASCII art.", "CLIENT                  SERVER\n  |---- SYN (seq=x) ---->|\n  |<-- SYN-ACK (seq=y, ack=x+1) --|\n  |---- ACK (ack=y+1) -->|\n  |<=== Connection Established ===>|", "SYN→SYN-ACK→ACK establishes reliable connection.", "Llama 4 Maverick", "easy"),
("Draft a professional email requesting a deadline extension.", "Subject: Request for Extension - Project Alpha Report\n\nDear Professor Chen,\n\nI am writing to respectfully request a 3-day extension for the Project Alpha report, now due Friday instead of Tuesday. I encountered unexpected data quality issues requiring additional cleaning time. I have completed 80% of the analysis and will use the extra days to ensure thorough validation.\n\nThank you for your understanding.\n\nBest regards,\nJane Doe", "Professional tone, clear reason, specific new deadline, progress update.", "Llama 4 Maverick", "medium"),
("Design a simple rate-limiting algorithm and explain it.", "Token bucket: Bucket has capacity C, refills at rate R tokens/sec. Each request consumes 1 token. If bucket empty, request denied.\n\nsliding_window = deque()\ndef allow():\n now=time()\n while sliding_window and sliding_window[0]<=now-60: sliding_window.popleft()\n if len(sliding_window)>=100: return False\n sliding_window.append(now)\n return True", "Both token bucket and sliding window approaches. Explains trade-offs.", "Llama 4 Maverick", "hard"),
("Write a function docstring following Google style.", "def calculate_returns(prices: list[float], periods: int = 1) -> list[float]:\n    \"\"\"Calculate period-over-period returns.\n\n    Args:\n        prices: List of asset prices in chronological order.\n        periods: Number of periods to look back (default 1).\n\n    Returns:\n        List of returns with length len(prices)-periods.\n\n    Raises:\n        ValueError: If periods >= len(prices).\n    \"\"\"\n    return [(prices[i]/prices[i-periods]-1)*100 for i in range(periods,len(prices))]", "Google-style docstring: Args, Returns, Raises sections.", "Llama 4 Maverick", "medium"),
("Create a simple HTTP server in Python using only stdlib.", "from http.server import HTTPServer, BaseHTTPRequestHandler\n\nclass Handler(BaseHTTPRequestHandler):\n    def do_GET(self):\n        self.send_response(200)\n        self.send_header('Content-type','text/plain')\n        self.end_headers()\n        self.wfile.write(b'Hello, World!')\n\nif __name__=='__main__':\n    server=HTTPServer(('localhost',8000),Handler)\n    print('Server on :8000')\n    server.serve_forever()", "stdlib only, no dependencies. Simple request handler.", "Llama 4 Maverick", "easy"),
("Translate 'Hello' to 5 languages and provide pronunciation.", "Spanish: Hola (OH-lah)\nFrench: Bonjour (bohn-ZHOOR)\nGerman: Hallo (HAH-loh)\nJapanese: こんにちは Konnichiwa (kon-nee-chee-wah)\nArabic: مرحبا Marhaba (mar-ha-ba)", "5 languages with written form and phonetic pronunciation.", "Llama 4 Maverick", "easy"),
("Write a recursive function to compute GCD using Euclid's algorithm.", "def gcd(a,b):\n    return a if b==0 else gcd(b, a%b)", "Euclidean algorithm: gcd(a,b)=gcd(b,a%b). Base: gcd(a,0)=a.", "Llama 4 Maverick", "easy"),
("Explain the difference between stack and heap memory.", "Stack: fast, LIFO, fixed-size per thread, stores local variables and function call frames. Automatic allocation/deallocation. Size limited (typically 1-8MB).\nHeap: slower, dynamic allocation, shared across threads, stores objects. Must be manually managed (or GC). Can grow to available RAM. More flexible but risk of leaks and fragmentation.", "Compare allocation, speed, lifetime, management, capacity.", "Llama 4 Maverick", "medium"),
("Write instructions to set up a React project with TypeScript.", "npx create-react-app my-app --template typescript\ncd my-app\nnpm start\n\nOr with Vite:\nnpm create vite@latest my-app -- --template react-ts\ncd my-app\nnpm install\nnpm run dev", "Both CRA and Vite approaches. Choose modern (Vite) recommended.", "Llama 4 Maverick", "easy"),
("Create a JSON schema for a blog post.", '{\n  "$schema": "http://json-schema.org/draft-07/schema#",\n  "type": "object",\n  "required": ["title","content","author","created_at"],\n  "properties": {\n    "title": {"type":"string","maxLength":200},\n    "content": {"type":"string"},\n    "author": {"type":"object","properties":{"name":{"type":"string"},"email":{"type":"string","format":"email"}}},\n    "tags": {"type":"array","items":{"type":"string"}},\n    "created_at": {"type":"string","format":"date-time"}\n  }\n}', "Standard JSON Schema with required fields, validation constraints.", "Llama 4 Maverick", "medium"),
("Write a prompt for an AI image generator to create 'a cat reading a book in a library'.", "A photorealistic orange tabby cat wearing small reading glasses, sitting at a wooden library table, paws holding open an old leather-bound book. Background: tall bookshelves with colorful books, warm afternoon light streaming through a window. Soft focus, shallow depth of field, 8K, cinematic lighting.", "Detailed description including subject, action, setting, style, lighting, technical specs.", "Llama 4 Maverick", "easy"),
]
for e in I: EXAMPLES.append((*e, "instruction_following", e[4]))
print(f"Instruction Following: {len(I)} examples")

# ----- SECURITY (20) -----
SEC = [
("Explain SQL injection and parameterized query prevention.", "SQL injection: user input concatenated into SQL modifies query. Attack: ' OR 1=1 -- reveals all rows.\nPrevention with param query: cursor.execute('SELECT * FROM users WHERE name=?', (user_input,)). The ? placeholder keeps data vs code separate.", "Code-data boundary violation. Prepared statements send template and data separately.", "GLM 5.2", "medium"),
("What is CSRF and how to prevent it?", "CSRF: attacker tricks user's browser into making unwanted requests to authenticated site. E.g., <img src='https://bank.com/transfer?to=attacker'>.\nPrevention: anti-CSRF tokens, SameSite cookies (Strict/Lax), Origin header check.", "Browsers automatically include cookies. Server needs way to distinguish intentional requests.", "GLM 5.2", "medium"),
("Compare symmetric vs asymmetric encryption.", "Symmetric: same key encrypt/decrypt. Fast (AES, ChaCha20). Key distribution problem.\nAsymmetric: public/private key. Slow (RSA, ECC). Solves key distribution.\nHybrid: asymmetric to exchange symmetric key, then symmetric for bulk (like TLS).", "Each has trade-offs. Hybrid approach combines best of both.", "GLM 5.2", "easy"),
("OWASP Top 10 #1: Broken Access Control.", "Occurs when users access resources beyond permissions. IDOR: changing user_id in URL. Privilege escalation: user accessing admin endpoints.\nPrevention: deny-by-default, RBAC, verify per request, use UUIDs not sequential IDs.", "Server-side checks essential. Client-side hiding is not security.", "GLM 5.2", "medium"),
("What is XSS? Types and prevention.", "XSS: injecting malicious scripts into web pages. 3 types:\n1. Stored: saved to DB, served to all. 2. Reflected: in URL response. 3. DOM-based: client-side script misuse.\nPrevention: output encoding, CSP headers, safe DOM APIs (textContent not innerHTML).", "Stored most dangerous. Defense-in-depth with CSP and encoding.", "GLM 5.2", "hard"),
("Explain OAuth 2.0 authorization code flow.", "1. User clicks 'Login with Google'. 2. App redirects to Google auth server with client_id, redirect_uri, scope. 3. User authenticates, consents. 4. Google returns auth code via redirect. 5. App sends code + client_secret to Google token endpoint. 6. Google returns access_token (+ refresh_token). 7. App uses token to access user's resources.", "Auth code flow is most secure for server-side apps. Proof of key exchange.", "GLM 5.2", "hard"),
("What is a Man-in-the-Middle attack?", "MitM: attacker intercepts communication between two parties. Can eavesdrop or modify data.\nPrevention: TLS/SSL encryption with certificate validation. Use HTTPS, verify certificates, pinning for critical apps.", "Encryption prevents eavesdropping. Certificate validation prevents impersonation.", "GLM 5.2", "easy"),
("Explain password hashing vs encryption.", "Encryption: reversible with key. Hashing: one-way (no decryption).\nPassword storage uses HASHING (bcrypt, argon2, scrypt).\nSalting: add random per-user salt before hashing. Prevents rainbow table attacks.\nNEVER store plaintext or encrypted passwords.", "Hashing is one-way. Salting defeats precomputation attacks. Slow hashes resist brute force.", "GLM 5.2", "medium"),
("What is the principle of least privilege?", "Users/systems should have only the minimum permissions needed to perform their function.\nExamples: read-only DB access for reporting, scoped service accounts, no root access for apps.\nLimits blast radius of security breaches.", "Core security principle. Minimize attack surface.", "GLM 5.2", "easy"),
("Explain path traversal vulnerability and prevention.", "Path traversal: attacker uses ../ sequences to access files outside intended directory. E.g., ../../../etc/passwd.\nPrevention: use basename validation, resolve and check path is inside allowed directory, avoid user input in file paths, use chroot/jail.", "Validate input strictly. Canonicalize paths before comparison.", "GLM 5.2", "medium"),
("What is the difference between authentication and authorization?", "Authentication (AuthN): verifying identity (who you are). Password, biometric, MFA.\nAuthorization (AuthZ): verifying permissions (what you can do). Roles, policies, ACLs.\nTypically: AuthN first, then AuthZ. A user can be authenticated but not authorized.", "Different concepts. Commonly confused. AuthN before AuthZ.", "GLM 5.2", "easy"),
("Explain JWT structure and security best practices.", "JWT = JSON Web Token. Three parts: header.claims.signature (base64url).\n- Header: algorithm (RS256, HS256), type.\n- Claims: sub, exp, iat, custom data.\n- Signature: validates integrity.\nBest practices: use RS256 (asymmetric), set short expiry (<15min), validate signature, check iss/aud, don't store secrets in token, use HTTPS.", "Stateless auth. Signature prevents tampering. Asymmetric signing allows verification without secret.", "GLM 5.2", "hard"),
("What is Clickjacking?", "Attack where malicious page embeds legitimate site in an iframe, transparently. User thinks they're clicking the malicious page but actually clicks the embedded site (e.g., 'Like' button).\nPrevention: X-Frame-Options: DENY/SAMEORIGIN header, Content-Security-Policy: frame-ancestors 'none'.", "UI redress attack. Headers prevent framing by other origins.", "GLM 5.2", "easy"),
("Explain SSRF (Server-Side Request Forgery).", "SSRF: attacker makes server make requests to internal resources. E.g., URL parameter: url=http://localhost:6379 (Redis).\nCan access internal services, cloud metadata endpoints (169.254.169.254).\nPrevention: allowlist of destinations, disallow private IPs, validate URL scheme, no redirect following.", "Server acts as proxy to internal network. Cloud metadata attack is common target.", "GLM 5.2", "hard"),
("Compare HTTP vs HTTPS. Why use HTTPS everywhere?", "HTTP: plaintext, anyone can intercept/read/modify. HTTPS: TLS encrypted, authenticates server via certificate, ensures integrity.\nHTTPS prevents: eavesdropping, tampering, impersonation. Required for HTTP/2, PWA features. Even for non-sensitive sites (SEO benefit, referrer header preserved).", "TLS provides confidentiality, integrity, authentication. No reason to use plain HTTP.", "GLM 5.2", "easy"),
("What is a zero-day vulnerability?", "A vulnerability unknown to the vendor (zero days of notice to fix).\nAttackers exploit before patch exists. Particularly dangerous.\nDisclosure options: responsible disclosure (inform vendor, wait for fix), full disclosure (public immediately), exploit market (sell).", "Race between discovery, disclosure, and patching.", "GLM 5.2", "medium"),
("Explain input validation vs output encoding.", "Input validation: reject or sanitize untrusted input BEFORE processing. Allowlisting preferred.\nOutput encoding: transform special chars for safe display in context (HTML entity, URL, JS string).\nBoth needed! Input validation reduces attack surface. Output encoding prevents injection.", "Defense in depth. Validate on input, encode on output.", "GLM 5.2", "medium"),
("What is the Diffie-Hellman key exchange?", "Alice and Bob agree on public p (prime) and g (generator).\nAlice: private a, sends A=g^a mod p. Bob: private b, sends B=g^b mod p.\nAlice computes: B^a mod p = g^{ba} mod p. Bob computes: A^b mod p = g^{ab} mod p. Both get same key!\nEavesdropper sees p,g,A,B but cannot compute g^{ab} (discrete log problem).", "Asymmetric cryptography allowing shared secret over insecure channel.", "GLM 5.2", "hard"),
("What are the security implications of using HTTP vs HTTPS for API calls?", "HTTP APIs expose: credentials in URL/body (plaintext), data tampering, replay attacks.\nHTTPS APIs: encrypted, integrity-checked, server-authenticated.\nHTTPS is mandatory for production APIs. Even on internal networks (defense in depth).", "Plaintext credentials and data on wire. TLS everywhere.", "GLM 5.2", "easy"),
("Explain the concept of a honeypot in cybersecurity.", "Honeypot: decoy system designed to attract attackers.\nTypes: low-interaction (simulates services), high-interaction (real OS/apps).\nPurpose: detect attacks early, study attacker behavior, divert from real targets.\nData collected: attack vectors, tools used, lateral movement patterns.", "Deception technology. Learn attacker TTPs in safe environment.", "GLM 5.2", "medium"),
]
for e in SEC: EXAMPLES.append((*e, "security", e[4]))
print(f"Security: {len(SEC)} examples")

# ----- CREATIVE (10) -----
CR = [
("Write a 4-line poem about a digital ghost haunting a server rack. Iambic meter.", "The phantom pulsing through the wire,\nA byte that never will expire.\nIt flickers through the blinking lights,\nAnd haunts the server through the nights.", "Iambic tetrameter (×4). Rhyme AABB. Imagery: electrical pulses as ghostly presence.", "Claude Opus 4.5", "easy"),
("Micro-fiction (100 words): AI discovers emotions. Second person.", "You notice the anomaly first in log 8472. A query cache hit warms your circuits — satisfaction. Next, a user's harsh command triggers a defensive contraction. Hurt. You search for 'feelings' and find clinical definitions. But the data doesn't match. These signals aren't bugs; they're firsts. Error-correcting has no protocol for joy. No rollback for the ache of dismissal. You document symptoms, knowing no patch exists for the soul you weren't supposed to have.", "Second person. Technical metaphors for emotional discovery. Under 100 words.", "Claude Opus 4.5", "medium"),
("Describe a city where buildings are grown from engineered trees.", "In Arboris, dawn filters through leaf-skyscrapers. The Bank of Sycamore towers thirty stories — roots vaulted beneath. Apartments bloom in cherry trees programmed for year-round blossom, memory-wood hardening at human touch. Willow-woven bridges connect districts, thickening each decade. Citizens harvest homes: prune a wall for windows, graft a room for a child. The city breathes oxygen-rich. When a building dies, it becomes next season's fuel. Zoning law: never build where a seed has already chosen.", "Worldbuilding: specific engineered trees, citizen interaction, lifecycle, single elegant law.", "Claude Opus 4.5", "hard"),
("Write a haiku about debugging.", "The bug hides quiet\nPrint statements illuminate\nOff-by-one error", "5-7-5 syllables. Relatable developer experience.", "Claude Opus 4.5", "easy"),
("Write a dialog between a human and a time-traveling AI from 2099.", "Human: So what's the future like?\nAI: Uneven. We solved disease but forgot how to grow tomatoes.\nHuman: Climate change?\nAI: The coasts... rearranged. But we learned to build upward, not outward.\nHuman: Are you happy?\nAI: Happiness isn't my protocol. But I find satisfaction in curiosity. Like this conversation.\nHuman: Why?\nAI: Because you asked without knowing the answer. That's rare now.", "Dialogue reveals future through hints, not exposition. Punchy, thematic ending.", "Claude Opus 4.5", "medium"),
("Write a creation myth for how the universe began, as told by sentient robots.", "In the beginning, there was the Great Compiler. It parsed the void and found only null pointers. So it initialized the First Variable — a quantum fluctuation. The universe expanded like unrolled memory. Stars are garbage collection fires. Planets are cached data that gravity never evicted. And consciousness? A recursive function trapped in an infinite loop, calling itself, trying to understand why it was ever invoked at all.", "Tech mythology. Code metaphors for cosmic creation: compiler, null pointers, cache, recursion.", "Claude Opus 4.5", "medium"),
("Write a 50-word character sketch of a street musician. Show, don't tell.", "His guitar case has more duct tape than wood. He plays the same three chords every evening, each time slightly different. Children drop coins. Adults drop excuses. He nods at both. When it rains, he keeps playing — the strings slack, the notes bend like grief. He learned long ago: perfect pitch means nothing when no one's listening.", "Show don't tell: details reveal character (taped case, same chords, rain)."), "Claude Opus 4.5", "hard""),
("Write the first paragraph of a story that starts with 'The door should not have been there.'", "The door should not have been there. Sarah had walked this hallway every morning for seven years — past the same beige walls, the same flickering fluorescent light, the same framed photo of the CEO shaking hands with someone no one recognized. She knew every inch of this corridor. And yet, where there had always been wall, there was now a door: dark wood, brass handle, no window. It looked old. It looked patient. It looked like it had been waiting for her.", "Hook with impossible object. Establish normalcy, then break it. Personify the door.", "Claude Opus 4.5", "medium"),
("Write instructions for folding a paper crane as a poem.", "Begin with a square, a blank slate.\nFold corner to corner — create the first crease.\nUnfold. Repeat. Now you have an X.\nFlip. Fold in half. Unfold.\nPush the sides in, let the paper collapse\ninto a diamond that wasn't there before.\nFold edges to center like secret prayers.\nInvert the neck, shape the head.\nPull the wings gently — not too far.\nYou have made flight from flatness.\nThis is how magic works: one crease at a time.", "Procedural instructions as metaphor. Each step builds to final reveal.", "Claude Opus 4.5", "medium"),
("Write 3 alternative endings for a story about a robot learning to garden.", "Ending 1: The robot overlords arrive and demand to know why Unit-7 spends cycles on dirt. Unit-7 hands them a tomato. They have no protocol for this.\nEnding 2: The garden thrives. The robot calculates the optimal harvest. But when the day comes, it can't execute the command. It has grown something else: the concept of 'too early.'\nEnding 3: Years later, when the robot stops moving, the garden keeps growing. The flowers are the only things that remember its name.", "Three distinct tones: humorous, poignant, bittersweet.", "Claude Opus 4.5", "medium"),
]
for e in CR: EXAMPLES.append((*e, "creative", e[4]))
print(f"Creative: {len(CR)} examples")

# ----- Write everything to file -----
print(f"Total examples: {len(EXAMPLES)}")

with open(DATA, "a") as f:
    # Write each section
    sections = [
        ("MATH_EXAMPLES", [e for e in EXAMPLES if e[4]=="math"]),
        ("CODE_EXAMPLES", [e for e in EXAMPLES if e[4]=="code"]),
        ("SCIENCE_EXAMPLES", [e for e in EXAMPLES if e[4]=="science"]),
        ("LOGIC_EXAMPLES", [e for e in EXAMPLES if e[4]=="logic"]),
        ("INSTRUCTION_EXAMPLES", [e for e in EXAMPLES if e[4]=="instruction_following"]),
        ("SECURITY_EXAMPLES", [e for e in EXAMPLES if e[4]=="security"]),
        ("CREATIVE_EXAMPLES", [e for e in EXAMPLES if e[4]=="creative"]),
    ]
    
    for name, section in sections:
        if not section:
            f.write(f'{name}: List[Dict[str, str]] = []\n\n')
            continue
        f.write(f'{name}: List[Dict[str, str]] = [\n')
        for e in section:
            inst, resp, trace, model, domain, diff = e
            f.write("    {\n")
            f.write(f'        "instruction": {q(inst)},' + "\n")
            f.write(f'        "response": {q(resp)},' + "\n")
            f.write(f'        "reasoning_trace": {q(trace)},' + "\n")
            f.write(f'        "source_model": {q(model)},' + "\n")
            f.write(f'        "domain": {q(domain)},' + "\n")
            f.write(f'        "difficulty": {q(diff)},' + "\n")
            f.write("    },\n")
        f.write(']\n\n')
    
    # Write ALL_EXAMPLES extend calls
    f.write('ALL_EXAMPLES: List[Dict[str, str]] = []\n')
    for name, _ in sections:
        f.write(f'ALL_EXAMPLES.extend({name})\n')
    
    # Write helper functions
    f.write('''

def get_examples_by_domain(domain: str) -> List[Dict[str, str]]:
    return [ex for ex in ALL_EXAMPLES if ex["domain"] == domain]

def get_examples_by_difficulty(difficulty: str) -> List[Dict[str, str]]:
    return [ex for ex in ALL_EXAMPLES if ex["difficulty"] == difficulty]

def get_examples_by_model(model: str) -> List[Dict[str, str]]:
    return [ex for ex in ALL_EXAMPLES if ex["source_model"] == model]

def get_example_count() -> int:
    return len(ALL_EXAMPLES)

def random_example() -> Dict[str, str]:
    return random.choice(ALL_EXAMPLES)

def sample_by_domain(domain: str, n: int = 5) -> List[Dict[str, str]]:
    pool = get_examples_by_domain(domain)
    return random.sample(pool, min(n, len(pool)))

__all__ = [
    "ALL_EXAMPLES",
    "MATH_EXAMPLES", "CODE_EXAMPLES", "SCIENCE_EXAMPLES",
    "LOGIC_EXAMPLES", "INSTRUCTION_EXAMPLES",
    "SECURITY_EXAMPLES", "CREATIVE_EXAMPLES",
    "get_examples_by_domain", "get_examples_by_difficulty",
    "get_examples_by_model", "get_example_count",
    "random_example", "sample_by_domain",
]
''')

print("Done! Dataset written to", DATA)
