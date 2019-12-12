import random
from util import Stack, Queue
class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # algos:
        # avgFriendships = total Friendships / numUsers
        # total friendships = avgFriendships * numUsers
        # add users:
        # call addUser() until our number of users is numUsers
        for i in range(numUsers):
            self.addUser(f'User {i+1}')
            
        # create random friendships
        # generate a list of all possible friendships
        possibleFriendships = []

        # avoid dupes by ensuring the first ID is smaller than the second
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append( (userID, friendID) )      
        print('possible friendships:')
        print(possibleFriendships)  

        # shuffle the list
        random.shuffle(possibleFriendships)

        # slice off totalFriendships from the front, create those friendships
        totalFriendships = avgFriendships * numUsers // 2
        print(f'Friendships to create: {totalFriendships}\n')
        for i in range(totalFriendships):
            friendship = possibleFriendships[i]
            self.addFriendship( friendship[0], friendship[1] )


    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

		# Create an empty Queue
        queue = Queue()
		# Create an empty Visited dictionary
        visited = {}
		# Add a PATH TO the starting vertex to the Queue
        queue.enqueue([userID])
		# While the queue is not empty...
        while queue.size() > 0:
		    # Dequeue the first PATH
            path = queue.dequeue()
		    # Grab the last vertex from the path
            v = path[-1]
			# If it has not been visited...
            if v not in visited:
			# When we reach an unvisited user, append the path to the visited dictionary
                visited[v] = path
				# Then enqueue PATHS TO each of its neighbors in the queue
                for neighbor in self.friendships[v]:
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    queue.enqueue(path_copy)
        # return visited
        return visited




if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(11, 2)
    print("USERS:")
    print(sg.users)
    print("FRIENDSHIPS:")
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
