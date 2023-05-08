$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(muvi) {
	let movie = muvi.result;
	movititle = movie.map(function(mov) {
		return mov.title;
	});
	$.each(movititle, function(title) {
		let lsit = $("<li></li>").text(title);
		$("#list_movies").append(lsit);
	});
});
