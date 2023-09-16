import os
from lib.connect import m_DBconnector
from lib.spider import m_mikan


class AddAnimeTask:
    def __init__(self):
        self.mikan_id_lists = []
        self.finishedEpisode = []

        self.getSubscribeAnime()

    def getSubscribeAnime(self):
        sql = 'select mikan_id from anime_list where subscribe_status=1'
        self.mikan_id_lists.extend(item[0] for item in m_DBconnector.execute(sql))  
    
    def mikanIdToName(self, mikan_id):
        sql = 'select anime_name from anime_list where mikan_id={}'.format(mikan_id)
        anime_name = m_DBconnector.execute(sql)[0][0]
        # print(anime_name)
        return anime_name

    def getAllSubscribeAnimeName(self):
        for mikan_id in  self.mikan_id_lists:
            self.mikanIdToName(mikan_id)
            print(self.mikanIdToName(mikan_id))
    
    def getAnimeTaskByMikanId(self, mikan_id):
        # 获取已经添加的任务
        anime_task_episode_lists_old = dict()
        sql = 'select episode,status from anime_task where mikan_id={}'.format(mikan_id)
        anime_tasks = m_DBconnector.execute(sql)
        
        for anime_task in anime_tasks:
            episode = anime_task[0]
            status = anime_task[1]
            anime_task_episode_lists_old[episode] = status
        print(anime_task_episode_lists_old)
        
        # 获取所有可以下载的剧集并去重
        anime_task_episode_lists_new = dict()
        sql = 'select episode,seed_url from anime_seed where mikan_id={}'.format(mikan_id)
        anime_lists = m_DBconnector.execute(sql)

        for anime_list in anime_lists:
            episode = anime_list[0]
            if episode in anime_task_episode_lists_new or episode in anime_task_episode_lists_old:
                continue
            seed_url = anime_list[1]
            anime_task_episode_lists_new[episode] = seed_url
        
        print(anime_task_episode_lists_new)

        dir = "seed/" + mikan_id + "/"
        print(dir)
        for episode, seed_url in anime_task_episode_lists_new.items():
            if not os.path.exists(dir):
                os.makedirs(dir)
            m_mikan.download_seed(seed_url, dir)

        return anime_task_episode_lists_new

AddAnimeTask().getAllSubscribeAnimeName()
AddAnimeTask().getAnimeTaskByMikanId(3071)


# sql = "INSERT INTO anime_task (mikan_id, status, episode) VALUES (3060, 0, 1)"
# m_DBconnector.execute(sql)
