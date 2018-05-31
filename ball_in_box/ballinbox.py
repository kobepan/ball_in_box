import math
import random
import numpy as np
import matplotlib.pyplot as plt

def ball_in_box(m=5, blockers=[(0.5, 0.5), (0.5, -0.5), (0.5, 0.3)]):
	candidate_num = 100
	candidates = [1 - candi*(1.0/candidate_num) for candi in range(candidate_num)]
	r_index = 0
	centroids = []
	for i in range(m):
		while(r_index < candidate_num):
			flag = isValid(candidates[r_index], blockers, centroids)
			if(flag):
				break
			else:
				r_index += 1
		if(i+1 != len(centroids)):
			print("error")
			exit(0)
		
	return centroids


def isValid(candidate, blockers, centroids):
	max_random_ite_time = 30000
	for i in range(max_random_ite_time):
		x = random.uniform(-1+candidate,1-candidate)
		y = random.uniform(-1+candidate,1-candidate)
		if(isValidate(blockers, centroids, (x,y,candidate))):
			centroids.append((x,y,candidate))
			return True
	
	return False


def isValidate(blockers, circless, proxies):
    # Is circle in the box?
    circles = circless.copy()
    circles.append(proxies)
    for circle in circles:
        xmr = circle[0] - circle[2]
        xpr = circle[0] + circle[2]
        ymr = circle[1] - circle[2]
        ypr = circle[1] + circle[2]

        if (not (xmr <= 1 and xmr >=-1 )) \
           or (not (xpr <= 1 and xpr >=-1 )) \
           or (not (ymr <= 1 and ymr >=-1 )) \
           or (not (ypr <= 1 and ypr >=-1 )):
            return False
    # Is circle good for blockers?
    if blockers is not None and len(blockers) > 0:
        for circle in circles:
            for block in blockers:
                x = circle[0]
                y = circle[1]
                r = circle[2]
                bx = block[0]
                by = block[1]
                if math.sqrt((x - bx)**2 + (y - by)**2) < r:
                    return False

    # Is circle good for each other?
    for circle1 in circles:
        for circle2 in circles:
            if(circle1 == circle2):
                continue
            x1 = circle1[0]
            y1 = circle1[1]
            r1 = circle1[2]
            x2 = circle2[0]
            y2 = circle2[1]
            r2 = circle2[2]
            if math.sqrt((x1 - x2)**2 + (y1 - y2)**2) < (r1 + r2):
                return False

    # all good
    return True




def visualization():
	proxies = ball_in_box()
	blockers=[(0.5, 0.5), (0.5, -0.5), (0.5, 0.3)]
	plt.Rectangle((-1,-1),2,2)
	area = 0.0
	for blocker in blockers:
		plt.scatter(blocker[0], blocker[1])
	for proxy in proxies:
		a = proxy[0]
		b = proxy[1]
		r = proxy[2]
		area += r**2 * math.pi
		plt.scatter(a,b)
		theta = np.arange(0, 2*np.pi, 0.01)
		x = a + r * np.cos(theta)
		y = b + r * np.sin(theta)
		plt.plot(x,y)
	print("Total area:{}".format(area))
	plt.xlim(-1, 1)
	plt.ylim(-1, 1)
	plt.show()


if __name__ == '__main__':
	visualization()
