$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(muvi) {
	let movie = muvi.result;
	let movititle = movie.map(function(mov) {
		return mov.title;
	});
	$.each(movititle, function(index, title) {
		let lsit = $("<li></li>").text(title);
		$("#list_movies").append("lsit");
	});
});
