import heapq


def get_median(m_list):
    median = 0
    heap = []
    sorted_heap = []
    for i in m_list:
        heapq.heappush(heap, i)
    for i in range(len(m_list)):
        val = heapq.heappop(heap)
        sorted_heap.append(val)
    if len(sorted_heap) % 2 == 0:
        median = (sorted_heap[int(len(sorted_heap) / 2)] + sorted_heap[int(len(sorted_heap) / 2) + 1])
    else:
        median = (sorted_heap[(len(sorted_heap) /  2) + 1])
    return median

get_median([13, 4, 10, 9, 7, 5, 4, 16, 2, 1])