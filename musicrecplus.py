'''
Homework10MusicRecommender
Name: Timothy Stephens,Rachael Kondrat
Date: April 14, 2020
Pledge: We pledge our honor that we have abided by the Stevens Honor System.
'''

# a very complex music recommender system ;-;

from cs115 import *

PREF_FILE = 'musicrecplus_ex2_b.txt'


def loadUsers(fileName):
    ''' Reads in a file of stored users' preferences
        stored in the file 'fileName'.
        Returns a dictionary containing a mapping
        of user names to a list preferred artists
    '''
    try:
        file = open(fileName, 'r')
        userDict={}
        for line in file:
            # Read and parse a single line
            [userName, bands] = line.strip().split(":")
            bandList = bands.split(",")
            bandList.sort()
            userDict[userName] = bandList
        file.close()
        return userDict
    except FileNotFoundError:
        userDict={}
        return userDict
        

def EnterPreferences(userName, userMap):
    ''' Allows user to enter preferences. Returns user to menu promptly after. '''
    newPref = ""
    prefs = []
    newPref = input("Enter an artist that you like (Enter to finish): ")
    while newPref != "":
        prefs.append(newPref.strip().title())
        newPref = input('Please enter another artist or band that you like or just press Enter to see Menu:')
    prefs.sort()
    userMap[userName] = prefs
    return userMap
    
#figure out how to get back to menu!!!



def getRecommendations(userName, prefs, userMap): #some error i forgot
    '''Gets recommendations for a user (userName) based
    on the users in userMap (a dictionary) and the user's
    preferences in pref (a list). Returns a list of recommend
    artists.'''
    bestUser = findBestUser(userName, prefs, userMap)
    if len(bestUser) == 0:
        print("No recommendations available at this time.")
    recommendations = []
    for user in bestUser:
        recs = drop(prefs,userMap[user])
        if recommendations == []:
            recommendations = recs
        else:
            recommendations.extend(recs)
    finalRec = recommendations
    finalRec.sort()
    print(*finalRec, sep = "\n")


def findBestUser(userName, prefs, userMap):
    '''Find the user whose tastes are closest to the current user.
    Return the best user's name ( a string) '''
    bestUser = []
    bestScore = -1
    maxScore = len(prefs)
    for user in userMap.keys():
        if '$' in user:
            continue
        newprefs = userMap[user]
        score = numMatches(prefs, newprefs)
        if score == 0:
            continue
        if maxScore == score:
            continue 
        if score > bestScore and userName != user:
            bestScore = score
            bestUser = [user]
        if score == bestScore and userName != user and user not in bestUser:
            bestUser.insert(-1,user)
    return bestUser



def drop(list1, list2):
    '''Return a new list that contains only the elements in
    list2 that were NOT in list1.'''

    list3 = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
                i += 1
                j += 1
        elif list1[i] < list2[j]:
                i += 1
        else:
                list3.append(list2[j])
                j += 1
    # add the rest of list2 if theres anything left
    while j < len(list2):
        list3.append(list2[j])
        j += 1

    return list3

def numMatches(list1, list2):
    '''return the number of elements that match between
    two sorted lists'''
    matches = 0
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
                matches += 1
                i += 1
                j += 1
        elif list1[i] < list2[j]:
                i += 1
        else:
                j += 1
    return matches

def mostPopular():
    '''print the artist that is liked by the most users.
    if there is a tie, print all artists with the most likes'''
    userList = []
    memo = loadUsers(PREF_FILE)

    newUserList = []
    artistList = []

    likeList = []
    mostLikes = 0
    mostPopular = []

    finalList = []
    
    #load into userList the list of users
    for users in memo.keys():
        userList.append(users)
        
    #first exclude users with a $
    for i in userList:
        if i[len(i)-1] != '$' and len(i) != 0:
            newUserList += [i]

    #second make a list of artists w/o users
    # i am comparing newUserList to the base list, since that has the artists
    #then adding the artists not attached to a private user to artistList
    for users in newUserList:
        if users in memo:
            artistList += memo[users]

    #next try to get the number of likes intoa list w/ the artist
    #the list will have [artist, likes]
    for artists in artistList:
        if likeList != []:
            for item in likeList:
                if artists != item[0]: #item[0] is the artist
                    likeList += [[artists,1]]
                else:
                    item[1] +=1 #item[1] is the like number
                    break
        else:
            likeList += [[artists,1]]
                
    #sort through likeList to find the artist with the most likes
    for term in likeList:
        if term[1] == mostLikes:
            mostPopular += [item[0]]
            mostPopular.sort()
        if term[1] > mostLikes:
            mostPopular = [term[0]]
            mostPopular.sort()
            mostLikes = term[1]
    
    #return the most popular artists
    #also account for if there are not top artists
    if len(mostPopular) == 0:
        print('Sorry no artists found')
    else:
        for item in mostPopular:
            if len(mostPopular) != 0:
                print(item)
 
      
