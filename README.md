# Drawing Binary Heap Trees

![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/windows%20terminal-4D4D4D?style=for-the-badge&logo=windows%20terminal&logoColor=white)

Author: [Andrew Gyakobo](https://github.com/Gyakobo)

This project serves to display ordered and balanced heap binary trees in the stdout.

## Introduction

To start off, a `binary heap` is a complete binary tree that satisfies the heap property. There are two types of binary heaps:

1. `Max-Heap:` In a max-heap, for any given node $i$:
    * The value $i$ is greater than or equal to the values of its children.
    * This means that the largest element is at the root of the heap.

1. `Min-Heap:` In a min-heap, for any given node $i$:
    * The value of $i$ is less than or equal to the values of its children.
    * This means that the smallest element is at the root of the heap.

### Fun facts about the applications of Binary Heaps

* `Priority Queues:` Binary heaps are commonly used to implement priority queues where the highest (or lowest) priority element needs to be efficiently retrieved.

* `Heapsort Algorithm:` A comparison-based sorting technique that uses a binary heap data structure.

* `Graph Algorithm:` Such as Dijkstra's shortest path algorithm and Prim's minimum spanning tree algorithm, which frequently use priority queues.

### Representation in Arrays:

Binary heaps are often represented as arrays data structures because they can be easily managed using array indices:




