nominee1 = input("Enter the name of 1st nominee: ")
nominee2 = input("Enter the name of 2st nominee: ")

nm1_votes = 0
nm2_votes = 0

voter_id = [1,2,3,4,5,6,7,8,9,10]

no_of_voter = len(voter_id)

while True:
    if voter_id == []:
        print("Voting session is over !!!")
        if nm1_votes > nm2_votes:
            percent = (nm1_votes / no_of_voter) * 100
            print(f"{nominee1} has won the election with {percent} %")
            break
        elif nm2_votes > nm1_votes:
            percent = (nm2_votes / no_of_voter) * 100
            print(f"{nominee2} has won the election with {percent} %")
        else:
            print("Both have equal number of votes !!! Government will decide who will rule")
            break


    voter = int(input("Enter your voter id : "))
    if voter in voter_id:
        print("You are a voter ")
        voter_id.remove(voter)
        print("------------------------------------")
        print(f"To give vote to {nominee1} Press 1 ")
        print(f"To give vote to {nominee2} Press 2 ")
        print("------------------------------------")
        print(f"To give vote to {nominee1} Press 1 ")
        vote = int(input("Enter your precious vote : "))
        if vote == 1:
            nm1_votes += 1
            print(f"{nominee1} Thanks you to give your important vote to him !!!")
        elif vote == 2:
            nm2_votes += 1
            print(f"{nominee2} Thanks you to give your important vote to him !!!")
        elif vote > 2:
            print("Check your pressed key !!!")
        else:
            print("You are not a voter OR You have already voted !!!")