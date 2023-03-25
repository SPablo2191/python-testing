from Queue import Queue
def test1():
    q = Queue(3)
    res = q.empty()
    if not res:
        print ("test1 NOT OK")
        return
    res = q.enqueue(10)
    if not res:
        print ("test1 NOT OK")
        return
    res = q.enqueue(11)
    if not res:
        print ("test1 NOT OK")
        return
    x = q.dequeue()
    if x != 10:
        print ("test1 NOT OK")
        return
    x = q.dequeue()
    if x != 11:
        print ("test1 NOT OK")
        return
    res = q.empty()
    if not res:
        print ("test1 NOT OK")
        return
    print ("test1 OK")

def test2():
    """Int Limits: Including -2147483648 to 2147483647"""
    q = Queue(4)
    try:
        q.enqueue(2147483648)
    except Exception as e:
     print(f"test2  OK => {e}")

def test3():
    try:
        q = Queue(0)
    except:
        print(f"test3  OK => you cannot dimension with maximum 0")
def test4():
    q = Queue(1)
    if(q.empty() and  q.full()):
        print("test4 NOT OK")
        return
    q.enqueue(1)
    if(q.empty() and  q.full()):
        print("test4 NOT OK")
        return
    print("test4 OK")
test1()
test2()
test3()
test4()