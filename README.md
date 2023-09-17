# autoAnime

## 流程 & Todo List:
1. ~~番剧列表更新与展示（手动触发）~~
   - ~~前端番剧列表展示~~
   - ~~前端番剧列表更新按钮~~
   - ~~后端接收前端post, 爬取最新番剧列表~~
   - ~~后端目前番剧列表, 查询数据库anime_list~~   
   - ~~后端新番剧插入数据库, 插入数据库anime_list~~
   - ~~后端下载新番剧封面~~
2. 番剧订阅（手动触发）
   - ~~前端订阅按钮~~
   - ~~后端接收前端post, 更新数据库anime_list~~
   - ~~后端获取种子信息, 更新数据库anime_seed~~
   - 后端种子筛选, 番剧订阅
   - ~~后端种子下载~~
   - 后端下发下载任务, 更新数据库anime_task
3. 番剧更新（手动触发）
   - 前端番剧现有集数展示
   - 前端番剧集数更新按钮
   - 后端接收前端post, 爬取种子信息
   - ~~后端更新种子信息, 更新数据库anime_seed~~
   - 后端种子筛选, 番剧更新
   - ~~后端种子下载~~
   - 后端下发下载任务, 更新数据库anime_task
4. 后端每天轮询爬取更新番剧，并把种子存入mysql。
5. 后端读取/轮询mysql，发现有新种子，则上传qb。上传同时需要根据番剧名称确认下载路径。
6. init.sh 脚本实现自动化部署。
7. ~~图床不做了~~
8. 日志
   - ~~基础日志功能~~
   - ~~修复日志重复打印~~
   - ~~日志大小超过阈值时分割日志文件~~
   - 添加日志打印到终端的选项，完善log_config，yaml对应功能
10. 数据库 [@bjrbh](https://github.com/bjrbh)
   - ~~基础crud~~
   - 高级查询
11. 守护进程拉起定时任务（4、5）
12. 前端美化
   - 番名隐藏&全名显示

## 使用
### flask测试
```
sh test.sh

// 数据库更新
flask db migrate
flask db upgrade
```
