KEY='newip'
NEED_AUTH=True
AUTH_USER='jcd'
AUTH_PASSWORD='Hooya911.'
PORT=3128


# Redis Conneection 
host = "47.100.121.120"
port = 6379
password = "Hooya911."
key = "/proxy/all"  # 检测完之后会分别进入 /proxy/ready 和 /proxy/stale
max_score = 20 # 加入队列的最大分数