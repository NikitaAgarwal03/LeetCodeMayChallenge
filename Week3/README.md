<strong> 15 May Challenge</strong></br>
Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)
</br>
 

Example 1:</br>
Input: [1,-2,3,-2]</br>
Output: 3</br>
Explanation: Subarray [3] has maximum sum 3</br>

Example 2:</br>
Input: [5,-3,5]</br>
Output: 10</br>
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10</br>

Example 3:</br>
Input: [3,-1,2,-1]</br>
Output: 4</br>
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4</br>

Example 4:</br>
Input: [3,-2,2,-3]</br>
Output: 3</br>
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3</br>

Example 5:</br>
Input: [-2,-3,-1]</br>
Output: -1</br>
Explanation: Subarray [-1] has maximum sum -1</br>
 

Note:</br>
<ul>
<li>-30000 <= A[i] <= 30000</li>
<li>1 <= A.length <= 30000</li>
</ul>

<strong> 16 May Challenge</strong></br>
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.</br>

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.</br>

Example 1:</br>
Input: 1->2->3->4->5->NULL</br>
Output: 1->3->5->2->4->NULL</br>

Example 2:</br>
Input: 2->1->3->5->6->4->7->NULL</br>
Output: 2->3->6->7->1->5->4->NULL</br>

Note:
1. The relative order inside both the even and odd groups should remain as it was in the input.
2. The first node is considered odd, the second node even and so on ...

<strong>17 May Challenge</strong></br>
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.</br>

Example 1:</br>
<b>Input:</br></b>
s: "cbaebabacd" p: "abc"</br>
<b>Output:</br></b>
[0, 6]</br>
<b>Explanation:</br></b>
The substring with start index = 0 is "cba", which is an anagram of "abc".</br>
The substring with start index = 6 is "bac", which is an anagram of "abc".</br>

Example 2:</br>
<b>Input:</br></b>
s: "abab" p: "ab"</br>
<b>Output:</br></b>
[0, 1, 2]</br>
<b>Explanation:</br></b>
The substring with start index = 0 is "ab", which is an anagram of "ab".</br>
The substring with start index = 1 is "ba", which is an anagram of "ab".</br>
The substring with start index = 2 is "ab", which is an anagram of "ab".</br>

<strong>18 May Challenge</strong></br>
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.</br>

 

Example 1:</br>
Input: s1 = "ab" s2 = "eidbaooo"</br>
Output: True</br>
Explanation: s2 contains one permutation of s1 ("ba").</br>

Example 2:</br>
Input:s1= "ab" s2 = "eidboaoo"</br>
Output: False</br>
 

Note:</br>

The input strings only contain lower case letters.</br>
The length of both given strings is in range [1, 10,000].</br>

<strong>19 May Challenge</strong></br>
Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.</br>

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.</br>

For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].</br>

 

Example 1:</br>
Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]</br>
Output: [null,1,1,1,2,1,4,6]</br>
Explanation: </br>
First, S = StockSpanner() is initialized.  Then:</br>
S.next(100) is called and returns 1,</br>
S.next(80) is called and returns 1,</br>
S.next(60) is called and returns 1,</br>
S.next(70) is called and returns 2,</br>
S.next(60) is called and returns 1,</br>
S.next(75) is called and returns 4,</br>
S.next(85) is called and returns 6.</br>

Note that (for example) S.next(75) returned 4, because the last 4 prices</br>
(including today's price of 75) were less than or equal to today's price.</br>
 

Note:</br>

1. Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.</br>
2. There will be at most 10000 calls to StockSpanner.next per test case.</br>
3. There will be at most 150000 calls to StockSpanner.next across all test cases.</br>
3. The total time limit for this problem has been reduced by 75% for C++, and 50% for all other languages.</br>



<strong>20 May Challenge</strong></br>
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.</br>

 

Example 1:</br>
Input: root = [3,1,4,null,2], k = 1</br>
Output: 1</br>

Example 2:</br>
Input: root = [5,3,6,2,4,null,null,1], k = 3</br>
Output: 3</br>

Follow up:</br>
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?</br>

 

Constraints:</br>

The number of elements of the BST is between 1 to 10^4.</br>
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.</br>


<strong>21 May Challenge</strong></br>
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.</br>

 

Example 1:</br>

Input: matrix =</br>
[</br>
  [0,1,1,1],</br>
  [1,1,1,1],</br>
  [0,1,1,1]</br>
]</br>
Output: 15</br>
Explanation: </br>
There are 10 squares of side 1.</br>
There are 4 squares of side 2.</br>
There is  1 square of side 3.</br>
Total number of squares = 10 + 4 + 1 = 15.</br>

Example 2:</br>

Input: matrix = </br>
[</br>
  [1,0,1],</br>
  [1,1,0],</br>
  [1,1,0]</br>
]</br>
Output: 7</br>
Explanation: </br>
There are 6 squares of side 1.  </br>
There is 1 square of side 2. </br>
Total number of squares = 6 + 1 = 7.</br>
 

Constraints:</br>

1 <= arr.length <= 300</br>
1 <= arr[0].length <= 300</br>
0 <= arr[i][j] <= 1</br>