def howPopular():
    '''returns the number of likes the most popluar artists received'''
    
 #I just copied mostPop to get a list w/ [arist,likes]
    userList = []
    memo = loadUsers(PREF_FILE)

    newUserList = []
    artistList = []

    likeList = []
    mostLikes = 0
    mostPopular = []
    
    
    #load into userList the list of users
    for users in memo.keys():
        userList.append(users)
        
    #first exclude users with a $
    for i in userList:
        if i[len(i)-1] != '$' and len(i) != 0:
            newUserList += [i]

    #second make a list of artists w/o users
    # i am comparing newUserList to the base list, since that has the artists
    #then adding the artists not attached to a private user to artistList
    for users in newUserList:
        if users in memo:
            artistList += memo[users]

    #next try to get the number of likes intoa list w/ the artist
    #the list will have [artist, likes]
    for artists in artistList:
        if likeList == []:
            likeList += [[artists,1]]
        else:
            for item in likeList:
                if artists != item[0]: #item[0] is the artist
                    likeList += [[artists,1]]
                else:
                    item[1] +=1 #item[1] is the like number
                    break
              
    #artists with the most likes
    for item in likeList:
        if item[1] > mostLikes:
            mostLikes = item[1]

    if mostLikes == 0:
       print('Sorry no artists found')
    else:
        print(mostLikes)


def RunPreferences(userName, UserMap): #name 'userMap' is not defined
    if userName in UserMap:
        prefs = UserMap[userName]
        return prefs
    else:
        prefs = []
        print('I see that you are a new user')
        newPref = input('Please enter the name of an artist you like: ')
        while newPref != '':
            prefs.append(newPref.strip().title())
            newPref = input('Please enter another artist or band that you like or just press Enter to see Menu:')
        prefs.sort()
        UserMap[userName] = prefs
        return prefs


def MostLikes(userMap):
    '''Finds and returns the user/users with the highest number of preferred
    artists.'''
    XuserMap = filter(lambda x:'$' not in x, userMap.keys()) #filters non $ users
    if len(XuserMap) == 0:
        print('Sorry no user found.')
    TopUser = [XuserMap[0]] #takes first user as base case
    for user in XuserMap:
        if len(userMap[user]) > len(userMap[TopUser[0]]): #replaces TopUser if more
            TopUser = [user]
        if len(userMap[user]) == len(userMap[TopUser[0]]) and user != TopUser[0]: #joins TopUser if equal?
            TopUser.append(user)
    TopUser.sort()
    print("\n".join(TopUser)) #prints the TopUser/users on individual lines



def Quit(userName, userMap, fileName):
    '''Saves changes made to the file's content and safely exits the program.'''
    try:
        file = open(fileName, 'w')
        for user in userMap:
            toSave = str(user) + ':' + ','.join(userMap[user]) + '\n'
            file.write(toSave)
        file.close()
    except FileNotFoundError:
        file = open(fileName, 'w+')
        for user in userMap:
            toSave = str(user) + ':' + ','.join(userMap[user]) + '\n'
            file.write(toSave)
        file.close()
                 
 
def main():
    ''' The main recommendation function '''

    #STARTING CODE SHOULD RUN BEFORE MAIN
    userMap = loadUsers(PREF_FILE)
    print('Welcome to the music recommender')
    userName = input('Please enter your name ( put a $ symbol after your name if you wish your preferences to remain private ): ')
    prefs = RunPreferences(userName, userMap)
    
    menuLoop = True
    while menuLoop == True:
        option = input('\n Enter a letter to choose an option :' '\n'
        'e - Enter preferences' '\n'
        'r - Get recommendations' '\n'
        'p - Show most popular artists' '\n'
        'h - How popular is the most popular' '\n'
        'm - Which user has the most likes' '\n'
        'q - Save and quit' '\n ')
        if option == 'e':
            prefs = EnterPreferences(userName, userMap)
        if option == 'r':
            Recs = getRecommendations(userName, prefs, userMap)
        if option == 'p':
            MVPs = mostPopular()
        if option == 'h':
            MVPsCount = howPopular()
        if option == 'm':
            SpotifyCamper = MostLikes(userMap)
        if option == 'q':
            Terminator = Quit(userName, userMap, PREF_FILE)
            break

if __name__ == "__main__": main()



