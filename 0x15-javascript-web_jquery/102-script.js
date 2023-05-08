$('document').ready(function () {
	let langcode = $.param({ lang: $("INPUT#language_code").val() });
	const url = "https://www.fourtonfish.com/hellosalut/hello/";
	$.get(url + langcode, function (data) {
		$("INPUT#btn_translate").on("click", function () {
			let trans = data.hello;
			$("DIV#hello").text(trans);
		});
	});
});
