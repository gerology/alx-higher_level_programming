$('document').ready(function () {
	let url = 'https://www.fourtonfish.com/hellosalut/?';
	$('INPUT#btn_translate').on('click', 'keydown', function () {
		$.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
			$('DIV#hello').html(data.hello);
		});
	});
});