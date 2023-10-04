$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const movieTitles = data.results;
  $.each(movieTitles, function (index, movie) {
    $('#list_movies').append($('<li>').text(movie.title));
  });
});
