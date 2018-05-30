import math
import random
import numpy as np
import matplotlib.pyplot as plt

def ball_in_box(m=5, blockers=[(0.5, 0.5), (0.5, -0.5), (0.5, 0.3)]):
	tol = 1e-2#set the accuracy, which means our answer should bounds in (r-tol,r+tol), r is the exactly right answer
	lower_bound = 0
	upper_bound = 2
	r_pre = -1
	r_now = 1
	proxies = None
	while(abs(r_pre-r_now) >= tol):#when our accuracy has not been satisfied yet, we continue iterate
		mid = (lower_bound + upper_bound) / 2
		isVal, proxies = isValid(mid, m, blockers)
		if(isVal):
			lower_bound = mid
			r_pre = r_now
			r_now = mid
		else:
			upper_bound = mid
	return proxies
			

def isValid(candidate, m, blockers):
	max_random_ite_time = 20000
	for i in range(max_random_ite_time):
		centroids = []
		for num in range(m):
			x = random.uniform(-1+candidate,1-candidate)
			y = random.uniform(-1+candidate,1-candidate)
			if(isValidate(candidate, blockers, centroids, [x,y])):
				centroids.append((x,y,candidate))
			else:
				x = random.uniform(-1+candidate,1-candidate)
				y = random.uniform(-1+candidate,1-candidate)
				if(isValidate(candidate, blockers, centroids, [x,y])):
					centroids.append((x,y,candidate))
				else:
					break;
					
		if(len(centroids)==m):
			return True, centroids
	
	return False, None
	

def isValidate(candidate, blockers, centroids, proxies):
	r_2 = candidate**2
	r_2_2 = 4 * r_2
	for blocker in blockers:
		if((proxies[0]-blocker[0])**2 + (proxies[1]-blocker[1])**2 < r_2):
			return False
	for centroid in centroids:
		if((proxies[0]-centroid[0])**2 + (proxies[1]-centroid[1])**2 < r_2_2):
			return False
	return True


def visualization():
	proxies = ball_in_box()
	blockers=[(0.5, 0.5), (0.5, -0.5), (0.5, 0.3)]
	plt.Rectangle((-1,-1),2,2)
	for blocker in blockers:
		plt.scatter(blocker[0], blocker[1])
	for proxy in proxies:
		a = proxy[0]
		b = proxy[1]
		r = proxy[2]
		plt.scatter(a,b)
		theta = np.arange(0, 2*np.pi, 0.01)
		x = a + r * np.cos(theta)
		y = b + r * np.sin(theta)
		plt.plot(x,y)
	plt.xlim(-1, 1)
	plt.ylim(-1, 1)
	plt.show()


if __name__ == '__main__':
	visualization()
