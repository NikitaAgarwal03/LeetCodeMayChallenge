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

<strong>11 May Challenge</strong></br>
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.</br>

Example 1:</br>
Input: </br>
image = [[1,1,1],[1,1,0],[1,0,1]]</br>
sr = 1, sc = 1, newColor = 2</br>
Output: [[2,2,2],[2,2,0],[2,0,1]]</br>
Explanation: </br>
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.</br>
</br>Note:</br>
<ul>
 <li>The length of image and image[0] will be in the range [1, 50].</li>
 <li>The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.</li>
 <li>The value of each color in image[i][j] and newColor will be an integer in [0, 65535].</li>
 </ul>

<strong>12 May Challenge</strong></br>
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.</br>

 

Example 1:</br>
Input: [1,1,2,3,3,4,4,8,8]</br>
Output: 2</br>

Example 2:</br>
Input: [3,3,7,7,10,11,11]</br>
Output: 10</br>
 

Note: Your solution should run in O(log n) time and O(1) space.
