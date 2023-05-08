$.get("https://fourtonfish.com/hellosalut/?lang=fr", function(data) {
	let valu = $("hello").val()
	$('#hello').text(valu);
});
