import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>
    
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .movie-plot {
            padding: 10px;
            background-color: black;
        }
        .movie-title {
            padding: 10px;
            background-color: black;
        }
        p {
            color: #919191;
        }
        h4 {
            color: #919191;
            font-weight: bold;
        }
        .btn-group {
            margin-bottom: 20px;
            padding-top: 20px;
        }
    
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        
        // When the movie poster is clicked, open a modal window, write the movie's title and plot in the modal window and start playing the video 
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var moviePlot = $(this).attr('data-movie-plot')
            var movieTitle = $(this).attr('data-movie-title')
            var releaseYear = $(this).attr('data-release-year')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
            document.getElementById('movie-title').innerHTML = "<h4>" + movieTitle + "</h4>";
            document.getElementById('movie-plot').innerHTML = "<p>Released: " + releaseYear + "<br>" + moviePlot + "</p>";
        });
        
        // Triggered by the click event on #sort-by-name, this function extracts the list of movies, sorts them by name alphabetically and reattaches them to the DOM
        $(document).on('click', '#sort-by-name', function(event) {
           var list = document.getElementById("movie-list"); // get the holder of the movie elements
           var items = document.getElementsByClassName("movie-tile"); // get the individual movie elements
           var itemsArr = [];
           for (var i in items) { // push each into the array
               if (items[i].nodeType == 1) { // get rid of the whitespace text nodes
                   itemsArr.push(items[i]); 
               }
           }
           // sort the array using a custom sorting function, that looks at the attribute data-movie-title
           itemsArr.sort(function(a, b) {
             return a.getAttribute("data-movie-title") == b.getAttribute("data-movie-title")
                     ? 0
                     : (a.getAttribute("data-movie-title") > b.getAttribute("data-movie-title") ? 1 : -1);
           });
           
           for (i = 0; i < itemsArr.length; ++i) {
             list.appendChild(itemsArr[i]);
           }
         });
            
         // Triggered by the click event on #sort-by-year, this function extracts the list of movies, sorts them by release date in descending order and reattaches them to the DOM
         $(document).on('click', '#sort-by-year', function(event) {
             //document.write("Hello world!");
            var list = document.getElementById("movie-list"); // get the holder of the movie elements
            var items = document.getElementsByClassName("movie-tile"); // get the individual movie elements
            var itemsArr = [];
            for (var i in items) { // push each into the array
                if (items[i].nodeType == 1) { // get rid of the whitespace text nodes
                    itemsArr.push(items[i]);
                }
            }
            // sort the array using a custom sorting function, that looks at the attribute data-release-year
            itemsArr.sort(function(a, b) {
              return a.getAttribute("data-release-year") == b.getAttribute("data-release-year")
                      ? 0
                      : (a.getAttribute("data-release-year") < b.getAttribute("data-release-year") ? 1 : -1);
            });
            
            for (i = 0; i < itemsArr.length; ++i) {
              list.appendChild(itemsArr[i]);
            }
          });
        
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="movie-title" id="movie-title"></div>
          <div class="scale-media" id="trailer-video-container"></div>
          <div class="movie-plot" id="movie-plot"></div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
      <!-- Buttons to sort the list of movies, either by name or release year, with bootstrap class names -->
      <div class="btn-group" role="group" aria-label="...">
        <button type="button" class="btn btn-default" id="sort-by-name">Sort by Name</button>
        <button type="button" class="btn btn-default" id="sort-by-year">Sort by Latest</button>
      </div>
    </div>
    <div class="container" id="movie-list">
      
      {movie_tiles}
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-movie-plot="{movie_story_line}" data-movie-title="{movie_title}" data-release-year="{release_year}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None
        
        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_story_line=movie.storyline,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            release_year = movie.release_year
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')
  
  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))
  
  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()
  
  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
