# rate limiter
# test_requests = [1, 2, 3, 11, 12, 13, 14]
# max_requests=3, window_size=10
# allowed 3 requests per 10 sec
from collections import deque

class RateLimiter:
	def __init__(self, max_requests, window_size):
		self.max_requests = max_requests
		self.window_size = window_size
		self.dequeu = deque()

	def is_requests_allowed(self, timestamp):

		while self.dequeu and timestamp - self.dequeu[0] >= self.window_size:
			self.dequeu.popleft()

		if len(self.dequeu) < self.max_requests:
			self.dequeu.append(timestamp)
			return True
		else:
			return False


limiter = RateLimiter(max_requests=3, window_size=10)

timestamps = [1, 2, 3, 11, 12, 13, 14]

for t in timestamps:
	allowed = limiter.is_requests_allowed(t)
	print(f"requests {t} is: {'allowed' if allowed else 'rejected'}")