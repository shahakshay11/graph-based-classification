import numpy as np
from numpy import linalg as LA
from util import Util
class Task3():
	def __init__(self, personalised = False):
		self.ut = Util()
		self.beta = 0.85
		self.transportation_probability = 1/3.0
		self.personalised = personalised
		self.image_id_mapping = self.ut.image_id_mapping

	def pagerank(graph, K, images):
		"""
		1. compute transition matrix denoting random walks -
		T =  βM(nxn) + (1−β).[1/N](n×n)
		M[i,j] = { 
					1/out(pi) ; if there is an edge between pi and pj
					1/N ; if out(pi) = 0
					0 ; if |out(pi)| not equal to 0 but there is no edge from pi to pj
				}

		2. pagerank of each page p is defined as percentage of time random surfer spends on visiting p -> 
			components of first eigen vector of T
		"""
		transition_matrix = self.compute_transition_matrix(graph, image_ids)
		pagerank = self.get_time_spent_by_random_surfer_on_a_page(transition_matrix)
		top_k(pagerank, K)

	def compute_transition_matrix(self, graph, image_ids):
		left_operand = self.compute_left_operand(graph)
		right_operand = self.compute_right_operand(graph, image_ids)
		return np.add(left_operand, right_operand)

	def compute_left_operand(self, graph):
		return np.multiply(self.beta, self.compute_M(graph))

	def compute_right_operand(self, graph, image_ids):
		if len(image_ids) != 0:
			return self.personalised_page_rank_right_operand(graph, image_ids)

		n = len(graph)
		return np.multiply((1 - self.beta), [[1/n] * n] * n)

	def personalised_page_rank_right_operand(self, graph, image_ids):
		n = len(graph)
		transport_matrix = [[0] * n] * n
		for iter in transport_matrix:
			if iter in image_ids:
				transport_matrix[iter] = [self.transportation_probability] * len(transport_matrix[iter])

		return np.multiply((1 - self.beta), transport_matrix)

	def compute_M(self, graph):
		n = len(graph)
		M = [[0] * n] * n
		for i in range(0, n):
			for j in range(0, n):
				out_degree_pi = len(graph[i])
				if out_degree_pi == 0:
					M[i,j] = 1/n
					continue
				try:
					edge_weight_pi_pj = graph[i][(i,j)]
					if edge_weight_pi_pj:
						M[i,j] = 1/out_degree_pi
				except:
					if out_degree_pi != 0:
						M[i][j] = 0
						continue
		return M

	def get_time_spent_by_random_surfer_on_a_page(self, transition_matrix):
		"""
		returns first eigen vector of the decomposed matrix
		"""
		w, v = LA.eig(transition_matrix) # w: eigen values, v: row matrix
		return v[0]

	def top_k(pagerank, K):
		image_id_score_mapping = {}
		for iter in range(0, len(pagerank)):
			image_id_score_mapping[self.image_id_mapping[iter]] = pagerank[iter]
		print("Top K images based on pagerank score\n")
		print(sorted(image_id_score_mapping.items(), key=lambda x: x[1], reverse=True)[:K])

	def runner(self):
		try:
			K = int(input("Enter the value of K: "))
			image_ids = []
			if self.personalised:
				print("Enter three image ids to compute PPR:\n")
				image_id1 = input("Image id1:")
				image_ids.append(self.image_id_mapping[image_id1])
				image_id2 = input("Image id2:")
				image_ids.append(self.image_id_mapping[image_id2])
				image_id3 = input("Image id3:")
				image_ids.append(self.image_id_mapping[image_id3])
			graph = self.ut.fetch_dict_graph()
			"""
			graph = [{(1,2): 0.8, (1,3): 0.7, ....},
					{(2,1): 0.8, (2,3): 0.75, ...}]
			"""
			k_dominant_images = pagerank(graph, K, image_ids)

		except Exception as e:
			print(constants.GENERIC_EXCEPTION_MESSAGE + "," + str(type(e)) + "::" + str(e.args))