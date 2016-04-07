# Quandles


This repository contains code written in Python for the paper in pre-print ***Classification of Quandles and Cohomology Groups*** by Mohamed Elhamdadi and Brian Hunter Jackson which is a continuation of the work by L. Vendramin which can be found [here](https://github.com/HunterUSF/Quandles/blob/master/papers/RIG.pdf). We extend his work of classifying all non-isomorphic indecomposable quandles of size < 36, by classifying all non-isomorphic indecomposable quandles up to order 431. We also calculate the cohomology groups of these quandles and create dense finite fields by identifying 2 co-cycles without corresponding coboundaries.  

Background
==========

![quandles](https://github.com/HunterUSF/Quandles/blob/master/images/basics.png)

![quandles](https://github.com/HunterUSF/Quandles/blob/master/images/RIG.png)

![quandles](https://github.com/HunterUSF/Quandles/blob/master/images/alexander.png)

![quandles](https://github.com/HunterUSF/Quandles/blob/master/images/example.png)

Usage
=====

All code contained within the repository is open-sourced and subject to the GNU [license](https://github.com/HunterUSF/Quandles/blob/master/License.md). The executable files can be found in the cohomology_calculation folder. With a lack of version control, and drastically different approaches we naively maintain multiple versions of the main executable file. Versions ***main_v10.py -- main_v12.py*** run without Sage; however, you will need Sage in order to run ***main_v13.py -- main_v15.py***. 

Results
=======

Below are the results for cohomology calculation of Quandle C30_1

The relations obtained by plugging in triples:
[[ 0 -1  0 ...,  0  0  0]
 [ 0 -1  1 ...,  0  0  0]
 [ 0 -1  0 ...,  0  0  0]
 ..., 
 [ 0  0  0 ...,  0 -1  0]
 [ 0  0  0 ...,  1 -1  0]
 [ 0  0  0 ...,  0 -1  0]]

[[0 1 0 ..., 1 0 0]
 [0 0 1 ..., 1 0 0]
 [0 0 0 ..., 1 0 0]
 ..., 
 [0 0 0 ..., 0 1 0]
 [0 0 0 ..., 0 0 0]
 [0 0 0 ..., 1 0 0]]

[[0 0 0 ..., 0 0 0]
 [0 1 0 ..., 0 0 0]
 [0 0 1 ..., 0 0 0]
 ..., 
 [0 0 0 ..., 1 0 0]
 [0 0 0 ..., 0 1 0]
 [0 0 0 ..., 0 0 0]]

[[0 0 0 ..., 0 0 0]
 [0 0 0 ..., 1 0 0]
 [0 0 0 ..., 1 0 0]
 ..., 
 [0 0 0 ..., 1 0 0]
 [0 0 0 ..., 0 1 0]
 [0 0 0 ..., 0 0 0]]

Transpose
[[0 0 0 ..., 0 0 0]
 [0 0 0 ..., 0 0 0]
 [0 0 0 ..., 0 0 0]
 ..., 
 [0 1 1 ..., 1 0 0]
 [0 0 0 ..., 0 1 0]
 [0 0 0 ..., 0 0 0]]

remove trivial
[[0 0 0 ..., 0 0 0]
 [0 0 1 ..., 0 0 0]
 [0 0 0 ..., 0 0 0]
 ..., 
 [0 0 0 ..., 0 0 0]
 [0 1 1 ..., 1 0 0]
 [0 0 0 ..., 0 1 0]]

row reduce
[[0 1 0 ..., 0 0 0]
 [0 0 1 ..., 0 1 0]
 [0 0 0 ..., 0 0 0]
 ..., 
 [0 0 0 ..., 0 0 0]
 [0 0 0 ..., 0 0 0]
 [0 0 0 ..., 0 0 0]]

Coboundary matrix:
[[ 0  1  1 ..., -1  0  0]
 [ 0  0 -1 ...,  0  0  0]
 [ 0  0  0 ...,  0  0  0]
 ..., 
 [ 0  0  0 ...,  0  0  0]
 [ 0  0  0 ...,  0  0  0]
 [ 0  0  0 ...,  1  1  0]]

Coboundaries reduced over a group:
[[0 1 0 ..., 0 0 0]
 [0 0 1 ..., 0 1 0]
 [0 0 0 ..., 0 0 0]
 ..., 
 [0 0 0 ..., 0 0 0]
 [0 0 0 ..., 0 0 0]
 [0 0 0 ..., 0 0 0]]

[[0 0 0 ..., 0 0 0]
 [0 0 0 ..., 0 0 0]
 [0 0 0 ..., 0 0 0]
 ..., 
 [0 0 0 ..., 0 0 0]
 [0 0 0 ..., 0 0 0]
 [0 0 0 ..., 0 0 0]]

We have
1 x 900 dense matrix over Finite Field of size 2 (type 'print function.str()' to see all of the entries)

[Finished in 490.1s]







