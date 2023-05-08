$('document').ready(function () {
	let langcode = $.param(("INPUT#language_code").val());
	const url = "https://www.fourtonfish.com/hellosalut/hello/";
	$.get(url + langcode, fuction (data) {
		$("INPUT#btn_translate").on("click", function () {
			let trans = data.hello;
			$("DIV#hello").text(trans);
		});
	});
});
