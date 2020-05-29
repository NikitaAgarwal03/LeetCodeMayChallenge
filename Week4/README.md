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

<strong> 25 May Challenge</strong></br>
We write the integers of A and B (in the order they are given) on two separate horizontal lines.</br>

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:</br>

A[i] == B[j];</br>
The line we draw does not intersect any other connecting (non-horizontal) line.</br>
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.</br>

Return the maximum number of connecting lines we can draw in this way.</br>

Example 1:</br>

Input: A = [1,4,2], B = [1,2,4]</br>
Output: 2</br>
Explanation: We can draw 2 uncrossed lines as in the diagram.</br>
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.</br>

Example 2:</br>

Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]</br>
Output: 3</br>

Example 3:</br>

Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]</br>
Output: 2</br>
 

Note:</br>

1 <= A.length <= 500</br>
1 <= B.length <= 500</br>
1 <= A[i], B[i] <= 2000</br>


<strong> 26 May Challenge</strong></br>
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.</br>

Example 1:</br>

Input: [0,1]</br>
Output: 2</br>
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.</br>

Example 2:</br>

Input: [0,1,0]</br>
Output: 2</br>
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.</br>

Note: The length of the given binary array will not exceed 50,000.</br>


<strong> 27 May Challenge</strong></br>
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.</br>

Each person may dislike some other people, and they should not go into the same group. </br>

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.</br>

Return true if and only if it is possible to split everyone into two groups in this way.</br>

 

Example 1:</br>

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]</br>
Output: true</br>
Explanation: group1 [1,4], group2 [2,3]</br>

Example 2:</br>

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]</br>
Output: false</br>

Example 3:</br>

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]</br>
Output: false</br>
 
Constraints:</br>

1 <= N <= 2000</br>
0 <= dislikes.length <= 10000</br>
dislikes[i].length == 2</br>
1 <= dislikes[i][j] <= N</br>
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].
