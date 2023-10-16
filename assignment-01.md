# CMPS 2200 Assignment 1

**Name:**Isaac Ratzan

In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository.

1. (2 pts ea) **Asymptotic notation** (12 pts)

- 1a. Is $2^{n+1} \in O(2^n)$? Why or why not?

Yes, because if we create integer c to produce an inequality to check if 2^N+1 > C \* 2^N, if C = 0 and n = 0, all instances are accounted for. Therefore, 2^n+1 can be in O(2^n) as it represents the worst case scenarios and includes the possibility of outputs.
.  
.  
.  
.  
.

- 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?  
   No, because if we checked if 2^{2^n} > C\*2^N, we couldn't find a value of c > 0 that can prove the equation. This is because there is no value of C that satisfies the equation for all values of N because 2^2^n grows much faster.
  .  
  .  
  .  
  .  
  .
- 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?  
  no, because as N grows, n^1.01 grows much faster exponentially and there is no value for C that will ensure equivalency.
  .  
  .  
  .  
  .

- 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
  Yes, because if we checked for equivalency with integer C multiplied for omega, we see that n=1 and c=1 show that n^1.01 can fall within all cases of c and n > 0. Big Omega notation looks to see a value where n^1.01 can fall within log^2n given certain restraints.
  .  
  .  
  .  
  .
- 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?
  Yes. As n gets larger, sqrt(n) grows much slower and remains in log(n)^3 for cases of c and n > 0.  
  .  
  .  
  .  
  .
- 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
  No, because you are looking for Big Omega notation means that there must be a value for c and n where sqrt(n) is larger. Since sqrt(n) is much slower over time of c and n > 0, there is no value that satisfies this statement.

2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ...

$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\
~~~~~~~~~~~~ra + rb\\
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$

- 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`

- 2b. (6 pts) What does this function do, in your own words?
  This function recursively creates an array to store numbers and adds the first element to the second element to produce a third one. It initially checks the array to see if it is greater then one for the base case. Then, this pattern repeats recursively to check and add the two previous terms to create a third one.

.  
.  
.  
.  
.  
.  
.  
.

3. **Parallelism and recursion** (26 pts)

Consider the following function:

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```

E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`

- 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.

- 3b. (4 pts) What is the Work and Span of this implementation?

The work is BigO(n) because the worst case is you run through the entire array once and then you don't find the key. The span is the same (BigO(n)) because the process behind finding the longest length given a key is still sequential as you would need to go through the entire array to get the time.

.  
.  
.  
.  
.  
.  
.  
.  
.

- 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.

- 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
  .  
  .  
  .  
  .  
  .  
  .  
  .  
  .  
  .  
  .  
  .

- 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?

.  
.  
.  
.  
.  
.  
.  
.
