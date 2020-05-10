<strong>8 May Challenge</strong></br>
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.</br>
Example 1:
<!-- <img src= "https://assets.leetcode.com/uploads/2019/10/15/untitled-diagram-2.jpg"/></br> -->
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]</br>
Output: true</br>

Example 2:
<!--<img src="https://assets.leetcode.com/uploads/2019/10/09/untitled-diagram-1.jpg"/></br> -->
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]</br>
Output: false</br>

Constraints:</br>
<ul>
 <li>2 <= coordinates.length <= 1000</li></br>
<li>coordinates[i].length == 2</li></br>
<li>-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4</li></br>
<li>coordinates contains no duplicate point.</li></br>
</ul>

<strong>9 May Challenge</strong></br>
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:</br>
Input: 16</br>
Output: true</br>

Example 2:</br>
Input: 14</br>
Output: false</br>

<strong>10 May Challenge</strong></br>
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.</br>

Example 1:</br>
Input: N = 2, trust = [[1,2]]</br>
Output: 2</br>


Example 2:</br>
Input: N = 3, trust = [[1,3],[2,3]]</br>
Output: 3</br>

Example 3:</br>
Input: N = 3, trust = [[1,3],[2,3],[3,1]]</br>
Output: -1</br>

Example 4:</br>
Input: N = 3, trust = [[1,2],[2,3]]</br>
Output: -1</br>

Example 5:</br>
Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]</br>
Output: 3</br>
