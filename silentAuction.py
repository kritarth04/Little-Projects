import os, random, time
import text_speech as tx
import threading as th

def speak():
    tx.text_to_speech("Welcome to the secret auction program")

# print("Welcome".center(175),"\n")

def show():
    print("Welcome".center(175),"\n")

t1 = th.Thread(target=show)
t2 = th.Thread(target=speak)
t1.start()
t2.start()
t1.join()
t2.join()

# time.sleep()

class auction:
    Items = ["Pablo Picasso's Nude, Green Leaves and Bust", "Roman-era statue, Artemis and the Stag","1957 Ferrari 250 Testa Rossa","Badminton Cabinet","Wittelsbach diamond","Mark McGwire's 70th-home-run baseball"]
    Price = 5,8,10,55,23,33.5
    print(f"The Rare Item Is {random.choices(Items, k = 1)} & The Bidding Starts Form $ {random.choices(Price, k =1 )} million  ")
    time.sleep(2)

    Bidders = {}

    def add_bidder(self):
        key = input("Enter Your name: ".capitalize())
        value = int(input("Bidding ammount [ in million ]: $"))
        self.Bidders[key] = value
        os.system('cls')
        self.question()


    def remove_bidders(self):
        ask2 = input("Do you want to quit [yes or no]: ")
        if (ask2.capitalize() == "Yes"):
            r_name = input("Enter your name: ".capitalize())
            self.Bidders.pop(r_name)
            os.system('cls')
            self.question()
        else:
            print("Well! Changed your dicision ")
            os.system('cls')
            self.question()

    def winner(self):
        sorted_values = sorted(self.Bidders.values()) 
        higgest_bid = sorted_values.pop()
        value = {i for i in self.Bidders if self.Bidders[i] == higgest_bid}
        print("Congratulations".center(171),"\n")
        time.sleep(1.5)
        print(f"The Winner Of The Auction is {value} With The Highest Bid Of {higgest_bid} Millon Dollars ")

    def question(self):
        user = input("Do You want to participate (yes or no): ")
        if user.capitalize() == "Yes":
            self.add_bidder()
        if user.capitalize() == "No":
            user2 = input("Does any one wants to quit (Yes or No): ")
            if user2.capitalize() == "Yes":
                self.remove_bidders()
            else:
                self.winner()
            


bid = auction()
bid.question()