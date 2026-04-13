# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

This recommender is made to suggest a few songs from a small catalog based on what a user says they like. It is meant for classroom exploration and not a real music service.

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

The model scores songs by checking genre, mood, energy, tempo, and valence. It adds points for matches and subtracts points for disliked moods. The closest energy and tempo songs get the biggest boosts, and then the system sorts the songs by score.

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.


---

## 4. Data  

The dataset is a small CSV with 18 songs. Each song includes genre, mood, energy, tempo, valence, danceability, and acousticness. The catalog has a few `lofi` songs and only one or two songs for genres like jazz, metal, and classical.

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

The system works well for clear energy-based profiles. It gives good high-energy recommendations for a pop or rock user and calm songs for a lofi listener. It also makes the score easy to understand with a simple point system.

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The current system can create a kind of filter bubble because it really pushes songs that match the energy range and tempo more than it cares about mood diversity. Since the catalog has more `lofi` songs and there are only a few songs in genres like jazz or metal, users who want less common sounds may not get good recommendations. Also, the energy gap math is simple and favors songs close to the preferred energy range, so users with unusual energy tastes or very narrow energy windows can get stuck seeing the same kinds of tracks again and again. 

---

## 7. Evaluation  

I tested three main user profiles and a set of edge cases to see how the model behaved. The main profiles were a high-energy pop listener, a chill lofi listener, and a rock listener. I also tried edge cases like conflicting mood preferences, a genre mismatch with strong energy/valence, a zero-width energy range, a profile with nonexistent genre/mood values, a high-valence low-energy request, and a reversed energy range.

For each profile I looked at the top 5 recommended songs and the score breakdown, especially whether the output matched the expected energy, mood, and genre. I was surprised to see that the energy weighting change made energy fit much more important than genre, so songs that matched the desired energy and tempo often outranked a genre match. I also noticed that the conflicting mood profile still favored energy-strong songs, which showed the score formula is very sensitive to energy closeness and tempo even after genre weight was reduced.

No formal numeric metric was used; I compared the outputs qualitatively by checking whether the recommended songs matched the stated user preferences.

---

## 8. Future Work  

- Add more songs and more balanced genres so recommendations do not favor one style.
- Add better mood handling instead of just liked/disliked mood labels.
- Let users choose tempo range or mood intensity directly.

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

The biggest thing I learned from this project was how sensitive the scoring formula is. Even tiny changes can shuffle the rankings in ways I didn’t expect, especially when energy starts to matter more than genre. It made me realize how much weight‑tuning affects the “feel” of a recommender, even a simple one like this. Using AI tools definitely helped me write and organize the model card and the explanations faster, but I still had to double‑check the code and the actual recommendation output to make sure everything I wrote matched what the program was really doing. I was honestly surprised that such a basic point‑based system could still feel like a real recommendation engine. The top songs usually matched the vibe I expected for each profile, even though the model is basically just adding up numbers. If I kept working on this, I’d want to add more realistic user preferences like better tempo ranges, more detailed mood labels, and a bigger, more balanced song catalog. That would make the recommendations feel even closer to what a real system might produce.

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
