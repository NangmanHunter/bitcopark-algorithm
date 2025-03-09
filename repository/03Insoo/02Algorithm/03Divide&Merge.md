
# 
problem  
ㄴbase case  
ㄴrecursive case  
　ㄴDivde  
　ㄴConquer  
　ㄴCombine  


# Strassen’s algorithm
행렬곱셈  
ㄴnxn  
ㄴ$O(n^{3})$

Strassen’s algorithm  
ㄴ행렬곱셈  
ㄴ시간복잡도  
ㄴ $O(n^{log_2 7}) ~ O(n^{2.81})$
#
Strassen’s algorithm  
$T(n)=7T(n/2)+\Theta(n^2)$
#
Master-Thm  
$T(n)=aT(n/b)+\Theta(n^d)$  
$a>b^d$  
$T(n)=O(n^{log_b a})$  
# Master-Thm  
$a>b^d$  
$T(n)=O(n^{log_b a})$  
$a=b^d$  
$T(n)=O(n^d log_n)$  
$a<b^d$  
$T(n)=O(n^d)$  
#
$O(n^d)$
$O(\frac{an^d}{b^d})$
$O(\frac{a^2 n^d}{b^{2d}})$
$O(\frac{a^3 n^d}{b^{3d}})$
...
$O(\frac{a^k n^d}{b^{kd}})$

$T(n)=O(n^d) + O(\frac{an^d}{b^d}) + O(\frac{a^2 n^d}{b^{2d}}) ...$  
$T(n)=O(n^d + \frac{an^d}{b^d} + \frac{a^2 n^d}{b^{2d}} ...)$  
$T(n)=O(n^d(1+ \frac{a}{b^d} + \frac{a^2 }{b^{2d}} ...))$  
$T(n)=O(n^d(1+ (\frac{a}{b^d})^1 + (\frac{a }{b^{d}})^2 ...))$  
#
트리높이▶$log_b n$  
트리깊이▶$log_b n$  
트리개수▶$log_b n$  
레벨개수▶$log_b n$  
트리레벨▶$log_b n$  
트리레벨▶$k$  
$k$개  
$k$개수  
$k$개항  
$k$항  
$log_b n$항 
#
0레벨▶$n$  
1레벨▶$n/b$  
2레벨▶$n/b^2$  
k레벨▶$n/b^k$  
$n/b^k$=1  
$n=b^k$  
$log_b n=k$  
$k=log_b n$  
#
$T(n)=O(n^d(\sum_{k=0}^{log_b n} (\frac{a}{b^d})^k))$  
#
$S=1+r+r^2 ...$  
$S=\frac{r^n-1}{r-1}$  

#
$T(n)=O(n^d(\frac{(\frac{a}{b^d})^{log_b n}-1}{\frac{a}{b^d}-1}))$  
$T(n)=O(\frac{n^d((\frac{a}{b^d})^{log_b n}-1)}{\frac{a}{b^d}-1})$  
$T(n)=O(n^d((\frac{a}{b^d})^{log_b n}-1))$  
$T(n)=O(n^d(\frac{a}{b^d})^{log_b n})-O(n^d)$  
$T(n)=O(n^d a^{log_b n}(\frac{1}{b^d})^{log_b n})-O(n^d)$  
$T(n)=O(n^d a^{log_b n}b^{-d\log_b n})-O(n^d)$  
$T(n)=O(n^d a^{log_b n}b^{\log_b n^{-d}})-O(n^d)$  
$T(n)=O(n^d a^{log_b n}n^{-d})-O(n^d)$  
$T(n)=O(n^d n^{-d} a^{log_b n})-O(n^d)$  
$T(n)=O(a^{log_b n})-O(n^d)$  
$T(n)=O(n^{log_b a})-O(n^d)$  
$T(n)=O(n^{log_b a})$  


#
$a>b^d$  
$log_b a>d$  
