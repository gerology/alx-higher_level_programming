$.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(name) {
	let datar = name;
	$("#character").text("datar");
});
