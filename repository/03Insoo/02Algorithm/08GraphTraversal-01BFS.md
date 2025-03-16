GraphTraversal
ㄴBFS
ㄴDFS

#
BFS
ㄴQueue이용
# PseudoCode
BFS(G,s)
    Q ← ∅
    Enqueue(Q,S):
    while Q≠∅ do
        u ← Dequeue(Q)
        for each v adjacent to u do
            if v is unvisited the
                mark v as visited;
                Enqueue(Q,v);
            end.
        end.
    end.


#
BFS
ㄴ각노드-최단경로길이
#
s= 출발노드
d[v]= s로부터 v까지의 최단경로길이(에지개수)
π[v]= s로부터 v까지의 최단경로상에서 v직전노드(predecessor)
# 
BFS(G,s)
    Q ← ∅
    d[s] ← 0;
    π[s] ← null;
    Enqueue(Q,S):
    while Q≠∅ do
        u ← Dequeue(Q)
        for each v adjacent to u do
            if v is unvisited the
                mark v as visited;
                d[v] ← d[u]+1
                π[v] ← u
                Enqueue(Q,v);
            end.
        end.
    end.

# 방문추가
BFS(G,s)
    Q ← ∅
    for each node u do
        d[u] ← -1;
        π[u] ← null;
    end.
    d[s] ← 0;
    π[s] ← null;
    Enqueue(Q,S):
    while Q≠∅ do
        u ← Dequeue(Q)
        for each v adjacent to u do
            if (d[v]==-1) is unvisited the
                mark v as visited;
                d[v] ← d[u]+1
                π[v] ← u
                Enqueue(Q,v);
            end.
        end.
    end.


#
∑degree(v)=2m
ㄴm
ㄴedge개수


#
BFS Tree
ㄴ최단경로-트리


#
PRINT-PATH(G,s,v)
    if v=s then
        print s;
    else if π[v]=null then
        print "no path from s to v exists";
    else
        PRINT-PATH(G,s,π[v]);
        print v;
end.
