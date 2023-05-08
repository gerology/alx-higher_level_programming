$.get("https://fourtonfish.com/hellosalut/?lang=fr", function(data) {
	let valu = data.hello;
	$('#hello').text(valu);
});
