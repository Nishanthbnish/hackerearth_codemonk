for _ in range(int(input())):
     [N,K]=list(map(int,input().split()))

     A=str(input())

     B=A[N-1]+A[:N-1]

     count=0

     o=0
     while(1):

          C=A[1:]+A[0]

          A=C

          if C!=B:

               count+=1

          if C==B:

               count+=1

               o+=1

          if o==K:

               break

     print(count)
