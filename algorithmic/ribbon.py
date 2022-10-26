def max_ribbon_product(n):
	"""Recursively calculates the maximum product of integer sized pieces of a ribbon of length n.
	
	:args
	n - integer that is the length of the ribbon.
	
	:return
	an integer that is the maximum product.
	"""
	
	if n <= 1:
		return 0
		
	max_product = 0
	
	for i in range(1, n):
		current_max = max(i * max_ribbon_product(n - i), i * (n - i))
		max_product = max(current_max, max_product)
		
	return max_product


def max_ribbon_product_dynamic(n, seen):
	"""Calculates the maximum product of integer sized pieces of a ribbon of length n using dynamic programming.

	:args
	n - integer that is the length of the ribbon.
	seen - a dictionary of seen values.

	:return
	an integer that is the maximum product.
	"""
	if n in seen:
		return seen[n]

	if n <= 1:
		seen[n] = 0
		return 0

	max_product = 0

	for i in range(1, n):
		calc_max = max_ribbon_product_dynamic(n - i, seen)
		seen[n] = calc_max
		current_max = max(i * calc_max, i * (n - i))
		max_product = max(current_max, max_product)

	return max_product
	
if __name__ == '__main__':
	for i in range(2, 8):
		#print(max_ribbon_product(i))
		print(max_ribbon_product_dynamic(i, {}))


