
### one code one day
### 2020、02、25
### 给出一个区间的集合，请合并所有重叠的区间
### 输入 [[1,3],[2,6],[8,10],[15,18]] 输出[[1,6],[8,10],[15,18]]
### leetcode 56 合并区间

def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    import functools
    # 自定义比较函数
    def sort_func(x,y):
        if(x[0] < y[0] or (x[0] == y[0] and x[1] < y[1])):
            return -1
        elif(x[0] == y[0] and x[1] == y[1]):
            return 0
        else:
            return 1
    # 注意排序写法
    intervals.sort(key=functools.cmp_to_key(sort_func))
    answer = []
    i = 0
    while(i < len(intervals)):
        start_interval, end_interval = intervals[i][0],intervals[i][1]
        #从当前位置开始找可以合并的区间
        j = i + 1
        while(j < len(intervals) and intervals[j][0] <= temp2):
            # 合并
            end_interval = max(intervals[j][1], end_interval)
            j += 1
        i = j
        answer.append([start_interval, end_interval])
    return answer

def test():
    pass