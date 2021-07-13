import pandas as pd
import matplotlib.pyplot as plt

def intro():
    print("India is one of the oldest civilizations in the world and boasts of many ethnic groups following different cultures and religions.")
    print("Being a diverse civilization, India is a land of myriad tongue with over 1650 spoken languages and dialects.")
    print("Despite of different cultures, religions and languages, people of India live together with love and brotherhood.")
    print("The immense unity in diversity makes India an example of cultural brotherhood.It is home to the largest number of different socio-cultural")
    print("groups based on race,religion, language, etc.")
    print("Being a large country with a large population, India presents endless varieties of physical features and cultural patterns.")
    print("It is only in India, people profess all the major religions of the world. In short, India is THE EPITOME OF THE WORLD.")
    print("The vast population is composed of people having diverse creeds, customs, and colours.")
def language():
    print("LINGUISTIC DIVERSITY")
    df=pd.read_csv("IndianLanguages.csv",index_col=0)
    print(df)
    x=df["LANGUAGES"]
    y=df["NO. OF SPEAKERS"]
    plt.title("Linguistic Diversity")
    plt.xlabel("Languages")
    plt.ylabel("No. of speakers")
    plt.xticks(rotation=30)
    plt.plot(x,y,marker="X",ls="dashed",linewidth=4,color="c")
    plt.show()

def handicrafts():
    print("STATES, THEIR CAPITALS AND HANDICRAFTS")
    print()
    print()
    df=pd.read_csv("IndianHandicrafts.csv",index_col=0)
    print(df)

def tourist():
    print("PLACES OF TOURIST ATTRACTION")
    df=pd.read_csv("IndianMonuments.csv")
    print(df)
    x=df["MONUMENTS"]
    y=df["NO. OF VISITORS IN MILLIONS"]
    plt.title("Places of tourist attraction")
    plt.xlabel("Monuments")
    plt.ylabel("No. of visitors in millions")
    plt.xticks(rotation=30)
    plt.bar(x,y,color="blue")
    plt.show()

def festival():
    print("A VARIETY OF FESTIVALS")
    print()
    print()
    df=pd.read_csv("IndianFestivals.csv",index_col=0)
    print(df)


def religion():
    print("RELIGIOUS DIVERSITY")
    df=pd.read_csv("IndianReligions.csv")
    print(df)
    x=df["RELIGIONS"]
    y=df["FOLLOWERS"]
    plt.title("Religious Diversity")
    plt.xlabel("Religions")
    plt.ylabel("Followers")
    plt.barh(x,y,color="orange",edgecolor="black")
    plt.show()

def cuisine():
    print("DELIGHTS OF INDIAN CUISINES")
    print()
    print()
    df=pd.read_csv("IndianCuisines.csv",index_col=0)
    print(df)


def dance():
    print("VARIOUS DANCE FORMS")
    print()
    print()
    df=pd.read_csv("IndianDance.csv", index_col=0)
    print(df)

def flora():
    print("FLORAL STATISTICS OF INDIA")
    df=pd.read_csv("IndianFlora.csv",index_col=0)
    print(df)
    x=df["FLORA"]
    y=df["NO. OF SPECIES"]
    plt.title("Floral Statictics of India")
    plt.xticks(rotation=30)
    plt.plot(x,y,marker="d",ls="solid",linewidth=4,color="y")
    plt.show()

def fauna():
    print("FAUNA IN INDIA")
    df=pd.read_csv("IndianFauna.csv",index_col=0)
    print(df)
    x=df["FAUNA"]
    y=df["NO. OF SPECIES"]
    plt.title("Fauna in India")
    plt.xlabel("Fauna")
    plt.ylabel("No. of species")
    plt.xticks(rotation=30)
    plt.plot(x,y,marker="o",ls="dashed",linewidth=4,color="m")
    plt.show()

def minerals():
    print("MINERAL RESOURCES")
    print()
    print()
    df=pd.read_csv("IndianMinerals.csv", index_col=0)
    print(df)



def showMenu():
    print("-------------------------------")
    print("          A VISIT TO INDIA       ")
    print("-------------------------------")
    print("Press 0  - A mirror to Indian Culture")
    print("Press 1  - Linguistic Diversity")
    print("Press 2  - States, their capitals and Handicrafts")
    print("Press 3  - Places of Tourist attraction")
    print("Press 4  - A variety of festivals")
    print("Press 5  - Religious diversity")
    print("Press 6  - Delights of Indian Cuisines")
    print("Press 7  - Various dance forms")
    print("Press 8  - Floral Statistics")
    print("Press 9  - Fauna in India")
    print("Press 10 - Mineral Resources")
    
a=showMenu()

opt=int(input("Enter your choice:"))
if opt==0:
    intro()
elif opt==1:
    language()
elif opt==2:
    handicrafts()
elif opt==3:
    tourist()
elif opt==4:
    festival()
elif opt==5:
    religion()
elif opt==6:
    cuisine()
elif opt==7:
    dance()
elif opt==8:
    flora()
elif opt==9:
     fauna()
elif opt==10:
    minerals()
else:
    print("invalid option")
    print("\a")
    
       
        
    

 


