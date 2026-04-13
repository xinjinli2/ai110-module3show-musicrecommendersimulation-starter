"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    # user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}
    user_prefs = {
        "favorite_genre": "pop",
        "liked_moods": ["happy", "intense"],  # Accept multiple
        "disliked_moods": ["dark"],           # Explicit rejects
        "energy_preference": "high",          # Flexible, not 0.80 exactly
        "energy_range": (0.70, 1.0),         # Acceptable band, not rigid
        "tempo_flexibility": "moderate",      # Allow 90–140 BPM, not just 120
        "valence_min": 0.60,                 # Minimum happiness
    }


    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for i, rec in enumerate(recommendations, 1):
        song, score, explanation = rec
        print(f"{i}. {song.title}")
        print(f"   Score: {score:.2f}")
        print(f"   Reasons: {explanation}")
        print()


if __name__ == "__main__":
    main()
