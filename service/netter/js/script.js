$('.category').click(function() {
	var category = $(this).text();
	$(".resultTitle").empty();
	$('<div></div>').attr("id", "resultCategory").css("color","#2196f3").html(category).append(" で<br>みんなが知ってるもの").prependTo(".resultTitle");
	addPageList(category);
});

// ajaxエラーメッセージ
function errorMessage(XMLHttpRequest, textStatus, errorThrown){
	$('<div></div>').attr("id", "XMLHttpRequest").html("XMLHttpRequest : " + XMLHttpRequest.status).appendTo("body");
	$('<div></div>').attr("id", "textStatus").html("textStatus : " + textStatus).appendTo("body");
	$('<div></div>').attr("id", "errorThrown").html("errorThrown : " + errorThrown.message).appendTo("body");
}

// ページランク出力
function showResult (pageList) {
	console.log(pageList);
	$('#tweetList').empty();
	for (var i = 0; i < pageList.length - 1; i++) {
	var title = pageList[i];
	tweetButton = '<h2 style="margin-bottom: 30px; font-size:20px">'+ title + '<br><a href="https:/twitter.com/intent/tweet?text=' + title + 'ってあり？" class="btn btn-primary" target="_brank">このネタでかまってもらう？</a></h3>';
	$(tweetButton).prependTo("#tweetList");
	}
}

// ajax通信を行い，ページランクを取得してくる
function addPageList (cat) {
	console.log(cat);
	var category = {
		"category" : cat
	};
	var pageList = [];
	$.ajax({
		url: 'http://www.ai.cs.kobe-u.ac.jp/~akita/wiki/getWikiPage.php?',
		type: "GET",
		data: category,
		dataType: "json",
		cache: false,
		timeout: 100000,
		success: function(response){
			if(response["title"] != null) {
				for (var i = 0; i < response["title"].length; i++){
					pageList.push(response["title"][i]);
				}
				showResult(pageList);

			}
		},
		error: function(XMLHttpRequest, textStatus, errorThrown) {
			errorMessage(XMLHttpRequest, textStatus, errorThrown);
		},
	});
}