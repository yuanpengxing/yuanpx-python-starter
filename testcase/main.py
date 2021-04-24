import threading
from testcase import sub1, sub2

# 开启名字叫chrome线程，表示以chrome浏览器跑Main().create_suite3里面引入的所有case
threading.Thread(target=sub1.Entry().run_suite(), name='chrome').start()

# 开启名字叫firefox线程，表示以firefox浏览器跑Main().create_suite1里面引入的所有case
threading.Thread(target=sub2.Entry().run_suite(), name='firefox').start()

# 开启名字叫ie线程，表示以ie浏览器跑Main().create_suite1里面引入的所有case
threading.Thread(target=sub2.Entry().run_suite(), name='ie').start()
