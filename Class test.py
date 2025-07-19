import random as rn
# print("computer",x)
# print("user",u)
for i in range(5):
  u =input("enter your choice among rock,paper,scissor:")
x=rn.choice(["rock","paper","scissor"])
if x==u:
        print("draw")
elif u=="rock" and x=="scissor":
        print("user won")
elif u=="paper" and x=="rock":
        print("user won")
elif u=="scissor" and x=="paper":
        print("user won")
elif u=="rock" and x=="paper":
        print("computer won")
elif u=="paper" and x=="scissor":
        print("computer won")
elif u=="scissor" and x=="rock":
        print("computer won")
else:
        print("invalid choice")
