$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(muvi) {
	let movititle = muvi.results.map(function(mov) {
		return mov.title;
	});
	$.each(movititle, function(index, title) {
		$("#list_movies").append(`<li>${title}</li>`);
	});
});
