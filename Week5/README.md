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
