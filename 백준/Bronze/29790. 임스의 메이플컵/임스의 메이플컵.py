a,b,c = map(int,input().split())
if a >= 1000 and (b >= 8000 or c >= 260): print("Very Good")
elif a >= 1000 and (not b>=8000 and not c>=260): print("Good")
else: print("Bad")