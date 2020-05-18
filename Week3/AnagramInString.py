class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
	l = len(p)
	dict_p = collections.defaultdict(int)       
	dict_s = collections.defaultdict(int)       
	for c in p:	dict_p[c] += 1                   
	for c in s[:l-1]: dict_s[c] += 1            
	res = []
	for i in range(l-1, len(s)):
		dict_s[s[i]] += 1                       
		if i >= l: dict_s[s[i-l]] -= 1          
		if not dict_s[s[i-l]]: del dict_s[s[i-l]]
		if dict_s == dict_p: res.append(i-l+1)
	return res
