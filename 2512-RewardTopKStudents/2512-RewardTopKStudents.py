# Last updated: 3/3/2026, 8:41:23 AM
1class Solution(object):
2    def topStudents(self, positive_feedback, negative_feedback, report, student_id, k):
3        """
4        :type positive_feedback: List[str]
5        :type negative_feedback: List[str]
6        :type report: List[str]
7        :type student_id: List[int]
8        :type k: int
9        :rtype: List[int]
10        """
11        pos = set(positive_feedback)
12        neg =set(negative_feedback)
13
14        points  = {}
15
16        for id, rep in zip(student_id, report):
17            if id not in points:
18                points[id] = 0
19            for word in rep.split():
20                if word in pos:
21                    points[id] +=3
22                elif word in neg:
23                    points[id] -=1
24        top_stud = sorted(points.keys(), key=lambda sid: (-points[sid], sid))
25
26        return top_stud[0:k]