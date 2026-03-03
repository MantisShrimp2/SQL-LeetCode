# Last updated: 3/3/2026, 9:26:55 AM
class Solution(object):
    def topStudents(self, positive_feedback, negative_feedback, report, student_id, k):
        """
        :type positive_feedback: List[str]
        :type negative_feedback: List[str]
        :type report: List[str]
        :type student_id: List[int]
        :type k: int
        :rtype: List[int]
        """
        pos = set(positive_feedback)
        neg =set(negative_feedback)

        points  = {}

        for id, rep in zip(student_id, report):
            if id not in points:
                points[id] = 0
            for word in rep.split():
                if word in pos:
                    points[id] +=3
                elif word in neg:
                    points[id] -=1
        top_stud = sorted(points.keys(), key=lambda sid: (-points[sid], sid))

        return top_stud[0:k]