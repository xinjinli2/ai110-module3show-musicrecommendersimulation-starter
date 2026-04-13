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

    user_prefs_pop = {
        "favorite_genre": "pop",
        "liked_moods": ["happy", "intense", "bright"],
        "disliked_moods": ["dark"],
        "energy_preference": "high",
        "energy_range": (0.75, 1.0),
        "tempo_flexibility": "fast",         
        "valence_min": 0.65
    }

    # Chill Lofi listener
    user_prefs_lofi = {
        "favorite_genre": "lofi",
        "liked_moods": ["calm", "chill", "soft"],
        "disliked_moods": ["intense", "aggressive"],
        "energy_preference": "low",
        "energy_range": (0.10, 0.45),
        "tempo_flexibility": "slow",         
        "valence_min": 0.30
    }

    user_prefs_rock = {
        "favorite_genre": "rock",
        "liked_moods": ["intense", "powerful", "moody"],
        "disliked_moods": ["happy"],
        "energy_preference": "high",
        "energy_range": (0.70, 1.0),
        "tempo_flexibility": "wide",          
        "valence_min": 0.20                 
    }






    test_profiles = [
        ("Pop listener", user_prefs_pop),
        ("Chill lofi listener", user_prefs_lofi),
        ("Rock listener", user_prefs_rock),
    ]

    edge_case_profiles = [
        (
            "Conflicting mood preferences",
            {
                "favorite_genre": "pop",
                "liked_moods": ["sad"],
                "disliked_moods": ["sad"],
                "energy_range": (0.4, 0.7),
                "valence_min": 0.2,
            },
        ),
        (
            "Genre mismatch with strong energy/valence",
            {
                "favorite_genre": "classical",
                "liked_moods": ["intense"],
                "disliked_moods": ["happy"],
                "energy_range": (0.8, 1.0),
                "valence_min": 0.0,
            },
        ),
        (
            "Zero-width energy range",
            {
                "favorite_genre": "rock",
                "liked_moods": ["powerful"],
                "disliked_moods": ["soft"],
                "energy_range": (0.5, 0.5),
                "valence_min": 0.4,
            },
        ),
        (
            "Nonexistent genre/mood values",
            {
                "favorite_genre": "ambient",
                "liked_moods": ["ethereal"],
                "disliked_moods": ["aggressive"],
                "energy_range": (0.2, 0.5),
                "valence_min": 0.8,
            },
        ),
        (
            "High valence minimum with low-energy mood",
            {
                "favorite_genre": "pop",
                "liked_moods": ["sad"],
                "disliked_moods": ["angry"],
                "energy_range": (0.1, 0.3),
                "valence_min": 0.95,
            },
        ),
        (
            "Reversed / invalid energy range",
            {
                "favorite_genre": "jazz",
                "liked_moods": ["mellow"],
                "disliked_moods": ["energetic"],
                "energy_range": (1.0, 0.0),
                "valence_min": 0.3,
            },
        ),
    ]

    print("\nStandard profiles:\n")
    for label, profile in test_profiles:
        print(f"=== {label} ===")
        recommendations = recommend_songs(profile, songs, k=5)
        for i, rec in enumerate(recommendations, 1):
            song, score, explanation = rec
            print(f"{i}. {song.title}")
            print(f"   Score: {score:.2f}")
            print(f"   Reasons: {explanation}")
        print()

    print("\nEdge-case / adversarial profiles:\n")
    for label, profile in edge_case_profiles:
        print(f"=== {label} ===")
        recommendations = recommend_songs(profile, songs, k=5)
        for i, rec in enumerate(recommendations, 1):
            song, score, explanation = rec
            print(f"{i}. {song.title}")
            print(f"   Score: {score:.2f}")
            print(f"   Reasons: {explanation}")
        print()


if __name__ == "__main__":
    main()
