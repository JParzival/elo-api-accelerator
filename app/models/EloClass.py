class EloClass:
    def __init__(self, initial_rating=1500, k_factor=30):
        """
        Initialize the Elo rating system with a specified initial rating and a K-factor.
        
        Args:
            initial_rating (int): The default Elo rating for all new players. Default is 1500.
            k_factor (int): The K-factor which controls the impact of a single game on players' ratings. Default is 30.
        """
        self.ratings = {}
        self.k = k_factor
        self.initial_rating = initial_rating

    def add_player(self, player_id):
        """
        Add a new player to the Elo rating system with an initial rating.
        
        Args:
            player_id (str): The identifier for the new player.
        """
        self.ratings[player_id] = self.initial_rating

    def get_expected_score(self, rating_a, rating_b):
        """
        Calculate the expected score for a player or team based on their ratings.
        
        Args:
            rating_a (float): The rating of player or team A.
            rating_b (float): The rating of player or team B.
        
        Returns:
            float: The expected score for player or team A against player or team B.
        """
        return 1 / (1 + 10 ** ((rating_b - rating_a) / 400))

    def update_individual_ratings(self, player_a, player_b, score_a):
        """
        Update the ratings of two players after an individual match.
        
        Args:
            player_a (str): The identifier for player A.
            player_b (str): The identifier for player B.
            score_a (float): The actual score for player A (1 for win, 0.5 for draw, 0 for loss).
        """
        rating_a = self.ratings[player_a]
        rating_b = self.ratings[player_b]

        expected_a = self.get_expected_score(rating_a, rating_b)
        expected_b = self.get_expected_score(rating_b, rating_a)

        score_b = 1 - score_a  # Derive score for player B

        # Update ratings
        self.ratings[player_a] = rating_a + self.k * (score_a - expected_a)
        self.ratings[player_b] = rating_b + self.k * (score_b - expected_b)

    def get_team_rating(self, team):
        """
        Calculate the average rating for a team.
        
        Args:
            team (list of str): A list of player identifiers representing the team.
        
        Returns:
            float: The average rating of the team.
        """
        total_rating = sum(self.ratings[player] for player in team)
        return total_rating / len(team)

    def update_team_ratings(self, team_a, team_b, score_a):
        """
        Update the ratings of all players in both teams after a team match.
        
        Args:
            team_a (list of str): The identifiers for team A players.
            team_b (list of str): The identifiers for team B players.
            score_a (float): The actual score for team A (1 for win, 0.5 for draw, 0 for loss).
        """
        team_rating_a = self.get_team_rating(team_a)
        team_rating_b = self.get_team_rating(team_b)

        expected_a = self.get_expected_score(team_rating_a, team_rating_b)
        expected_b = self.get_expected_score(team_rating_b, team_rating_a)

        score_b = 1 - score_a  # Derive score for team B

        # Update individual player ratings based on team performance
        for player in team_a:
            player_rating = self.ratings[player]
            self.ratings[player] = player_rating + self.k * (score_a - expected_a)
        for player in team_b:
            player_rating = self.ratings[player]
            self.ratings[player] = player_rating + self.k * (score_b - expected_b)

    def get_rating(self, player_id):
        """
        Retrieve the current rating of a player.
        
        Args:
            player_id (str): The identifier of the player.
        
        Returns:
            float or str: The current rating of the player, or an error message if not found.
        """
        return self.ratings.get(player_id, "Player not found")