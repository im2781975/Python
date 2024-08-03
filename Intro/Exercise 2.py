#Add Data in Dict
studentData = [
    {"Name: ":"A", "roll": 10, "Age": 22, "course": "python",},
    {"Name: ": "B", "roll": 12, "Age": 24, "course": "java",}
]
def AddData(name, rollno, age, Course):
    newStudent = {}
    newStudent["Name"] = name
    newStudent["roll"] = rollno
    newStudent["Age"] = age
    newStudent["course"] = Course
    studentData.append(newStudent)
AddData("C", 15, 23, "C++")
print(studentData)
#Bidd Auction
def FindWinner(BidderData):
    highest = 0
    winner = ""
    for i in BidderData:
        BiddingPrice = BidderData[i]
        if BiddingPrice > highest:
            highest = BiddingPrice
            winner = i
    print(BidderData)
    print(f"{winner} with highest Bid {highest} ")
        
BidderData={}
EndOfBidding = False
while not EndOfBidding: 
    name = input("Enter Name: ")
    price = int(input("Enter Price: "))
    BidderData[name] = price
    MoreBidder = input("More Bidder?Type 'yes' or 'no': ").lower()
    if MoreBidder == 'no':
        EndOfBidding = True
        FindWinner(BidderData)

