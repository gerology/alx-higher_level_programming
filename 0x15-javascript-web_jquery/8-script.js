$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function('title') {
	$('#list_movies').append(title);
});
