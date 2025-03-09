def hanoi(n, source, target, auxiliary):
  if n==1:
    print(f"원반1을 {source}에서 {target}으로 옮깁니다.")
    return
  hanoi(n-1,source,auxiliary,target)
  print(f"원반{n}을 {source}에서 {target}으로 옮깁니다.")
  hanoi(n-1,auxiliary,source,target)

hanoi(3,'A','C','B')

