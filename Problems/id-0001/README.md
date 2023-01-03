## P.1: Multiples of 3 or 5
***Problem Statement***

If we list all the natural numbers below 10 that are multiples 
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

***Algorithm***

Multiples of a specific modulus span the number line in a discrete,
linear fashion, proportional to modulus size. 

This implies that we must scan through almost all elements below 
the specified upper bound (eg. 1000). So the bestcomplexity we can
achieve is O(n). I'll leave the rigerous proof as an exercise for
the reader. 

So we start by scanning through all integers below our upper bound,
ubound. Once inside the loop you then check in sequence if the 
element is a multiple of any provided multiple. Stop once you find any
multiplicity. 

```
sum = 0
for (i = 0; i < ubound; ++i) {
	for m in multiples {
		if (i % m == 0) {
			sum += i
}}} return sum
```

This is a good method when your range is small and you're given many
multiples.


***Additonal Optimizations***

Since multiplicity spans the number line in a linear fashion, each 
multiple of a given modulus must be exactly a modulo more from the
prior multiple. So we can sum all multiples of each modulus, then 
sum the common multiplicities of the modulo and subtract. This is 
just the probabilistic expansion of each modulos multiple set.

This method would work well for very few multiples and large ranges.
