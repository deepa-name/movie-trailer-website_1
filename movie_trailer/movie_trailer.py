import movie
import fresh_tomatoes

# Create an array of instances of movie.Movie to store details about different movies
movies = [
          movie.Movie("Toy Story", 
                      "Toy Story follows a group of anthropomorphic toys who pretend to be lifeless whenever humans are present, and focuses on the relationship between Woody, a pullstring cowboy doll (voiced by Tom Hanks), and Buzz Lightyear, an astronaut action figure (voiced by Tim Allen)", 
                      "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc", 
                      1995),
          
          movie.Movie("Frozen", 
                      "When the newly crowned Queen Elsa accidentally uses her power to turn things into ice to curse her home in infinite winter, her sister, Anna, teams up with a mountain man, his playful reindeer, and a snowman to change the weather condition.", 
                      "http://ia.media-imdb.com/images/M/MV5BMTQ1MjQwMTE5OF5BMl5BanBnXkFtZTgwNjk3MTcyMDE@._V1_SX300.jpg", 
                      "https://www.youtube.com/watch?v=TbQm5doF_Uc", 
                      2015),
          
         movie.Movie("Ice Age",
                     "Set during the Ice Age, a sabertooth tiger, a sloth, and a wooly mammoth find a lost human infant, and they try to return him to his tribe.",
                     "http://upload.wikimedia.org/wikipedia/en/a/a9/Ice_Age.jpg",
                     "https://www.youtube.com/watch?v=cMfeWyVBidk",
                     2002),

         movie.Movie("Ratatouille",
                     "A rat who can cook makes an unusual alliance with a young kitchen worker at a famous restaurant.",
                     "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                     "www.youtube.com/watch?v=c3sBBRxDAqk",
                     2007),
          
         movie.Movie("The Lion King",
                     "Tricked into thinking that he caused the death of his father, a lion cub flees and abandons his destiny as the future king.",
                     "http://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",
                     "www.youtube.com/watch?v=MPugv1k7r-s",
                     1994),

         movie.Movie("Finding Nemo",
                     "After his son is captured in the Great Barrier Reef and taken to Sydney, a timid clownfish sets out on a journey to bring him home.",
                     "http://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
                     "www.youtube.com/watch?v=SPHfeNgogVs",
                     2003)]

# Open the movie trailer application, giving it an input of the array of movies
fresh_tomatoes.open_movies_page(movies)
