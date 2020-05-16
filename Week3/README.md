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
