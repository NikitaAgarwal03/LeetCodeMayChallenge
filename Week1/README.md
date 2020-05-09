# LeetCodeMayChallenge
<strong>2 May challenge</strong></br>
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"</br>
Output: 3</br>
Example 2:</br>
Input: J = "z", S = "ZZ"</br>
Output: 0</br>
Note:
S and J will consist of letters and have length at most 50.
The characters in J are distinct.

<strong>3 May challenge</strong></br>
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.</br>
Example:</br>
canConstruct("a", "b") -> false</br>
canConstruct("aa", "ab") -> false</br>
canConstruct("aa", "aab") -> true</br>


<strong>4 May challenge</strong></br>
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.</br>
Example 1:

Input: 5</br>
Output: 2</br>
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.</br>
 

Example 2:</br>

Input: 1</br>
Output: 0</br>
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 

Note:

The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.

<strong>5 May challenge</strong></br>
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"</br>
return 0.</br>

s = "loveleetcode"</br>
return 2.</br>
Note: You may assume the string contain only lowercase letters.

<strong>6 May challenge</strong></br>
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:</br>
Input: [3,2,3]</br>
Output: 3</br>

Example 2:</br>
Input: [2,2,1,1,1,2,2]</br>
Output: 2</br>

<strong>7 May challenge</strong></br>
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

Example 1:</br>
Input: root = [1,2,3,4], x = 4, y = 3</br>
Output: false</br>

Example 2:</br>
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4</br>
Output: true</br>

Example 3:</br>
Input: root = [1,2,3,null,4], x = 2, y = 3</br>
Output: false</br>

Note:</br>

The number of nodes in the tree will be between 2 and 100.</br>
Each node has a unique integer value from 1 to 100.</br>
