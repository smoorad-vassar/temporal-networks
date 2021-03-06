import heapq
from copy import deepcopy

# =============================
#  FILE:    incremental.py
#  AUTHOR:  Sudais Moorad / Muhammad Furrukh Asif
#  DATE:    June 2020
# =============================

class Incremental:

    @staticmethod
    def update_potential_function(network, src_idx, potential_function, backward=False):
        # small fixes TBD
        updated_potential_function = deepcopy(potential_function)
        # 0 equals not yet in queue, 1 equals in queue, 2 equals already popped from queue
        in_queue = [0 for i in range(len(potential_function))]
        NOT_YET_IN_QUEUE, IN_QUEUE, POPPED_OFF = 0, 1, 2

        def update_value(node_idx, edge_weight, successor_idx):
            new_value = potential_function[successor_idx] - edge_weight
            if updated_potential_function[node_idx] < new_value:
                updated_potential_function[node_idx] = new_value
                new_key = potential_function[node_idx] - \
                    updated_potential_function[node_idx]
                if in_queue[node_idx] == NOT_YET_IN_QUEUE:
                    heapq.heappush(min_heap, (node_idx, new_key))
                    in_queue[node_idx] = IN_QUEUE
                elif in_queue[node_idx] == IN_QUEUE:
                    heapq.heappush(min_heap, (node_idx, new_key))
                    in_queue[node_idx] = POPPED_OFF
                else:
                    return False
            return True
        min_heap = []
        heapq.heappush(
            min_heap, (src_idx, updated_potential_function[src_idx]))

        while min_heap:
            node_idx, _ = heapq.heappop(min_heap)
            for successor_idx, edge_weight in network.successor_edges[node_idx].items():
                if not update_value(node_idx, edge_weight, successor_idx):
                    return False
        return True
