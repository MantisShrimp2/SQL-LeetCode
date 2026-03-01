# Last updated: 3/1/2026, 9:54:30 AM
1import pandas as pd
2
3def getDataframeSize(players: pd.DataFrame) -> List[int]:
4    return [players.shape[0], players.shape[1]]