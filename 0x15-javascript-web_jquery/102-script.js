$.get("https://www.fourtonfish.com/hellosalut/hello/", fuction (data) {
	 $("INPUT#btn_translate").on("click", function () {
		 let langcode = $("INPUT#language_code").val();
		 let trans = data.hello.langcode;
		$("DIV#hello").text(trans);
	});
});
