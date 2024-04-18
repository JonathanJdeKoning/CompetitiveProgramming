class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        d = defaultdict(list)
        for u, v, w in edges:
            d[u].append((v,w))
            d[v].append((u,w))
        out = [-1]*n
        seen = set()
        h = [(0,0)]

        while h:
            currWeight, currNode = heapq.heappop(h)
            if currNode in seen: continue
            seen.add(currNode)
            out[currNode] = currWeight

            for edgeNode, edgeWeight in d[currNode]:
                if edgeNode in seen: continue
                newdist = edgeWeight+currWeight
                if newdist >= disappear[edgeNode]:
                    out[edgeNode] = -1
                else:
                    heapq.heappush(h, (newdist, edgeNode))
        return out

        
