class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        return moves.count("_") + (abs(moves.count("L")-moves.count("R")))
