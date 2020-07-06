class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        src_cities = [path[0] for path in paths]
        dst_cities = [path[1] for path in paths]

        for city in dst_cities:
            if city not in src_cities:
                return city

        return None