<strong> 22 May Challenge</strong></br>
Given a string, sort it in decreasing order based on the frequency of characters.</br>

Example 1:</br>

Input:</br>
"tree"</br>
Output:</br>
"eert"</br>
Explanation:</br>
'e' appears twice while 'r' and 't' both appear once.</br>
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.</br>

Example 2:</br>

Input:</br>
"cccaaa"</br>
Output:</br>
"cccaaa"</br>
Explanation:</br>
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.</br>
Note that "cacaca" is incorrect, as the same characters must be together.</br>

Example 3:</br>

Input:</br>
"Aabb"</br>
Output:</br>
"bbAa"</br>
Explanation:</br>
"bbaA" is also a valid answer, but "Aabb" is incorrect.</br>
Note that 'A' and 'a' are treated as two different characters.</br>

<strong> 23 May Challenge</strong></br>
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.</br>

Return the intersection of these two interval lists.</br>

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)</br>

Example 1:</br>
Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]</br>
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]</br>
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.</br>
 

Note:</br>

(1) 0 <= A.length < 1000</br>
(2) 0 <= B.length < 1000</br>
(3) 0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9</br>

<b>NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.</b></br>

<strong>24 May Challenge</strong></br>
Return the root node of a binary search tree that matches the given preorder traversal.</br>

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)</br>

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.</br>

Example 1:</br>
Input: [8,5,1,7,10,12]</br>
Output: [8,5,10,1,7,null,12]</br>

Constraints:</br>

1 <= preorder.length <= 100</br>
1 <= preorder[i] <= 10^8</br>
The values of preorder are distinct.</br>
