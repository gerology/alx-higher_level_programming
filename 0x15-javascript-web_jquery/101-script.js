$('document').ready(function () {
	$('#add_item').on('click', function () {
		$('.my_list').append('<li>Item</li>');
	});

	$('#remove_item').on('click', function () {
		$('.my_list').last().remove();
	});

	$('#clear_list').on('click', function () {
		while ($('.my_list')) {
			$('my_list').removeChild(.my_list.firstChild);
		};
	});
});
