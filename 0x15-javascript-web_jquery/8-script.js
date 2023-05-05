$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(movie) {
	let movieTitle = movie.title;
	$("#list_movies").append(movieTitle);
});
