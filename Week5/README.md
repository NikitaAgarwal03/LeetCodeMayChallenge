<strong>29 May challenge</strong></br>
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.</br>

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]</br>

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?</br>

Example 1:</br>

Input: numCourses = 2, prerequisites = [[1,0]]</br>
Output: true</br>
Explanation: There are a total of 2 courses to take. </br>
           &nbsp;&emsp; &emsp;&emsp;&emsp;&emsp;To take course 1 you should have finished course 0. So it is possible.</br>
             
Example 2:</br>

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]</br>
Output: false</br>
Explanation: There are a total of 2 courses to take. </br>
            &nbsp;&emsp;&emsp;&emsp;&emsp;&emsp;To take course 1 you should have finished course 0, and to take course 0 you should</br>
             also have finished course 1. So it is impossible.</br>
 

Constraints:</br>

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.</br>
You may assume that there are no duplicate edges in the input prerequisites.</br>
1 <= numCourses <= 10^5</br>


<strong>30 May challenge</strong></br>
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).</br>

(Here, the distance between two points on a plane is the Euclidean distance.)</br>

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)</br>

 

Example 1:</br>

Input: points = [[1,3],[-2,2]], K = 1</br>
Output: [[-2,2]]</br>
Explanation: </br>
The distance between (1, 3) and the origin is sqrt(10).</br>
The distance between (-2, 2) and the origin is sqrt(8).</br>
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.</br>
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].</br>

Example 2:</br>

Input: points = [[3,3],[5,-1],[-2,4]], K = 2</br>
Output: [[3,3],[-2,4]]</br>
(The answer [[-2,4],[3,3]] would also be accepted.)</br>
 

Note:</br>

1 <= K <= points.length <= 10000</br>
-10000 < points[i][0] < 10000</br>
-10000 < points[i][1] < 10000</br>

<strong>31 May challenge</strong></br>
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.</br>

You have the following 3 operations permitted on a word:</br>

Insert a character</br>
Delete a character</br>
Replace a character</br>

Example 1:</br>

Input: word1 = "horse", word2 = "ros"</br>
Output: 3</br>
Explanation: </br>
horse -> rorse (replace 'h' with 'r')</br>
rorse -> rose (remove 'r')</br>
rose -> ros (remove 'e')</br>

Example 2:</br>

Input: word1 = "intention", word2 = "execution"</br>
Output: 5</br>
Explanation: </br>
intention -> inention (remove 't')</br>
inention -> enention (replace 'i' with 'e')</br>
enention -> exention (replace 'n' with 'x')</br>
exention -> exection (replace 'n' with 'c')</br>
exection -> execution (insert 'u')</br>
