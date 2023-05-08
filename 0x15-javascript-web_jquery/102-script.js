$('document').ready(function () {
	let langcode = $.param({ lang: $("INPUT#language_code").val() });
	const url = "https://www.fourtonfish.com/hellosalut/?";
	$("INPUT#btn_translate").on("click", function () {
		$.get(url + langcode, function (data) {
			let trans = data.hello;
			$("DIV#hello").text(trans);
		});
	});
});
