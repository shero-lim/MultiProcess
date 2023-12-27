import time

import blog_spider
import threading


def single_thread():
    print("single thread start")
    for url in blog_spider.urls:
        blog_spider.craw(url)
    print("single thread end")



def multi_thread():
    print("multi thread start")
    threads = []

    for url in blog_spider.urls:
        threads.append(threading.Thread(target=blog_spider.craw, args=(url,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("multi thread end")


if __name__ == "__main__":
    start = time.time()
    single_thread()
    end = time.time()
    print("单线程花费时间", end-start)
    start = time.time()
    multi_thread()
    end = time.time()
    print("多线程花费时间", end - start)



