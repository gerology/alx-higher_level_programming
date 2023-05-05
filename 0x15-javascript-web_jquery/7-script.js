$.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(xter) {
	let datar = xter.name;
	$("#character").text(datar);
});
