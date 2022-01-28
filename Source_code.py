"""Student Id = 20CE063
    Student name = Preet Padariya"""
#Mr. Anant is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.
#One fine day, a finite number of tourists come to stay at the hotel.
#The tourists consist of:
#→ A Captain.
#→ An unknown group of families consisting K of  members per group where  K ≠ 1.
#The Captain was given a separate room, and the rest were given one room per group. Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear K times per group except for the Captain's room. Mr. Anant needs you to help him find the Captain's room number. The total number of tourists or the total number of groups of families is not known to you. You only know the value of K and the room number list.


N = int(input())

Room_No = map(int, input().split())
Room_No = sorted(Room_No)

for i in range(len(Room_No)):
    if(i != len(Room_No)-1):
        if(Room_No[i]!=Room_No[i-1] and Room_No[i]!=Room_No[i+1]):
            print(Room_No[i])
            break;
    else:
        print(Room_No[i])
