# Reflection on Profile Comparisons

- Pop listener vs Chill lofi listener: The pop listener prefers high-energy songs with fast tempo, while the chill lofi listener shifts toward calmer tracks and softer moods. This makes sense because the energy range and mood list are very different, so the model should rank energetic pop-style songs higher for pop and mellow tracks higher for lofi.

- Rock listener vs Conflicting mood preferences: The rock listener output stays focused on intense rock tracks with strong energy, while the conflicting mood profile is dominated by energy fit and can include non-genre songs. That matches the idea that a rock user is still looking for genre plus energy, but the conflicting mood profile is more about whether the song is close to the wanted energy range.

- Genre mismatch with strong energy/valence vs Nonexistent genre/mood values: The first profile shows that a classical genre preference can be overridden when songs have very strong energy and valence, while the second profile shows the model falls back to energy/tempo when genre and mood do not match anything. This helps me understand that the current system will still recommend a good numerical fit even if the genre or mood labels are missing.
