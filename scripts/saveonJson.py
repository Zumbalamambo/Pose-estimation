
""" 
To save JSON format
0 - 16개의 Joint point
"""
def makePoint(y, x, keyNum, score):
    keypoints={
                0: "nose",
                1: "left_eye",
                2: "right_eye",
                3: "left_ear",
                4: "right_ear",
                5: "left_shoulder",
                6: "right_shoulder",
                7: "left_elbow",
                8: "right_elbow",
                9: "left_wrist",
                10: "right_wrist",
                11: "left_hip",
                12: "right_hip",
                13: "left_knee",
                14: "right_knee",
                15: "left_ankle",
                16: "right_ankle"
            }
    """
    docstring
    """
    points = {"position": {"y": 0, "x": 0}, "part": "", "score": 0}

    points["position"]["y"] = y
    points["position"]["x"] = x
    points["part"] = keypoints[keyNum]
    points["score"] = score
    return points