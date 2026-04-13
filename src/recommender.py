import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    liked_moods: List[str]
    disliked_moods: List[str]
    energy_range: Tuple[float, float]
    valence_min: float

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Recommend top k songs based on user preferences."""
        # Score all songs and sort by score descending
        scored_songs = []
        for song in self.songs:
            score, reasons = self._score_song(user, song)
            scored_songs.append((song, score))
        
        scored_songs.sort(key=lambda x: x[1], reverse=True)
        return [song for song, score in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain the recommendation score and reasons for a song."""
        score, reasons = self._score_song(user, song)
        return f"Score: {score:.2f} - Reasons: {', '.join(reasons)}"

    def _score_song(self, user: UserProfile, song: Song) -> Tuple[float, List[str]]:
        """Score a song against user preferences and return reasons."""
        score = 0.0
        reasons = []
        
        # Genre match: +2.0 points
        if song.genre == user.favorite_genre:
            score += 2.0
            reasons.append("genre match (+2.0)")
        
        # Liked mood: +1.0 point
        if song.mood in user.liked_moods:
            score += 1.0
            reasons.append("liked mood (+1.0)")
        
        # Disliked mood: -2.0 points
        if song.mood in user.disliked_moods:
            score -= 2.0
            reasons.append("disliked mood (-2.0)")
        
        # Energy closeness: up to +1.5 points
        energy_min, energy_max = user.energy_range
        if energy_min <= song.energy <= energy_max:
            energy_points = 1.5
        else:
            dist = min(abs(song.energy - energy_min), abs(song.energy - energy_max))
            energy_points = max(0, 1.5 - 1.5 * (dist / 0.3))
        score += energy_points
        reasons.append(f"energy closeness (+{energy_points:.2f})")
        
        # Tempo closeness: up to +1.0 point (moderate: 90-140 BPM)
        tempo_min, tempo_max = 90, 140
        if tempo_min <= song.tempo_bpm <= tempo_max:
            tempo_points = 1.0
        else:
            dist = min(abs(song.tempo_bpm - tempo_min), abs(song.tempo_bpm - tempo_max))
            tempo_points = max(0, 1.0 - 1.0 * (dist / 30))
        score += tempo_points
        reasons.append(f"tempo closeness (+{tempo_points:.2f})")
        
        # Passing valence minimum: +0.5 points
        if song.valence >= user.valence_min:
            score += 0.5
            reasons.append("passes valence minimum (+0.5)")
        
        return score, reasons

def load_songs(csv_path: str) -> List[Song]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    numeric_fields = {
        "id": int,
        "energy": float,
        "tempo_bpm": float,
        "valence": float,
        "danceability": float,
        "acousticness": float,
    }

    songs: List[Song] = []
    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            song = Song(
                id=int(row["id"]),
                title=row["title"],
                artist=row["artist"],
                genre=row["genre"],
                mood=row["mood"],
                energy=float(row["energy"]),
                tempo_bpm=float(row["tempo_bpm"]),
                valence=float(row["valence"]),
                danceability=float(row["danceability"]),
                acousticness=float(row["acousticness"])
            )
            songs.append(song)

    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Song) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons = []
    
    # Genre match: +2.0 points
    if song.genre == user_prefs['favorite_genre']:
        score += 2.0
        reasons.append("genre match (+2.0)")
    
    # Liked mood: +1.0 point
    if song.mood in user_prefs['liked_moods']:
        score += 1.0
        reasons.append("liked mood (+1.0)")
    
    # Disliked mood: -2.0 points
    if song.mood in user_prefs['disliked_moods']:
        score -= 2.0
        reasons.append("disliked mood (-2.0)")
    
    # Energy closeness: up to +1.5 points
    energy_min, energy_max = user_prefs['energy_range']
    if energy_min <= song.energy <= energy_max:
        energy_points = 1.5
    else:
        # Simple closeness: distance to nearest bound
        dist = min(abs(song.energy - energy_min), abs(song.energy - energy_max))
        energy_points = max(0, 1.5 - 1.5 * (dist / 0.3))  # Assuming 0.3 is max dist
    score += energy_points
    reasons.append(f"energy closeness (+{energy_points:.2f})")
    
    # Tempo closeness: up to +1.0 point
    # For "moderate" flexibility, assume 90-140 BPM
    tempo_min, tempo_max = 90, 140
    if tempo_min <= song.tempo_bpm <= tempo_max:
        tempo_points = 1.0
    else:
        dist = min(abs(song.tempo_bpm - tempo_min), abs(song.tempo_bpm - tempo_max))
        tempo_points = max(0, 1.0 - 1.0 * (dist / 30))
    score += tempo_points
    reasons.append(f"tempo closeness (+{tempo_points:.2f})")
    
    # Passing valence minimum: +0.5 points
    if song.valence >= user_prefs['valence_min']:
        score += 0.5
        reasons.append("passes valence minimum (+0.5)")
    
    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Song], k: int = 5) -> List[Tuple[Song, float, str]]:
    """Recommend songs with scores and explanations using functional approach."""
    # Score all songs and create (song, score, explanation) tuples
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored_songs.append((song, score, explanation))
    
    # Sort by score descending and return top k
    scored_songs.sort(key=lambda x: x[1], reverse=True)
    return scored_songs[:k]
