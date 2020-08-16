

###最近月神需要在移动端部署一个卷积神经网络模型,但是月神碰到了一个问题,即月神使用了一个核非常大的最大池化(max-pooling)操作,但现有推理引擎不支持这一操作,作为月神的好朋友,你能帮帮月神么。
#所谓max-pooling,指的是给定一个数组（为了简化问题,暂定数组为一维）,在每一个滑动窗口内找出最大的那个数,举例如下：
#假设数组为[16, 19, 15, 13, 16, 20],且核大小为3,则当窗口依次滑过数组时,取出如下4个子数组：
#[16, 19, 15], [19, 15, 13], [15, 13, 16], [13, 16, 20],这4个子数组中的最大值分别为19, 19, 16, 20,故该数组经过大小为3的核的max-pooling的结果为19 19 16 20.
n = int(input())

nums = [int(num) for num in input().split(' ')]
k = int(input())

def solution(nums, k):
    queue = []
    res = []
    ## init queue
    for i in range(k):
        while(queue and nums[queue[-1]]<=nums[i]):
            queue.pop()
        queue.append(i)
    res.append(nums[queue[0]])
    for i in range(k, len(nums)):
        if(queue[0] == i-k):
            queue.pop(0)
        while(queue and nums[queue[-1]]<=nums[i]):
            queue.pop()
        queue.append(i)
        res.append(nums[queue[0]])
    return res

if(k == 1):
    print(' '.join([str(num) for num in nums]))
elif(k == n):
    print(max(nums))
else:
    res = solution(nums, k)
    print(' '.join([str(num) for num in res]))
