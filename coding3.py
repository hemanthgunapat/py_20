# l=list(map(int,input().split()))
# for i in range(len(l)):
#     b=False
#     for j in range(len(l)-1):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
#             b=True
#     if b==False:
#         break
# print(*l)

# def bubbleSort(l):
#     n=len(l)
#     for i in range(n):
#         b=False
#         for j in range(0,n-i-1):
#             if l[j]>l[j+1]:
#                 l[j],l[j+1]=l[j+1],l[j]
#                 b=True
#         if (b==False):
#             break
# if __name__=="__main__":
#     l=[64,34,25,12,22,11,90]
#     bubbleSort(l)
#     print("Sorted array:")
#     for i in range(len(l)):
#         print("%d"%l[i],end=" ")

l=[20, 40, 30, 10, 50, 60]
for i in range(1, len(l)):
    k=l[i]
    j=i-1
    while j>=0 and l[j]>k:
        l[j+1]=l[j]
        j-=1
    l[j+1]=k
print(*l)

