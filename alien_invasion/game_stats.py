class GameStats():
    '''跟踪游戏统计信息'''

    def __init__(self, ai_setting):
        '''初始化统计信息'''
        self.ai_setting = ai_setting
        self.reset_stats()
        # 游戏一开始出于非活动状态
        self.game_active = False
        # 最高得分
        self.high_score = 0

    def reset_stats(self):
        '''初始化游戏运行期间可能发生变化的统计信'''
        self.ships_left = self.ai_setting.ship_limit
        self.score = 0