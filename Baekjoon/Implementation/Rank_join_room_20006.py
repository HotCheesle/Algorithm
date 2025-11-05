class RankGame: 
    def __init__(self, M):
        self.rooms = []
        self.players = []
        self.player_num = 0
        self.room_capacity = M

    def new_player(self, player): 
        self.players.append(player)
        p_id = self.player_num
        self.player_num += 1
        room_id = self.find_room(player.get_level())
        if room_id: 
            self.rooms[room_id].join_player(p_id)
        else: 
            new_room = GameRoom(self.room_capacity, p_id, player.get_level())
            self.rooms.append(new_room)

    def find_room(self, lv): 
        for room_id in range(len(self.rooms)): 
            if (abs(self.rooms[room_id].get_std_level() - lv) <= 10 
            and self.rooms[room_id].is_joinable()): 
                return room_id
        return None
    
    def print_games(self): 
        for room in self.rooms: 
            if room.is_joinable(): 
                print("Waiting!")
            else: 
                print("Started!")
            for p_id in room.get_player_list(): 
                print(f"{self.players[p_id].get_level()} {self.players[p_id].get_nickname()}")

class GameRoom: 
    def __init__(self, max_player, p_id, lv):
        self.player = [p_id]
        self.std_level = lv
        self.capacity = max_player
        if max_player == 1: 
            self.is_full = True
        else: 
            self.is_full = False

    def join_player(self, p_id):
        self.player.append(p_id)
        if len(self.player) >= self.capacity: 
            self.is_full = True

    def is_joinable(self): 
        return not self.is_full
    
    def get_std_level(self): 
        return self.std_level
    
    def get_player_list(self): 
        return self.player

class Player: 
    def __init__(self, lv, name):
        self.nickname = name
        self.level = lv

    def get_nickname(self): 
        return self.nickname
    
    def get_level(self): 
        return self.level
    

P, M = map(int, input().split())
game = RankGame(M)
for _ in range(P): 
    lv, name = input().split()
    player = Player(int(lv), name)
    game.new_player(player)
game.print_games()